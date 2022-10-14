# @file diagram.py
#
# Copyright IBM Corporation 2022
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
#   diagrams.py - iterate diagram objects, invokes shapes.py
#   shapes.py - build ibm types, invokes types.py
#   types.py - build drawio types, invokes xml.py with tables.py
#   elements.py - build drawio objects  

from math import isnan

from common.common import Common
from diagram.shapes import Shapes
from diagram.tables import names, points, zoneCIDRs 

class Diagram:
   data = None
   common = None
   shapes = None

   def __init__(self, common, data):
      self.common = common
      self.data = data
      self.shapes = Shapes(common)

   def buildDiagrams(self):
      outputFolder = self.common.getOutputFolder()
      if outputFolder[-1] != '/':
         self.common.setOutputFolder(outputFolder + '/')

      regiondata = {}

      for regionname, regionvalues in self.data.getRegionTable().items():
         vpcdata = self.buildVPCs(regionname, regionvalues)
         regiondata[regionname] = vpcdata

      for regionname, regionvalues in regiondata.items():
         #if self.userregion != "all" and self.userregion != regionname:
         if self.common.getRegion().value != "all" and self.common.getRegion().value != regionname:
            # Covers the case for Yaml data which includes all regions whereas RIAS data can include single or all regions.
            continue
         for vpcname, vpcvalues in regionvalues.items():
            self.shapes.buildXML(vpcvalues, regionname + ':' + vpcname)
            if self.common.isVPCSplit():
               self.shapes.dumpXML(regionname + "_" + vpcname + "_" + self.common.getOutputFile(), self.common.getOutputFolder())
               self.shapes.resetXML()
         if self.common.isRegionSplit():
            self.shapes.dumpXML(regionname + "_" + self.common.getOutputFile(), self.common.getOutputFolder())
            self.shapes.resetXML()

         if self.common.isSingleSplit():
            self.shapes.dumpXML(self.common.getOutputFile(), self.common.getOutputFolder())

   def buildVPCs(self, regionname, regionvalues):
      data = {}

      publicx = 0
      publicy = 0
      publicnode = self.shapes.buildPublicNetwork(names['publicNetworkName'], '', names['publicNetworkName'], '', publicx, publicy, points['publicNetworkWidth'], points['publicNetworkHeight'], None)
      publicusernode = self.shapes.buildUser(names['publicUserName'], names['publicNetworkName'], names['publicUserName'], '', points['firstIconX'], points['firstIconY'], points['iconWidth'], points['iconHeight'], None)
      publicinternetnode = self.shapes.buildInternet(names['internetName'], names['publicNetworkName'], names['internetName'], '', points['secondIconX'], points['secondIconY'], points['iconWidth'], points['iconHeight'], None)

      enterprisex = 0
      enterprisey = points['publicNetworkHeight'] + points['groupSpace']
      enterprisenode = self.shapes.buildEnterpriseNetwork(names['enterpriseNetworkName'], '', names['enterpriseNetworkName'], '', enterprisex, enterprisey, points['enterpriseNetworkWidth'], points['enterpriseNetworkHeight'], None)
      enterpriseusernode = self.shapes.buildUser(names['enterpriseUserName'], names['enterpriseNetworkName'], names['enterpriseUserName'], '', points['firstIconX'], points['firstIconY'], points['iconWidth'], points['iconHeight'], None)

      if self.common.isLogicalShapes():
         cloudname = "Cloud"
      else:
         cloudname = "IBM Cloud"

      for vpcid in regionvalues:
         #vpcframe = findrow(user, self.inputdata['vpcs'], 'id', vpcid)
         vpcframe = self.data.getVPC(vpcid)
         if len(vpcframe) == 0:
            self.common.printInvalidVPC(vpcid)
         else:
            nodes = []
            links = []
            values = []
            
            nodes.append(publicnode)
            nodes.append(publicusernode)
            nodes.append(publicinternetnode)

            #SAVE publiclink = genlink(user, publicname, publicname, internetname)
            #SAVE links.append(publiclink)

            publicuserlink = self.shapes.buildDoubleArrow('', names['internetName'], names['publicUserName'], None)
            links.append(publicuserlink)

            nodes.append(enterprisenode)
            nodes.append(enterpriseusernode)

            enterpriseuserlink = self.shapes.buildDoubleArrow('', names['internetName'], names['enterpriseUserName'], None)
            links.append(enterpriseuserlink)

            vpcname = vpcframe['name']

            #SAVE if not vpcname.startswith('jww'):
            #SAVE    continue
         
            zonenodes, zonelinks, zonevalues, zonesizes = self.buildZones(vpcname, vpcid)
            nodes = nodes + zonenodes
            links = links + zonelinks
            values = values + zonevalues

            width = points['iconWidth']
            height = points['iconHeight']

            routername = vpcname + '-router'
            routernode = self.shapes.buildRouter(routername, vpcid, '', '', points['firstIconX'], points['firstIconY'], width, height, None)
            nodes.append(routernode)

            routerlink = self.shapes.buildDoubleArrow('', routername, names['internetName'], None)
            links.append(routerlink)

            width = 0
            height = 0
            for size in zonesizes:
               if size[0] > width:
                  width = size[0]

               height = height + size[1] + points['groupSpace']

            width = points['leftSpace'] + width + points['groupSpace']  # space after inner groups
            height = height + points['topSpace'] # space at top of outer group to top inner group
            height  = height - points['groupSpace']  # TODO Remove extra groupspace.

            x = points['groupSpace']
            y = points['topSpace']

            vpcnode = self.shapes.buildVPC(vpcid, regionname, vpcname, '', x, y, width, height, None) 
            nodes.append(vpcnode)

            x = 30
            y = 70

            width = width + (points['groupSpace'] * 2)
            height = height + (points['topSpace'] + points['groupSpace'])

            regionnode = self.shapes.buildRegion(regionname, cloudname, regionname, '', x, y, width, height, None)
            nodes.append(regionnode)
         
            lbnodes, lblinks  = self.buildLoadBalancers(vpcname, vpcid)
            if len(lbnodes) > 0:
               nodes = nodes + lbnodes
               links = links + lblinks

            #publicwidth = (groupspace * 2) + (48 * 3)
            #x  = (groupspace * 4) + (48 * 3)  # Allow space for public network.
            x = points['publicNetworkWidth'] + points['groupSpace']  # Allow space for public network.
            y = 0

            width = width + (points['groupSpace'] * 2)
            height = height + (points['topSpace'] + points['groupSpace'])

            cloudnode = self.shapes.buildCloud(cloudname, '', cloudname, '', x, y, width, height, None)
            nodes.append(cloudnode)
   
            data[vpcname] = {'nodes': nodes, 'values': values, 'links': links}

      return data

   def buildZones(self, vpcname, vpcid):
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0

      vpcTable = self.data.getVPCTable() 
      count = 0
      for regionzonename in vpcTable[vpcid]:
         count = count + 1

         zonelink = self.shapes.buildLink(regionzonename + ':' + vpcname, regionzonename, vpcname, None)
         #SAVE links.append(zonelink)

         subnetnodes, subnetlinks, subnetvalues, subnetsizes = self.buildSubnets(regionzonename, vpcname)
         nodes = nodes + subnetnodes
         links = links + subnetlinks
         values = values + subnetvalues

         width = 0
         height = 0

         for size in subnetsizes:
            if size[0] > width:
               width = size[0]

            height = height + size[1] + points['groupSpace']

         width = points['leftSpace'] + width + points['groupSpace']
         height = height + points['topSpace']  # space at top of outer group to top inner group
         height = height - points['groupSpace']

         x = (points['iconSpace'] * 2) + points['iconWidth']
         y = points['topSpace'] + saveheight + (points['groupSpace'] * (count - 1))

         saveheight += height

         zonename = regionzonename.split(':')[1]
         if zonename in zoneCIDRs:
            zonecidr = zoneCIDRs[zonename]
         else:
            zonecidr = ''

         zonenode = self.shapes.buildZone(regionzonename, vpcid, regionzonename, zonecidr, x, y, width, height, None)
         nodes.append(zonenode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([points['leftSpace'] - points['groupSpace'], 0])

      return nodes, links, values, sizes

   def buildSubnets(self, zonename, vpcname): 
      nodes = []
      links = []
      values = []
      sizes = []

      saveheight = 0

      zoneTable = self.data.getZoneTable()
      count = 0
      save_subnetpubgateid = None

      for subnetid in zoneTable[zonename]:
         count = count + 1
         pubgateid = None

         width = 0
         height = 0

         #subnetframe = findrow(user, self.inputdata['subnets'], 'id', subnetid)
         subnetframe = self.data.getSubnet(subnetid)
         subnetname = subnetframe['name']
         subnetid = subnetframe['id']

         subnetzonename = subnetframe['zone.name']
         subnetregion = 'us-south-1'
         subnetvpcid = subnetframe['vpc.id']
         subnetvpcname = subnetframe['vpc.name']
         subnetcidr = subnetframe['ipv4_cidr_block']

         #vpcframe = findrow(user, self.inputdata['vpcs'], 'id', subnetvpcid)
         vpcframe = self.data.getVPC(subnetvpcid)
         subnetvpcname = subnetframe['name']

         regionname = zonename.split(':')[0]
         regionzonename = regionname + ':' + subnetzonename;

         zonelink = self.shapes.buildLink(regionzonename + ':' + subnetname, regionzonename, subnetname, None)
         #SAVE links.append(zonelink)

         if 'public_gateway.id' in subnetframe:
            subnetpubgateid = subnetframe['public_gateway.id']
         else:
            subnetpubgateid = None

         pubgatefipip = None
         pubgatename = None
         if subnetpubgateid != None:
            #pubgateframe = findrow(user, self.inputdata['publicGateways'], 'id', subnetpubgateid)
            pubgateframe = self.data.getPublicGateway(subnetpubgateid)
            if len(pubgateframe) > 0:
               if self.common.isInputRIAS(): 
                  pubgatefipip = pubgateframe['floating_ip.address']
               else: # yaml
                  pubgatefipip = pubgateframe['floatingIP']
               pubgatename = pubgateframe['name']

         vpngateip = None
         vpngatename = None
         vpngateways = self.data.getVPNGateways()
         if not vpngateways.empty:
            vpngateframe = self.data.getVPNGateway(subnetid)
            #if self.common.isInputRIAS():
            #   vpngateframe = findrow(user, self.inputdata['vpnGateways'], 'subnet.id', subnetid)
            #else:
            #   vpngateframe = findrow(user, self.inputdata['vpnGateways'], 'networkId', subnetid)
            if len(vpngateframe) > 0:
               vpngateid = vpngateframe['id']
               # TODO Retrieve VPNGatewayMember[], 
               #      For each memberi get public_ip and private_ip.
               vpngateip = ''
               vpngatename = vpngateframe['name']
               vpnsubnetid = subnetid

         instancenodes, instancelinks, instancevalues, instancesizes = self.buildInstances(subnetid, subnetname, subnetvpcname, vpcname)

         nodes = nodes + instancenodes
         links = links + instancelinks
         values = values + instancevalues

         bastion = False
         if subnetname.lower().find("bastion") != -1:
            bastion = True

         if (len(instancesizes) == 0):
            width = points['minGroupWidth']
            height = points['minGroupHeight']
         else:
            width = points['groupSpace']
            height = 0

         for size in instancesizes:
            width = width + size[0] + points['groupSpace']

            if size[1] > height:
               height = size[1]

         # Leave height as groupheight if no instances.
         if (len(instancesizes) != 0):
            height = height + points['topSpace'] + points['groupSpace']  # space at top and bottom of group

         #SAVE x = (iconspace * 2) + iconwidth
         #SAVE y = topspace + (height * (count - 1)) + (groupspace * (count - 1))

         x = (points['iconSpace'] * 2) + points['iconWidth']
         y = points['topSpace'] + saveheight + (points['groupSpace'] * (count - 1))

         saveheight += height

         subnetnode = self.shapes.buildSubnet(subnetid, regionzonename, subnetname, subnetcidr, x, y, width, height, None) 
         nodes.append(subnetnode)
         sizes.append([width, height])

         if count == 1:
            sizes.append([points['leftSpace'] - points['groupSpace'], 0])

         internetname = 'Internet'

         if pubgatefipip != None:

            if save_subnetpubgateid == None:
               save_subnetpubgateid = subnetpubgateid

               publicnode = self.shapes.buildPublicGateway(subnetpubgateid, regionzonename, pubgatename, pubgatefipip, points['firstIconX'], points['firstIconY'], points['iconWidth'], points['iconHeight'], None)
               nodes.append(publicnode)

               routername = vpcname + '-router'
               publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid, None)
               links.append(publiclink1)
               publiclink2 = self.shapes.buildSingleArrow('', subnetpubgateid, routername, None)
               links.append(publiclink2)

            elif subnetpubgateid != save_subnetpubgateid:
               self.common.printInvalidPublicGateway(subnetpubgateid)

            else:
               publiclink1 = self.shapes.buildSingleArrow('', subnetid, subnetpubgateid, None)
               links.append(publiclink1)

         if vpngateip != None:
             # TODO Handle >1 VPN gateways.
            #vpngatenode = self.shapes.buildVPNGateway(vpngatename, regionzonename, vpngatename, vpngateip, points['thirdIconX'], points['thirdIconY'], points['iconWidth'], points['iconHeight'])
            vpngatenode = self.shapes.buildVPNGateway(vpngatename, subnetvpcid, vpngatename, vpngateip, points['thirdIconX'], points['thirdIconY'], points['iconWidth'], points['iconHeight'], None)
            nodes.append(vpngatenode)
                
            routername = vpcname + '-router'
            # This link can be assumed since everything inside zone is accesible by the VPN.
            #vpnlink1 = gensolidlink_doublearrow(user, '', subnetname, vpngatename)
            #links.append(vpnlink1)
            vpnlink1 = self.shapes.buildDoubleArrow('', regionzonename, vpngatename, None)
            links.append(vpnlink1)
            vpnlink2 = self.shapes.buildDoubleArrow('', vpngatename, routername, None)
            links.append(vpnlink2)

            # label, source, target 
            #vpngatelink1 = gensolidlink_doublearrow(user, '', subnetname, vpngatename)
            #links.append(vpngatelink1)

            # label, source, target 
            #vpngatelink2 = gensolidlink_doublearrow(user, '', vpngatename, username)
            #links.append(vpngatelink2)

      return nodes, links, values, sizes

   def buildInstances(self, subnetid, subnetname, subnetvpcname, vpcname):
      nodes = []
      links = []
      values = []
      sizes = []

      #nicstable = self.setupdata['nics']
      instances = self.data.getInstanceTable(subnetid)

      count = 0

      #for nicframe in nicstable[subnetid]:
      for instanceframe in instances:
         count = count + 1

         instancename = instanceframe['name']
         instanceid = instanceframe['id']
         nics = self.data.getNICTable(subnetid, instanceid)

         nicips = ''
         nicid = ''
         nicfipid = None
         nicfipip = None
         nicfipname = None

         #nics = instanceframe['network_interfaces'] if self.common.isInputRIAS() else instanceframe['networkInterfaces']

         #for nicframe in nics:
         for nicframe in nics:
            #if nicframe.empty:
            #   continue

            nicname = nicframe['name']
            #nicinstanceid = nicframe['instance.id']
            nicinstanceid = instanceframe['id'] if self.common.isInputRIAS() else nicframe['instanceId']

            #nicip = nicframe['primary_ip.address']
            nicip = nicframe['primary_ip']['address'] if self.common.isInputRIAS() else nicframe['ip']
            if nicips == '':
               nicips = nicip
            else:
              nicips = nicips + '<br>' + nicip
            nicid = nicframe['id']
            #fipframe = findrow(user, self.inputdata['floatingIPs'], 'target.id', nicid)
            fipframe = self.data.getFloatingIP(nicid)
            if len(fipframe) > 0:
               nicfipid = fipframe['id']
               nicfipip = fipframe['address']
               nicfipname = fipframe['name']

         #old instanceframe = findrow(user, self.inputdata['instances'], 'id', nicinstanceid)
         #instanceframe = self.data.getInstance(nicinstanceid)
         #if len(instanceframe) == 0:
         #   self.common.printInvalidInstance(nicinstanceid)
         #   continue

         instancename = instanceframe['name']
         instanceid = instanceframe['id']

         instanceOS = instanceframe['image.name']
         if instanceOS == None:
            instanceOS = 'Unknown OS'
         instanceprofile = instanceframe['profile.name'] 
         instancememory = instanceframe['memory']

         bandwidth = instanceframe['bandwidth']
         if bandwidth == '' or (isinstance(bandwidth, float) and isnan(bandwidth)):
            instancecpuspeed = 0
         else:
            instancecpuspeed = int(instanceframe['bandwidth'] / 1000)

         instancecpucount = instanceframe['vcpu.count']

         osdetails = instanceOS
         profiledetails = instanceprofile
         storagedetails = '100GB/3000IOPS'

         if self.common.isLowDetail(): 
            width = points['iconWidth']
            height = points['iconHeight']
            extrawidth = width * 3
            extraheight = height * 2
            x = width + (extrawidth * (count - 1)) + (points['groupSpace'] * count)
            y = points['topSpace']
         else:
            width = 240
            height = 152
            x = (width * (count - 1)) + (points['groupSpace'] * count) 
            y = points['topSpace']

         #SAVE x = (width * (count - 1)) + (groupspace * count) 
         #SAVE y = topspace

         #SAVE instancenode = geninstance(user, instancename, subnetname, nicip, instancedetails, width, height, x, y)

         #SAVE osnode = geninstanceexpandedstack(user, instancename, subnetname, nicip, width, height, x, y)

         bastion = False

         meta = {'Operating-System': osdetails,
                 'Instance-Profile': profiledetails,
                 'Boot-Volume': storagedetails} 

         if self.common.isLowDetail(): 
            if instancename.lower().find("bastion") != -1:
               bastion = True
               instancenode = self.shapes.buildInstanceBastion(nicid, subnetid, instancename, nicips, x, y, width, height, meta)
            else:
               instancenode = self.shapes.buildInstance(nicid, subnetid, instancename, nicips, x, y, width, height, meta)
            sizes.append([extrawidth, extraheight])
         else:
            if instancename.lower().find("bastion") != -1:
               bastion = True
               instancenode = self.shapes.buildInstanceBastionExpandedStack(nicid, subnetid, instancename, nicips, x, y, width, height, meta)
            else:
               instancenode = self.shapes.buildInstanceExpandedStack(nicid, subnetid, instancename, nicips, x, y, width, height, meta)
            sizes.append([width, height])

         nodes.append(instancenode)

         if not self.common.isLowDetail(): 
            textwidth = width - (points['textGroupSpace'] * 2)
            textheight = height - (points['textTopSpace'] + points['textGroupSpace'])

            textx = points['textGroupSpace']
            texty = points['textTopSpace']

            #textid = nicid + ':details'
            textid = instanceid + ':details'
            textname = instancename + ':details'

            stackwidth = 252
            stackheight = 16
            stackx = 16
            stacky = 64
            osnode = self.shapes.buildItemOS(nicid + ':' + osdetails, nicid, osdetails, '', stackx, stacky, stackwidth, stackheight, None)
            profilenode = ''
            if profiledetails[0] == 'b':
               profilenode = self.shapes.buildItemProfileBalanced(nicid + ':' + profiledetails, nicid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight, None)
            elif profiledetails[0] == 'c' or profiledetails[0] == 'g':
               profilenode = self.shapes.buildItemProfileCompute(nicid + ':' + profiledetails, nicid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight, None)
            elif profiledetails[0] == 'm' or profiledetails[0] == 'u' or profiledetails[1] == 'v':
               profilenode = self.shapes.buildItemProfileMemory(nicid + ':' + profiledetails, nicid, profiledetails, '', stackx, stacky + 24, stackwidth, stackheight, None)
            storagenode = self.shapes.buildItemBlockStorage(nicid + ':' + storagedetails, nicid, storagedetails, '', stackx, stacky + 48, stackwidth, stackheight, None)

            nodes.append(osnode)
            nodes.append(profilenode)
            nodes.append(storagenode)

         if nicfipip != None:
            # Save for option to show FIP icon.
            #SAVE fipnode = genfloatingip(user, nicfipname, nicfipip)
            #SAVE nodes.append(fipnode)
            #SAVE fiplink1 = gensolidlink_doublearrow(user, '', instancename, nicfipname)
            #SAVE links.append(fiplink1)
            #SAVE internetname = 'Internet'
            #SAVE fiplink2 = gensolidlink_doublearrow(user, '', nicfipname, internetname)
            #SAVE links.append(fiplink2)

            routername = vpcname + '-router'
            iplabel =  "fip:" + nicfipip
            #fiplink = self.shapes.buildDoubleArrow(iplabel, instanceid, routername)
            fiplink = self.shapes.buildDoubleArrow(iplabel, nicid, routername, None)
            links.append(fiplink)

      return nodes, links, values, sizes

   def buildLoadBalancers(self, vpcname, vpcid):
      nodes = []
      links = []

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
                     else:
                        instanceid = member['instanceId']
                        instance = self.data.getInstance(instanceid)
                        if len(instance) > 0:
                           addressarray = instance['ipAddresses']
                           address = addressarray[0]
                        else:
                           return nodes, links

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
                              lbnode = self.shapes.buildLoadBalancer(lbid, vpcid, lbname, lbiplist, points['secondIconX'], points['secondIconY'], points['iconWidth'], points['iconHeight'], None)
                              nodes.append(lbnode)
                              routername = vpcname + '-router'
                              lblink = self.shapes.buildDoubleArrow('', lbid, routername, None)
                              links.append(lblink)
                
                           # label, source, target
                           instancelink = self.shapes.buildDoubleArrow('', nicid, lbid, None)
                           links.append(instancelink)

      return nodes, links