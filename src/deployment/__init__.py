# deployment/__init__.py

# Import the deployment-related components for easy access
from .containerization import setup_docker, setup_kubernetes
from .monitoring import setup_monitoring, log_metrics
from .cost_optimization import optimize_costs
from .security import setup_security

# Define versioning or configuration related to the deployment pipeline
__version__ = '1.0.0'

# Expose essential functions/classes in the public API for deployment
__all__ = [
    'setup_docker',
    'setup_kubernetes',
    'setup_monitoring',
    'log_metrics',
    'optimize_costs',
    'setup_security'
]


################################################################################################################################################

# Example of how to use the deployment module

from deployment import setup_docker, setup_kubernetes, setup_monitoring, log_metrics, optimize_costs, setup_security

# 1. Docker Setup: Build and run the RAG system in a Docker container
setup_docker()

# 2. Kubernetes Setup: Deploy the system on a Kubernetes cluster
setup_kubernetes()

# 3. Monitoring: Set up Prometheus and Grafana for system performance monitoring
setup_monitoring()

# 4. Log Metrics: Log system performance metrics (e.g., latency, errors)
log_metrics("response_latency", 150)  # Log latency in milliseconds

# 5. Cost Optimization: Manage and optimize costs, e.g., OpenAI API usage
optimize_costs()

# 6. Security Setup: Configure security measures (e.g., SSL, authentication)
setup_security()
