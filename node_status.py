from kubernetes import client, config


config.load_kube_config()


v1 = client.CoreV1Api()


def get_node_status():
    nodes = v1.list_node()
    for node in nodes.items:
        node_name = node.metadata.name
        capacity = node.status.capacity
        allocatable = node.status.allocatable

        print(f"Node: {node_name}")
        print(f"  CPU capacity: {capacity.get('cpu')}")
        print(f"  Memory capacity: {capacity.get('memory')}")
        print(f"  CPU allocatable: {allocatable.get('cpu')}")
        print(f"  Memory allocatable: {allocatable.get('memory')}")



get_node_status()

