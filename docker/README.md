# 🐳 Docker & Server Deployment

This directory contains container configurations, Docker Compose setups, and environment templates for deploying the Linux NVR Hub in home lab servers, NAS appliances, and Docker environments.

## 📌 Features & Responsibilities

- **Single-Command Setup**: Rapid deployment using `docker compose up -d`.
- **GPU Acceleration Passthrough**: Intel QuickSync (`/dev/dri`) and Nvidia NVENC GPU passthrough configurations.
- **NAS Mount Integration**: Pre-configured volume bindings for NFS, SMB, and local disk arrays.

## 📁 Proposed Folder Layout

```
docker/
├── docker-compose.yml     # Multi-container stack (NVR Core, AI Engine, Web Portal)
├── Dockerfile             # Alpine/Debian minimal NVR daemon Dockerfile
├── .env.example           # Example environment variables (storage paths, ports)
└── configs/               # Containerized service configuration templates
```
