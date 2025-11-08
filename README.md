# EthrAUTH - Keycloak Authentication Service

EthrAUTH is a dedicated authentication service built on Keycloak, providing centralized identity management for the Ethr ecosystem.

## 🚀 Features

- **Keycloak Integration**: Industry-standard identity and access management
- **PostgreSQL Backend**: Scalable database storage for users and sessions
- **Docker Deployment**: Containerized setup for easy development and production
- **Multi-Realm Support**: Separate realms for different applications and environments
- **OAuth2/OIDC Compliance**: Standard protocols for secure authentication

## 🏗️ Architecture

### Core Components

- **Keycloak Server**: Central authentication provider
- **PostgreSQL Database**: User and session data storage
- **Docker Compose**: Simplified deployment and management

### Integration Points

- **EthrSITE**: Frontend website builder platform
- **EthrSECRETS**: Secrets management service
- **Future Services**: Additional Ethr ecosystem components

## 🛠️ Quick Start

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/iniitydev/ethrauth.git
   cd ethrauth
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

3. **Start Keycloak**
   ```bash
   docker-compose up -d
   ```

4. **Access Keycloak Admin Console**
   - URL: http://localhost:8080
   - Username: admin
   - Password: [from KEYCLOAK_ADMIN_PASSWORD in .env]

## 🔧 Configuration

### Keycloak Realm Setup

1. Create a new realm for your application
2. Configure clients for each service (EthrSITE, etc.)
3. Set up users, roles, and groups
4. Configure identity providers if needed (Authentik, etc.)

### Environment Variables

See [`.env.example`](.env.example) for all required environment variables.

## 🔌 Integration with EthrSITE

### Client Configuration

1. In Keycloak Admin, create a new client for EthrSITE
2. Set Valid Redirect URIs to your EthrSITE URLs
3. Configure client authentication (secret or public)
4. Update EthrSITE environment variables with client details

### Environment Variables for EthrSITE

```bash
KEYCLOAK_URL=http://localhost:8080
KEYCLOAK_REALM=your-realm-name
KEYCLOAK_CLIENT_ID=ethrsite-frontend
KEYCLOAK_CLIENT_SECRET=your-client-secret
```

## 🚢 Deployment

### Production Deployment

1. **Set production environment variables**
   ```bash
   # Update .env with production values
   KEYCLOAK_URL=https://auth.yourdomain.com
   KEYCLOAK_ADMIN_URL=https://auth.yourdomain.com
   ```

2. **Deploy with Docker Compose**
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

### Docker Production Overrides

Create `docker-compose.prod.yml` for production-specific settings:

```yaml
version: '3.8'

services:
  keycloak:
    environment:
      - KC_PROXY=edge
      - KC_HOSTNAME_STRICT=true
      - KC_HOSTNAME_STRICT_HTTPS=true
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.keycloak.rule=Host(`auth.yourdomain.com`)"
      - "traefik.http.services.keycloak.loadbalancer.server.port=8080"
```

## 📊 Monitoring & Logs

### View Logs
```bash
docker-compose logs keycloak
docker-compose logs postgres
```

### Health Checks
- Keycloak: http://localhost:8080/health
- Metrics: http://localhost:8080/metrics

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📄 License

MIT License - see LICENSE file for details.

## 🆘 Support

- Create issues in GitHub repository
- Check Keycloak documentation
- Review Docker and PostgreSQL logs for troubleshooting