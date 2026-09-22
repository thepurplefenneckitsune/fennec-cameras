# 🦊 Fennec Cameras - Linux-First Offline Security Camera Hub

> **100% Offline, Privacy-First Security Camera NVR Mesh System**
> Repurposing old Android smartphones, Linux laptops, USB webcams, Raspberry Pis, and OpenWrt routers into a cloud-free home security network.

---

> [!IMPORTANT]
> **Community-Driven Concept Roadmap — Single Maintainer Notice**
> This repository showcases the proposed master architectural blueprint (`ideas.md`) and public showcase page (`public_cam_idea.php`). Nothing is guaranteed. This is an open-source initiative managed and developed by a single maintainer. Features will be researched, built, and shipped sequentially as time and resources allow.

---

## 🌟 Key Architectural Highlights

- **App-First Architecture & Headless Web Portal**: App-first daily controls with embedded local web administration for headless 1U/2U server racks.
- **Conflict-Free Auto-Port Relocation Protocol**: Detects occupied ports (80/8080/8443) and auto-relocates to 8081 without colliding with Plex or Home Assistant.
- **Tiered Storage & Storage Node Auto-Denial**: Local flash used strictly as a 5-15m rolling ring buffer; auto-outsources clips to NAS/Storage Nodes; auto-denies low-space (<16GB) nodes.
- **Custom Router Firmware Nodes (OpenWrt/DD-WRT)**: Flashes old routers into dedicated camera mesh nodes with dual-SSID (main + hidden encrypted camera mesh) and video stream QoS.
- **Samsung Wi-Fi Sharing Mesh Repeaters**: Harnesses native Wi-Fi sharing on Samsung Galaxy S / Pixel phones into mesh repeaters to eliminate dead zones.
- **Anti-App-Store Distribution Policy**: Absolutely NO publishing to Google Play or Apple App Store (F-Droid, GitHub Releases, Patreon exclusive).

---

## 📄 Public Showcase Web Page

Deploy `public_cam_idea.php` to your web server for a standalone, SEO-optimized public showcase of all 24 roadmap categories.

---

## 📜 License

Distributed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
