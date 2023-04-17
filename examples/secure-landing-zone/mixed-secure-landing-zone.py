from drawit import Diagram, Cluster, Node, Edge

with Diagram("mixed-secure-landing-zone"):

  with Cluster("Cloud", icon="cloud"):

    with Cluster("Region", icon="region"):

      with Cluster("Management Resource Group", icon="resourcegroup"):
        with Cluster("Management VPC", icon="vpc"):
          with Cluster("Management ACL", icon="acl"):
            with Cluster("Zone 1", icon="zone", direction="TB"):
              with Cluster("10.10.10.0/24 : VSI", icon="subnet"):
                vsi = Node("Virtual Server", icon="virtualserver") 
              with Cluster("10.10.20.0/24 : VPE", icon="subnet"):
                vpe = Node("Virtual Private Endpoint", icon="vpe") 
              with Cluster("10.10.30.0/24 : VPN", icon="subnet"):
                vpn = Node("VPN Gateway", icon="vpngateway") 
            with Cluster("Zone 2", icon="zone", direction="TB"):
              with Cluster("10.20.10.0/24 : VSI", icon="subnet"):
                vsi = Node("Virtual Server", icon="virtualserver") 
              with Cluster("10.20.20.0/24 : VPE", icon="subnet"):
                vpe = Node("Virtual Private Endpoint", icon="vpe") 
            with Cluster("Zone 3", icon="zone", direction="TB"):
              with Cluster("10.30.10.0/24 : VSI", icon="subnet"):
                vsi = Node("Virtual Server", icon="virtualserver") 
              with Cluster("10.30.20.0/24 : VPE", icon="subnet"):
                vpe = Node("Virtual Private Endpoint", icon="vpe") 

      with Cluster("Workload Resource Group", icon="resourcegroup"):
        with Cluster("Workload VPC", icon="vpc"):
          with Cluster("Workload ACL", icon="acl"):
            with Cluster("Zone 1", icon="zone", direction="TB"):
              with Cluster("10.40.10.0/24 : VSI", icon="subnet"):
                vsi = Node("OpenShift Cluster", icon="openshift") 
              with Cluster("10.40.20.0/24 : VPE", icon="subnet"):
                vpe = Node("Virtual Private Endpoint", icon="vpe") 
            with Cluster("Zone 2", icon="zone", direction="TB"):
              with Cluster("10.50.10.0/24 : VSI", icon="subnet"):
                vsi = Node("OpenShift Cluster", icon="openshift") 
              with Cluster("10.50.20.0/24 : VPE", icon="subnet"):
                vpe = Node("Virtual Private Endpoint", icon="vpe") 
            with Cluster("Zone 3", icon="zone", direction="TB"):
              with Cluster("10.60.10.0/24 : VSI", icon="subnet"):
                vsi = Node("OpenShift Cluster", icon="openshift") 
              with Cluster("10.60.20.0/24 : VPE", icon="subnet"):
                vpe = Node("Virtual Private Endpoint", icon="vpe") 

      with Cluster("Cloud Services Resource Group", icon="resourcegroup"):
        with Cluster("Cloud Services", icon="cloudservices", direction="TB"):
          service1 = Node("Activity Tracker Object Storage", icon="objectstorage") 
          service2 = Node("Activity Tracker", icon="activitytracker") 
          service3 = Node("Key Management", icon="keyprotect") 
          service4 = Node("Transit Gateway", icon="transitgateway") 
          service5 = Node("Object Storage", icon="objectstorage") 
          service6 = Node("Management VPC Flow Log Collector", icon="flowlogs") 
          service7 = Node("Workload VPC Flow Log Collector", icon="flowlogs") 
