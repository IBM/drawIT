from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-multi-region"):

  with Cluster("Public Network", icon="publicnetwork", direction="TB"):
    with Cluster("Consumer", direction="TB"):
      user = Node("User", icon="user", shape="actor") 
      internet = Node("Internet", icon="internet") 

  with Cluster("Cloud", icon="cloud"):
    glb = Node("Global Load Balancer", icon="globalloadbalancer") 

    with Cluster("Region A", icon="region", direction="TB"):
      with Cluster("VPC 1 (Management)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 
        with Cluster("Zone 1", sublabel="10.10.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.10.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.10.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.10.30.0/24 - ACL3", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpngateway") 
        with Cluster("Zone 2", sublabel="10.20.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.20.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.20.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.20.30.0/24 - ACL3", icon="subnet"):
            bastion = Node("Bastion", icon="bastionhost") 
            vsi = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        with Cluster("Zone 3", sublabel="10.30.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.30.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.30.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.30.30.0/24 - ACL3", icon="subnet"):
            bastion = Node("Bastion", icon="bastionhost") 
            vsi = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      dl = Node("Direct Link", icon="directlink") 
      vpn = Node("VPN Connection", icon="vpn") 
      tg = Node("Transit Gateway", icon="transitgateway") 

      with Cluster("VPC 2 (Workload)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 

        with Cluster("Zone 1", sublabel="10.40.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.40.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.40.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.40.30.0/24 - ACL3", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpngateway") 

        with Cluster("Zone 2", sublabel="10.50.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.50.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              vsi3 = Node("VSI", icon="virtualserver") 
              vsi4 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.50.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.50.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="virtualserver") 
            vsi2 = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 

        with Cluster("Zone 3", sublabel="10.60.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.60.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              vsi3 = Node("VSI", icon="virtualserver") 
              vsi4 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.60.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.60.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="virtualserver") 
            vsi2 = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      with Cluster("Cloud Services", icon="cloudservices"):
        with Cluster("Logging", direction="TB"):
          service1 = Node("Logging", icon="cloudlogging") 
          service2 = Node("Activity Tracker", icon="activitytracker") 
        with Cluster("Monitoring", direction="TB"):
          service1 = Node("Monitoring", icon="cloudmonitoring") 
        with Cluster("Messaging", direction="TB"):
          service1 = Node("Event Streams", icon="undefined") 
        with Cluster("Security", direction="TB"):
          service1 = Node("Identity Access Manager", icon="idmanagement") 
          service2 = Node("HCPS", icon="undefined") 
          service3 = Node("AppID", icon="undefined") 
        with Cluster("Storage", direction="TB"):
          service1 = Node("HP DBaaS", icon="undefined") 
          service2 = Node("Object Storage", icon="objectstorage") 

    with Cluster("Region B", icon="region", direction="TB"):
      with Cluster("VPC 1 (Management / Controls)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 
        with Cluster("Zone 1", sublabel="10.70.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.70.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.70.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.70.30.0/24 - ACL3", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpngateway") 
        with Cluster("Zone 2", sublabel="10.80.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.80.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.80.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.80.30.0/24 - ACL3", icon="subnet"):
            bastion = Node("Bastion", icon="bastionhost") 
            vsi = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        with Cluster("Zone 3", sublabel="10.90.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.90.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.90.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.90.30.0/24 - ACL3", icon="subnet"):
            bastion = Node("Bastion", icon="bastionhost") 
            vsi = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      dl = Node("Direct Link", icon="directlink") 
      vpn = Node("VPN Connection", icon="vpn") 
      tg = Node("Transit Gateway", icon="transitgateway") 

      with Cluster("VPC 2 (Workload)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 

        with Cluster("Zone 1", sublabel="10.100.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.10o.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.100.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 

        with Cluster("Zone 2", sublabel="10.110.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.110.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              vsi3 = Node("VSI", icon="virtualserver") 
              vsi4 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.110.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.110.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="virtualserver") 
            vsi2 = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 

        with Cluster("Zone 3", sublabel="10.120.0.0/18", icon="availabilityzone", direction="TB"):
          with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
            with Cluster("Subnet 1", sublabel="10.120.10.0/24 - ACL1", icon="subnet"):
              vsi1 = Node("VSI", icon="virtualserver") 
              vsi2 = Node("VSI", icon="virtualserver") 
              vsi3 = Node("VSI", icon="virtualserver") 
              vsi4 = Node("VSI", icon="virtualserver") 
              block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.120.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.120.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="virtualserver") 
            vsi2 = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      with Cluster("Cloud Services", icon="cloudservices"):
        with Cluster("Logging", direction="TB"):
          service1 = Node("Logging", icon="cloudlogging") 
          service2 = Node("Activity Tracker", icon="activitytracker") 
        with Cluster("Monitoring", direction="TB"):
          service1 = Node("Monitoring", icon="cloudmonitoring") 
        with Cluster("Messaging", direction="TB"):
          service1 = Node("Event Streams", icon="undefined") 
        with Cluster("Security", direction="TB"):
          service1 = Node("Identity Access Manager", icon="idmanagement") 
          service2 = Node("HCPS", icon="undefined") 
          service3 = Node("AppID", icon="undefined") 
        with Cluster("Storage", direction="TB"):
          service1 = Node("HP DBaaS", icon="undefined") 
          service2 = Node("Object Storage", icon="objectstorage") 

  with Cluster("Enterprise Network", icon="enterprisenetwork", direction="TB"):
    directory = Node("Enterprise User Directory", icon="undefined") 
    user = Node("Enterprise User", icon="user", shape="actor") 
    app = Node("Enterprise Applications", icon="undefined") 
