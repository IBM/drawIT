# @file rias.py
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

from json import loads as json_load
from requests import post as post_request
from requests import get as get_request
from sys import exit as sys_exit
from urllib3 import disable_warnings 
from pandas import json_normalize

from .common import Common

class RIAS:
   floatingIPs = {}
   instances = {}
   clusters = {}
   keys = {}
   networkInterfaces = {}
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
   data = {}
   types = []
   common = None

   def __init__(self, common):
      self.types = ['vpcs', 'subnets', 'instances', 'public_gateways', 'floating_ips', 'vpn_gateways', 'endpoint_gateways', 'load_balancers']
      #self.types = ['vpcs', 'subnets', 'instances', 'clusters', 'public_gateways', 'floating_ips']
      self.common = common
      return

   def gettoken(self, accountID, apiKey):
      endpoint = 'https://iam.cloud.ibm.com'
      if len(accountID) > 0:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
         }
      data = {
         'grant_type': 'urn:ibm:params:oauth:grant-type:apikey', 
         'apikey': apiKey
      }
      disable_warnings()
      response = post_request(url=endpoint + "/identity/token", headers=headers, data=data, verify=False)
      token_dict = json_load(response.text)
      if 'errorCode' in token_dict:
         self.common.printResponseMessage(token_dict['errorCode'], token_dict['errorMessage']) 
         sys_exit()
      token = token_dict["token_type"] + " " + token_dict["access_token"]
      return token

   def getriasdata(self, token, accountID, group):
      #version = '2022-03-15'
      version = '2022-07-05'
      endpoint = 'https://' + self.common.getRegion().value + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         if group == 'vpn_gateways' or group == 'endpoint_gateways' or group == 'load_balancers':
            # Exit for now as causing error with other accounts:
            #    not_authorized: The request is not authorized. href=https://us-south.iaas.cloud.ibm.com/v1/vpn_gateways
            return {}
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': '2'
      }
      request = endpoint + "/v1/" + group
      response = get_request(url=request, headers=headers, params=params, verify=False)
      print(request)
      print(response)
      rawdata = json_load(response.text)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         self.common.printRequestMessage(error['code'], error['message'], request) 
         sys_exit()
      elif group == "vpcs" and rawdata['total_count'] == 0:
         #self.common.printMissingVPCs('href=' + request)
         self.common.printMissingVPCs()
         sys_exit()
      elif group == "subnets" and rawdata['total_count'] == 0:
         #self.commonprintMissingSubnets('href=' + request)
         self.commonprintMissingSubnets()
         sys_exit()
      data = rawdata[group]
      #if group == "vpcs":
      #   for vpc in data:
      #      print(vpc["name"])
      return data

   def getriasdatavpc(self, token, accountID, group, designatedVPC):
      #version = '2022-03-15'
      version = '2022-07-05'
      endpoint = 'https://' + self.common.getRegion().value + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         if group == 'vpn_gateways' or group == 'endpoint_gateways' or group == 'load_balancers':
            # Exit for now as causing error with other accounts:
            #    not_authorized: The request is not authorized. href=https://us-south.iaas.cloud.ibm.com/v1/vpn_gateways
            return {}
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': '2'
      }
      request = endpoint + "/v1/" + group
      #request = endpoint + "/v1/" + group + "/" + designatedVPC
      response = get_request(url=request, headers=headers, params=params, verify=False)
      rawdata = json_load(response.text)
      print("rawdata:")
      print(rawdata)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         self.common.printRequestMessage(error['code'], error['message'], request) 
         sys_exit()
      #elif group == "vpcs" and rawdata['total_count'] == 0:
      #   #self.common.printMissingVPCs('href=' + request)
      #   self.common.printMissingVPCs()
      #   sys_exit()
      #elif group == "subnets" and rawdata['total_count'] == 0:
      #   #self.commonprintMissingSubnets('href=' + request)
      #   self.commonprintMissingSubnets()
      #   sys_exit()
      #data = rawdata[group]
      data = rawdata
      #if group == "vpcs":
      #   for vpc in data:
      #      print(vpc["name"])
      return data

   def getriassubdata(self, token, accountID, id, group, subgroup):
      #version = '2022-05-31'
      version = '2022-07-05'
      endpoint = 'https://' + self.common.getRegion().value + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': 2
      }
      request = endpoint + "/v1/" + group + '/' + id + '/' + subgroup
      response = get_request(url=request, headers=headers, params=params, verify=False)
      rawdata = json_load(response.text)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         self.common.printRequestMessage(error['code'], error['message'], request) 
         sys_exit()
      #data = rawdata[group]
      #data = rawdata[subgroup]
      #return data
      return rawdata

   def getriassubdata2(self, token, accountID, id, group, subgroup, id2, subgroup2):
      #version = '2022-05-31'
      version = '2022-07-05'
      endpoint = 'https://' + self.common.getRegion().value + '.iaas.cloud.ibm.com'
      if len(accountID) > 0:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token,
            'X-Account-ID': accountID
         }
      else:
         headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Authorization': token
         }
      params = {
         'version': version, 
         'generation': '2'
      }
      request = endpoint + "/v1/" + group + '/' + id + '/' + subgroup + '/' + id2 + '/' + subgroup2
      response = get_request(url=request, headers=headers, params=params, verify=False)
      rawdata = json_load(response.text)
      if 'errors' in rawdata:
         errors = rawdata['errors']
         error = errors[0]
         self.common.printRequestMessage(error['code'], error['message'], request) 
         sys_exit()
      #data = rawdata[group]
      #data = rawdata[subgroup2]
      #return data
      return rawdata

   def loadRIAS(self):
      listenerdata = []
      pooldata = []
      memberdata = []
      #nicdata = []
      vpndata = []
      token = self.gettoken(self.common.getAccountID(), self.common.getAPIKey())
      #rawdata = getriasdata(self.common, token, accountid, 'vpcs')
      #data[datatype] = rawdata
      #return data
 
      for datatype in self.types:
         #designatedVPC = self.common.getDesignatedVPC()
         #if designatedVPC == '*':
         #   rawdata = self.getriasdata(token, self.common.getAccountID(), datatype)
         #else:
         #   rawdata = self.getriasdatavpc(token, self.common.getAccountID(), datatype, designatedVPC)
         rawdata = self.getriasdata(token, self.common.getAccountID(), datatype)
         self.data[datatype] = rawdata

      self.normalizeData()

      if 'load_balancers' in self.types:
         self.loadLoadBalancersSubdata(token)

      return

   def loadLoadBalancersSubdata(self, token):
      datatype = 'load_balancers'
      lbdata = self.data[datatype]
      for lb in lbdata:
         id = lb['id']
         lbname = lb['name']
         lbsubnets = lb['subnets']
         lbsubnet = lbsubnets[0]
         lbsubnetid = lbsubnet['id']
         subnet = self.getSubnet(lbsubnetid)
         if not 'vpc.id' in subnet:
            continue

         vpcid = subnet['vpc.id']

         rawdata = self.getriassubdata(token, self.common.getAccountID(), id, datatype, 'listeners')
         listeners = rawdata['listeners']
         listenerdict = {} 
         lblistenerdata = []
         extended = {}

         for listener in listeners:
            listenerid = listener['id']

            extended = listener
            extended['lbid'] = id
            lblistenerdata.append(extended)

            listenerdict = {'id': id, 'listeners': lblistenerdata}
            lblistenerdata.append(listenerdict)

            rawdata = self.getriassubdata(token, self.common.getAccountID(), id, datatype, 'pools')
            pools = rawdata['pools']
            pooldict = {} 
            memberdict = {} 
            lbpooldata = []
            lbmemberdata = []
            extended = {}
            for pool in pools:
               poolid = pool['id']

               extended = pool
               extended['lbid'] = id
               #pooldata.append(extended)

               rawdata = self.getriassubdata2(token, self.common.getAccountID(), id, datatype, 'pools', poolid, 'members')
               members = rawdata['members']
               lbmemberdata.append(members)

               for member in members:
                  # TODO Review need for target, address, instance with RIAS.
                  #target = member['target']
                  #address = target['address'] if address in target 
                  #instance = self.findRow2(self.getInstances(), 'vpc.id', vpcid, 'ip', address)

                  extended['members'] = members
                  lbpooldata.append(extended)

            memberdict = {'id': id, 'name': lbname, 'listeners': lblistenerdata, 'pools': lbpooldata}
            lbmemberdata.append(memberdict)

      self.data['load_balancer_listeners'] = lblistenerdata
      self.data['load_balancer_pools'] = lbpooldata
      self.data['load_balancer_members'] = lbmemberdata
      #self.data['load_balancers'] = memberdata
  
      return

   def findRow(self, dictionarylist, columnname, columnvalue):
      if len(dictionarylist) > 0:
         for dictionaryindex, dictionary in dictionarylist.iterrows():
            if columnname in dictionary:
               if dictionary[columnname] == columnvalue:
                  return dictionary
      return {}

   def findRow2(self, dictionarylist, columnname1, columnvalue1, columnname2, columnvalue2):
      if len(dictionarylist) > 0:
         for dictionaryindex, dictionary in dictionarylist.iterrows():
            if columnname1 in dictionary and columnname2 in dictionary:
               if dictionary[columnname1] == columnvalue1 and dictionary[columnname2] == columnvalue2:
                  return dictionary
      return {}

   def normalizeData(self):
      self.vpcs = json_normalize(self.data['vpcs'] if ('vpcs' in self.data) else json_normalize({}))
      self.subnets = json_normalize(self.data['subnets'] if ('subnets' in self.data) else json_normalize({}))
      self.instances = json_normalize(self.data['instances'] if ('instances' in self.data) else json_normalize({}))
      self.instances['type'] = 'Instance'
      self.networkInterfaces = json_normalize(self.data['network_interfaces'] if ('network_interfaces' in self.data) else json_normalize({}))
      self.publicGateways = json_normalize(self.data['public_gateways'] if ('public_gateways' in self.data) else json_normalize({}))
      self.floatingIPs = json_normalize(self.data['floating_ips'] if ('floating_ips' in self.data) else json_normalize({}))
      self.vpnGateways = json_normalize(self.data['vpn_gateways'] if ('vpn_gateways' in self.data) else json_normalize({}))
      self.vpnConnections = json_normalize({})
      self.vpeGateways = json_normalize(self.data['vpes'] if ('vpes' in self.data) else json_normalize({}))
      self.loadBalancers = json_normalize(self.data['load_balancers'] if ('load_balancers' in self.data) else json_normalize({}))
      #self.loadBalancerListeners = json_normalize(self.data['load_balancer_listeners'] if ('load_balancer_listeners' in self.data) else json_normalize({}))
      #self.loadBalancerPools = json_normalize(self.data['load_balancer_pools'] if ('load_balancer_pools' in self.data) else json_normalize({}))
      #self.loadBalancerMembers = json_normalize(self.data['load_balancer_members'] if ('load_balancer_members' in self.data) else json_normalize({}))
      self.clusters = json_normalize({})
      self.volumes = json_normalize({})
      self.networkACLs = json_normalize({})
      self.securityGroups = json_normalize({})
      self.services = json_normalize({})
      self.keys = json_normalize({})

      self.vpcs['type'] = 'VPC'
      self.subnets['type'] = 'Network'
      self.instances['type'] = 'Instance'
      self.clusters['type'] = 'OpenShift'
      self.networkInterfaces['type'] = 'NetworkInterface'
      self.publicGateways['type'] = 'PublicGateway'
      self.floatingIPs['type'] = 'FloatingIP'
      self.vpeGateways['type'] = 'VPE'

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

   def getInstance(self, id):
      return self.findRow(self.instances, 'id', id)

   def getCluster(self, id):
      return self.findRow(self.clusters, 'id', id)

   def getSubnet(self, id):
      return self.findRow(self.subnets, 'id', id)

   def getVPC(self, id):
      return self.findRow(self.vpcs, 'id', id)

   def getFloatingIP(self, id):
      return self.findRow(self.floatingIPs, 'target.id', id)

   def getPublicGateway(self, id):
      return self.findRow(self.publicGateways(), 'id', id)

   def getVPNGateway(self, id):
      if self.user.isInputRIAS() == 'rias':
         return self.findRow(self.vpnGateways, 'subnet.id', id)
      else:
         return self.findRow(self.vpnGateways, 'networkId', id)
