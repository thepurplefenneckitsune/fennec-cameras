<div align="center">

  <img src="https://thepurplefox.sirv.com/kistune%20cam/purple_kitsune_logo2.jpg?cx=67&cy=74&cw=890&ch=890" width="128" height="128" alt="Fennec Cameras Logo" style="border-radius: 24px;">

  # 🦊 Fennec Cameras
  ### Linux-First Offline Security Camera Hub & NVR Mesh System

  *100% Open-Source, Privacy-First, Cloud-Free Home Security Network*

  [![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-purple.svg)](LICENSE)
  [![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Android%20%7C%20OpenWrt-indigo.svg)](#-platform-matrix)
  [![Architecture](https://img.shields.io/badge/Architecture-Offline--First%20Mesh-emerald.svg)](#-key-architectural-highlights)
  [![Distribution](https://img.shields.io/badge/Distribution-F--Droid%20%7C%20GitHub-blue.svg)](#-distribution-policy)
  [![Showcase](https://img.shields.io/badge/Live%20Showcase-thepurplefox.site-ff007f.svg)](https://thepurplefox.site/public_cam_idea.php)

  [🌐 Public Web Showcase](https://thepurplefox.site/public_cam_idea.php) • [📚 Full Roadmap Specs](docs/ideas.md) • [🤝 Contributing](CONTRIBUTING.md) • [📜 License](LICENSE)

</div>

---

> [!IMPORTANT]
> **Community-Driven Concept Roadmap — Single Maintainer Notice**  
> This repository showcases the proposed master architectural blueprint ([`docs/ideas.md`](docs/ideas.md)) and public showcase web page ([`web-portal/public-site/public_cam_idea.php`](web-portal/public-site/public_cam_idea.php)). Features will be researched, built, and shipped sequentially as time and community support allow.

---

## 🌟 Overview

**Fennec Cameras** turns drawer smartphones, old laptops, USB webcams, Raspberry Pis, 1U/2U server racks, and flashed Wi-Fi routers into a unified, zero-cloud home security network.

- **Zero Cloud Accounts**: Operates 100% offline over local Wi-Fi and P2P WireGuard mesh.
- **Zero Subscription Fees**: Hardware and software under your complete control.
- **Zero Telemetry**: No tracking, no external server pings, and 100% local edge AI processing.

---

## 📁 Repository Monorepo Architecture

To prevent monolithic UI clutter, every platform component and interface is decoupled and purpose-built for its target hardware role:

```
fennec-cameras/
├── 📱 android/                        # Android Camera Node app (Kotlin / Java / Native NDK daemons)
├── 💻 desktop-core/                   # Linux NVR daemon, V4L2 drivers, AI engine (ONNX/YOLOv8) & GUI
├── 🌐 web-portal/                     # Decoupled platform web interfaces:
│   ├── 🖥️ headless-server-admin/      #   └─ Heavy-duty NVR console for 1U/2U server racks & PCs
│   ├── 📱 mobile-node-ui/             #   └─ Touch-first lightweight UI for phone camera nodes
│   └── 🌐 public-site/                #   └─ Public showcase site & QR generator (public_cam_idea.php)
├── 📡 openwrt-mesh/                   # Custom OpenWrt router firmware scripts, QoS & WireGuard mesh
├── 🐳 docker/                         # Docker Compose stack, GPU acceleration passthrough & configs
├── 📚 docs/                           # System architecture specs, ideas.md & hardware matrix
└── 🎨 assets/                         # Branding logos, diagrams & graphics
```

---

## ⚡ Key Architectural Highlights

| Feature | Description |
| :--- | :--- |
| **Decoupled Application UIs** | Dedicated, role-specific UIs—a heavy-duty administrative management console for server racks, a touch-first mobile UI for phone nodes, and native Android/Linux binaries. |
| **Conflict-Free Auto-Port Relocation** | Automatically detects occupied ports (`80`, `8080`, `8443`) and shifts server binding to `8081` without colliding with Plex or Home Assistant. |
| **Tiered Storage & Auto-Denial** | Local phone flash is used strictly as a 5-15m rolling ring buffer before auto-offloading clips to NAS storage nodes. Low-space drives (<16GB) are auto-denied. |
| **OpenWrt Router Firmware Nodes** | Flashes old Wi-Fi routers into dedicated camera mesh nodes with dual-SSID (main + hidden encrypted camera mesh) and video stream QoS. |
| **Wi-Fi Sharing Mesh Repeaters** | Harnesses native Wi-Fi sharing on Samsung / Pixel phones into mesh repeaters to eliminate dead zones. |
| **Anti-App-Store Policy** | Explicitly distributed via **F-Droid**, **GitHub Releases**, and Patreon—bypassing Play Store background execution bans and battery-saver restrictions. |

---

## 🖥️ Platform Matrix

- **Android Camera Nodes**: Android 8.0+ (API 26+) with battery-saver bypass and multi-camera (front + rear 360°) capture.
- **Linux NVR Servers**: Ubuntu, Debian, Arch, Alpine, Raspberry Pi OS, TrueNAS/Unraid via Docker.
- **Router Nodes**: OpenWrt 21.02+ / DD-WRT on devices with 16MB+ Flash / 64MB+ RAM.

---

## 🤝 Contributing & Community

We welcome contributions of all kinds! Check out our [**Contributing Guide**](CONTRIBUTING.md) to learn how to test hardware, submit profiles, or contribute code.

---

## 📜 License

Distributed under the **GNU Affero General Public License v3.0 ([AGPL-3.0](LICENSE))**.
