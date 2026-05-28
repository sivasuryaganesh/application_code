# AKS GitOps Python Application

Simple Flask application deployed to Azure Kubernetes Service (AKS) using GitOps.

---

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Azure Kubernetes Service (AKS)
- GitHub Actions
- ArgoCD

---

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run application

```bash
python app.py
```

Application runs on:

```bash
http://localhost:5000
```

---

## Docker Build

```bash
docker build -t aks-python-app .
```

Run container:

```bash
docker run -p 5000:5000 aks-python-app
```

---

