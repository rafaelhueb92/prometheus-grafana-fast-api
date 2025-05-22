# FastAPI Monitoring with Prometheus, Grafana, and Docker Compose

This project demonstrates how to monitor a Python FastAPI application using Prometheus and Grafana, all orchestrated with Docker Compose.

## Features

- **FastAPI**: Simple Python web API exposing metrics.
- **Prometheus**: Collects and stores metrics from FastAPI.
- **Grafana**: Visualizes metrics from Prometheus.
- **Docker Compose**: Runs everything with a single command.

---

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-directory>
```

### 2. Project Structure

```
.
├── app/
|    └── app.py
├── Dockerfile
├── prometheus.yml
├── docker-compose.yml
└── grafana/
    └── provisioning/
        └── datasources/
            └── prometheus.yml
```

### 3. Build and Run the Stack

To build and start all services (FastAPI, Prometheus, Grafana):

```bash
docker compose up --build
```

_To rebuild without cache:_

```bash
docker compose up --build --no-cache
```

### 4. Access the Services

- **FastAPI App**: [http://localhost:8000](http://localhost:8000)
- **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
- **Grafana UI**: [http://localhost:3000](http://localhost:3000)

---

## Grafana Setup

Grafana is pre-configured to use Prometheus as a data source via provisioning.
Default login:

- **Username:** `admin`
- **Password:** `admin` (you may be prompted to change this on first login)

You can now create dashboards and visualize metrics such as request count and request duration.

---

## File Overview

- **app.py**: FastAPI application exposing `/` and `/metrics` endpoints.
- **Dockerfile**: Builds the FastAPI app image.
- **prometheus.yml**: Prometheus configuration to scrape metrics from FastAPI.
- **docker-compose.yml**: Orchestrates all services.
- **grafana/provisioning/datasources/prometheus.yml**: Auto-configures Prometheus as a Grafana data source.

---

## Example FastAPI Metrics

- **request_count**: Total number of requests received.
- **request_processing_seconds**: Time spent processing each request.

You can expand metrics in `app.py` as needed.

---

## Stopping the Stack

To stop all services:

```bash
docker compose down
```

---

## Customization

- Add more metrics in `app.py` using the `prometheus_client` library.
- Add Grafana dashboards by placing JSON files in `grafana/provisioning/dashboards/`.

---

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
