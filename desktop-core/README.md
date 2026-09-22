# 💻 Linux Desktop & Server NVR Core

This directory contains the core backend daemon, video processing pipelines, and desktop interface for PCs, laptops, 1U/2U server racks, and Single-Board Computers (Raspberry Pi, Orange Pi, Rockchip).

## 📌 Features & Responsibilities

- **Headless Linux NVR Daemon**: Low-overhead `systemd` daemon handling ONVIF/RTSP ingestion, V4L2 USB webcams, and WebRTC streaming.
- **Edge AI Motion & Object Detection**: Local ONNX / YOLOv8 / Coral TPU inference for real-time person, vehicle, animal, and package detection without cloud dependencies.
- **Tiered Ring-Buffer Storage Manager**: Manages short-term rolling memory/SSD ring buffers and coordinates automatic offloading to NAS (TrueNAS, Unraid, NFS/SMB mounts).
- **Ethernet DHCP Bridge Gateway**: Converts Linux laptops or PCs into auto-configuring network bridges for hardware PoE switches and IP cameras.
- **Hardware Acceleration**: Intel QuickSync / Nvidia NVENC / VA-API video decoding and encoding pipelines.

## 📁 Proposed Folder Layout

```
desktop-core/
├── daemon/               # Core NVR daemon (C++ / Rust / Go)
├── ai-engine/            # Local ONNX / YOLO / Coral TPU detection pipelines
├── storage/              # Storage manager, ring buffer & NAS sync engine
├── network/              # mDNS, WireGuard P2P & Ethernet DHCP bridge drivers
└── ui/                   # Linux Desktop GUI / Kiosk application
```
