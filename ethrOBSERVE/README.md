# ethrOBSERVE - Observability Module

`ethrOBSERVE` is a standalone observability module for the EthrPlatform ecosystem. It provides a pre-configured Prometheus and Grafana stack for monitoring Ethr services.

## 🚀 Features

- **Prometheus**: Metrics collection and alerting
- **Grafana**: Visualization and dashboards
- **Docker Deployment**: Containerized setup for easy development and production

## 🛠️ Quick Start

### Prerequisites

- Docker and Docker Compose

### Installation

1. **Start the observability stack**
   ```bash
   docker-compose up -d
   ```

2. **Access Grafana**
   - URL: http://localhost:3000
   - Default credentials: admin/admin

3. **Access Prometheus**
   - URL: http://localhost:9090
