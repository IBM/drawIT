from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-single-region-edge"):

  with Cluster("Public Network", icon="publicnetwork", direction="TB"):
    with Cluster("Consumer", direction="TB"):
      user = Node("User", icon="user") 
      internet = Node("Internet", icon="internet") 

  with Cluster("Cloud", icon="cloud"):
    glb = Node("Global Load Balancer (CIS)", icon="glb") 

    with Cluster("Region A", icon="region", direction="TB"):
      dl = Node("Direct Link", icon="dl") 
      tg = Node("Transit Gateway", icon="tg") 

      with Cluster("VPC 0 (Edge/Transit)", icon="vpc"):
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 
        with Cluster("Zone 1", sublabel="10.5.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.5.10.0/24 - ACL1", icon="subnet"):
            vsn = Node("FUU Tunnel VPN", icon="vpn") 
          with Cluster("Subnet 2", sublabel="10.5.20.0/24 - ACL2", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpn") 
          with Cluster("Subnet 3", sublabel="10.5.30.0/24 - ACL3", icon="subnet"):
            mgmt = Node("Management Interface", icon="mgmt") 
            vsi = Node("FT VSI", icon="f5") 
          with Cluster("Subnet 4", sublabel="10.5.40.0/24 - ACL4", icon="subnet"):
            mgmt = Node("External Interface", icon="mgmt") 
            vsi = Node("Floating IP", icon="fip") 
          with Cluster("Subnet 5", sublabel="10.5.50.0/24 - ACL5", icon="subnet"):
            work = Node("Workload Interface", icon="mgmt") 
          with Cluster("Subnet 6", sublabel="10.5.60.0/24 - ACL6", icon="subnet"):
            work = Node("Bastion Interface", icon="bastion") 
          with Cluster("Subnet 7", sublabel="10.5.70.0/24 - ACL7", icon="subnet"):
            with Cluster("SG VPC Default", icon="zone"):
              work = Node("Bastion Interface", icon="bastion") 
          with Cluster("Subnet 8", sublabel="10.5.80.0/24 - ACL8", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
        with Cluster("Zone 1", sublabel="10.6.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.6.10.0/24 - ACL1", icon="subnet"):
            vsn = Node("FUU Tunnel VPN", icon="vpn") 
          with Cluster("Subnet 2", sublabel="10.6.20.0/24 - ACL2", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpn") 
          with Cluster("Subnet 3", sublabel="10.6.30.0/24 - ACL3", icon="subnet"):
            mgmt = Node("Management Interface", icon="mgmt") 
            vsi = Node("FT VSI", icon="f5") 
          with Cluster("Subnet 4", sublabel="10.6.40.0/24 - ACL4", icon="subnet"):
            mgmt = Node("External Interface", icon="mgmt") 
            vsi = Node("Floating IP", icon="fip") 
          with Cluster("Subnet 5", sublabel="10.6.50.0/24 - ACL5", icon="subnet"):
            work = Node("Workload Interface", icon="mgmt") 
          with Cluster("Subnet 6", sublabel="10.6.60.0/24 - ACL6", icon="subnet"):
            work = Node("Bastion Interface", icon="bastion") 
          with Cluster("Subnet 7", sublabel="10.6.70.0/24 - ACL7", icon="subnet"):
            with Cluster("SG VPC Default", icon="zone"):
              work = Node("Bastion Interface", icon="bastion") 
          with Cluster("Subnet 8", sublabel="10.6.80.0/24 - ACL8", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
        with Cluster("Zone 3", sublabel="10.7.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.7.10.0/24 - ACL1", icon="subnet"):
            vsn = Node("FUU Tunnel VPN", icon="vpn") 
          with Cluster("Subnet 2", sublabel="10.7.20.0/24 - ACL2", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpn") 
          with Cluster("Subnet 3", sublabel="10.7.30.0/24 - ACL3", icon="subnet"):
            mgmt = Node("Management Interface", icon="mgmt") 
            vsi = Node("FT VSI", icon="f5") 
          with Cluster("Subnet 4", sublabel="10.7.40.0/24 - ACL4", icon="subnet"):
            mgmt = Node("External Interface", icon="mgmt") 
            vsi = Node("Floating IP", icon="fip") 
          with Cluster("Subnet 5", sublabel="10.7.50.0/24 - ACL5", icon="subnet"):
            work = Node("Workload Interface", icon="mgmt") 
          with Cluster("Subnet 6", sublabel="10.7.60.0/24 - ACL6", icon="subnet"):
            work = Node("Bastion Interface", icon="bastion") 
          with Cluster("Subnet 7", sublabel="10.7.70.0/24 - ACL7", icon="subnet"):
            with Cluster("SG VPC Default", icon="zone"):
              work = Node("Bastion Interface", icon="bastion") 
          with Cluster("Subnet 8", sublabel="10.7.80.0/24 - ACL8", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      with Cluster("VPC 1 (Management)", icon="vpc"):
        lb = Node("Public Load Balancer", icon="lb") 
        with Cluster("Zone 1", sublabel="10.10.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet", sublabel="10.10.10.0/24 - ACL1", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet", sublabel="10.10.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
        with Cluster("Zone 2", sublabel="10.20.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet", sublabel="10.20.10.0/24 - ACL1", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet", sublabel="10.20.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
        with Cluster("Zone 3", sublabel="10.30.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.30.10.0/24 - ACL1", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.30.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 

      #dl1 = Node("Direct Link", icon="directlink") 
      #vpn1 = Node("VPN Connection", icon="vpn") 
      #tg = Node("Transit Gateway", icon="transitgateway") 
      #dl2 = Node("*Direct Link* (same)", icon="directlink") 
      #vpn2 = Node("VPN Connection", icon="vpn") 

      with Cluster("VPC 2 (Workload)", icon="vpc"):
        lb = Node("Public Load Balancer", icon="lb") 
        with Cluster("Zone 1", sublabel="10.40.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.40.10.0/24 - ACL1", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 1", sublabel="10.40.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
        with Cluster("Zone 2", sublabel="10.50.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.50.10.0/24 - ACL1", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.50.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.50.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
        with Cluster("Zone 3", sublabel="10.60.0.0/18", icon="zone", direction="TB"):
          with Cluster("Subnet 1", sublabel="10.60.10.0/24 - ACL1", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.60.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.60.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="vsi") 
            vsi2 = Node("VSI", icon="vsi") 
            block = Node("Block Storage", icon="blockstorage") 

      vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      with Cluster("Cloud Services", icon="cloudservices"):
        with Cluster("Container", direction="TB"):
          service1 = Node("Registry", icon="registry") 
          service2 = Node("Master Nodes", icon="openshift") 
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
    user = Node("Enterprise User", icon="user") 
    app = Node("Enterprise Applications", icon="undefined") 
