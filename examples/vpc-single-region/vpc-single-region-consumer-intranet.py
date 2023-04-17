from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-single-region-consumer-intranet"):

  with Cluster("Public Network", icon="publicnetwork", direction="TB"):
    with Cluster("Consumer", direction="TB"):
      user = Node("User", icon="user", shape="actor") 
      internet = Node("Intranet", icon="internet") 

  with Cluster("Cloud", icon="cloud"):
    glb = Node("Global Load Balancer", icon="globalloadbalancer") 

    with Cluster("Region A", icon="region", direction="TB"):
      with Cluster("VPC 1 (Management)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 
        with Cluster("Zone 1", sublabel="10.10.0.0/18", icon="zone", direction="TB"):
          with Cluster("Multi-Zone OpenShift Managed Cluster Service", icon="openshift"):
            with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
              with Cluster("Subnet 1", sublabel="10.10.10.0/24 - ACL1", icon="subnet"):
                open1 = Node("Worker", icon="openshift") 
                open2 = Node("Worker", icon="openshift") 
                block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.10.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.10.30.0/24 - ACL3", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpngateway") 
        with Cluster("Zone 2", sublabel="10.20.0.0/18", icon="zone", direction="TB"):
          with Cluster("Multi-Zone OpenShift Managed Cluster Service", icon="openshift"):
            with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
              with Cluster("Subnet 1", sublabel="10.20.10.0/24 - ACL1", icon="subnet"):
                open1 = Node("Worker", icon="openshift") 
                open2 = Node("Worker", icon="openshift") 
                block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.20.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.20.30.0/24 - ACL3", icon="subnet"):
            bastion = Node("Bastion", icon="bastionhost") 
            vsi = Node("Virtual Server", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        with Cluster("Zone 3", sublabel="10.30.0.0/18", icon="zone", direction="TB"):
          with Cluster("Multi-Zone OpenShift Managed Cluster Service", icon="openshift"):
            with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
              with Cluster("Subnet 1", sublabel="10.30.10.0/24 - ACL1", icon="subnet"):
                open1 = Node("Worker", icon="openshift") 
                open2 = Node("Worker", icon="openshift") 
                block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.30.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.30.30.0/24 - ACL3", icon="subnet"):
            bastion = Node("Bastion", icon="bastionhost") 
            vsi = Node("Virtual Server", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 
        vpegw = Node("VPE Gateway", icon="vpe", many=True) 

      dl1 = Node("Direct Link", icon="directlink") 
      vpn1 = Node("VPN Connection", icon="vpn") 
      tg = Node("Transit Gateway", icon="transitgateway") 
      dl2 = Node("*Direct Link* (same)", icon="directlink") 
      vpn2 = Node("VPN Connection", icon="vpn") 

      with Cluster("VPC 2 (Workload)", icon="vpc"):
        lb = Node("Private Load Balancer", icon="loadbalancer") 

        with Cluster("Zone 1", sublabel="10.40.0.0/18", icon="zone", direction="TB"):
          with Cluster("Multi-Zone OpenShift Managed Cluster Service", icon="openshift"):
            with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
              with Cluster("Subnet 1", sublabel="10.40.10.0/24 - ACL1", icon="subnet"):
                open1 = Node("Worker", icon="openshift") 
                open2 = Node("Worker", icon="openshift") 
                open3 = Node("Worker", icon="openshift") 
                open4 = Node("Worker", icon="openshift") 
                block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.40.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.40.30.0/24 - ACL3", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpngateway") 

        with Cluster("Zone 2", sublabel="10.50.0.0/18", icon="zone", direction="TB"):
          with Cluster("Multi-Zone OpenShift Managed Cluster Service", icon="openshift"):
            with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
              with Cluster("Subnet 1", sublabel="10.50.10.0/24 - ACL1", icon="subnet"):
                open1 = Node("Worker", icon="openshift") 
                open2 = Node("Worker", icon="openshift") 
                open3 = Node("Worker", icon="openshift") 
                open4 = Node("Worker", icon="openshift") 
                block = Node("Block Storage", icon="blockstorage") 
          with Cluster("Subnet 2", sublabel="10.50.20.0/24 - ACL2", icon="subnet"):
            vpe1 = Node("VPE", icon="vpe") 
            vpe2 = Node("VPE", icon="vpe") 
          with Cluster("Subnet 3", sublabel="10.50.30.0/24 - ACL3", icon="subnet"):
            vsi1 = Node("VSI", icon="virtualserver") 
            vsi2 = Node("VSI", icon="virtualserver") 
            block = Node("Block Storage", icon="blockstorage") 

        with Cluster("Zone 3", sublabel="10.60.0.0/18", icon="zone", direction="TB"):
          with Cluster("Multi-Zone OpenShift Managed Cluster Service", icon="openshift"):
            with Cluster("SG VPC Default & Cluster", icon="securitygroup", shape="zone"):
              with Cluster("Subnet 1", sublabel="10.60.10.0/24 - ACL1", icon="subnet"):
                open1 = Node("Worker", icon="openshift") 
                open2 = Node("Worker", icon="openshift") 
                open3 = Node("Worker", icon="openshift") 
                open4 = Node("Worker", icon="openshift") 
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

  with Cluster("Enterprise Network", icon="enterprisenetwork", direction="TB"):
    directory = Node("Enterprise User Directory", icon="undefined") 
    user = Node("Enterprise User", icon="user", shape="actor") 
    app = Node("Enterprise Applications", icon="undefined") 
