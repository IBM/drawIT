from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-high-level-edge"):

  with Cluster("Cloud", icon="cloud"):

    with Cluster("Region", icon="region", direction="TB"):

      with Cluster("VPC 1 (Edge/Transit)", icon="vpc"):
        lb = Node("Public Load Balancer", icon="loadbalancer") 
        with Cluster("Zone", icon="zone", direction="TB"):
          with Cluster("10.10.10.0/24 : ACL1", icon="subnet"):
            vpe = Node("VPE", icon="vpe") 
            vpn = Node("VPN Gateway", icon="vpngateway") 
            #vnf = Node("VNF", icon="vnf") 
            bastion = Node("Bastion", icon="bastionhost") 
            storage = Node("Block Storage", icon="blockstorage") 

      dl = Node("Direct Link", icon="directlink") 
      vpn = Node("VPN Connection", icon="vpn") 
      tg = Node("Transit Gateway", icon="transitgateway") 

      with Cluster("VPC 2 (Management)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 
        with Cluster("Zone", icon="zone", direction="TB"):
          with Cluster("10.20.10.0/24 : ACL1", icon="subnet"):
            vpe = Node("VPE", icon="vpe") 
            with Cluster("Security Group", icon="securitygroup", shape="zone"):
              vsi = Node("VSI", icon="virtualserver") 
            roks = Node("ROKS", icon="openshift") 
            storage = Node("Block Storage", icon="blockstorage") 

      with Cluster("VPC 3 (Workload)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 
        with Cluster("Zone", icon="zone", direction="TB"):
          with Cluster("10.30.10.0/24 : ACL1", icon="subnet"):
            vpe = Node("VPE", icon="vpe") 
            with Cluster("Security Group", icon="securitygroup", shape="zone"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
            roks = Node("ROKS", icon="openshift") 
            storage = Node("Block Storage", icon="blockstorage") 

      with Cluster("Cloud Services", icon="cloudservices", direction="TB"):
        service1 = Node("Logging", icon="objectstorage") 
        service2 = Node("Auditing", icon="activitytracker") 
        service3 = Node("Monitoring", icon="keyprotect") 
        service4 = Node("Event Streams", icon="transitgateway") 
        service5 = Node("App ID", icon="objectstorage") 
        service6 = Node("HCPS", icon="flowlogs") 
        service7 = Node("HP DBaaS", icon="flowlogs") 
        service1 = Node("COS", icon="objectstorage") 

      with Cluster("Platform Services", icon="cloudservices", direction="TB"):
        service1 = Node("Identity Access Manager", icon="objectstorage") 
