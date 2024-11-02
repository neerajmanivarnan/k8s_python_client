from kubernetes import client, config
#
# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()
#
# v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()

# Initialize the CoreV1Api
v1 = client.CoreV1Api()

def get_pod_and_node_info(namespace="monitoring"):
    # Retrieve all pods in the specified namespace
    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        pod_name = pod.metadata.name
        node_name = pod.spec.node_name  # Node where the pod is deployed
        print(f"Pod: {pod_name} is running on Node: {node_name}")

# Example: Get pod and node info in the "default" namespace
get_pod_and_node_info("monitoring")

