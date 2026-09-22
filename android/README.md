# 📱 Android Camera Node Application

This directory contains the source code for the **Native Android Camera Node** client app.

## 📌 Features & Responsibilities

- **24/7 Camera Node Execution**: Native Android daemon for capturing, encoding, and streaming local phone camera feeds over LAN/mesh.
- **Battery Optimization Bypass**: Implements foreground services and `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` to prevent Android OS from sleeping background camera captures.
- **Multi-Camera API Capture**: Dual-lens front + rear simultaneous capture and 360° panoramic view stitching (Android API 28+).
- **USB Host API Driver**: Custom audio/video driver to bypass default Android USB audio hijack when connecting USB webcams or microphones via OTG.
- **Kiosk & Pinning Mode**: Locks phone screen to camera mode using `LockTask` / Screen Pinning APIs with master password protection.
- **Anti-App-Store Distribution**: Build scripts tailored for **F-Droid**, **GitHub Releases**, and Patreon direct APK downloads.

## 📁 Proposed Folder Layout

```
android/
├── app/                  # Android Studio application module
│   ├── src/main/
│   │   ├── java/         # Kotlin/Java codebase
│   │   ├── cpp/          # Native C/C++ daemons & V4L2/USB wrappers
│   │   └── res/          # UI resources, layouts & vector drawables
│   └── build.gradle.kts
├── fdroid/               # F-Droid build configuration & metadata
└── scripts/              # APK signing & release automation scripts
```
