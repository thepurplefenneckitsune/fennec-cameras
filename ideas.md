# Linux-First Offline-Resilient NVR & Security Camera System
*Concept & Feature Roadmap*

---

## 1. Universal Camera Protocols, Dual-Lens & 360° Capture
- [ ] **Headless Linux Core**: Lightweight Linux daemon capable of running on old laptops, mini PCs, or 1U/2U server racks (Debian, Ubuntu, Proxmox).
- [ ] **Universal Camera Nodes & Feeds**:
  - [ ] **USB Webcams**: Native V4L2 (`/dev/video*`) capture for old 720p/1080p webcams.
  - [ ] **Android Devices**: Lightweight web/native client that captures camera feeds without Android's aggressive background app sleep routines.
  - [ ] **PoE & IP Cameras (ONVIF / RTSP)**: Native ingestion of Power over Ethernet (PoE) and standard RTSP/HTTP IP camera feeds.
  - [ ] **VoIP & SIP Camera Doorbell Support**: Full support for VoIP/SIP video doorbells with 2-way audio intercom capability.
- [ ] **PTZ Camera Controls**: Control Pan, Tilt, Zoom (PTZ) on supported ONVIF/IP cameras directly from the Web Dashboard.
- [ ] **Flash / Torch Light Remote & Motion Control**: Remote toggle for device flashlights and auto-turn-on flash when motion is detected in low light.
- [ ] **Built-in Night Vision & IR Sensor Support**:
  - [ ] Native driver support for hardware Infrared (IR) / Night Vision sensors on rugged smartphones (Doogee, Ulefone, AGM, Blackview).
  - [ ] Auto-switch IR illuminator LEDs in pitch-black conditions.
- [ ] **Dual-Lens & 360° Panoramic Mode for Mobile**:
  - [ ] **Simultaneous Multi-Camera Capture**: Multi-camera API (Camera2 / Android API 28+) to stream both **Front + Back** lenses concurrently (and ultra-wide/telephoto rear lenses).
  - [ ] **Stitched 360° View**: Combine front and back camera streams into a single side-by-side or stitched 360° panoramic view.
- [ ] **Dual-Mode Flex**: Any machine can act as a **Node** (capture), **Hub** (NVR engine), or **Both**.
- [ ] **Low-Latency Streaming Pipeline**: WebRTC / go2rtc integration for sub-second live feeds without heavy RTSP re-encoding.
- [ ] **Circular Buffer Recording**: Auto-rolling continuous recording (e.g. 7-day retention) with automatic deletion of old clips based on storage quotas.

---

## 2. One-Scan Setup QR Provisioning & Automated Network Re-registration
- [ ] **One-Touch All-in-One Setup QR Code & Info Display**:
  - [ ] **Comprehensive Setup Payload**: Master QR code encodes complete setup metadata (Device IP, Hub IP, Temporary Setup Password, Master Password, camera role, port, and encryption tokens).
  - [ ] **On-Screen Setup Card**: UI clearly displays the QR code alongside readable setup credentials (IP, Port, Temp Password, Pairing Status) for quick visual reference.
- [ ] **Zero-Typing Node Provisioning**:
  - [ ] Scan the QR code on any phone, laptop, or edge node to automatically configure network credentials, verify security tokens, pair with the Hub, and lock into Camera Mode in a single step.
- [ ] **Automated Network Scanning & Node Re-registration Engine**:
  - [ ] **Network Auto-Discovery Sweep**: Server nodes and dedicated Hubs run background mDNS/Zeroconf, BLE beacon sweeps, and local subnet ARP discovery to find camera nodes after power cycles or router DHCP IP changes.
  - [ ] **Seamless Auto-Re-registration**: When a node disconnects or changes IP address, server nodes automatically re-verify its cryptographic identity token and re-register the node into the live stream pipeline without requiring manual user intervention or re-scanning QR codes.

---

## 3. Bluetooth BLE Hotspot Credential Sharing & Failover Handshake
- [ ] **BLE Hotspot Credential Sync**: When a phone node switches to mobile SIM hotspot mode, it automatically broadcasts encrypted hotspot credentials over Bluetooth Low Energy (BLE).
- [ ] **Auto-Connect Hub & Laptop Gateway**: Laptops, Linux Hubs, and nearby nodes automatically receive the BLE payload and connect to the phone's hotspot without manual user intervention.

