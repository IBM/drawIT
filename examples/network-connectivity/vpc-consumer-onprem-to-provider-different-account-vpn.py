from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-consumer-onprem-to-provider-different-account-vpn"):

  with Cluster("Enterprise Network", icon="enterprise"):
    consumer = Node("Consumer Location", icon="user") 
    vpn = Node("VPN Peer/Endpoint", icon="vpn") 

  with Cluster("Internet", icon="internet"):
    vpn = Node("VPN Connection", icon="vpn") 

  with Cluster("IBM Cloud (Provider Account)", icon="cloud"):
    with Cluster("Region", icon="region"):

      with Cluster("Workload VPC", icon="vpc"):
        lb = Node("Private LB", icon="lb") 
        with Cluster("Zone", icon="zone"):
          with Cluster("10.10.10.0/24 : VSI", icon="subnet"):
            vsi = Node("VSI", icon="vsi") 

  with Cluster("IBM Cloud (Consumer Account)", icon="cloud"):
    with Cluster("Region", icon="region"):

      with Cluster("Consumer VPC", icon="vpc"):
        lb = Node("Private LB", icon="lb") 
        with Cluster("Zone", icon="zone"):
          with Cluster("10.20.10.0/24 : VSI", icon="subnet"):
            vpn = Node("VSI", icon="vpn") 
            vpe = Node("VSI", icon="vpe") 
