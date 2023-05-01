# @file compose.py
#
# Copyright contributors to the drawIT project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Hierarchy:
#   diagram.py - optional diagram-as-code in python, invokes draw.py 
#   colors.py - optional colors for use by diagram-as-code in python
#   draw.py - iterate diagram objects, invokes shapes.py
#   shapes.py - build ibm types, invokes types.py
#   types.py - build drawio types, invokes xml.py with tables.py
#   elements.py - build drawio objects  

from math import isnan
from uuid import uuid4

from .common import Common

from .attributes import Attributes
from .build import Build
from .constants import ComponentFill, FillPalette, ShapeKind, ShapeName, ShapePos, ZoneCIDR
from .shapes import Shapes

@staticmethod
def randomid():
   return uuid4().hex

class Compose:
   data = None
   attributes = None
   diagrams = {}
   clusters = {}
   nodes = {}
   edges = {}

   common = None
   shapes = None
   cloudname = ""

   def __init__(self, common, data):
      self.common = common
      self.data = data
      self.shapes = Shapes(common)
      self.attributes = Attributes()
      self.cloudname = ShapeName.CLOUD.value if self.common.isProviderAny() else ShapeName.IBM_CLOUD.value

   def composeDiagrams(self):
      validdata = False
      vpcs = self.data.getVPCs()
      for vpcindex, vpcframe in vpcs.iterrows():
         diagrams = {}
         clusters = {}
         nodes = {}
         edges = {}

         vpcid = vpcframe['id']
         vpcname = vpcframe['name']

         vpcTable = self.data.getVPCTable() 
         if not vpcid in vpcTable:
            self.common.printInvalidVPC(vpcid)
            continue

         diagramid = randomid()
         self.attributes.updateSequence(self.common.compress(diagramid))

         publicid = randomid()
         internetid = randomid()
         self.attributes.updateSequence(self.common.compress(publicid))
         clusters, nodes, edges = self.composePublic(clusters, nodes, edges, publicid, internetid)

         cloudid = "Cloud" + ":" + vpcid
         self.attributes.updateSequence(self.common.compress(cloudid))

         regionid = "Region" + ":" + vpcid
         self.attributes.updateSequence(self.common.compress(regionid))

         self.attributes.updateSequence(self.common.compress(vpcid))
         clusters, nodes, edges = self.composeLoadBalancers(vpcname, vpcid, clusters, nodes, edges, internetid)

         if not self.common.isInputTerraform():
            clusters, nodes, edges = self.composeNetworkACLs(vpcname, vpcid, clusters, nodes, edges, internetid)

         #routername = vpcname + '-router'
         #self.attributes.updateSequence(self.common.compress(routername))

         #internetid = randomid()
         self.attributes.updateSequence(self.common.compress(internetid))

         publicedgeid = randomid()
         self.attributes.updateSequence(self.common.compress(publicedgeid))

         for regionzonename in vpcTable[vpcid]:
            zoneid = self.common.compress(regionzonename)
            self.attributes.updateSequence(zoneid)

            clusters, nodes, edges = self.composeSubnets(regionzonename, vpcname, clusters, nodes, edges, internetid)

            zonename = regionzonename.split(':')[1]

            if 'availabilityZones' in vpcframe:
               usercidrs = vpcframe['availabilityZones']
            else:
               usercidrs = None

            if usercidrs != None:
               for usercidr in usercidrs:
                   if zonename == usercidr['name']:
                      zonecidr = usercidr['addressPrefix']
                      break
                   else:
                      zonecidr = ''
            else:
               zonecidr = self.getZoneCIDR(zonename)

            # Zone attributes with parent vpcid
            attributes = self.attributes.getClusterAttributes(label=zonename, sublabel=zonecidr, icon='availabilityzone', parentid=self.common.compress(vpcid))

            #zoneid = self.common.compress(regionzonename)
            clusters[zoneid] = attributes

         # VPC attributes with parent region:vpcid
         #regionid = "Region" + ":" + vpcid
         attributes = self.attributes.getClusterAttributes(label=vpcname, icon='vpc', direction='TB', parentid=self.common.compress(regionid))
         clusters[self.common.compress(vpcid)] = attributes

         # Region attributes with parent cloud:vpcid
         #cloudid = "Cloud" + ":" + vpcid
         attributes = self.attributes.getClusterAttributes(label='Region', icon='region', parentid=self.common.compress(cloudid))
         clusters[self.common.compress(regionid)] = attributes

         attributes = self.attributes.getClusterAttributes(label='Cloud', icon='cloud', parentid=None)
         clusters[self.common.compress(cloudid)] = attributes

         #routername = vpcname + '-router'

         #attributes = {"type": "node", "label": routername, "sublabel": '', "shape": '', "pencolor": '', "bgcolor": '', "badgetext": '', "badgeshape": '', "badgepencolor": '', "badgebgcolor": '', "icon": 'router', "hideicon": '', "direction": '', "many": '', "provider": '', "fontname": '', "fontsize": 0, "parentid": self.common.compress(vpcid)}
         #nodes[self.common.compress(routername)] = attributes

         #clusters, nodes, edges = self.composeLoadBalancers(vpcname, vpcid, clusters, nodes, edges, internetid)

         #clusters, nodes, edges = self.composePublic(clusters, nodes, edges, publicid, internetid)

         #attributes = {"type": "edge", "label": '', "sourceid": self.common.compress(publicuserid), "targetid": self.common.compress(internetid), "style": '', "arrow": '', "fontname": '', "fontsize": 0}

         #publicedgeid = randomid()
         #edges[self.common.compress(publicedgeid)] = attributes

         attributes = self.attributes.getDiagramAttributes(name=vpcname, filename='*')
         #diagramid = randomid()
         diagrams[diagramid] = attributes

         self.attributes.setDiagrams(diagrams)
         self.attributes.setClusters(clusters)
         self.attributes.setNodes(nodes)
         self.attributes.setEdges(edges)

         build = Build(self.common, self.attributes)
         xmldata = build.buildDiagrams()
         if xmldata == None:
            self.common.printInvalidVPC(vpcid)
         else:
            self.shapes.buildXML(xmldata, vpcname)
            validdata = True

      if validdata:
         self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())
         self.shapes.resetXML()

      return

   def composePublic(self, clusters, nodes, edges, publicid, internetid):
      attributes = self.attributes.getClusterAttributes(label='Public Network', icon='publicnetwork', direction='TB', parentid=None)

      #publicid = randomid()
      clusters[self.common.compress(publicid)] = attributes

      attributes = self.attributes.getNodeAttributes(label='User', icon='user', parentid=self.common.compress(publicid))

      userid = randomid()
      nodes[self.common.compress(userid)] = attributes
      self.attributes.updateSequence(self.common.compress(userid))

      attributes = self.attributes.getNodeAttributes(label='Internet', icon='internet', parentid=self.common.compress(publicid))

      nodes[self.common.compress(internetid)] = attributes
      self.attributes.updateSequence(self.common.compress(internetid))

      attributes = self.attributes.getDoubleArrowAttributes(sourceid=self.common.compress(userid), targetid=self.common.compress(internetid))

      internetedgeid = randomid()
      edges[self.common.compress(internetedgeid)] = attributes
      self.attributes.updateSequence(self.common.compress(internetedgeid))

      return clusters, nodes, edges

   def composeEnterprise(self, clusters, nodes, edges, enterpriseid):
      attributes = self.attributes.getClusterAttributes(label='Enterprise Network', icon='enterprisenetwork', direction='TB', parentid=None)

      #enterpriseid = randomid()
      clusters[enterpriseid] = attributes

      attributes = self.attributes.getNodeAttributes(label='User', icon='user', parentid=self.common.compress(enterpriseid))
      userid = randomid()
      nodes[userid] = attributes

      return clusters, nodes, edges

   def composeSubnets(self, regionzonename, vpcname, clusters, nodes, edges, internetid): 
      attributes = {}

      zoneTable = self.data.getZoneTable()
      save_subnetpubgateid = None

      for insubnetid in zoneTable[regionzonename]:
         pubgateid = None

         subnetframe = self.data.getSubnet(insubnetid)
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         subnetregion = 'us-south-1'
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']
         subnetcidr = subnetframe['ipv4_cidr_block']

         vpcframe = self.data.getVPC(subnetvpcid)
         subnetvpcname = subnetframe['name']

         regionname = regionzonename.split(':')[0]
         #regionzonename = regionname + ':' + subnetzonename;

         '''
         if self.common.isLinks():
            zonelink = self.shapes.buildLink(regionzonename + ':' + subnetname, regionzonename, subnetname, None)
         '''

         if self.common.isInputTerraform():
            subnetpubgateid = subnetframe['public_gateway']
         elif 'public_gateway.id' in subnetframe:
            subnetpubgateid = subnetframe['public_gateway.id']
         else:
            subnetpubgateid = None

         pubgatefipip = None
         pubgatename = None
         if subnetpubgateid != None:
            pubgateframe = self.data.getPublicGateway(subnetpubgateid)
            if len(pubgateframe) > 0:
               if self.common.isInputRIAS():
                  pubgatefipip = pubgateframe['floating_ip.address']
               elif self.common.isInputTerraform(): 
                  pubgatefip = pubgateframe['floating_ip']
                  pubgatefipip = pubgatefip['address']
               else: # yaml
                  pubgatefipip = pubgateframe['floatingIP']
               pubgatename = pubgateframe['name']

         clusters, nodes, edges = self.composeSubnetIcons(subnetid, subnetname, subnetvpcname, vpcname, clusters, nodes, edges, internetid)

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         attributes = self.attributes.getClusterAttributes(label=subnetname, sublabel=subnetcidr, icon='subnet', direction='TB', parentid=self.common.compress(regionzonename))

         #subnetid = self.common.compress(subnetid)
         #self.attributes.updateSequence(self.common.compress(subnetid))
         clusters[self.common.compress(subnetid)] = attributes

         if pubgatefipip != None:

            if save_subnetpubgateid == None:
               save_subnetpubgateid = subnetpubgateid

               attributes = self.attributes.getNodeAttributes(label=pubgatename, sublabel=pubgatefipip, icon='publicgateway', parentid=self.common.compress(regionzonename))
               #pubgateid = randomid()
               nodes[self.common.compress(subnetpubgateid)] = attributes
               self.attributes.updateSequence(self.common.compress(subnetpubgateid))

               attributes = self.attributes.getSingleArrowAttributes(sourceid=self.common.compress(subnetid), targetid=self.common.compress(subnetpubgateid))

               edgeid = randomid()
               edges[self.common.compress(edgeid)] = attributes
               self.attributes.updateSequence(self.common.compress(edgeid))

               #routername = vpcname + '-router'
               attributes = self.attributes.getSingleArrowAttributes(sourceid=self.common.compress(subnetpubgateid), targetid=self.common.compress(internetid))

               edgeid = randomid()
               edges[self.common.compress(edgeid)] = attributes
               self.attributes.updateSequence(self.common.compress(edgeid))

            elif subnetpubgateid != save_subnetpubgateid:
               self.common.printInvalidPublicGateway(subnetpubgateid)

            else:
               attributes = self.attributes.getSingleArrowAttributes(sourceid=self.common.compress(subnetid), targetid=self.common.compress(subnetpubgateid))

               edgeid = randomid()
               edges[self.common.compress(edgeid)] = attributes
               self.attributes.updateSequence(self.common.compress(edgeid))

         self.attributes.updateSequence(self.common.compress(subnetid))

      return clusters, nodes, edges

   def composeSubnetIcons(self, subnetid, subnetname, subnetvpcname, vpcname, clusters, nodes, edges, internetid):
      attributes = {}

      icons = self.data.getSubnetIconTable(subnetid)

      for iconframe in icons:
         iconname = iconframe['name']
         iconid = iconframe['id']
         icontype = iconframe['type']

         if icontype.lower() == 'instance':
            instancename = iconname
            instanceid = iconid
            instanceframe = iconframe
            icontype = "virtualserver"  # NEW

            if instancename.lower().find("bastion") != -1:
               icontype = "bastionhost"

            nics = self.data.getNICTable(subnetid, instanceid)

            nicips = ''
            nicid = ''
            nicfipid = None
            nicfipip = None
            nicfipname = None
            nicfips = ''

            for nicframe in nics:
               nicname = nicframe['name']
               if self.common.isInputTerraform():
                  nicinstanceid = nicframe["id"]
                  nicip = nicframe['primary_ipv4_address']
               else:
                  nicinstanceid = instanceframe['id'] if self.common.isInputRIAS() else nicframe['instanceId']
                  nicip = nicframe['primary_ip']['address'] if self.common.isInputRIAS() else nicframe['ip']
               if nicips == '':
                  nicips = nicip
               else:
                  nicips = nicips + '<br>' + nicip
               nicid = nicframe['id']

               fipframe = self.data.getFloatingIP(nicid)
               if len(fipframe) > 0:
                  nicfipid = fipframe['id']
                  nicfipip = fipframe['address']
                  nicfipname = fipframe['name']
                  if nicfips == '':
                     nicfips = nicfipip
                  else:
                     nicfips = nicfips + '<br>' + nicfipip

            secondarytext = nicips

            meta = {}

            if 'image.name' in instanceframe:
               instanceOS = instanceframe['image.name']
               if instanceOS == None:
                  instanceOS = 'Unknown OS'
               meta = meta | {'Operating-System': instanceOS}

            if 'profile.name' in instanceframe:
               instanceprofile = instanceframe['profile.name'] 
               meta = meta | {'Profile': instanceprofile}

            if 'memory' in instanceframe:
               instancememory = instanceframe['memory']
               meta = meta | {'Memory': str(instancememory)}

            if 'bandwidth' in instanceframe:
               bandwidth = instanceframe['bandwidth']
               if bandwidth == '' or (isinstance(bandwidth, float) and isnan(bandwidth)):
                  instancecpuspeed = 0
               else:
                  instancecpuspeed = int(instanceframe['bandwidth'] / 1000)
               meta = meta | {'CPU-Speed': str(instancecpuspeed)}

            if 'vcpu.count' in instanceframe:
               instancecpucount = instanceframe['vcpu.count']
               meta = meta | {'CPU-Count': str(instancecpucount)}

            if meta:
               meta = meta | {'Boot-Volume': '100GB/3000IOPS'}
            else:
               meta = None

            if nicfipip != None:
               #if self.common.isLinks():
               routername = vpcname + '-router'
               iplabel =  "fip:" + nicfipip
               #fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername, None)
               #links.append(fiplink)

               attributes = self.attributes.getDoubleArrowAttributes(label=iplabel, sourceid=self.common.compress(instanceid), targetid=self.common.compress(internetid))

               fipedgeid = randomid()
               edges[self.common.compress(fipedgeid)] = attributes
               self.attributes.updateSequence(self.common.compress(fipedgeid))

         elif icontype.lower() == 'vpngateway':
            icontype = "vpngateway"  # NEW
            secondarytext = ''
            meta = None
         else:
            secondarytext = ''
            meta = None

         #attributes = self.attributes.getClusterAttributes(label=iconname, sublabel=secondarytext, shape="node", icon=icontype, data=meta, parentid=self.common.compress(subnetid))
         attributes = self.attributes.getNodeAttributes(label=iconname, sublabel=secondarytext, icon=icontype, data=meta, parentid=self.common.compress(subnetid))

         iconid = self.common.compress(iconid)
         nodes[iconid] = attributes
         self.attributes.updateSequence(iconid)

      return clusters, nodes, edges

   def composeLoadBalancers(self, vpcname, vpcid, clusters, nodes, edges, internetid):
      lbs = self.data.getLoadBalancers(vpcid)
      if lbs != None:
         for lbpool in lbs:
            #for lbmembers in lbs:
            for lbkey in lbpool:
               #for lbid, members in lbmembers.items():
               for lbid, members in lbpool[lbkey].items():
                  lb = self.data.getLoadBalancer(lbid)
                  lbid = lb['id']
                  lbname = lb['name']

                  if lbname[0:4] == 'kube':
                     # Kube LB not implemented for now.
                     # self.common.printInvalidLoadBalancer(lbname)
                     continue

                  if self.common.isInputRIAS():
                     lbispublic = lb['is_public']
                     lbprivateips = lb['private_ips']
                     lbpublicips = lb['public_ips']
                  elif self.common.isInputTerraform():
                     lbispublic = lb['type'] == "public"
                     lbprivateips = lb['private_ips']
                     lbpublicips = lb['public_ips']
                  else:  # yaml
                     lbispublic = lb['isPublic']
                     lbprivateips = lb['privateIPs']
                     lbpublicips = lb['publicIPs']

                  lbiplist = ""
                  if lbispublic == False:
                     for lbprivateip in lbprivateips:
                        if self.common.isInputRIAS():
                           ip = lbprivateip['address']
                        else:
                           ip = lbprivateip
                        if lbiplist == "":
                           lbiplist = ip
                        else:
                           lbiplist = lbiplist + "<br>" + ip
                  else:
                     for lbpublicip in lbpublicips:
                        if self.common.isInputRIAS():
                           ip = lbpublicip['address']
                        else:
                           ip = lbpublicip
                        if lbiplist == "":
                           lbiplist = ip
                        else:
                           lbiplist = lbiplist + "<br>" + ip

                  lbgenerated = False

                  for member in members:
                     if self.common.isInputRIAS():
                        # TODO Get instance id.
                        target = member['target']
                        address = target['address']
                     elif self.common.isInputTerraform():
                        instancename = None
                        memberaddress = member['target_address']
                        nicdata = self.data.getNetworkInterface3(memberaddress)
                        instances = self.data.getInstances()
                        if not instances.empty:
                           for instanceindex, instanceframe in instances.iterrows():
                              nics = instanceframe["networkInterfaces"]
                              for nicframe in nics:
                                 nicaddress = nicframe["primary_ipv4_address"]
                                 if memberaddress == nicaddress:
                                    saveinstanceframe = instanceframe
                                    instancename = saveinstanceframe["name"]
                                    break
                              if instancename != None:
                                 break
                        instanceframe = saveinstanceframe
                        instanceid = instanceframe['id']
                        instancevpcid = instanceframe['vpc']

                        if instancevpcid == vpcid:
                           if not lbgenerated:
                              lbgenerated = True
                              # TODO Handle spacing for > 1 LBs.
                              attributes = self.attributes.getNodeAttributes(label=lbname, sublabel=lbiplist, icon='loadbalancer', parentid=self.common.compress(vpcid))
                              lbid = randomid()
                              #lbid = self.common.compress(lbid)
                              nodes[self.common.compress(lbid)] = attributes
                              self.attributes.updateSequence(self.common.compress(lbid))

                              #routername = vpcname + '-router'
                              attributes = self.attributes.getDoubleArrowAttributes(sourceid=self.common.compress(lbid), targetid=self.common.compress(internetid))

                              edgeid = randomid()
                              edges[self.common.compress(edgeid)] = attributes
                              self.attributes.updateSequence(self.common.compress(edgeid))

                           # label, source, target
                           #instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                           attributes = self.attributes.getDoubleArrowAttributes(sourceid=self.common.compress(instanceid), targetid=self.common.compress(lbid))

                           edgeid = randomid()
                           edges[self.common.compress(edgeid)] = attributes
                           self.attributes.updateSequence(self.common.compress(edgeid))
                     else:
                        instanceid = member['instanceId']
                        instance = self.data.getInstance(instanceid)
                        if len(instance) > 0:
                           nics = instance['networkInterfaces']
                           if nics:
                              for nic in nics:
                                 address = nic['ip']
                                 break
                           else:
                              return clusters, nodes, edges
                        else:
                           return clusters, nodes, edges

                     if not self.common.isInputTerraform():
                        nicdata = self.data.getNetworkInterface(address, instanceid)
                        if len(nicdata) != 0:
                           nicid = nicdata['id']
                           nicinstanceid = nicdata['instance.id']
                           instanceframe = self.data.getInstance(nicinstanceid)
                           instancename = instanceframe['name']
                           instancevpcid = instanceframe['vpc.id']

                           if instancevpcid == vpcid:
                              if not lbgenerated:
                                 lbgenerated = True
                                 # TODO Handle spacing for > 1 LBs.
                                 meta = {}
                                 meta = meta | {'Type': "public" if lbispublic else "private"}
                                 meta = meta | {'IPs': lbiplist}
                                 attributes = self.attributes.getNodeAttributes(label=lbname, sublabel=lbiplist, icon='loadbalancer', data=meta, parentid=self.common.compress(vpcid))
                                 lbid = randomid()
                                 #lbid = self.common.compress(lbid)
                                 nodes[self.common.compress(lbid)] = attributes
                                 self.attributes.updateSequence(self.common.compress(lbid))

                                 #routername = vpcname + '-router'
                                 attributes = self.attributes.getDoubleArrowAttributes(sourceid=self.common.compress(lbid), targetid=self.common.compress(internetid))

                                 edgeid = randomid()
                                 edges[self.common.compress(edgeid)] = attributes
                                 self.attributes.updateSequence(self.common.compress(edgeid))

                              # label, source, target
                              #instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                              attributes = self.attributes.getDoubleArrowAttributes(sourceid=self.common.compress(instanceid), targetid=self.common.compress(lbid))

                              edgeid = randomid()
                              edges[self.common.compress(edgeid)] = attributes
                              self.attributes.updateSequence(self.common.compress(edgeid))

      return clusters, nodes, edges

   def composeNetworkACLs(self, vpcname, vpcid, clusters, nodes, edges, internetid):
      meta = {}
      acls = self.data.getNetworkACLs(vpcid)
      if acls != None:
          for acl in acls:
              #for aclid, aclmember in acl.items():
              #print(acl)
              aclname = acl['name']
              aclid = acl['id']
              #print(acl['subnetIds'])
              rules = acl['rules']
              count = 0
              for rule in rules:
                 count = count + 1
                 meta = meta | {'Rule' + str(count): rule}
              attributes = self.attributes.getNodeAttributes(label=aclname, icon='acl', data=meta, parentid=self.common.compress(vpcid))

              nodes[self.common.compress(aclid)] = attributes
              self.attributes.updateSequence(self.common.compress(aclid))

      return clusters, nodes, edges

   # Get zone CIDR.
   def getZoneCIDR(self, zone):
      match zone:
         case 'au-syd-1': cidr = ZoneCIDR.AU_SYD_1
         case 'au-syd-2': cidr = ZoneCIDR.AU_SYD_2
         case 'au-syd-3': cidr = ZoneCIDR.AU_SYD_3

         case 'br-sao-1': cidr = ZoneCIDR.BR_SAO_1
         case 'br-sao-2': cidr = ZoneCIDR.BR_SAO_2
         case 'br-sao-3': cidr = ZoneCIDR.BR_SAO_3

         case 'ca-tor-1': cidr = ZoneCIDR.CA_TOR_1
         case 'ca-tor-2': cidr = ZoneCIDR.CA_TOR_2
         case 'ca-tor-3': cidr = ZoneCIDR.CA_TOR_3

         case 'eu-de-1': cidr = ZoneCIDR.EU_DE_1
         case 'eu-de-2': cidr = ZoneCIDR.EU_DE_2
         case 'eu-de-3': cidr = ZoneCIDR.EU_DE_3

         case 'eu-gb-1': cidr = ZoneCIDR.EU_GB_1
         case 'eu-gb-2': cidr = ZoneCIDR.EU_GB_2
         case 'eu-gb-3': cidr = ZoneCIDR.EU_GB_3

         case 'jp-osa-1': cidr = ZoneCIDR.JP_OSA_1
         case 'jp-osa-2': cidr = ZoneCIDR.JP_OSA_2
         case 'jp-osa-3': cidr = ZoneCIDR.JP_OSA_3

         case 'jp-tok-1': cidr = ZoneCIDR.JP_TOK_1
         case 'jp-tok-2': cidr = ZoneCIDR.JP_TOK_2
         case 'jp-tok-3': cidr = ZoneCIDR.JP_TOK_3

         case 'us-east-1': cidr = ZoneCIDR.US_EAST_1
         case 'us-east-2': cidr = ZoneCIDR.US_EAST_2
         case 'us-east-3': cidr = ZoneCIDR.US_EAST_3

         case 'us-south-1': cidr = ZoneCIDR.US_SOUTH_1
         case 'us-south-2': cidr = ZoneCIDR.US_SOUTH_2
         case 'us-south-3': cidr = ZoneCIDR.US_SOUTH_3

         case _: cidr = ZoneCIDR.NONE

      return cidr.value
