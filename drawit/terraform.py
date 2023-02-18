# @file terraform.py
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

from sys import exit

from json import loads as json_load, dumps as json_dumps
from pandas import concat, DataFrame, json_normalize, read_json
from tabulate import tabulate

from .common import Common
from .icons import Icons

class Terraform:
   floatingIPs = {}
   instances = {}
   clusters = {}
   keys = {}
   networkInterfaces = {} # Used to match NICs referenced in LB members.
   loadBalancers = {}
   loadBalancerListeners = {}
   loadBalancerPools = {}
   loadBalancerMembers = {}
   networkACLs = {}
   publicGateways = {}
   securityGroups = {}
   subnets = {}
   volumes = {}
   vpcs = {}
   vpnGateways = {}
   vpnConnections = {}
   vpeGateways = {}
   services = {}
   types = {}
   data = {}
   common = None
   icons = None

   def __init__(self, common):
      self.types = ['vpcs', 'subnets', 'instances', 'clusters', 'public_gateways', 'floating_ips', 'vpn_gateways', 'load_balancers']
      self.common = common
      self.icons = Icons(common)
      return

   def loadTerraform(self):
      stream = open(self.common.getInputFile(), 'r', encoding='utf-8-sig')
      self.data = json_load(stream.read())
      resources = self.data['resources']
      df = json_normalize(resources)

      vpcs = df[df["type"] == "ibm_is_vpc"]
      subnets = df[df["type"] == "ibm_is_subnet"]

      if vpcs.empty:
         self.common.printMissingVPCs()
         exit()
      elif subnets.empty:
         self.common.printMissingSubnets()
         exit()

      tempvpcs = {}
      tempsubnets = {}
      tempinstances = {}
      temppublicGateways = {}
      tempfloatingIPs = {}
      temploadBalancers = {}
      temploadBalancerListeners = {}
      temploadBalancerPools = {}
      temploadBalancerMembers = {}

      vpcInstances = df[df["type"] == "ibm_is_vpc"]["instances"]
      subnetInstances = df[df["type"] == "ibm_is_subnet"]["instances"]
      instanceInstances = df[df["type"] == "ibm_is_instance"]["instances"]
      publicGatewayInstances = df[df["type"] == "ibm_is_public_gateway"]["instances"]
      floatingIPInstances = df[df["type"] == "ibm_is_floating_ip"]["instances"]
      loadBalancerInstances = df[df["type"] == "ibm_is_lb"]["instances"]
      loadBalancerListenerInstances = df[df["type"] == "ibm_is_lb_listener"]["instances"]
      loadBalancerPoolInstances = df[df["type"] == "ibm_is_lb_pool"]["instances"]
      loadBalancerMemberInstances = df[df["type"] == "ibm_is_lb_pool_member"]["instances"]

      count = 0
      tempvpcs = {}
      for instances in vpcInstances: 
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #tempvpcs[instanceid] = instanceattributes
         tempvpcs[count] = instancerow
         count += 1
         #print(json_dumps(instance["attributes"], indent=4))

      if tempvpcs != {}:
         self.vpcs = DataFrame.from_dict(tempvpcs, orient="index")
      else:
         self.vpcs = DataFrame()

      count = 0
      tempsubnets = {}
      for instances in subnetInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            region = instanceattributes["zone"]
            regionindex = region.rfind('-')
            region = region[0:regionindex]
            instancerow = {"id": instanceid, "region": region} | instanceattributes
         #tempsubnets[instanceid] = instanceattributes
         tempsubnets[count] = instancerow
         count += 1

      if tempsubnets != {}:
         self.subnets = DataFrame.from_dict(tempsubnets, orient="index")

         self.subnets.rename(
            columns={'zone': 'zone.name',
                     'vpc': 'vpc.id'}, inplace=True)

         self.subnets['vpc.name'] = self.subnets['vpc.id']
      else:
         self.subnets = DataFrame()

      count = 0
      tempinstances = {}
      for instances in instanceInstances:
          for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
          #tempinstances[instanceid] = instanceattributes
          tempinstances[count] = instancerow
          count += 1

      if tempinstances != {}:
         self.instances = DataFrame.from_dict(tempinstances, orient="index")

         #self.instances.rename(
         #   columns={'network_interfaces': 'networkInterfaces'}, inplace=True)
         self.instances.rename(
            columns={'primary_network_interface': 'networkInterfaces'}, inplace=True)

         self.instances['type'] = 'Instance'
      else:
         self.instances = DataFrame()

      count = 0
      temppublicGateways = {}
      for instances in publicGatewayInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #temppublicGateways[instanceid] = instanceattributes
         temppublicGateways[count] = instancerow
         count += 1

      if temppublicGateways != {}:
         self.publicGateways = DataFrame.from_dict(temppublicGateways, orient="index")
      else:
         self.publicGateways = DataFrame()

      count = 0
      tempfloatingIPs = {}
      for instances in floatingIPInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #tempfloatingIPs[instanceid] = instanceattributes
         tempfloatingIPs[count] = instancerow
         count += 1

      if tempfloatingIPs != {}:
         self.floatingIPs = DataFrame.from_dict(tempfloatingIPs, orient="index")
      else:
         self.floatingIPs = DataFrame()

      count = 0
      temploadBalancers = {}
      for instances in loadBalancerInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #temploadBalancers[instanceid] = instanceattributes
         temploadBalancers[count] = instancerow
         count += 1

      if temploadBalancers != {}:
         self.loadBalancers = DataFrame.from_dict(temploadBalancers, orient="index")
      else:
         self.loadBalancers = DataFrame()

      count = 0
      temploadBalancerListeners = {}
      for instances in loadBalancerListenerInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #temploadBalancerListeners[instanceid] = instanceattributes
         temploadBalancerListeners[count] = instancerow
         count += 1

      if temploadBalancerListeners != {}:
         self.loadBalancerListeners = DataFrame.from_dict(temploadBalancerListeners, orient="index")
      else:
         self.loadBalancerListeners = DataFrame()

      count = 0
      temploadBalancerPools = {}
      for instances in loadBalancerPoolInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #temploadBalancerPools[instanceid] = instanceattributes
         temploadBalancerPools[count] = instancerow
         count += 1

      if temploadBalancerPools != {}:
         self.loadBalancerPools = DataFrame.from_dict(temploadBalancerPools, orient="index")
      else:
         self.loadBalancerPools = DataFrame()

      count = 0
      temploadBalancerMembers = {}
      for instances in loadBalancerMemberInstances:
         for instance in instances:
            instanceattributes = instance["attributes"]
            instanceid = instanceattributes["id"]
            instancerow = {"id": instanceid} | instanceattributes
         #temploadBalancerMembers[instanceid] = instanceattributes
         temploadBalancerMembers[count] = instancerow
         count += 1

      if temploadBalancerMembers != {}:
         self.loadBalancerMembers = DataFrame.from_dict(temploadBalancerMembers, orient="index")
      else:
         self.loadBalancerMembers = DataFrame()

      self.clusters = DataFrame()
      self.vpnGateways = DataFrame()
      self.vpnConnections = DataFrame()
      self.vpeGateways = DataFrame()
      self.volumes = DataFrame()
      self.networkACLs = DataFrame()
      self.securityGroups = DataFrame()
      self.services = DataFrame()
      self.keys = DataFrame()

      #if self.data != None:
      #   self.normalizeData()

      return

   def normalizeData(self):
      self.vpcs = json_normalize(self.data['vpcs'] if ('vpcs' in self.data) else json_normalize({}))
      self.subnets = json_normalize(self.data['subnets'] if ('subnets' in self.data) else json_normalize({}))
      self.instances = json_normalize(self.data['instances'] if ('instances' in self.data) else json_normalize({}))
      self.clusters = json_normalize(self.data['clusters'] if ('clusters' in self.data) else json_normalize({}))
      self.networkInterfaces = json_normalize(self.data['networkInterfaces'] if ('networkInterfaces' in self.data) else json_normalize({}))
      self.publicGateways = json_normalize(self.data['publicGateways'] if ('publicGateways' in self.data) else json_normalize({}))
      self.floatingIPs = json_normalize(self.data['floatingIPs'] if ('floatingIPs' in self.data) else json_normalize({}))
      self.vpnGateways = json_normalize(self.data['vpnGateways'] if ('vpnGateways' in self.data) else json_normalize({}))
      self.vpnConnections = json_normalize(self.data['vpnConnections'] if ('vpnConnections' in self.data) else json_normalize({}))
      self.vpeGateways = json_normalize(self.data['vpes'] if ('vpes' in self.data) else json_normalize({}))
      self.loadBalancers = json_normalize(self.data['loadBalancers'] if ('loadBalancers' in self.data) else json_normalize({}))
      self.loadBalancerListeners = json_normalize(self.data['loadBalancerListeners'] if ('loadBalancerListeners' in self.data) else json_normalize({}))
      self.loadBalancerPools = json_normalize(self.data['loadBalancerPools'] if ('loadBalancerPools' in self.data) else json_normalize({}))
      self.loadBalancerMembers = json_normalize(self.data['loadBalancerMembers'] if ('loadBalancerMembers' in self.data) else json_normalize({}))
      self.volumes = json_normalize(self.data['volumes'] if ('volumes' in self.data) else json_normalize({}))
      self.networkACLs = json_normalize(self.data['networkACLs'] if ('networkACLs' in self.data) else json_normalize({}))
      self.securityGroups = json_normalize(self.data['securityGroups'] if ('securityGroups' in self.data) else json_normalize({}))
      self.services = json_normalize(self.data['services'] if ('services' in self.data) else json_normalize({}))
      self.keys = json_normalize(self.data['keys'] if ('keys' in self.data) else json_normalize({}))

      if not self.vpcs.empty:
         self.vpcs.rename(
            columns={'availabilityZone': 'zone.name'}, inplace=True)

      if not self.subnets.empty:
         self.subnets.rename(
            columns={'availabilityZone': 'zone.name',
                     'subnet': 'ipv4_cidr_block',
                     'publicGateway.id': 'public_gateway.id',
                     'vpcId': 'vpc.id'}, inplace=True)

         self.subnets['vpc.name'] = self.subnets['vpc.id'] 

      if not self.instances.empty:
         self.instances.rename(
            columns={'memoryGb': 'memory',
                     'bandwidthMb': 'bandwidth',
                     'cpuCount': 'vcpu.count',
                     'profile': 'profile.name',
                     'osVersion': 'image.name'}, inplace=True)
         if len(self.instances) == 1:
            for instanceindex, instanceframe in self.instances.iterrows():
               if instanceframe['name'] == '*':
                  self.addAllIcons()
                  self.common.setAllIcons()
                  break

      if not self.networkInterfaces.empty:
         self.networkInterfaces.rename(
            columns={'ip': 'primary_ip.address',
                     'networkId': 'subnet.id',
                     'instanceId': 'instance.id'}, inplace=True)

      if not self.vpnGateways.empty:
         self.vpnGateways.rename(
            columns={'floatingIP': 'floating_ip.address'}, inplace=True)

      return

   def addAllIcons(self):
      iconDictionary = self.icons.getIconDictionary()
      iconCount = len(iconDictionary)
      newinstances = concat([self.instances]*iconCount, ignore_index=True)
      iconIndex = 0

      for iconkey, iconvalue in iconDictionary.items():
         icon = iconvalue['icon']
         newinstances.at[iconIndex, 'name'] =  icon
         newinstances.at[iconIndex, 'id'] = icon + '-id'
         newinstances.at[iconIndex, 'networkInterfaces.id'] = icon + '-eth0-id'
         iconIndex += 1

      self.instances = newinstances

      for instanceindex, instanceframe in self.instances.iterrows():
         instanceid = instanceframe['id']
         niclist = instanceframe['networkInterfaces']
         nic = niclist[0]
         nic['id'] = instanceid + '-eth0'

      return

   def getFloatingIPs(self):
      return self.floatingIPs

   def getInstances(self):
      return self.instances

   def getClusters(self):
      return self.clusters

   def getKeys(self):
      return self.keys

   def getNetworkInterfaces(self):
      return self.networkInterfaces

   def getLoadBalancers(self):
      return self.loadBalancers

   def getLoadBalancerListeners(self):
      return self.loadBalancerListeners

   def getLoadBalancerPools(self):
      return self.loadBalancerPools

   def getLoadBalancerMembers(self):
      return self.loadBalancerMembers

   def getNetworkACLs(self):
      return self.networkACLs

   def getPublicGateways(self):
      return self.publicGateways

   def getSecurityGroups(self):
      return self.securityGroups

   def getSubnets(self):
      return self.subnets

   def setSubnets(self, subnets):
      self.subnets = subnets

   def getServices(self):
      return self.services

   def setServices(self, services):
      self.services = services

   def getVolumes(self):
      return self.volumes

   def getVPCs(self):
      return self.vpcs

   def setVPCs(self, vpcs):
      self.vpcs = vpcs

   def getVPNGateways(self):
      return self.vpnGateways

   def getVPNConnections(self):
      return self.vpnConnections

   def getVPEGateways(self):
      return self.vpeGateways
