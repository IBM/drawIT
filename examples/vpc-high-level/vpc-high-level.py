from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-high-level"):

  with Cluster("Cloud", icon="cloud"):

    with Cluster("Region", icon="region", direction="TB"):

      with Cluster("VPC 1 (Management)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="lb") 
        with Cluster("Zone", icon="zone", direction="TB"):
          with Cluster("10.10.10.0/24 : ACL1", icon="subnet"):
            vpc = Node("VPC", icon="vpc") 
            vpn = Node("VPN Gateway", icon="vpngateway") 
            with Cluster("Security Group", icon="securitygroup", shape="zone"):
              vsi = Node("VSI", icon="vsi") 
            roks = Node("ROKS", icon="openshift") 
            bastion = Node("Bastion", icon="bastion") 
            storage = Node("Block Storage", icon="blockstorage") 

      dl = Node("Direct Link", icon="dl") 
      vpn = Node("VPN Connection", icon="vpn") 
      tg = Node("Transit Gateway", icon="tg") 

      with Cluster("VPC 2 (Workload)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="lb") 
        with Cluster("Zone", icon="zone", direction="TB"):
          with Cluster("10.20.10.0/24 : ACL1", icon="subnet"):
            vpc = Node("VPC", icon="vpc") 
            vpn = Node("VPN Gateway", icon="vpngateway") 
            with Cluster("Security Group", icon="securitygroup", shape="zone"):
              vsi1 = Node("VSI", icon="vsi") 
              vsi2 = Node("VSI", icon="vsi") 
            roks = Node("ROKS", icon="openshift") 
            bastion = Node("Bastion", icon="bastion") 
            storage = Node("Block Storage", icon="blockstorage") 

      with Cluster("Cloud Services", icon="cloudservices", direction="TB"):
        service1 = Node("Logging", icon="objectstorage") 
        service2 = Node("Auditing", icon="activitytracker") 
        service3 = Node("Monitoring", icon="keyprotect") 
        service4 = Node("Event Streams", icon="tg") 
        service5 = Node("App ID", icon="objectstorage") 
        service6 = Node("HCPS", icon="flowlogs") 
        service7 = Node("HP DBaaS", icon="flowlogs") 
        service1 = Node("COS", icon="objectstorage") 

      with Cluster("Platform Services", icon="cloudservices", direction="TB"):
        service1 = Node("Identity Access Manager", icon="objectstorage") 
