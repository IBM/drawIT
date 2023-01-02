# @file iconsdac.py
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

from enum import Enum

#from .constants import Colors.lines[" ShapeKind
from .colors import Colors

class Icons:
   iconDictionary = { 
      'undefined': 	        
            {'icon': 'undefined', 'color': Colors.lines["network"]},
      'usercollaboration': 	        
            {'icon': 'collaborate', 'color': Colors.lines["user"]},
      'credentials': 	        
            {'icon': 'credentials', 'color': Colors.lines["network"]},
      'devices': 	        
            {'icon': 'devices', 'color': Colors.lines["user"]},
      'meeting': 	        
            {'icon': 'events', 'color': Colors.lines["user"]},
      'authorizationBoundary': 	        
            {'icon': 'flag', 'color': Colors.lines["network"]},
      'cloud-prescribed': 	        
            {'icon': 'ibm-cloud', 'color': Colors.lines["network"]},
      'user':  	        
            {'icon': 'user', 'color': Colors.lines["user"]}, 
      'vsi-logical': 	        
            {'icon': 'virtual-machine', 'color': Colors.lines["network"]},
      'vpc-logical':  	        
            {'icon': 'virtual-private-cloud', 'color': Colors.lines["network"]}, 
      'vpc-prescribed':  	        
            {'icon': 'virtual-private-cloud--alt', 'color': Colors.lines["network"]}, 
      'region': 	        
            {'icon': 'location', 'color': Colors.lines["location"]},
      'security': 	        
            {'icon': 'security', 'color': Colors.lines["security"]},
      'fingerprintrecognition': 	        
            {'icon': 'fingerprint-recognition', 'color': Colors.lines["network"]},
      'network2':  	        
            {'icon': 'network--2', 'color': Colors.lines["network"]}, 
      'edgenode':  	        
            {'icon': 'edge-node', 'color': Colors.lines["network"]}, 
      'group':  	        
            {'icon': 'group', 'color': Colors.lines["user"]}, 
      'mobile':  	        
            {'icon': 'mobile', 'color': Colors.lines["user"]}, 
      'policy':  	        
            {'icon': 'policy', 'color': Colors.lines["security"]}, 
      'rule':  	        
            {'icon': 'rule', 'color': Colors.lines["security"]}, 
      'terminal':  	        
            {'icon': 'terminal', 'color': Colors.lines["network"]}, 
      'objectstorage-prescribed':  	        
            {'icon': 'object-storage', 'color': Colors.lines["storage"]}, 
      'laptop':  	        
            {'icon': 'laptop', 'color': Colors.lines["user"]}, 
      'tablet':  	        
            {'icon': 'tablet', 'color': Colors.lines["user"]}, 
      'archive':  	        
            {'icon': 'archive', 'color': Colors.lines["network"]}, 
      'zone':  	        
            {'icon': 'data--base--alt', 'color': Colors.lines["location"]}, 
      'internet':  	        
            {'icon': 'wikis', 'color': Colors.lines["network"]}, 
      'database':  	        
            {'icon': 'data--base', 'color': Colors.lines["network"]}, 
      'subnet-logical':  	        
            {'icon': 'locked', 'color': Colors.lines["network"]}, 
      'application':  	        
            {'icon': 'application', 'color': Colors.lines["network"]}, 
      'arrows--horizontal': 	        
            {'icon': 'arrows--horizontal', 'color': Colors.lines["network"]},
      'cloud-logical': 
            {'icon': 'cloud', 'color': Colors.lines["network"]},
      'serverlessapplication': 	        
            {'icon': 'function', 'color': Colors.lines["network"]},
      'openshift':  	        
            {'icon': 'logo--openshift', 'color': Colors.lines["compute"]}, 
      'password': 	        
            {'icon': 'password', 'color': Colors.lines["network"]},
      'script': 	        
            {'icon': 'script', 'color': Colors.lines["network"]},
      'administrator': 	        
            {'icon': 'user--admin', 'color': Colors.lines["user"]},
      'cloudfoundry': 	        
            {'icon': 'cloud-foundry--1', 'color': Colors.lines["network"]},
      'cloud-satellite':  	        
            {'icon': 'cloud-satellite', 'color': Colors.lines["network"]}, 
      'timer':  	        
            {'icon': 'timer', 'color': Colors.lines["network"]}, 
      'deploy':  	        
            {'icon': 'deploy', 'color': Colors.lines["network"]}, 
      'shuffle': 	        
            {'icon': 'shuffle', 'color': Colors.lines["network"]},
      'wifi--controller': 	        
            {'icon': 'wifi--controller', 'color': Colors.lines["network"]},
      'switch-layer-3': 	        
            {'icon': 'switch-layer-3', 'color': Colors.lines["network"]},
      'vpngateway': 	        
            {'icon': 'gateway--vpn', 'color': Colors.lines["network"]},
      'baremetalserver': 	        
            {'icon': 'bare-metal-server', 'color': Colors.lines["compute"]},
      'switch-layer-2': 	        
            {'icon': 'switch-layer-2', 'color': Colors.lines["network"]},
      'loadbalancer-prescribed': 	        
            {'icon': 'load-balancer--vpc', 'color': Colors.lines["network"]},
      'aclrules': 	        
            {'icon': 'subnet-acl-rules', 'color': Colors.lines["security"]},
      'vpnconnection': 	        
            {'icon': 'vpn--connection', 'color': Colors.lines["network"]},
      'enterprisenetwork': 	        
            {'icon': 'network--enterprise', 'color': Colors.lines["network"]},
      'direct-link': 	        
            {'icon': 'direct-link', 'color': Colors.lines["network"]},
      'securityservices-prescribed': 	        
            {'icon': 'ibm-security--services', 'color': Colors.lines["network"]},
      'resourcegroup': 	        
            {'icon': 'group--resource', 'color': Colors.lines["network"]},
      'servicedeskuser': 	        
            {'icon': 'user--service-desk', 'color': Colors.lines["user"]},
      'document--protected': 	        
            {'icon': 'document--protected', 'color': Colors.lines["network"]},
      'securitygroup': 	        
            {'icon': 'group--security', 'color': Colors.lines["network"]},
      'application--virtual': 	        
            {'icon': 'application--virtual', 'color': Colors.lines["network"]},
      'load-balancer--pool': 	        
            {'icon': 'load-balancer--pool', 'color': Colors.lines["network"]},
      'vehicle--services': 	        
            {'icon': 'vehicle--services', 'color': Colors.lines["network"]},
      'security-services': 	        
            {'icon': 'security-services', 'color': Colors.lines["network"]},
      'user--military': 	        
            {'icon': 'user--military', 'color': Colors.lines["network"]},
      'message-queue': 	        
            {'icon': 'message-queue', 'color': Colors.lines["network"]},
      'databackup': 	        
            {'icon': 'data-backup', 'color': Colors.lines["network"]},
      'gui': 	        
            {'icon': 'gui', 'color': Colors.lines["network"]},
      'cloudmonitoring': 	        
            {'icon': 'cloud--monitoring', 'color': Colors.lines["management"]},
      'firewall': 	        
            {'icon': 'firewall', 'color': Colors.lines["security"]},
      'wifi--not-secure': 	        
            {'icon': 'wifi--not-secure', 'color': Colors.lines["network"]},
      'cdn': 	        
            {'icon': 'content-delivery-network', 'color': Colors.lines["network"]},
      'cloudalerting': 	        
            {'icon': 'cloud--alerting', 'color': Colors.lines["management"]},
      'flowlogs-prescribed': 	        
            {'icon': 'flow-logs-vpc', 'color': Colors.lines["management"]},
      'servicemanagement': 	        
            {'icon': 'cloud--service-management', 'color': Colors.lines["management"]},
      'nlb': 	        
            {'icon': 'load-balancer--network', 'color': Colors.lines["network"]},
      'publicnetwork': 	        
            {'icon': 'network--public', 'color': Colors.lines["network"]},
      'server--dns': 	        
            {'icon': 'server--dns', 'color': Colors.lines["network"]},
      'vehicle--api': 	        
            {'icon': 'vehicle--api', 'color': Colors.lines["network"]},
      'classicinfrastructure': 	        
            {'icon': 'infrastructure--classic', 'color': Colors.lines["network"]},
      'classicvsi': 	        
            {'icon': 'instance--classic', 'color': Colors.lines["network"]},
      'alb': 	        
            {'icon': 'load-balancer--application', 'color': Colors.lines["network"]},
      'ibm-cloud--dedicated-host': 	        
            {'icon': 'ibm-cloud--dedicated-host', 'color': Colors.lines["network"]},
      'internetservices-prescribed': 	        
            {'icon': 'ibm-cloud--internet-services', 'color': Colors.lines["network"]},
      'radio--push-to-talk': 	        
            {'icon': 'radio--push-to-talk', 'color': Colors.lines["network"]},
      'glb': 	        
            {'icon': 'load-balancer--global', 'color': Colors.lines["network"]},
      'firewall--classic': 	        
            {'icon': 'firewall--classic', 'color': Colors.lines["network"]},
      'blockstorage-logical': 	        
            {'icon': 'block-storage--alt', 'color': Colors.lines["network"]},
      'accessgroup': 	        
            {'icon': 'group--access', 'color': Colors.lines["network"]},
      'vpn--policy': 	        
            {'icon': 'vpn--policy', 'color': Colors.lines["network"]},
      'code-signing-service': 	        
            {'icon': 'code-signing-service', 'color': Colors.lines["network"]},
      'memoryprofile': 	        
            {'icon': 'instance--mx', 'color': Colors.lines["compute"]},
      'hybrid-networking--alt': 	        
            {'icon': 'hybrid-networking--alt', 'color': Colors.lines["network"]},
      'document--unprotected': 	        
            {'icon': 'document--unprotected', 'color': Colors.lines["network"]},
      'bastion-host': 	        
            {'icon': 'bastion-host', 'color': Colors.lines["network"]},
      'blob': 	        
            {'icon': 'data-blob', 'color': Colors.lines["network"]},
      'objectstorage-logical': 	        
            {'icon': 'object-storage--alt', 'color': Colors.lines["storage"]},
      'server--proxy': 	        
            {'icon': 'server--proxy', 'color': Colors.lines["network"]},
      'application--mobile': 	        
            {'icon': 'application--mobile', 'color': Colors.lines["network"]},
      'mobility--services': 	        
            {'icon': 'mobility--services', 'color': Colors.lines["network"]},
      'filestorage': 	        
            {'icon': 'file-storage', 'color': Colors.lines["storage"]},
      'router--wifi': 	        
            {'icon': 'router--wifi', 'color': Colors.lines["network"]},
      'intrusion-prevention': 	        
            {'icon': 'intrusion-prevention', 'color': Colors.lines["network"]},
      'edge-node--alt': 	        
            {'icon': 'edge-node--alt', 'color': Colors.lines["network"]},
      'vlan-prescribed': 	        
            {'icon': 'vlan--ibm', 'color': Colors.lines["network"]},
      'cloudservices': 	        
            {'icon': 'cloud-services', 'color': Colors.lines["network"]},
      'blockstorage-prescribed': 	        
            {'icon': 'block-storage', 'color': Colors.lines["storage"]},
      'floatingip': 	        
            {'icon': 'floating-ip', 'color': Colors.lines["network"]},
      'vehicle--connected': 	        
            {'icon': 'vehicle--connected', 'color': Colors.lines["network"]},
      'accountgroup': 	        
            {'icon': 'group--account', 'color': Colors.lines["network"]},
      'image-service': 	        
            {'icon': 'image-service', 'color': Colors.lines["network"]},
      'balancedprofile': 	        
            {'icon': 'instance--bx', 'color': Colors.lines["network"]},
      'objectstorageaccessor': 	        
            {'icon': 'data-accessor', 'color': Colors.lines["network"]},
      'gateway--user-access': 	        
            {'icon': 'gateway--user-access', 'color': Colors.lines["network"]},
      'document--signed': 	        
            {'icon': 'document--signed', 'color': Colors.lines["network"]},
      'application--web': 	        
            {'icon': 'application--web', 'color': Colors.lines["network"]},
      'instancegroup': 	        
            {'icon': 'autoscaling', 'color': Colors.lines["network"]},
      'lblistener': 	        
            {'icon': 'load-balancer--listener', 'color': Colors.lines["network"]},
      'radio--combat': 	        
            {'icon': 'radio--combat', 'color': Colors.lines["network"]},
      'user--settings': 	        
            {'icon': 'user--settings', 'color': Colors.lines["network"]},
      'wifi-bridge--alt': 	        
            {'icon': 'wifi-bridge--alt', 'color': Colors.lines["network"]},
      'pop': 	        
            {'icon': 'point-of-presence', 'color': Colors.lines["network"]},
      'datacenter': 	        
            {'icon': 'data--center', 'color': Colors.lines["network"]},
      'sim-card': 	        
            {'icon': 'sim-card', 'color': Colors.lines["network"]},
      'chat--operational': 	        
            {'icon': 'chat--operational', 'color': Colors.lines["network"]},
      'vpe-prescribed': 	        
            {'icon': 'ibm-cloud--vpc-endpoints', 'color': Colors.lines["network"]},
      'id-management': 	        
            {'icon': 'id-management', 'color': Colors.lines["network"]},
      'vsi-prescribed': 	        
            {'icon': 'instance--virtual', 'color': Colors.lines["compute"]},
      'gui--management': 	        
            {'icon': 'gui--management', 'color': Colors.lines["network"]},
      'virtual-desktop': 	        
            {'icon': 'virtual-desktop', 'color': Colors.lines["network"]},
      'computeprofile': 	        
            {'icon': 'instance--cx', 'color': Colors.lines["compute"]},
      'phone--settings': 	        
            {'icon': 'phone--settings', 'color': Colors.lines["network"]},
      'overlaynetwork': 	        
            {'icon': 'network--overlay', 'color': Colors.lines["network"]},
      'gateway': 	        
            {'icon': 'gateway', 'color': Colors.lines["network"]},
      'document--security': 	        
            {'icon': 'document--security', 'color': Colors.lines["network"]},
      'router': 	        
            {'icon': 'router', 'color': Colors.lines["network"]},
      'router--voice':  	        
            {'icon': 'router--voice', 'color': Colors.lines["network"]}, 
      'dns-services': 	        
            {'icon': 'dns-services', 'color': Colors.lines["network"]},
      'vlan-logical': 	        
            {'icon': 'vlan', 'color': Colors.lines["network"]},
      'server--time': 	        
            {'icon': 'server--time', 'color': Colors.lines["network"]},
      'gateway--api': 	        
            {'icon': 'gateway--api', 'color': Colors.lines["network"]},
      'wifi--secure': 	        
            {'icon': 'wifi--secure', 'color': Colors.lines["network"]},
      'gateway--mail': 	        
            {'icon': 'gateway--mail', 'color': Colors.lines["network"]},
      'publicgateway': 	        
            {'icon': 'gateway--public', 'color': Colors.lines["network"]},
      'phone--application': 	        
            {'icon': 'phone--application', 'color': Colors.lines["network"]},
      'transmission-lte': 	        
            {'icon': 'transmission-lte', 'color': Colors.lines["network"]},
      'vehicle--insights': 	        
            {'icon': 'vehicle--insights', 'color': Colors.lines["network"]},
      'activitytracker': 	        
            {'icon': 'cloud--auditing', 'color': Colors.lines["management"]},
      'hardware-security-module': 	        
            {'icon': 'hardware-security-module', 'color': Colors.lines["network"]},
      'two-factor-authentication': 	        
            {'icon': 'two-factor-authentication', 'color': Colors.lines["network"]},
      'wifi-bridge': 	        
            {'icon': 'wifi-bridge', 'color': Colors.lines["network"]},
      'classiclb': 	        
            {'icon': 'load-balancer--classic', 'color': Colors.lines["network"]},
      'locallb': 	        
            {'icon': 'load-balancer--local', 'color': Colors.lines["network"]},
      'cloud--logging': 	        
            {'icon': 'cloud--logging', 'color': Colors.lines["network"]},
      'subnet-prescribed': 	        
            {'icon': 'ibm-cloud--subnets', 'color': Colors.lines["network"]},
      'data-diode': 	        
            {'icon': 'data-diode', 'color': Colors.lines["network"]},
      'folderdetails': 	        
            {'icon': 'folder--details', 'color': Colors.lines["storage"]},
      'gateway--security': 	        
            {'icon': 'gateway--security', 'color': Colors.lines["network"]},
      'baremetalserver1': 	        
            {'icon': 'bare-metal-server--01', 'color': Colors.lines["network"]},
      'baremetalserver2':  	        
            {'icon': 'bare-metal-server--02', 'color': Colors.lines["network"]}, 
      'boot':  	        
            {'icon': 'boot', 'color': Colors.lines["network"]}, 
      'box--extra-large': 	        
            {'icon': 'box--extra-large', 'color': Colors.lines["network"]},
      'box--large': 	        
            {'icon': 'box--large', 'color': Colors.lines["network"]},
      'box--medium': 	        
            {'icon': 'box--medium', 'color': Colors.lines["network"]},
      'box--small': 	        
            {'icon': 'box--small', 'color': Colors.lines["network"]},
      'cloud-satellite--config':  	        
            {'icon': 'cloud-satellite--config', 'color': Colors.lines["network"]}, 
      'cloud-satellite--link':  	        
            {'icon': 'cloud-satellite--link', 'color': Colors.lines["network"]}, 
      'cloud-satellite--services':  	        
            {'icon': 'cloud-satellite--services', 'color': Colors.lines["network"]}, 
      'communication--unified': 	        
            {'icon': 'communication--unified', 'color': Colors.lines["network"]},
      'datastax': 	        
            {'icon': 'database--datastax', 'color': Colors.lines["network"]},
      'elasticdb': 	        
            {'icon': 'database--elastic', 'color': Colors.lines["network"]},
      'enterprisedb': 	        
            {'icon': 'database--enterprisedb', 'color': Colors.lines["network"]},
      'etcd': 	        
            {'icon': 'database--etcd', 'color': Colors.lines["network"]},
      'mongodb': 	        
            {'icon': 'database--mongodb', 'color': Colors.lines["network"]},
      'postgresql': 	        
            {'icon': 'database--postgresql', 'color': Colors.lines["network"]},
      'rabbitdb':	        
            {'icon': 'database--rabbit', 'color': Colors.lines["network"]},
      'redis': 	        
            {'icon': 'database--redis', 'color': Colors.lines["network"]},
      'directory-domain':  	        
            {'icon': 'directory-domain', 'color': Colors.lines["network"]}, 
      'encryption': 	        
            {'icon': 'encryption', 'color': Colors.lines["network"]},
      'ibm-cloud-pak--applications':  	        
            {'icon': 'ibm-cloud-pak--applications', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--data':  	        
            {'icon': 'ibm-cloud-pak--data', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--integration':  	        
            {'icon': 'ibm-cloud-pak--integration', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--multicloud-mgmt':  	        
            {'icon': 'ibm-cloud-pak--multicloud-mgmt', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--network-automation':  	        
            {'icon': 'ibm-cloud-pak--network-automation', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--security':  	        
            {'icon': 'ibm-cloud-pak--security', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--system':  	        
            {'icon': 'ibm-cloud-pak--system', 'color': Colors.lines["network"]}, 
      'ibm-cloud-pak--watson-aiops':  	        
            {'icon': 'ibm-cloud-pak--watson-aiops', 'color': Colors.lines["network"]}, 
      'military-camp': 	        
            {'icon': 'military-camp', 'color': Colors.lines["network"]},
      'network--admin-control': 	        
            {'icon': 'network--admin-control', 'color': Colors.lines["network"]},
      'pcn--e-node': 	        
            {'icon': 'pcn--e-node', 'color': Colors.lines["network"]},
      'pcn--military': 	        
            {'icon': 'pcn--military', 'color': Colors.lines["network"]},
      'pcn--p-node': 	        
            {'icon': 'pcn--p-node', 'color': Colors.lines["network"]},
      'pcn--z-node': 	        
            {'icon': 'pcn--z-node', 'color': Colors.lines["network"]},
      'session-border-control': 	        
            {'icon': 'session-border-control', 'color': Colors.lines["network"]},
      'tank': 	        
            {'icon': 'tank', 'color': Colors.lines["network"]},
      'blockstoragevolume': 	        
            {'icon': 'volume--block-storage', 'color': Colors.lines["storage"]},
      'filestoragevolume': 	        
            {'icon': 'volume--file--storage', 'color': Colors.lines["storage"]},
      'objectstoragevolume': 	        
            {'icon': 'volume--object-storage', 'color': Colors.lines["storage"]},
      'transitgateway-prescribed': 	        
            {'icon': 'ibm-cloud--transit-gateway', 'color': Colors.lines["network"]},
      'enterprise': 	        
            {'icon': 'enterprise', 'color': Colors.lines["network"]},
      'linux-prescribed':  	        
            {'icon': 'linux', 'color': Colors.lines["network"]}, 
      'linux--logical':  	        
            {'icon': 'linux--alt', 'color': Colors.lines["network"]}, 
      'objectstorageslicestor': 	        
            {'icon': 'slicestor', 'color': Colors.lines["network"]},
      'concept': 	        
            {'icon': 'concept', 'color': Colors.lines["network"]},
      'deployment-unit--data': 	        
            {'icon': 'deployment-unit--data', 'color': Colors.lines["network"]},
      'deployment-unit--execution': 	        
            {'icon': 'deployment-unit--execution', 'color': Colors.lines["network"]},
      'deployment-unit--installation': 	        
            {'icon': 'deployment-unit--installation', 'color': Colors.lines["network"]},
      'deployment-unit--presentation': 	        
            {'icon': 'deployment-unit--presentation', 'color': Colors.lines["network"]},
      'deployment-unit--technical--data': 	        
            {'icon': 'deployment-unit--technical--data', 'color': Colors.lines["network"]},
      'deployment-unit--technical--execution': 	        
            {'icon': 'deployment-unit--technical--execution', 'color': Colors.lines["network"]},
      'deployment-unit--technical--installation': 	        
            {'icon': 'deployment-unit--technical--installation', 'color': Colors.lines["network"]},
      'deployment-unit--technical--presentation': 	        
            {'icon': 'deployment-unit--technical--presentation', 'color': Colors.lines["network"]},
      'api': 	        
            {'icon': 'api', 'color': Colors.lines["applications"]},
      'buildtool':  	        
            {'icon': 'build-tool', 'color': Colors.lines["applications"]}, 
      'cd':  	        
            {'icon': 'continuous-deployment', 'color': Colors.lines["management"]}, 
      'ci': 	        
            {'icon': 'continuous-integration', 'color': Colors.lines["management"]},
      'keyprotect-prescribed':  	        
            {'icon': 'ibm-cloud--key-protect', 'color': Colors.lines["security"]}, 
      'secretsmanager': 	        
            {'icon': 'ibm-cloud--secrets-manager', 'color': Colors.lines["security"]},
      'artifactrepository': 	        
            {'icon': 'repo--artifact', 'color': Colors.lines["storage"]},
      'sourcecoderepository': 	        
            {'icon': 'repo--source-code', 'color': Colors.lines["storage"]},
      'serviceid':  	        
            {'icon': 'service-id', 'color': Colors.lines["security"]}, 
      'testtool': 	        
            {'icon': 'test-tool', 'color': Colors.lines["applications"]}
   }

   common = None

   def __init__(self, common):   
      self.common = common

   def getIconDictionary(self):
      return self.iconDictionary

   #def getIcon(self, name, shapetype):
   def getIcon(self, shapetype):
      #if self.common.isAllIcons():
      #   iconname = name
      #   iconcolor = Colors.lines["network"]
      #elif self.common.isLogicalShapes():
      if self.common.isLogicalShapes():
         if shapetype in self.iconDictionary:
            icon = self.iconDictionary[shapetype]
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-logical' in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-logical']
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-prescribed' in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-prescribed']
            iconname = icon['icon']
            iconcolor = icon['color']
         else:
            icon = self.iconDictionary['undefined']
            iconname = icon['icon']
            iconcolor = icon['color']
      else: # check prescribed
         if shapetype in self.iconDictionary:
            icon = self.iconDictionary[shapetype]
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-prescribed' in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-prescribed']
            iconname = icon['icon']
            iconcolor = icon['color']
         elif shapetype + '-logical' in self.iconDictionary:
            icon = self.iconDictionary[shapetype + '-logical']
            iconname = icon['icon']
            iconcolor = icon['color']
         else:
            icon = self.iconDictionary['undefined']
            iconname = icon['icon']
            iconcolor = icon['color']

      return iconname, iconcolor    

   def validIcon(self, iconname):
      #for name, values in self.iconDictionary.items():
      #   if iconname == values['icon']:
      #      return True
      if iconname in self.iconDictionary:
         return True
      if iconname + '-logical' in self.iconDictionary:
         return True
      if iconname + '-prescribed' in self.iconDictionary:
         return True
      return False
