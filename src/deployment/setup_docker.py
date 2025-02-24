# deployment/containerization.py

import subprocess

def setup_docker():
    # Generate a Dockerfile and build the image
    dockerfile_content = """
    FROM python:3.9-slim
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["python", "main.py"]
    """
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

    # Build and run the container
    subprocess.run(["docker", "build", "-t", "rag_system", "."])
    subprocess.run(["docker", "run", "-d", "rag_system"])
