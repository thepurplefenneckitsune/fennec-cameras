# 🤝 Contributing to Fennec Cameras

Thank you for your interest in contributing to **Fennec Cameras**! This project is an open-source, privacy-first initiative dedicated to building a 100% offline security camera hub and NVR mesh system.

---

## 🚀 How You Can Contribute

### 1. 📱 Testing Hardware & Device Profiles
- Test drawer phones, USB webcams, laptops, and single-board computers (Raspberry Pi, Orange Pi, Rockchip).
- Submit device capability benchmarks (CPU usage, thermal performance, max FPS, battery charge limiting).

### 2. 📡 OpenWrt Router Firmware Testing
- Test legacy Wi-Fi router flashing with OpenWrt/DD-WRT.
- Contribute custom QoS configuration rules and WireGuard mesh pairing scripts.

### 3. 💻 Code & Documentation
- Help implement core NVR daemons, WebRTC streaming pipelines, and local AI object detection modules.
- Improve system documentation, setup guides, and hardware compatibility matrices in [`docs/`](docs/).

---

## 📋 Pull Request Guidelines

1. **Keep PRs Focused**: Submit small, well-scoped pull requests focused on a single feature or bug fix.
2. **Follow Decoupled Monorepo Structure**: Place code into its respective target module (`android/`, `desktop-core/`, `web-portal/`, `openwrt-mesh/`, `docker/`, `docs/`).
3. **Privacy First**: Ensure NO code introduces external cloud dependencies, mandatory account sign-ins, or telemetry.

---

## 📜 Code of Conduct

All contributors are expected to uphold a welcoming, respectful, and collaborative environment. See our [Code of Conduct](CODE_OF_CONDUCT.md) for details.