---

## 4. Native Android Permissions & Battery Optimization Bypass
- [ ] **Automatic Battery Saver Bypass (`REQUEST_IGNORE_BATTERY_OPTIMIZATIONS`)**: Guided one-tap setup to whitelist app from Android Doze mode and manufacturer power savers (Samsung, Xiaomi, Huawei).
- [ ] **Foreground Service Enforcer**: High-priority Foreground Service with persistent notification to prevent Android OS from killing camera background threads.
- [ ] **System Overlay & Alert Window**: `SYSTEM_ALERT_WINDOW` permission to keep camera capture active across reboots and screen lock states.

---

## 5. Active SIM Cellular Hotspot Failover & Laptop Ethernet Auto-Bridge
- [ ] **Active SIM & Mobile Data Auto-Detection**: Detect phones with active cellular SIM cards; auto-configure mobile hotspot and fail back to cellular data when Wi-Fi drops.
- [ ] **Laptop/PC Ethernet Auto-Bridge (Ethernet Out)**:
  - [ ] Turn any laptop or PC with Wi-Fi and Ethernet into an auto-configuring Network Gateway (`dnsmasq` / NetworkManager auto-bridge).
  - [ ] Plug PoE switches, IP cameras, or server rack UPS hardware directly into the laptop's Ethernet jack without needing a standalone router.
- [ ] **UPS & Power Outage Failover**: Maintain full network routing and NVR recording for server racks during power outages using battery-backed laptops.

---

## 6. Universal USB Bus Engine & Audio Routing (Android, Linux, Raspberry Pi, Servers)
- [ ] **Cross-Platform USB Device Discovery**: Unified `libusb` / V4L2 / ALSA detection protocol for Linux PCs, Laptops, Raspberry Pis, Server Racks, and Android OTG hubs.
- [ ] **Android Audio Hijack Bypass**: Direct USB Host API audio driver prevents Android OS from hijacking system audio routing when a USB microphone is plugged in.
- [ ] **Bi-Directional USB Audio (Mic + Speaker)**: Use external USB microphones for audio recording/AI detection, and USB audio out for 2-way walkie-talkie intercom or siren output.
- [ ] **External USB Webcams & Storage**: Support USB cameras and USB flash drives/SSDs across all devices (Android, Linux, Pi).
- [ ] **Hardware USB Motion Detectors**: Ingest signals from USB PIR motion sensors and USB serial devices on any node.

---

## 7. Instant Boot-Time Auto-Start & Headless Appliance Mode
- [ ] **Auto-Start on Boot (`BOOT_COMPLETED` / `systemd`)**: Node app and Linux daemon automatically start streaming the second power is turned on or restored.
- [ ] **Zero-Touch Startup**: No manual unlock or touch interaction required—immediately initializes camera feeds, NVR engine, and Kiosk Lock Mode on boot.

---

## 8. Tiered Storage Architecture, Dedicated Storage Nodes & NAS Outsourcing
- [ ] **Tiered Storage Pipeline (Quick-Time Local Buffer -> External Retention)**:
  - [ ] **On-Device Ring Buffer**: Internal flash/SD storage on camera nodes is strictly used as a quick-time rolling ring buffer (5–15 min buffer or offline network drop buffer) to preserve flash memory health.
  - [ ] **Auto-Outsourcing to NAS & Storage Nodes**: Continuous background streaming/upload of recorded video segments to central NAS (TrueNAS, Unraid, OpenMediaVault, Synology via NFS/SMB/iSCSI) or designated storage nodes.
- [ ] **Dedicated Storage Node Role (Hardware Agnostic)**:
  - [ ] **Flexible Storage Nodes**: ANY device in the cluster—whether an old laptop with an external hard drive/SSD, a server rack node, a mini PC, or a Raspberry Pi with USB RAID—can be designated as a Dedicated Storage Node.
- [ ] **Storage Node Qualification & Auto-Denial Engine**:
  - [ ] **Automatic Storage Denial**: System automatically checks storage capacity and write performance, denying storage node roles to devices with insufficient free disk space (< 16 GB free) or low flash memory endurance.
  - [ ] **Manual Storage Opt-Out**: One-tap admin setting to explicitly deny specific low-end devices or budget phones from acting as storage nodes.
