# 📡 OpenWrt Router Firmware & Mesh Utilities

This directory contains build scripts, custom configurations, and WireGuard package rules for converting old Wi-Fi routers into dedicated camera system mesh nodes.

## 📌 Features & Responsibilities

- **Custom OpenWrt / DD-WRT Flashing**: Repurposes legacy Wi-Fi routers into encrypted camera mesh repeaters.
- **Dual-SSID Mesh Architecture**: Flashes routers to host a standard user Wi-Fi SSID alongside a hidden, encrypted camera mesh SSID.
- **QoS Video Stream Prioritization**: Configures router Quality of Service (QoS) rules to guarantee bandwidth for 24/7 video feeds without stutter.
- **WireGuard Mesh Tunnels**: Automated P2P encrypted tunneling between out-of-range property nodes and NVR storage hubs.

## 📁 Proposed Folder Layout

```
openwrt-mesh/
├── imagebuilder/         # OpenWrt ImageBuilder custom target configs
├── packages/             # Custom mesh routing & WireGuard helper packages
├── uci-defaults/         # Pre-configured default router settings & QoS rules
└── docs/                 # Router hardware compatibility guide (16MB/64MB minimum)
```
