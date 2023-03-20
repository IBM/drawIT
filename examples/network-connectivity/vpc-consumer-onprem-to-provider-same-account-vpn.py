from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-consumer-onprem-to-provider-same-account-vpn"):

  with Cluster("Enterprise Network", icon="enterprise"):
    consumer = Node("Consumer Location", icon="user") 
    vpn = Node("VPN Peer/Endpoint", icon="vpn") 

  with Cluster("Internet", icon="internet"):
    vpn = Node("VPN Connection", icon="vpn") 

  with Cluster("IBM Cloud (Provider Account)", icon="cloud"):
    with Cluster("Region", icon="region"):

      with Cluster("Workload VPC", icon="vpc"):
        with Cluster("Zone", icon="zone"):
          with Cluster("10.10.10.0/24 : VSI", icon="subnet"):
            vpn = Node("VPN Gateway", icon="vpngateway") 