- [ ] **High-Performance Timeline Scrubbing & Playback**:
  - [ ] Fast, low-latency UI timeline scrubber allowing users to seamlessly scrub through historical footage stored across local buffers, dedicated storage nodes, and NAS shares.
  - [ ] Visual event markers for motion triggers, AI object detections, and offline buffer catch-up sync markers.
- [ ] **Home Lab & Home Assistant Integration**:
  - [ ] **Home Assistant Auto-Discovery**: Native MQTT Auto-Discovery to push camera streams, motion sensors, battery stats, and flashlight toggles into Home Assistant.
  - [ ] **MQTT Broker Ingestion & Telemetry**: Publish motion detection events, frame snapshots, battery levels, and tamper alerts (`home/cameras/cam1/motion`).
  - [ ] **External Home Lab Sensor Triggers**: Trigger high-priority recording, PTZ positions, or flashlights from external Zigbee/Z-Wave sensors.
  - [ ] **Apple HomeKit & Google Home via Scrypted / Homebridge**: Expose feeds to Apple HomeKit/Google Home.
  - [ ] **Inbound & Outbound Webhooks**: Webhook engine for Node-RED, Matrix, Discord, and custom home lab scripts.

---

## 9. Local Edge AI, Smart Detection & Natural Language Search
- [ ] **Local Object Detection (Person, Vehicle, Animal, Package)**: Run lightweight ONNX / YOLOv8 / Coral TPU models locally without sending frames to the cloud.
- [ ] **Facial Recognition & License Plate (ALPR/ANPR)**: Tag known family members vs. visitors and log vehicle license plates entering driveways.
- [ ] **Audio AI Recognition**: Detect glass breaking, dog barking, baby crying, or smoke/CO alarm sound patterns via edge microphones.
- [ ] **Local Natural Language Clip Search**: Query recordings using plain text (e.g., *"Show clips of a delivery truck yesterday"*) powered by local CLIP vector indexing.

---

## 10. Battery, Thermal Protection & Solar Duty Cycling
- [ ] **Overheat Throttling & Thermal Protection**: Monitor battery/CPU temperatures on phone nodes; automatically dim screen, lower frame rates, or pause heavy processing if thermal thresholds are exceeded.
- [ ] **Solar & Deep Sleep Duty Cycling**: Dynamic deep sleep mode for off-grid solar-powered nodes, waking in milliseconds via BLE/PIR triggers to conserve battery for days.

---

## 11. Mesh Relay & Multi-Hub High Availability
- [ ] **P2P Wireless Mesh Relay**: Edge nodes out of range act as intermediate wireless repeaters, hopping video streams back to the central Hub.
- [ ] **High Availability Multi-Hub Failover**: Secondary Linux PC, Raspberry Pi, or phone automatically promotes itself to active Hub if the primary Hub crashes or loses power.

---

## 12. Active Defense & Two-Way Intercom
- [ ] **Two-Way Walkie-Talkie Intercom**: Full-duplex live voice communication between the Web Dashboard and any Android phone node, Linux camera, or SIP doorbell.
- [ ] **Remote Siren & Strobe Deterrence**: Trigger loud alarm sirens and flashing light strobes on edge phone nodes to deter intruders.

---

## 13. Offline-First, Hybrid Networking & Multi-AP Mesh Roaming
- [ ] **100% Offline LAN Operation**: No internet, cellular SIM, or external cloud dependency required for live viewing or NVR recording.
- [ ] **Multi-AP Mesh & Cheap Wi-Fi Repeater Support**:
  - [ ] **Seamless AP Hopping & BSSID Re-binding**: Full support for multi-AP mesh systems (UniFi, Eero, Orbi, Asus AI-Mesh) and cheap Wi-Fi extenders/repeaters.
  - [ ] **Fast Roaming Protocols (802.11k/v/r)**: Leverages 802.11k/v/r fast transition protocols so moving mobile phone nodes switch between Wi-Fi APs and cheap repeaters without dropping video sockets or freezing.
- [ ] **Smartphone Wi-Fi Sharing Mesh Repeater Mode**:
  - [ ] **Mobile Wi-Fi Repeater Points**: Harnesses hardware Wi-Fi Sharing / Wi-Fi Repeater capability on smartphones (e.g. Samsung Galaxy S-series, Pixel) to transform phones into active wireless mesh extenders, widening coverage for distant camera nodes.
