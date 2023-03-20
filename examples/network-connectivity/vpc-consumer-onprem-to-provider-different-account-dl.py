from drawit import Diagram, Cluster, Node, Edge

with Diagram("vpc-consumer-onprem-to-provider-different-account-dl"):

  consumer = Node("Consumer Location", icon="user") 

  with Cluster("Data Center/Campus", sublabel="(Same DC as IBM POP & Customer)", icon="enterprise"):
    edge = Node("SP Edge Device", icon="edge") 
    dl = Node("Direct Link", icon="dl") 

    with Cluster("IBM POP", icon="pop"):
      xcr = Node("IBM XCR", icon="router") 

  with Cluster("IBM Cloud", icon="cloud"):
    with Cluster("Region", icon="region"):

      with Cluster("Workload VPC", icon="vpc"):
        with Cluster("Zone", icon="zone"):
          with Cluster("10.10.10.0/24 : VSI", icon="subnet"):
            vsi = Node("VSI", icon="vsi") 
