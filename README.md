# 🦊 Fennec Cameras - Linux-First Offline Security Camera Hub

> **100% Offline, Privacy-First Security Camera NVR Mesh System**  
> Repurposing old Android smartphones, Linux laptops, USB webcams, Raspberry Pis, and OpenWrt routers into a cloud-free home security network.

---

> [!IMPORTANT]
> **Community-Driven Concept Roadmap — Single Maintainer Notice**  
> This repository showcases the proposed master architectural blueprint (`docs/ideas.md`) and public showcase page (`web-portal/public-site/public_cam_idea.php`). Nothing is guaranteed. This is an open-source initiative managed and developed by a single maintainer. Features will be researched, built, and shipped sequentially as time and resources allow.

---

## 📁 Repository Monorepo Architecture

To prevent monolithic UI bloat, each component and interface is decoupled and purpose-built for its target hardware role:

```
fennec-cameras/
├── 📱 android/                        # Android Camera Node app (Kotlin / Java / NDK daemons)
├── 💻 desktop-core/                   # Linux NVR daemon, V4L2 drivers, AI engine (ONNX/YOLOv8) & GUI
├── 🌐 web-portal/                     # Purpose-built web interfaces:
│   ├── 🖥️ headless-server-admin/      #   └─ Heavy-duty NVR console for 1U/2U server racks & PCs
│   ├── 📱 mobile-node-ui/             #   └─ Touch-first lightweight UI for phone camera nodes
│   └── 🌐 public-site/                #   └─ Public showcase site & QR generator (public_cam_idea.php)
├── 📡 openwrt-mesh/                   # Custom OpenWrt router firmware scripts, QoS & WireGuard mesh
├── 🐳 docker/                         # Docker Compose stack, GPU acceleration passthrough & configs
├── 📚 docs/                           # System architecture specs, ideas.md & hardware matrix
└── 🎨 assets/                         # Branding logos, diagrams & graphics
```

---

## 🌟 Key Architectural Highlights

- **Decoupled Application Interfaces**: Separate, role-specific UI consoles—a heavy-duty administrative management portal for server racks, a lightweight touch UI for mobile nodes, and native Kotlin/C++ applications.
- **Conflict-Free Auto-Port Relocation Protocol**: Server portal automatically detects occupied ports (80/8080/8443) and auto-relocates to 8081 without colliding with Plex or Home Assistant.
- **Tiered Storage & Storage Node Auto-Denial**: Local flash used strictly as a 5-15m rolling ring buffer; auto-outsources clips to NAS/Storage Nodes; auto-denies low-space (<16GB) nodes.
- **Custom Router Firmware Nodes (OpenWrt/DD-WRT)**: Flashes old routers into dedicated camera mesh nodes with dual-SSID (main + hidden encrypted camera mesh) and video stream QoS.
- **Samsung Wi-Fi Sharing Mesh Repeaters**: Harnesses native Wi-Fi sharing on Samsung Galaxy S / Pixel phones into mesh repeaters to eliminate dead zones.
- **Anti-App-Store Distribution Policy**: Absolutely NO publishing to Google Play or Apple App Store (F-Droid, GitHub Releases, Patreon exclusive).

---

## 📄 Public Showcase Web Page

Deploy `web-portal/public-site/public_cam_idea.php` to your web server for a standalone, SEO-optimized public showcase of all 24 roadmap categories.

---

## 📜 License

Distributed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