- [ ] **Linux AP Hotspot Mode**: Linux hub can host an offline Wi-Fi Access Point (`hostapd` / `nmcli`) so cameras can connect directly without a router.
- [ ] **Android Local-Only Hotspot Support**: Utilize Android's API 26+ local-only Wi-Fi socket to bypass carrier tethering/SIM restrictions.
- [ ] **Bluetooth Low Energy (BLE) Beaconing**:
  - [ ] Automatic device discovery & pairing signal without manual IP configuration.
  - [ ] Low-power failover heartbeat signaling when main Wi-Fi disconnects.
- [ ] **Store & Forward Offline Buffering**:
  - [ ] Nodes write 30-second video clips to local flash/SD storage if Wi-Fi connection drops.
  - [ ] Background checksum/rsync upload automatically catches up footage to the Hub upon reconnection.

---

## 14. App-First Architecture & Headless Appliance Local Web Management Portal
- [ ] **App-First Native Application Paradigm & Bi-Directional Sync**:
  - [ ] **Primary User Experience**: Native mobile (Android APK) and desktop applications serve as the primary ("App-First") interface for daily camera management, live viewing, instant push notifications, QR provisioning, and camera configuration.
  - [ ] **Seamless Web-to-App Handoff**: Once initial setup/provisioning is performed on the local Web Dashboard, full control, configuration updates, layout re-arrangements, storage allocation edits, and system updates become fully available directly within the native app for ultimate convenience and ease of use.
  - [ ] **Bi-Directional Real-Time Synchronization**: Any configuration edit, camera toggle, or system change made in the mobile/desktop app immediately syncs back to the headless web server engine in real-time.
- [ ] **Headless Appliance Web Management Portal**:
  - [ ] **Dedicated Headless Server Management**: Embedded local web server specifically built as an administration portal for headless 1U/2U server racks, mini PCs, Raspberry Pis, or screenless laptops.
  - [ ] **Direct Ethernet / Local LAN Administration**: Plug an Ethernet cable directly into a headless server or connect via local IP, open `http://<device-ip>:8080` in any browser, and immediately configure network bridges, storage arrays, camera feeds, and system health without installing client software on the admin computer.
  - [ ] **Conflict-Free Auto-Port Relocation Protocol**:
    - [ ] Web server automatically inspects local occupied ports on shared home networks (e.g., ports 80, 8080, 8443, 3000 used by Plex, Home Assistant, Pi-hole, local web servers).
    - [ ] If port collisions occur, the web daemon automatically relocates to open available ports (e.g. 8081, 8444) without interfering with existing home web services.
    - [ ] Broadcasts newly assigned ports across mDNS and native apps so client connections update seamlessly.
  - [ ] **Stable Immutable Service Identity (`nvr-hub-<uuid>.local`)**:
    - [ ] Every hub generates a persistent service UUID during setup (`nvr-hub-<uuid>.local`). Client apps and bookmarks track the immutable UUID identity, treating IP addresses and port numbers as dynamic attributes so port relocations never break bookmarks or client pairings.
  - [ ] **100% Zero-Cloud Local Hosting**: Embedded native web daemon runs on local device hardware with zero external domain hooks or cloud dependencies for 100% private operation.
- [ ] **Responsive Multi-Cam WebRTC Grid**: Dynamic 1x1, 2x2, 3x3, and custom grid views with sub-second ultra-low latency.
- [ ] **Scrubbable Event Timeline**: Interactive timeline showing motion event triggers, continuous recording, and offline sync markers.

---

## 15. Server Rack & Home Lab Integration
- [ ] **Docker & Podman Containerization**: One-command setup (`docker compose up -d`) for Hub, database, and Web UI.
- [ ] **Hardware Acceleration Passthrough**: Native support for Intel QuickSync, Nvidia NVENC, and V4L2 passthrough inside containers.
- [ ] **Flexible Storage Backends**: Support saving clips directly to local NVMe/HDD arrays or network shares (NFS / SMB / NAS).

---

## 16. Multi-Tier Passwords, Privacy Mode & Optional Supabase Auth (Lowest Priority)
> [!NOTE]
> **LOWEST PRIORITY / OPTIONAL COMMUNITY FEATURE**: Supabase backend integration (Google OAuth / cloud tables) is strictly optional and will be the **very last feature added**, ONLY if users explicitly ask for cloud login support. All core authentication (Master Password, Per-Camera Passwords, Guest Passwords, Family Roles) operates 100% locally and offline by default.

