from kubernetes import client, config

# Load kubeconfig (for local development) or in-cluster config (if running inside the cluster)
config.load_kube_config()  # Or use config.load_incluster_config() for in-cluster

# Initialize the API client
v1 = client.CoreV1Api()

# List all pods in a specific namespace or cluster-wide by removing the 'namespace' parameter
namespace = "monitoring"
pods = v1.list_namespaced_pod(namespace)

# Loop through the pods and print the node where each pod is scheduled
for pod in pods.items:
    print(f"Pod: {pod.metadata.name} | Node: {pod.spec.node_name}")

