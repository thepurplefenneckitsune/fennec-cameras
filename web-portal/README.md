# 🌐 Web Portals & Platform-Specific Interfaces

This directory contains the decoupled web interfaces and portals for the Fennec Cameras system.

Rather than forcing a single monolithic web interface that feels clunky on smartphones and underpowered for server racks, each interface is purpose-built for its target hardware role:

---

## 📁 Decoupled Sub-Portals

### 1. 🖥️ [`headless-server-admin/`](headless-server-admin/)
- **Target**: 1U/2U Linux Server Racks, Home Lab Servers, TrueNAS/Unraid, and NVR Hub PCs (`http://<hub-ip>:8081`).
- **Scope**: Heavy-duty, server-grade NVR console featuring multi-channel grid playback, high-performance timeline scrubbing, local AI model tuning (YOLOv8/ONNX), NAS storage quota management, and hardware acceleration controls.

### 2. 📱 [`mobile-node-ui/`](mobile-node-ui/)
- **Target**: Android smartphones, drawer phones, and mobile touch controllers.
- **Scope**: Touch-first, lightweight interface optimized specifically for phone camera nodes, quick stream previews, battery/thermal management, and handheld touch operation without heavy server desktop clutter.

### 3. 🌐 [`public-site/`](public-site/)
- **Target**: Public web hosting servers (e.g., `thepurplefox.site/public_cam_idea.php`).
- **Scope**: SEO-optimized public project showcase page (`public_cam_idea.php`), interactive roadmap, and online preset setup QR code generator.