- [ ] **Multi-Tiered Local Camera Passwords**:
  - [ ] **Global Master Password**: Set one password to unlock/authenticate across all camera nodes.
  - [ ] **Per-Camera Passwords**: Custom password protection for individual camera nodes/servers.
- [ ] **Temporary Guest Access & Auto-Expiring Credentials**:
  - [ ] Generate temporary Guest User IDs & Passwords.
  - [ ] Auto-expiring time limits (e.g., clear access after 2 hours, 24 hours, or 5 views).
- [ ] **Family Roles & Granular Camera Access**:
  - [ ] Multi-user RBAC for family members with per-camera view/edit permissions.
- [ ] **Hardware Privacy Mode**:
  - [ ] One-tap Hardware Privacy toggle per camera.
  - [ ] Physically cuts power/stream to camera hardware modules (`v4l2-ctl` stream stop / camera sensor kill) so no video can be captured or leaked.
- [ ] **[OPTIONAL / LAST PRIORITY] Supabase Cloud Auth Integration**:
  - [ ] Relational schema for `users`, `devices`, `camera_passwords`, `guest_tokens`, and `family_permissions`.
  - [ ] **Emergency OAuth Remote Login**: Optional sign-in with Google / OAuth for emergency remote camera access (only built if requested by community).

---

## 17. Device Security & Tamper Lock Mode
- [ ] **Dedicated "Camera-Only" Kiosk Lock Mode**:
  - [ ] **Android Lock Task / Screen Pinning**: Hard-locks phone into Camera Mode. Prevents access to Android settings, home screen, or app switcher even if someone bypasses or unlocks the lock screen.
  - [ ] **Linux Edge Kiosk**: Locks Linux camera nodes into fullscreen camera-only mode with disabled system hotkeys (`Alt+Tab`, `Ctrl+Alt+Fx`).
  - [ ] **Admin PIN/Password Unlock**: Exiting Camera-Only Mode strictly requires entering an Admin PIN or security password.
  - [ ] **Tamper & Theft Protection**: Auto-dims screen while remaining active; alerts Hub instantly if phone/node is physically moved or disconnected.

---

## 18. Sustainable FOSS & Crowdfunding Model
- [ ] **100% Open Source Core**: Free from ads, forced cloud subscriptions, or tracking (AGPLv3 / MIT).
- [ ] **Crowdfunded Development**: Community supported via Patreon, GitHub Sponsors, or Ko-fi.
- [ ] **Patron Community Perks**: Voting on roadmap features, early access experimental builds, and pre-built turnkey ISOs.

---

## 19. Anti-App-Store & Independent Distribution Policy (F-Droid, GitHub & Patreon ONLY)
> [!IMPORTANT]
> **NON-NEGOTIABLE POLICY DIRECTIVE (NO CHECKBOX / FIXED DIRECTIVE)**:
> This app will **NEVER** be published to the **Google Play Store** or **Apple App Store**.

- **Rationale for Absolute App Store Ban**:
  - **Background Camera Restrictions**: Both Google Play and Apple App Store strictly ban or terminate apps capturing video or streaming cameras continuously in the background.
  - **Battery Bypass Bans**: Google Play flags and rejects apps using `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` for non-whitelisted categories.
  - **Permission Lockouts**: App stores block system overlays (`SYSTEM_ALERT_WINDOW`), custom USB host audio drivers, and persistent background services required for a reliable security NVR.
  - **Monetization & Censorship**: Avoid 30% store cuts, mandatory cloud dependencies, and store policy censorship.
- **Exclusive Official Distribution Channels**:
  - **F-Droid**: Official FOSS Android application repository.
  - **GitHub Releases**: Direct APK downloads, signed release assets, and source code tags.
  - **Patreon & Custom F-Droid Repo**: Direct APK downloads, custom F-Droid repository link, and early-access builds for project supporters.

---

## 20. Official Dedicated Web Portal & Custom Domain Brand
- [ ] **Full Custom Domain & Standalone Brand Website**:
  - [ ] Dedicated official web portal on its own custom domain (beyond just a basic GitHub repo README).
  - [ ] Sleek, high-production landing page showcasing project capabilities, live WebRTC demos, hardware compatibility matrix, and setup guides.
