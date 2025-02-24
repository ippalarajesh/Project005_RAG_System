# deployment/containerization.py

def setup_kubernetes():
    # Example Kubernetes YAML for deploying the system
    k8s_deployment = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: rag-system
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: rag-system
      template:
        metadata:
          labels:
            app: rag-system
        spec:
          containers:
            - name: rag-system
              image: rag_system:latest
              ports:
                - containerPort: 80
    """

    with open("k8s_deployment.yaml", "w") as f:
        f.write(k8s_deployment)

    # Apply the Kubernetes configuration
    subprocess.run(["kubectl", "apply", "-f", "k8s_deployment.yaml"])
