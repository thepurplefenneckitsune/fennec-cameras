# 🔬 Maintainer Hardware Test Bench & Device Matrix

> **Low-End & Real-World Hardware First Philosophy**  
> Fennec Cameras is developed and tested by a single maintainer using budget, entry-level, and everyday hardware. If it runs smoothly on this test bench, it will run smoothly on anything!

---

## 💻 Available Test Bench Hardware Inventory

The maintainer currently owns and tests on the following specific devices:

### 🐧 Linux Laptops (Primary Development & Hub Nodes)
1. **Intel N150 Laptop** (Linux OS)
   - *Role*: Low-power efficiency Linux NVR Hub & daemon testing.
2. **Intel Pentium Gold 6500Y Laptop** (Linux OS)
   - *Role*: Secondary budget Linux node & local web admin console testing.

### 📱 Mobile Devices (Camera Nodes & Touch Controllers)
1. **Samsung Galaxy S24 FE** (Android 14+)
   - *Role*: High-definition Android Camera Node & Multi-Camera API testing.
2. **Moto G 5G (2024)** (Android 14)
   - *Role*: Budget 5G Android Camera Node & background service resilience testing.
3. **iPhone XR** (iOS)
   - *Role*: Mobile browser preview & cross-platform WebRTC streaming testing.
4. **iPad (6th Generation) Cellular** (iPadOS)
   - *Role*: Tablet touch controller & cellular connection testing.

---

## 🛑 Hardware Limitations & What I DO NOT Have

Because this is a solo-maintainer open-source initiative, **there are NO high-end devices or commercial server racks in this test lab**:

- ❌ **NO Mac / macOS Computers**: No MacBook Pro, Mac mini, or Mac Studio (Cannot natively build/test macOS desktop binaries).
- ❌ **NO Windows PC / Windows Laptops**: No dedicated Windows 10/11 desktop or laptop testing environment.
- ❌ **NO High-End GPUs or Workstations**: No Nvidia RTX 3090/4090, Intel Arc desktop GPUs, or high-throughput CUDA acceleration rigs.
- ❌ **NO Enterprise 1U/2U Server Racks**: No dedicated rackmount NVR hardware or enterprise SAN/NAS hardware.

---

## 🎯 Why This Is Great For The Project

Developing on budget Linux laptops (Intel N150 & Pentium 6500Y) ensures that Fennec Cameras **remains ultra-lightweight, zero-cloud, and non-bloated**. It forces the software to operate with extreme resource efficiency so that old laptops, budget phones, and small Single-Board Computers (SBCs) can run 24/7 without overheating or freezing.

---

## 🤝 Community Call to Action: Help Test What I Don't Have!

If you own hardware that the maintainer lacks, **your feedback and test reports are invaluable!** We especially need community testers for:

- 🍎 **macOS Users**: Testing WebRTC streaming & desktop UI on Mac.
- 🪟 **Windows Users**: Testing local web portal & native Windows daemon wrappers.
- ⚡ **High-End GPU Owners**: Benchmarking Intel QuickSync, NVENC, and Coral TPU ONNX AI acceleration.
- 📡 **OpenWrt Router Flashing**: Testing custom OpenWrt/DD-WRT router firmware node scripts.

👉 **Got hardware to report?** Open a report in [**GitHub Discussions**](https://github.com/thepurplefenneckitsune/fennec-cameras/discussions) or submit an issue!