- [ ] **Integrated Online Resources & Web Services**:
  - [ ] **Interactive Preset QR Code Generator**: Web tool allowing users to generate setup QR codes online directly from the website.
  - [ ] **Hosted Web App Dashboard / PWA**: Option to launch or connect to Web Dashboard directly from the browser on the custom domain.
  - [ ] **Direct Downloads & Custom F-Droid Repo Host**: Host direct APK downloads, SHA-256 checksums, turnkey ISO images, and self-hosted F-Droid repository XML index.
  - [ ] **Hardware Compatibility & Setup Wiki**: Interactive guide covering phone battery wiring/bypasses, Linux server configs, PoE switches, USB devices, and home automation integrations.

---

## 21. Custom OS Distros, Appliance ISOs, Router Firmware & SBC Images
- [ ] **Turnkey Server Rack & Bare-Metal PC Appliance OS**:
  - [ ] **Dedicated Minimalist NVR Appliance ISO**: Custom Debian/Alpine-based lightweight OS ISO designed to turn bare-metal PCs or 1U/2U/4U rackmount servers into dedicated NVR appliances.
  - [ ] **Proxmox VE & Virtualization Templates**: Pre-configured Proxmox LXC container templates and QEMU/KVM VM images with GPU passthrough pre-enabled.
  - [ ] **Kernel Optimizations**: Real-time Linux kernel tweaks for high-throughput multi-stream USB V4L2 capture and NVENC/QuickSync hardware encoding.
- [ ] **[COMMUNITY-DRIVEN PHASE] Custom Router OS & Router Flashing Firmware (OpenWrt / DD-WRT / Tomato)**:
  - [ ] **Community OpenWrt Package & Firmware Builds**: Custom OpenWrt / DD-WRT `.bin` firmware builds developed as a community-maintained package phase, turning old Wi-Fi routers into **Dedicated System Network Router Nodes**.
  - [ ] **Router Hardware Qualification Filter**: Employs hardware profiling (§23) for router hardware:
    - *Basic Package*: Requires minimum 16 MB Flash / 64 MB RAM.
    - *Full Mesh Package*: Requires 128 MB+ Flash / 256 MB+ RAM for full WireGuard mesh, mDNS, and Smart Queue Management (QoS). Underpowered 4 MB flash legacy routers are automatically excluded.
  - [ ] **Dual-SSID Architecture (Main Visible + Hidden Camera Mesh)**:
    - [ ] **Public / Main SSID**: Flashed router hosts the standard visible Wi-Fi SSID for normal household internet devices.
    - [ ] **Hidden Security Camera Mesh SSID**: Concurrently hosts an isolated SSID dedicated for camera nodes and phones (providing UI separation/convenience; primary cryptographic security is strictly enforced by WPA3 / AES-256 and §24 E2EE).
    - [ ] **App & Local Web Panel Management**: Fully configurable via the native mobile/desktop app or the local Ethernet web panel.
  - [ ] **Intelligent Video Traffic QoS & Routing**: Router firmware automatically prioritizes real-time camera video streams over general home web traffic (Smart Queue Management / QoS).
  - [ ] **Embedded Router Mesh & Tunneling**: Runs embedded WireGuard mesh tunnels, mDNS auto-discovery, and local IP routing directly on qualified router hardware.
- [ ] **Single-Board Computer (SBC) Flashed Disk Images**:
  - [ ] Pre-built, bootable `.img.xz` disk images for Raspberry Pi 3/4/5, Orange Pi, Rockchip, and Radxa boards.
  - [ ] Plug-and-play boot into either **Node Mode** (camera capture) or **Hub Mode** (NVR server).
- [ ] **Dedicated Mobile Phone Appliance Firmware (AOSP / GSI / Magisk)**:
  - [ ] **Custom AOSP / LineageOS Builds & GSIs**: Bloatware-free Android system images optimized for old smartphones used as security cameras.
  - [ ] **Boot-on-Charge Enforcer**: Firmware patch that forces devices to automatically power ON and boot into Camera Mode the moment AC/USB power is connected (even with a missing or drained battery).
  - [ ] **Battery-Bypass & Battery Health Protection**: Kernel-level charge limiting (stopping charge at 50-60%) to prevent lithium battery swelling in 24/7 plugged-in phones.
