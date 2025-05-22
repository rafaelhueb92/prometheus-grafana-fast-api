# Install dependencies
pip install fastapi uvicorn prometheus_client

# Run the app
uvicorn app:app --host 0.0.0.0 --port 8000

# Build and run the image
docker build -t fastapi-app .
docker run -d --name fastapi-app -p 8000:8000 fastapi-app

# Run Docker compose
docker compose build --no-cache
docker compose up