# Advanced MLOps Activity — Versioned ML Pipeline with Docker, Airflow & Container Registry

This repository contains starter code for the advanced class activity.

This activity builds on mlopsclassactivity1 to implement a production-like MLOps pipeline.

Students will:

    1. Use Docker to containerize training & serving

    2. Apply model versioning (v1, v2, …)

    3. Automate retraining using Apache Airflow

    4. Push images to DockerHub (or private registry)

    5. Add basic monitoring & rollback mechanisms

# Versioned ML Pipeline

![Versioned ML Pipeline](Actv2img.png)


# 1. Train a Versioned Model
python train.py v2 data/iris.csv data/new_data.csv
Saves model as model_v2.pkl

# 2. Build & Push Docker Images
docker build -f Dockerfile.train -t <dockerhub-username>/ml-train:v2 .
docker push <dockerhub-username>/ml-train:v2

docker build -f Dockerfile.serve -t <dockerhub-username>/ml-api:v2 .
docker push <dockerhub-username>/ml-api:v2

# 3. Run Serving Container
docker run -p 8000:8000 -e MODEL_PATH=model_v2.pkl <dockerhub-username>/ml-api:v2

# 4. Test API Endpoint
curl -X POST "http://localhost:8000/predict" \
    -H "Content-Type: application/json" \
    -d '{"features": [5.1, 3.5, 1.4, 0.2]}'


Example response:

{"prediction": 0, "version": "model_v2.pkl"}

# 5. Airflow DAG

Start Airflow:

airflow standalone


Copy dags/ml_pipeline_versioned.py into the dags/ folder.

Trigger DAG run. The DAG will:

Check for new_data.csv

Retrain & version model (v2, v3, …)

Build & push image

Deploy container

Rollback if accuracy is worse

# 6. Monitoring

API logs request latency & errors

Returns model version in prediction response

# Deliverables

Students must submit:

1. Modified train.py, app.py, and Dockerfiles

2. Airflow DAG (ml_pipeline_versioned.py)

3. Screenshots of:

    a. DockerHub with versioned images

    b. Airflow DAG run logs

    c. API predictions showing model version

    d. Rollback demonstration