- [ ] **Laptop Appliance & Dedicated Kiosk OS**:
  - [ ] Lightweight Kiosk ISO for old laptops, disabling desktop bloat and converting screen + keyboard into an instant NVR monitor and gateway.

---

## 22. Multi-WAN Concurrency & NAT Traversal Topology
- [ ] **Multi-WAN Concurrent Decentralized Topology**:
  - [ ] **Zero Bottleneck Concurrency**: EVERY device with active internet or cellular data runs its own independent WAN connection concurrently—there is NO single primary WAN node bottleneck.
  - [ ] **Localized Scope for Budget Devices**: Older/budget phones that cannot handle multi-stream LAN-to-WAN bridging stream strictly their OWN camera feed to WAN, preventing memory exhaustion or device locks.
  - [ ] **Adaptive LAN-to-WAN Protocol Translation**: High-capacity nodes (servers, PCs, laptops) bridge legacy local-only cameras (RTSP/ONVIF/V4L2) out to encrypted WAN feeds automatically.
- [ ] **Native Direct P2P Mesh vs. Fallback TURN Traversal Split**:
  - [ ] **Native Direct Path (Zero Relay, Zero Bottleneck)**: WireGuard / Tailscale-style encrypted P2P mesh + self-hosted rendezvous server. Direct socket-to-socket encrypted communication between client and camera node with zero third-party data relay.
  - [ ] **Fallback Path (Last Resort Only)**: WebRTC STUN for NAT hole-punching, and self-hosted TURN servers strictly as a last resort when direct P2P is blocked by restrictive symmetric NATs (clearly flagged in UI as a relayed connection with bandwidth quotas).

---

## 23. Zero-Telemetry Local Hardware Profiling & Load-Shedding Engine
- [ ] **100% Offline Static Hardware Database**:
  - [ ] **Local Static Capability Matrix**: Shipped as a static JSON database (`hardware_profiles.json`) bundled directly inside official signed software releases.
  - [ ] **Zero Runtime Telemetry / Zero Fingerprinting**: Devices detect their CPU cores, RAM, and network chipset **locally** via offline OS APIs. Absolutely ZERO hardware metrics, CPU strings, or device fingerprints are ever sent to remote servers (maintaining strict Section 19 FOSS privacy).
  - [ ] **Open-Source Community Contributions**: Updates to hardware capability profiles happen via GitHub Pull Requests to the open-source repository and are distributed in signed release updates.
- [ ] **Hardware-Aware Task Allocation & Adaptive Load Shedding**:
  - [ ] **Differentiated Workload Assignment**: High-spec nodes (Core i7 8th Gen with 5GHz Wi-Fi / Ethernet) take on heavy multi-stream proxying and AI object detection.
  - [ ] **Budget Hardware Protection**: Low-spec nodes (Intel Pentium laptops with 2.4 GHz Wi-Fi and no Bluetooth) handle single light streams to prevent CPU/RAM lockups, thermal throttling, or freezing.

---

## 24. Cryptographic Security Architecture & Complete Key Lifecycle
- [ ] **Hardware-Enforced Key Storage**:
  - [ ] **Android Keystore System**: Secure hardware-backed key generation and storage (`KeyGenParameterSpec` / StrongBox TPM enclave).
  - [ ] **Linux Hardware Security**: Integration with Linux TPM 2.0 / kernel keyring for encrypted key isolation.
- [ ] **Complete Cryptographic Key Lifecycle Management**:
  - [ ] **Automated Key Rotation**: Ephemeral session keys rotated automatically every 60 minutes or 10 GB of streamed video data.
  - [ ] **Instant Device Revocation**: Administrator signs a revocation vector broadcasted across the local mesh/BLE network; revoked devices are immediately blacklisted and their encrypted handshakes rejected.
  - [ ] **Perfect Forward Secrecy (PFS)**: Ephemeral ECDH key exchanges ensure past recorded clips cannot be decrypted even if a current device identity key is compromised.
  - [ ] **Emergency Account & Key Recovery**: Zero-cloud offline recovery via Shamir's Secret Sharing (SSS) key shards or a 24-word offline seed phrase (BIP-39) to regain cluster access without external servers.




