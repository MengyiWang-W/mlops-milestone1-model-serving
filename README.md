# mlops-milestone1-model-serving
The purpose of this project is to demonstrate a simple machine learning model serving pipeline using FastAPI and Docker.

A machine learning model is trained using scikit-learn and saved as a `model.pkl` file.  
FastAPI is used to expose a REST API endpoint for prediction, and Docker is used to containerize the application to ensure reproducibility and portability.
---
## Project Structure
mlops-milestone1-model-serving/
│
├── main.py # FastAPI application for model serving
├── train_model.py # Script to train and save model.pkl
├── model.pkl # Trained machine learning model
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── screenshots/ # Screenshots of Docker build and API testing
├── cloud_function/ # Placeholder for future cloud deployment
└── README.md
## Dependencies
All required Python packages are listed in `requirements.txt`.
Dependencies can be installed using:
```bash
pip install -r requirements.txt
```
The project targets Python 3.10, consistent with the Docker base image configuration.
## Model Training
The model is trained using a simple Linear Regression model from scikit-learn. Run the following command to generate the trained model file: 
python train_model.py
This will create a model.pkl file in the project directory.
## Build Docker Image
docker build -t mlops-milestone1 .
## Run Docker Container
docker run -p 8000:8000 mlops-milestone1
After running, the FastAPI server will start at: http://localhost:8000
## API Endpoint
POST /predict
Request example:{"features": [1, 2, 3]}
Response example:{"prediction": 10,"model_version": "1.0"}
## Screenshots
Screenshots of Docker build and API testing are provided in the screenshots/ folder, including:
Docker image build success
Docker container running
FastAPI /predict endpoint tested in browser and command line
## Relation to the ML Lifecycle
This project demonstrates the deployment stage of the machine learning lifecycle.
By training a model, saving it as a serialized file, and serving it through an API endpoint, the project connects model development with production-style serving.
Using Docker ensures a reproducible runtime environment and reduces discrepancies between local execution and deployment environments.
## Technologies Used
Python
FastAPI
Docker
scikit-learn
NumPy
Joblib