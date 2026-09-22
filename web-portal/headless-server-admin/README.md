# 🖥️ Headless Server Administration Portal

This directory contains the heavy-duty, server-grade web management console tailored for 1U/2U Linux server racks, home lab servers, TrueNAS/Unraid appliances, and Raspberry Pi NVR hubs.

## 🎯 Target Hardware & Use Case

- **Environment**: Headless Linux servers, rackmount systems, and high-performance NVR hubs accessed via `http://<hub-ip>:8081`.
- **Design Philosophy**: Server-grade, feature-rich management console built for multi-monitor displays and deep administrative control. NOT cluttered or limited by mobile layout constraints.

## 📌 Core Capabilities

- **Multi-Camera Grid & Timeline Scrubbing**: Low-latency multi-stream monitoring (WebRTC/go2rtc) with fast timeline scrubbing across local ring buffers and NAS archives.
- **Local AI Object Detection Console**: Granular threshold controls for YOLOv8/ONNX detection models, Coral TPU acceleration, and audio AI trigger sensitivity.
- **Tiered Storage & NAS Management**: Storage node qualification, hard disk endurance monitoring, auto-denial of low-space drives (<16GB), and NFS/SMB mount configurations.
- **Hardware Acceleration Tuning**: Controls for Intel QuickSync (`/dev/dri`), Nvidia NVENC, and VA-API hardware transcoders.
- **Conflict-Free Auto-Port Relocation**: Automatically detects port collisions (80, 8080, 8443) and shifts server binding to 8081 without interfering with Home Assistant or Plex.
