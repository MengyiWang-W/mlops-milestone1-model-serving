## mlops-milestone1-model-serving
This project demonstrates a simple machine learning model serving pipeline using both a FastAPI container deployed on Google Cloud Run and a serverless deployment using Google Cloud Functions.

A lightweight scikit-learn regression model is trained and saved as a serialized artifact (model.pkl). The model is exposed through HTTP endpoints for inference.

## Project Workflow
The workflow follows the machine learning deployment lifecycle:
Input data → HTTP API → trained model → prediction output.

Steps:
Train and save a regression model as model.pkl.
Implement a FastAPI service exposing a /predict endpoint.
Containerize the FastAPI application using Docker.
Deploy the container to Google Cloud Run.
Implement the same prediction logic using Google Cloud Functions.
Test both deployments using HTTPS requests.

## Technologies Used
Python 3.10, FastAPI, scikit-learn, NumPy, Joblib, Docker, Google Cloud Run, and Google Cloud Functions.

## Local FastAPI Service
Install dependencies: pip install -r requirements.txt
Run locally: uvicorn main:app --host 0.0.0.0 --port 8000
POST /predict 
Request example: {"features":[1,2,3]}
Response example:{"prediction":10.0,"model_version":"1.0"}

## Cloud Run Deployment (FastAPI Container)
The FastAPI service is deployed as a container to Google Cloud Run and is publicly accessible via HTTPS.
Example endpoint:
https://mlops-model-service-76924655583.us-central1.run.app/predict

Example request:
curl -X POST https://mlops-model-service-76924655583.us-central1.run.app/predict \
-H "Content-Type: application/json" \
-d '{"features":[1,2,3]}'

The Docker image is stored in Google Artifact Registry, ensuring a reproducible runtime environment.

## Cloud Function Deployment (Serverless)
The same prediction logic is implemented using Google Cloud Functions.

Example endpoint:
https://us-central1-project-26ae2bab-32e3-4c7d-bac.cloudfunctions.net/predict

Example request:
curl -X POST https://us-central1-project-26ae2bab-32e3-4c7d-bac.cloudfunctions.net/predict \
-H "Content-Type: application/json" \
-d '{"features":[1,2,3]}'

The Cloud Function loads the model artifact and returns predictions through an HTTP-triggered function.

## Cold Start and Warm Instance
A cold start occurs when no instance is running and the platform must initialize the runtime and load the model. This causes higher latency for the first request. A warm instance already has the model loaded in memory and responds much faster to subsequent requests.

Cloud Functions typically experience more noticeable cold starts than Cloud Run containers due to their stateless nature.

## FastAPI Container vs Cloud Function
The FastAPI container on Cloud Run runs as a long-lived service where the model is loaded once per container lifecycle, resulting in lower latency for warm requests and better control over the environment.

Cloud Functions are fully stateless and reload the model during cold starts, which increases latency but simplifies deployment and scaling.

Cloud Run emphasizes reproducibility and flexibility through Docker images, while Cloud Functions prioritize simplicity and automatic scaling.

## Reproducibility
Reproducibility is ensured through:
Fixed dependencies in requirements.txt
Docker-based deployment for Cloud Run
Deterministic loading of the same model.pkl artifact
Clear setup and deployment instructions

## Lifecycle Understanding (Deployment Stage)
This project demonstrates two model serving approaches:
a containerized FastAPI service using Cloud Run and a serverless Cloud Function deployment. It highlights differences in lifecycle management, latency (cold starts), and reproducibility, providing practical insight into modern MLOps deployment patterns.

This project focuses on the deployment/serving stage of the ML lifecycle.

Training → Artifact creation: train_model.py trains a scikit-learn model and exports a portable artifact (model.pkl). This file represents the model output of the training stage and is treated as a versioned runtime dependency.

Artifact management:

In Cloud Run, the artifact is bundled inside the Docker image at build time, so the runtime environment (code + dependencies + model) is reproducible and portable.

In Cloud Functions, the artifact is packaged with the function source and loaded from the function directory at runtime. This keeps deployment simple but emphasizes stateless execution.

Model-API interaction: Both deployments implement the same inference contract: the client sends JSON input (features) → the API validates/parses the request → the model runs inference → the API returns a JSON prediction (prediction, model_version).
This clarifies the boundary between model logic (scikit-learn inference) and serving layer (HTTP request/response).