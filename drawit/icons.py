# @file icons.py
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

from .colors import Colors

class Icons:
   iconDictionary = { 
      'undefined': 	        
            {'icon': 'undefined', 'color': Colors.lines["network"]},
      #'collaborate': 	        
      #      {'icon': 'collaborate', 'color': Colors.lines["user"]},
      #'credentials': 	        
      #      {'icon': 'credentials', 'color': Colors.lines["network"]},
      'devices': 	        
            {'icon': 'devices', 'color': Colors.lines["user"]},
      'meeting': 	        
            {'icon': 'events', 'color': Colors.lines["user"]},
      'authorizationboundary': 	        
            {'icon': 'flag', 'color': Colors.lines["network"]},
      'cloud-ibm': 	        
            {'icon': 'ibm-cloud', 'color': Colors.lines["network"]},
      'user':  	        
            {'icon': 'user', 'color': Colors.lines["user"]}, 
      'virtualserver-any': 	        
            {'icon': 'virtual-machine', 'color': Colors.lines["network"]},
      'vpc-any':  	        
            {'icon': 'virtual-private-cloud', 'color': Colors.lines["network"]}, 
      'vpc-ibm':  	        
            {'icon': 'virtual-private-cloud--alt', 'color': Colors.lines["network"]}, 
      'region': 	        
            {'icon': 'location', 'color': Colors.lines["location"]},
      'security': 	        
            {'icon': 'security', 'color': Colors.lines["security"]},
      'fingerprintrecognition': 	        
            {'icon': 'fingerprint-recognition', 'color': Colors.lines["network"]},
      'network':  	        
            {'icon': 'network--2', 'color': Colors.lines["network"]}, 
      'edgenode':  	        
            {'icon': 'edge-node', 'color': Colors.lines["network"]}, 
      #'group':  	        
      #      {'icon': 'group', 'color': Colors.lines["user"]}, 
      #'mobile':  	        
      #      {'icon': 'mobile', 'color': Colors.lines["user"]}, 
      'policy':  	        
            {'icon': 'policy', 'color': Colors.lines["security"]}, 
      'rule':  	        
            {'icon': 'rule', 'color': Colors.lines["security"]}, 
      #'terminal':  	        
      #      {'icon': 'terminal', 'color': Colors.lines["network"]}, 
      'objectstorage-ibm':  	        
            {'icon': 'object-storage', 'color': Colors.lines["storage"]}, 
      #'laptop':  	        
      #      {'icon': 'laptop', 'color': Colors.lines["user"]}, 
      #'tablet':  	        
      #      {'icon': 'tablet', 'color': Colors.lines["user"]}, 
      'archive':  	        
            {'icon': 'archive', 'color': Colors.lines["network"]}, 
      'availabilityzone':  	        
            {'icon': 'data--base--alt', 'color': Colors.lines["location"]}, 
      'internet':  	        
            {'icon': 'wikis', 'color': Colors.lines["network"]}, 
      'database':  	        
            {'icon': 'data--base', 'color': Colors.lines["storage"]}, 
      'subnet-any':  	        
            {'icon': 'locked', 'color': Colors.lines["network"]}, 
      'app':  	        
            {'icon': 'application', 'color': Colors.lines["network"]}, 
      'horizontalarrows': 	        
            {'icon': 'arrows--horizontal', 'color': Colors.lines["network"]},
      'cloud-any': 
            {'icon': 'cloud', 'color': Colors.lines["network"]},
      'serverlessapp': 	        
            {'icon': 'function', 'color': Colors.lines["network"]},
      'openshift':  	        
            {'icon': 'logo--openshift', 'color': Colors.lines["compute"]}, 
      'password': 	        
            {'icon': 'password', 'color': Colors.lines["network"]},
      'script': 	        
            {'icon': 'script', 'color': Colors.lines["network"]},
      'admin': 	        
            {'icon': 'user--admin', 'color': Colors.lines["user"]}, 
      'cloudfoundry': 	        
            {'icon': 'cloud-foundry--1', 'color': Colors.lines["network"]},
      'cloudsatellite':  	        
            {'icon': 'cloud-satellite', 'color': Colors.lines["network"]}, 
      'timer':  	        
            {'icon': 'timer', 'color': Colors.lines["network"]}, 
      'deploy':  	        
            {'icon': 'deploy', 'color': Colors.lines["network"]}, 
      'shuffle': 	        
            {'icon': 'shuffle', 'color': Colors.lines["network"]},
      #'wificontroller': 	        
      #      {'icon': 'wifi--controller', 'color': Colors.lines["network"]},
      'switchlayer3': 	        
            {'icon': 'switch-layer-3', 'color': Colors.lines["network"]},
      'vpngateway': 	        
            {'icon': 'gateway--vpn', 'color': Colors.lines["network"]},
      'baremetal': 	        
            {'icon': 'bare-metal-server', 'color': Colors.lines["compute"]},
      'switchlayer2': 	        
            {'icon': 'switch-layer-2', 'color': Colors.lines["network"]},
      'loadbalancer-ibm': 	        
            {'icon': 'load-balancer--vpc', 'color': Colors.lines["network"]},
      'acl': 	        
            {'icon': 'subnet-acl-rules', 'color': Colors.lines["security"]},
      'vpn': 	        
            {'icon': 'vpn--connection', 'color': Colors.lines["network"]},
      'enterprisenetwork': 	        
            {'icon': 'network--enterprise', 'color': Colors.lines["network"]},
      'directlink': 	        
            {'icon': 'direct-link', 'color': Colors.lines["network"]},
      'securityservices-ibm': 	        
            {'icon': 'ibm-security--services', 'color': Colors.lines["network"]},
      'resourcegroup': 	        
            {'icon': 'group--resource', 'color': Colors.lines["security"]},
      'servicedeskuser': 	        
            {'icon': 'user--service-desk', 'color': Colors.lines["user"]},
      'protecteddocument': 	        
            {'icon': 'document--protected', 'color': Colors.lines["network"]},
      'securitygroup': 	        
            {'icon': 'group--security', 'color': Colors.lines["security"]},
      'virtualapp': 	        
            {'icon': 'application--virtual', 'color': Colors.lines["network"]},
      'loadbalancerpool': 	        
            {'icon': 'load-balancer--pool', 'color': Colors.lines["network"]},
      #'vehicleservices': 	        
      #      {'icon': 'vehicle--services', 'color': Colors.lines["network"]},
      'securityservices': 	        
            {'icon': 'security-services', 'color': Colors.lines["network"]},
      #'militaryuser': 	        
      #      {'icon': 'user--military', 'color': Colors.lines["network"]},
      'messagequeue': 	        
            {'icon': 'message-queue', 'color': Colors.lines["network"]},
      'databackup': 	        
            {'icon': 'data-backup', 'color': Colors.lines["network"]},
      'gui': 	        
            {'icon': 'gui', 'color': Colors.lines["network"]},
      'cloudmonitoring': 	        
            {'icon': 'cloud--monitoring', 'color': Colors.lines["management"]},
      'firewall': 	        
            {'icon': 'firewall', 'color': Colors.lines["security"]},
      #'wifinotsecure': 	        
      #      {'icon': 'wifi--not-secure', 'color': Colors.lines["network"]},
      'cdn': 	        
            {'icon': 'content-delivery-network', 'color': Colors.lines["network"]},
      'cloudalerting': 	        
            {'icon': 'cloud--alerting', 'color': Colors.lines["management"]},
      'flowlogs-ibm': 	        
            {'icon': 'flow-logs-vpc', 'color': Colors.lines["management"]},
      'servicemanagement': 	        
            {'icon': 'cloud--service-management', 'color': Colors.lines["management"]},
      'networkloadbalancer': 	        
            {'icon': 'load-balancer--network', 'color': Colors.lines["network"]},
      'publicnetwork': 	        
            {'icon': 'network--public', 'color': Colors.lines["network"]},
      'dnsserver': 	        
            {'icon': 'server--dns', 'color': Colors.lines["network"]},
      #'vehicleapi': 	        
      #      {'icon': 'vehicle--api', 'color': Colors.lines["network"]},
      #'classicinfrastructure': 	        
      #      {'icon': 'infrastructure--classic', 'color': Colors.lines["network"]},
      #'classicvirtualserver': 	        
      #      {'icon': 'instance--classic', 'color': Colors.lines["network"]},
      'apploadbalancer': 	        
            {'icon': 'load-balancer--application', 'color': Colors.lines["network"]},
      'dedicatedhost-ibm': 	        
            {'icon': 'ibm-cloud--dedicated-host', 'color': Colors.lines["network"]},
      'internetservices-ibm': 	        
            {'icon': 'ibm-cloud--internet-services', 'color': Colors.lines["network"]},
      #'pushtotalkradio': 	        
      #      {'icon': 'radio--push-to-talk', 'color': Colors.lines["network"]},
      'globalloadbalancer': 	        
            {'icon': 'load-balancer--global', 'color': Colors.lines["network"]},
      #'classicfirewall': 	        
      #      {'icon': 'firewall--classic', 'color': Colors.lines["network"]},
      'blockstorage-any': 	        
            {'icon': 'block-storage--alt', 'color': Colors.lines["network"]},
      'accessgroup': 	        
            {'icon': 'group--access', 'color': Colors.lines["security"]},
      'vpnpolicy': 	        
            {'icon': 'vpn--policy', 'color': Colors.lines["network"]},
      'codesigningservice': 	        
            {'icon': 'code-signing-service', 'color': Colors.lines["security"]},
      'memoryprofile': 	        
            {'icon': 'instance--mx', 'color': Colors.lines["compute"]},
      'hybridnetworking': 	        
            {'icon': 'hybrid-networking--alt', 'color': Colors.lines["network"]},
      'unprotecteddocument': 	        
            {'icon': 'document--unprotected', 'color': Colors.lines["network"]},
      'bastionhost': 	        
            {'icon': 'bastion-host', 'color': Colors.lines["security"]},
      'blob': 	        
            {'icon': 'data-blob', 'color': Colors.lines["network"]},
      'objectstorage-any': 	        
            {'icon': 'object-storage--alt', 'color': Colors.lines["storage"]},
      'proxyserver': 	        
            {'icon': 'server--proxy', 'color': Colors.lines["network"]},
      'mobileapp': 	        
            {'icon': 'application--mobile', 'color': Colors.lines["network"]},
      'mobilityservices': 	        
            {'icon': 'mobility--services', 'color': Colors.lines["network"]},
      'filestorage': 	        
            {'icon': 'file-storage', 'color': Colors.lines["storage"]},
      #'wifirouter': 	        
      #      {'icon': 'router--wifi', 'color': Colors.lines["network"]},
      'intrusionprevention': 	        
            {'icon': 'intrusion-prevention', 'color': Colors.lines["network"]},
      'edgenode': 	        
            {'icon': 'edge-node--alt', 'color': Colors.lines["network"]},
      'vlan-ibm': 	        
            {'icon': 'vlan--ibm', 'color': Colors.lines["network"]},
      'cloudservices': 	        
            {'icon': 'cloud-services', 'color': Colors.lines["network"]},
      'blockstorage-ibm': 	        
            {'icon': 'block-storage', 'color': Colors.lines["storage"]},
      'floatingip': 	        
            {'icon': 'floating-ip', 'color': Colors.lines["network"]},
      #'connectedvehicle': 	        
      #       {'icon': 'vehicle--connected', 'color': Colors.lines["network"]},
      'accountgroup': 	        
          {'icon': 'group--account', 'color': Colors.lines["security"]},
      'imageservice': 	        
            {'icon': 'image-service', 'color': Colors.lines["network"]},
      'balancedprofile': 	        
            {'icon': 'instance--bx', 'color': Colors.lines["network"]},
      #'objectstorageaccessor': 	        
      #      {'icon': 'data-accessor', 'color': Colors.lines["network"]},
      'useraccessgateway': 	        
            {'icon': 'gateway--user-access', 'color': Colors.lines["network"]},
      'signeddocument': 	        
            {'icon': 'document--signed', 'color': Colors.lines["network"]},
      'webapp': 	        
            {'icon': 'application--web', 'color': Colors.lines["network"]},
      'instancegroup': 	        
            {'icon': 'autoscaling', 'color': Colors.lines["network"]},
      'loadbalancerlistener': 	        
            {'icon': 'load-balancer--listener', 'color': Colors.lines["network"]},
      #'combatradio': 	        
      #      {'icon': 'radio--combat', 'color': Colors.lines["network"]},
      'usersettings': 	        
            {'icon': 'user--settings', 'color': Colors.lines["network"]},
      #'wifi-bridge--alt': 	        
      #      {'icon': 'wifi-bridge--alt', 'color': Colors.lines["network"]},
      'pointofpresence': 	        
            {'icon': 'point-of-presence', 'color': Colors.lines["network"]},
      'datacenter': 	        
            {'icon': 'data--center', 'color': Colors.lines["network"]},
      'simcard': 	        
            {'icon': 'sim-card', 'color': Colors.lines["network"]},
      'operationalchat': 	        
            {'icon': 'chat--operational', 'color': Colors.lines["network"]},
      'vpe-ibm': 	        
            {'icon': 'ibm-cloud--vpc-endpoints', 'color': Colors.lines["network"]},
      'idmanagement': 	        
            {'icon': 'id-management', 'color': Colors.lines["network"]},
      'virtualserver-ibm': 	        
            {'icon': 'instance--virtual', 'color': Colors.lines["compute"]},
      'managementgui': 	        
            {'icon': 'gui--management', 'color': Colors.lines["network"]},
      'virtualdesktop': 	        
            {'icon': 'virtual-desktop', 'color': Colors.lines["network"]},
      'computeprofile': 	        
            {'icon': 'instance--cx', 'color': Colors.lines["compute"]},
      'phonesettings': 	        
            {'icon': 'phone--settings', 'color': Colors.lines["network"]},
      'overlaynetwork': 	        
            {'icon': 'network--overlay', 'color': Colors.lines["network"]},
      'gateway': 	        
            {'icon': 'gateway', 'color': Colors.lines["network"]},
      'documentsecurity': 	        
            {'icon': 'document--security', 'color': Colors.lines["network"]},
      'router': 	        
            {'icon': 'router', 'color': Colors.lines["network"]},
      #'voicerouter':  	        
      #      {'icon': 'router--voice', 'color': Colors.lines["network"]}, 
      'dnsservices': 	        
            {'icon': 'dns-services', 'color': Colors.lines["network"]},
      'vlan-any': 	        
            {'icon': 'vlan', 'color': Colors.lines["network"]},
      'timeserver': 	        
            {'icon': 'server--time', 'color': Colors.lines["network"]},
      'apigateway': 	        
            {'icon': 'gateway--api', 'color': Colors.lines["network"]},
      #'securewifi': 	        
      #      {'icon': 'wifi--secure', 'color': Colors.lines["network"]},
      'mailgateway': 	        
            {'icon': 'gateway--mail', 'color': Colors.lines["network"]},
      'publicgateway': 	        
            {'icon': 'gateway--public', 'color': Colors.lines["network"]},
      #'phoneapp': 	        
      #      {'icon': 'phone--application', 'color': Colors.lines["network"]},
      #'ltetransmission': 	        
      #      {'icon': 'transmission-lte', 'color': Colors.lines["network"]},
      #'vehicleinsights': 	        
      #      {'icon': 'vehicle--insights', 'color': Colors.lines["network"]},
      'activitytracker': 	        
            {'icon': 'cloud--auditing', 'color': Colors.lines["management"]},
      'hardwaresecuritymodule': 	        
            {'icon': 'hardware-security-module', 'color': Colors.lines["network"]},
      '2fa': 	        
            {'icon': 'two-factor-authentication', 'color': Colors.lines["network"]},
      #'wifibridge': 	        
      #      {'icon': 'wifi-bridge', 'color': Colors.lines["network"]},
      'loadbalancer-any': 	        
            {'icon': 'load-balancer--classic', 'color': Colors.lines["network"]},
      #'locallb': 	        
      #      {'icon': 'load-balancer--local', 'color': Colors.lines["network"]},
      'cloudlogging': 	        
            {'icon': 'cloud--logging', 'color': Colors.lines["network"]},
      'subnet-ibm': 	        
            {'icon': 'ibm-cloud--subnets', 'color': Colors.lines["network"]},
      #'datadiode': 	        
      #      {'icon': 'data-diode', 'color': Colors.lines["network"]},
      #'folderdetails': 	        
      #      {'icon': 'folder--details', 'color': Colors.lines["storage"]},
      'securitygateway': 	        
            {'icon': 'gateway--security', 'color': Colors.lines["network"]},
      #'baremetalserver1': 	        
      #      {'icon': 'bare-metal-server--01', 'color': Colors.lines["network"]},
      #'baremetalserver2':  	        
      #      {'icon': 'bare-metal-server--02', 'color': Colors.lines["network"]}, 
      #'boot':  	        
      #      {'icon': 'boot', 'color': Colors.lines["network"]}, 
      #'extralargebox': 	        
      #      {'icon': 'box--extra-large', 'color': Colors.lines["network"]},
      #'largebox': 	        
      #      {'icon': 'box--large', 'color': Colors.lines["network"]},
      #'mediumbox': 	        
      #      {'icon': 'box--medium', 'color': Colors.lines["network"]},
      #'smallbox': 	        
      #      {'icon': 'box--small', 'color': Colors.lines["network"]},
      'satelliteconfig':  	        
            {'icon': 'cloud-satellite--config', 'color': Colors.lines["network"]}, 
      'satellitelink':  	        
            {'icon': 'cloud-satellite--link', 'color': Colors.lines["network"]}, 
      'satelliteservices':  	        
            {'icon': 'cloud-satellite--services', 'color': Colors.lines["network"]}, 
      'unifiedcommunication': 	        
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
      'domaindirectory':  	        
            {'icon': 'directory-domain', 'color': Colors.lines["network"]}, 
      'encryption': 	        
            {'icon': 'encryption', 'color': Colors.lines["network"]},
      #'pakapplications-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--applications', 'color': Colors.lines["network"]}, 
      #'datapak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--data', 'color': Colors.lines["network"]}, 
      #'integrationpak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--integration', 'color': Colors.lines["network"]}, 
      #'multicloudmgmtpak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--multicloud-mgmt', 'color': Colors.lines["network"]}, 
      #'networkautomationpak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--network-automation', 'color': Colors.lines["network"]}, 
      #'securitypak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--security', 'color': Colors.lines["network"]}, 
      #'systempak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--system', 'color': Colors.lines["network"]}, 
      #'watsonaiopspak-ibm':  	        
      #      {'icon': 'ibm-cloud-pak--watson-aiops', 'color': Colors.lines["network"]}, 
      #'militarycamp': 	        
      #      {'icon': 'military-camp', 'color': Colors.lines["network"]},
      #'admincontrolnetwork': 	        
      #      {'icon': 'network--admin-control', 'color': Colors.lines["network"]},
      #'enodepcn': 	        
      #      {'icon': 'pcn--e-node', 'color': Colors.lines["network"]},
      #'militarypcn': 	        
      #      {'icon': 'pcn--military', 'color': Colors.lines["network"]},
      #'pnodepcn': 	        
      #      {'icon': 'pcn--p-node', 'color': Colors.lines["network"]},
      #'znodepcn': 	        
      #      {'icon': 'pcn--z-node', 'color': Colors.lines["network"]},
      'sessionbordercontrol': 	        
            {'icon': 'session-border-control', 'color': Colors.lines["network"]},
      #'tank': 	        
      #      {'icon': 'tank', 'color': Colors.lines["network"]},
      #'blockstoragevolume': 	        
      #      {'icon': 'volume--block-storage', 'color': Colors.lines["storage"]},
      #'filestoragevolume': 	        
      #      {'icon': 'volume--file--storage', 'color': Colors.lines["storage"]},
      #'objectstoragevolume': 	        
      #      {'icon': 'volume--object-storage', 'color': Colors.lines["storage"]},
      'transitgateway-ibm': 	        
            {'icon': 'ibm-cloud--transit-gateway', 'color': Colors.lines["network"]},
      'enterprisenetwork': 	        
            {'icon': 'enterprise', 'color': Colors.lines["network"]},
      'linux-ibm':  	        
            {'icon': 'linux', 'color': Colors.lines["network"]}, 
      'linux-any':  	        
            {'icon': 'linux--alt', 'color': Colors.lines["network"]}, 
      #'objectstorageslicestor': 	        
      #      {'icon': 'slicestor', 'color': Colors.lines["network"]},
      #'concept': 	        
      #      {'icon': 'concept', 'color': Colors.lines["network"]},
      #'datadeploymentunitdata': 	        
      #      {'icon': 'deployment-unit--data', 'color': Colors.lines["network"]},
      #'executiondeploymentunit': 	        
      #      {'icon': 'deployment-unit--execution', 'color': Colors.lines["network"]},
      #'installationdeploymentunit': 	        
      #      {'icon': 'deployment-unit--installation', 'color': Colors.lines["network"]},
      #'presentationdeploymentunit': 	        
      #      {'icon': 'deployment-unit--presentation', 'color': Colors.lines["network"]},
      #'technicaldatadeploymentunit': 	        
      #      {'icon': 'deployment-unit--technical--data', 'color': Colors.lines["network"]},
      #'technicalexecutiondeploymentunit': 	        
      #      {'icon': 'deployment-unit--technical--execution', 'color': Colors.lines["network"]},
      #'technicalinstallationdeploymentunit': 	        
      #      {'icon': 'deployment-unit--technical--installation', 'color': Colors.lines["network"]},
      #'technicalpresentationdeploymentunit': 	        
      #      {'icon': 'deployment-unit--technical--presentation', 'color': Colors.lines["network"]},
      'api': 	        
            {'icon': 'api', 'color': Colors.lines["applications"]},
      'buildtool':  	        
            {'icon': 'build-tool', 'color': Colors.lines["applications"]}, 
      'continuousdeployment':  	        
            {'icon': 'continuous-deployment', 'color': Colors.lines["management"]}, 
      'continuousintegration': 	        
            {'icon': 'continuous-integration', 'color': Colors.lines["management"]},
      'keyprotect-ibm':  	        
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

   def getIcon(self, iconusage):
      if self.common.isProviderAny():
         if iconusage in self.iconDictionary:
            icon = self.iconDictionary[iconusage]
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-any' in selfs.iconDictionary:
            icon = selfs.iconDictionary[iconusage + '-any']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-ibm' in self.iconDictionary:
            icon = self.iconDictionary[iconusage + '-ibm']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         else:
            icon = self.iconDictionary['undefined']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
      else: # check prescribed
         if iconusage in self.iconDictionary:
            icon = self.iconDictionary[iconusage]
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-ibm' in self.iconDictionary:
            icon = self.iconDictionary[iconusage + '-ibm']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         elif iconusage + '-any' in self.iconDictionary:
            icon = self.iconDictionary[iconusage + '-any']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""
         else:
            icon = self.iconDictionary['undefined']
            iconname = icon['icon']
            iconcolor = icon['color']
            #iconshape = icon['shape'] if 'shape' in icon else ""
            #hideicon = icon['hideicon'] if 'hideicon' in icon else ""

      #return iconname, iconcolor, iconshape, hideicon
      return iconname, iconcolor

   def validIcon(self, iconname):
      if iconname in self.iconDictionary:
         return True
      if iconname + '-any' in self.iconDictionary:
         return True
      if iconname + '-ibm' in self.iconDictionary:
         return True
      return False
