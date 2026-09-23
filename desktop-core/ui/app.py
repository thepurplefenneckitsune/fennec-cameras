# CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
#!/usr/bin/env python3
"""
CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
Fennec Cameras - Linux Desktop NVR Application (PySide6 / Qt6)

Native Linux Desktop App GUI with Start-Up Splash Screen,
Multi-Page Dashboard Navigation, Live Camera Grid Controls with Active Tile Selection,
Expanded Single-Camera Focus View with Dynamic Hardware Capabilities,
Keyboard Shortcuts & Visual Control Activation Glowing Feedback,
Cohesive Theme Engine with High-Contrast Natural Light Mode & Dark Mode,
Unmistakable Active Selection Indicators (Left Accent Bars, Neon Selection Borders & Focus Rings),
Per-Device Passcodes, Mobile Nodes, Tiered Storage, OpenWrt Mesh,
Local Edge AI Configuration, and System Health Diagnostics.

NOTE: All settings changes are held in TEMPORARY DEV IN-MEMORY STATE.
Refer to HOW_TO_REMOVE_TEMP_STATE.md to switch to persistent SQLite storage.
"""

import sys
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QFont, QPixmap, QColor, QKeyEvent
from PySide6.QtWidgets import (
    QApplication, QDialog, QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMessageBox, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSlider, QSpinBox, QSplitter,
    QStackedWidget, QTabBar, QCheckBox, QComboBox, QTextEdit, QVBoxLayout, QWidget
)


# Global Dev Temporary In-Memory State DB with Hardware Capabilities
DEV_TEMPORARY_DEVICE_DB = {
    "cam-01": {
        "id": "cam-01",
        "name": "Front Yard Camera",
        "type": "V4L2 USB Webcam",
        "ip": "Local (/dev/video0)",
        "passcode": "8921",
        "resolution": "1080p (1920x1080)",
        "fps": 30,
        "rtsp_url": "v4l2:///dev/video0",
        "privacy": False,
        "motion_sensitivity": 75,
        "rec_schedule": "24/7 Continuous",
        "capabilities": {
            "has_ptz": False,
            "has_zoom": False,
            "has_audio": True,
            "has_intercom": False
        }
    },
    "cam-02": {
        "id": "cam-02",
        "name": "Driveway Node",
        "type": "Android Phone S24",
        "ip": "192.168.1.105",
        "passcode": "4490",
        "resolution": "4K (3840x2160)",
        "fps": 24,
        "rtsp_url": "rtsp://192.168.1.105:8554/live",
        "privacy": False,
        "motion_sensitivity": 80,
        "rec_schedule": "Motion Only",
        "capabilities": {
            "has_ptz": True,
            "has_zoom": True,
            "has_audio": True,
            "has_intercom": True
        }
    },
    "cam-03": {
        "id": "cam-03",
        "name": "Garage Gate",
        "type": "ONVIF / RTSP IP",
        "ip": "192.168.1.120",
        "passcode": "7712",
        "resolution": "1080p (1920x1080)",
        "fps": 30,
        "rtsp_url": "rtsp://admin:7712@192.168.1.120:554/stream1",
        "privacy": False,
        "motion_sensitivity": 60,
        "rec_schedule": "24/7 Continuous",
        "capabilities": {
            "has_ptz": True,
            "has_zoom": True,
            "has_audio": False,
            "has_intercom": False
        }
    },
    "cam-04": {
        "id": "cam-04",
        "name": "Porch 360° View",
        "type": "Dual-Lens Panoramic",
        "ip": "192.168.1.135",
        "passcode": "1234",
        "resolution": "2K Panoramic",
        "fps": 30,
        "rtsp_url": "rtsp://192.168.1.135:8554/pano",
        "privacy": False,
        "motion_sensitivity": 85,
        "rec_schedule": "24/7 Continuous",
        "capabilities": {
            "has_ptz": False,
            "has_zoom": True,
            "has_audio": True,
            "has_intercom": True
        }
    },
    "cam-05": {
        "id": "cam-05",
        "name": "Backyard Node",
        "type": "Pixel 7 Pro Node",
        "ip": "192.168.1.112",
        "passcode": "9102",
        "resolution": "1080p (1920x1080)",
        "fps": 30,
        "rtsp_url": "rtsp://192.168.1.112:8554/live",
        "privacy": False,
        "motion_sensitivity": 70,
        "rec_schedule": "24/7 Continuous",
        "capabilities": {
            "has_ptz": True,
            "has_zoom": True,
            "has_audio": True,
            "has_intercom": True
        }
    },
    "cam-06": {
        "id": "cam-06",
        "name": "Hallway Backup",
        "type": "iPhone 11 Node",
        "ip": "192.168.1.140",
        "passcode": "3311",
        "resolution": "1080p (1920x1080)",
        "fps": 30,
        "rtsp_url": "rtsp://192.168.1.140:8554/live",
        "privacy": False,
        "motion_sensitivity": 80,
        "rec_schedule": "Motion Only",
        "capabilities": {
            "has_ptz": False,
            "has_zoom": True,
            "has_audio": True,
            "has_intercom": True
        }
    },
    "cam-07": {
        "id": "cam-07",
        "name": "Side Alley Cam",
        "type": "ONVIF / RTSP IP",
        "ip": "192.168.1.145",
        "passcode": "7743",
        "resolution": "1080p (1920x1080)",
        "fps": 30,
        "rtsp_url": "rtsp://admin:7743@192.168.1.145:554/stream1",
        "privacy": False,
        "motion_sensitivity": 65,
        "rec_schedule": "24/7 Continuous",
        "capabilities": {
            "has_ptz": True,
            "has_zoom": True,
            "has_audio": False,
            "has_intercom": False
        }
    },
    "cam-08": {
        "id": "cam-08",
        "name": "Attic Sensor Cam",
        "type": "V4L2 USB Webcam",
        "ip": "Local (/dev/video1)",
        "passcode": "8854",
        "resolution": "720p (1280x720)",
        "fps": 30,
        "rtsp_url": "v4l2:///dev/video1",
        "privacy": False,
        "motion_sensitivity": 50,
        "rec_schedule": "Motion Only",
        "capabilities": {
            "has_ptz": False,
            "has_zoom": False,
            "has_audio": True,
            "has_intercom": False
        }
    },
    "cam-09": {
        "id": "cam-09",
        "name": "Basement Perimeter",
        "type": "Dual-Lens Panoramic",
        "ip": "192.168.1.155",
        "passcode": "9965",
        "resolution": "2K Panoramic",
        "fps": 30,
        "rtsp_url": "rtsp://192.168.1.155:8554/pano",
        "privacy": False,
        "motion_sensitivity": 90,
        "rec_schedule": "24/7 Continuous",
        "capabilities": {
            "has_ptz": False,
            "has_zoom": True,
            "has_audio": True,
            "has_intercom": True
        }
    }
}


# ==========================================
# 1. SPLASH SCREEN
# ==========================================
class SplashScreen(QWidget):
    """Start-Up Splash Screen with Dark Kitsune Aesthetic."""
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.setFixedSize(620, 390)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.progress_val = 0
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #0d0714;
                border: 2px solid #8a2be2;
                border-radius: 20px;
            }
        """)
        
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(30, 40, 30, 30)
        card_layout.setSpacing(14)

        title = QLabel("🦊 Fennec Cameras")
        title.setFont(QFont("sans-serif", 26, QFont.Bold))
        title.setStyleSheet("color: #ffffff; border: none; background: transparent;")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)

        subtitle = QLabel("Linux-First Offline Security Camera Hub")
        subtitle.setFont(QFont("sans-serif", 11, QFont.Medium))
        subtitle.setStyleSheet("color: #ff007f; letter-spacing: 2px; border: none; background: transparent;")
        subtitle.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitle)

        card_layout.addSpacing(10)

        self.status_label = QLabel("Initializing hardware video acceleration...")
        self.status_label.setFont(QFont("sans-serif", 10))
        self.status_label.setStyleSheet("color: #9ba1a6; border: none; background: transparent;")
        self.status_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.status_label)

        self.progress = QProgressBar()
        self.progress.setFixedHeight(8)
        self.progress.setTextVisible(False)
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #1a102a;
                border: 1px solid #371d5a;
                border-radius: 4px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff007f, stop:1 #8a2be2);
                border-radius: 4px;
            }
        """)
        card_layout.addWidget(self.progress)

        disclaimer = QLabel("UNTESTED ROADMAP CONCEPT PROTOTYPE")
        disclaimer.setFont(QFont("sans-serif", 8, QFont.Bold))
        disclaimer.setStyleSheet("color: #d4aaff; border: none; background: transparent;")
        disclaimer.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(disclaimer)

        layout.addWidget(card)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(25)

    def update_progress(self):
        self.progress_val += 2
        self.progress.setValue(self.progress_val)
        
        if self.progress_val == 20:
            self.status_label.setText("Loading V4L2 USB camera drivers...")
        elif self.progress_val == 45:
            self.status_label.setText("Verifying 16GB auto-denial flash protection rules...")
        elif self.progress_val == 70:
            self.status_label.setText("Binding local HTTP API to port 8081...")
        elif self.progress_val == 90:
            self.status_label.setText("Initializing visual selection indicators...")
        elif self.progress_val >= 100:
            self.timer.stop()
            self.finished.emit()


# ==========================================
# 2. PER-DEVICE SETTINGS & PASSCODE DIALOG
# ==========================================
class PerDeviceSettingsDialog(QDialog):
    """Modal Dialog for Editing Specific Device Settings & Security Passcode."""

    def __init__(self, cam_id, parent=None, is_dark_mode=True):
        super().__init__(parent)
        self.cam_id = cam_id
        self.config = DEV_TEMPORARY_DEVICE_DB[cam_id]
        self.is_dark_mode = is_dark_mode
        
        self.setWindowTitle(f"Device Settings && Security — {self.config['name']}")
        self.setMinimumSize(580, 620)
        self.resize(600, 650)
        self.apply_dialog_theme()
        self.init_ui()

    def apply_dialog_theme(self):
        if self.is_dark_mode:
            self.setStyleSheet("""
                QDialog { background-color: #0d0714; color: #ffffff; }
                QLabel { color: #d4aaff; font-size: 12px; font-weight: 500; min-height: 24px; background: transparent; }
                QLineEdit, QComboBox, QSpinBox {
                    background-color: #1a102a; border: 1px solid #371d5a; color: #ffffff;
                    padding: 6px 10px; border-radius: 6px; min-height: 32px; font-size: 12px;
                }
                QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
                    border: 2px solid #ff007f;
                }
                QPushButton {
                    background: linear-gradient(45deg, #ff007f, #8a2be2); color: #ffffff;
                    border: none; padding: 8px 18px; border-radius: 8px; font-weight: bold; min-height: 32px;
                }
                QPushButton:focus { border: 2px solid #ffffff; }
                QCheckBox { color: #ffffff; font-size: 12px; min-height: 24px; background: transparent; }
            """)
        else:
            self.setStyleSheet("""
                QDialog { background-color: #f8fafc; color: #0f172a; }
                QLabel { color: #334155; font-size: 12px; font-weight: 600; min-height: 24px; background: transparent; }
                QLineEdit, QComboBox, QSpinBox {
                    background-color: #ffffff; border: 1px solid #cbd5e1; color: #0f172a;
                    padding: 6px 10px; border-radius: 6px; min-height: 32px; font-size: 12px;
                }
                QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
                    border: 2px solid #7c3aed;
                }
                QPushButton {
                    background: #7c3aed; color: #ffffff;
                    border: none; padding: 8px 18px; border-radius: 8px; font-weight: bold; min-height: 32px;
                }
                QPushButton:focus { border: 2px solid #0f172a; }
                QCheckBox { color: #0f172a; font-size: 12px; min-height: 24px; background: transparent; }
            """)

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        head = QHBoxLayout()
        icon = QLabel("⚙️")
        icon.setFont(QFont("sans-serif", 22))
        
        t_box = QVBoxLayout()
        title = QLabel(f"Per-Device Configuration ({self.cam_id})")
        title.setFont(QFont("sans-serif", 15, QFont.Bold))
        title.setStyleSheet("min-height: 26px; background: transparent;")
        
        t_box.addWidget(title)
        head.addWidget(icon)
        head.addLayout(t_box)
        head.addStretch()
        layout.addLayout(head)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        form_frame = QFrame()
        bg_card = "#08040d" if self.is_dark_mode else "#ffffff"
        bd_card = "#201235" if self.is_dark_mode else "#cbd5e1"
        form_frame.setStyleSheet(f"background-color: {bg_card}; border: 1px solid {bd_card}; border-radius: 12px; padding: 16px;")
        
        f_grid = QGridLayout(form_frame)
        f_grid.setVerticalSpacing(14)
        f_grid.setHorizontalSpacing(16)
        f_grid.setColumnMinimumWidth(0, 170)

        # 1. Device Name
        lbl_name = QLabel("Device Name:")
        f_grid.addWidget(lbl_name, 0, 0, Qt.AlignVCenter)
        self.edit_name = QLineEdit(self.config["name"])
        f_grid.addWidget(self.edit_name, 0, 1)

        # 2. Node Security Passcode / Token
        lbl_pass = QLabel("Node Passcode (PIN):")
        f_grid.addWidget(lbl_pass, 1, 0, Qt.AlignVCenter)
        self.edit_passcode = QLineEdit(self.config["passcode"])
        self.edit_passcode.setEchoMode(QLineEdit.Password)
        f_grid.addWidget(self.edit_passcode, 1, 1)

        self.chk_show_pass = QCheckBox("Show Passcode")
        self.chk_show_pass.setStyleSheet("color: #475569; font-size: 11px; background: transparent;" if not self.is_dark_mode else "color: #9ba1a6; font-size: 11px; background: transparent;")
        self.chk_show_pass.toggled.connect(
            lambda checked: self.edit_passcode.setEchoMode(QLineEdit.Normal if checked else QLineEdit.Password)
        )
        f_grid.addWidget(self.chk_show_pass, 2, 1)

        # 3. RTSP / Stream URL
        lbl_rtsp = QLabel("Stream RTSP Endpoint:")
        f_grid.addWidget(lbl_rtsp, 3, 0, Qt.AlignVCenter)
        self.edit_rtsp = QLineEdit(self.config["rtsp_url"])
        f_grid.addWidget(self.edit_rtsp, 3, 1)

        # 4. Stream Resolution
        lbl_res = QLabel("Resolution Profile:")
        f_grid.addWidget(lbl_res, 4, 0, Qt.AlignVCenter)
        self.cmb_res = QComboBox()
        self.cmb_res.addItems(["720p (1280x720)", "1080p (1920x1080)", "2K (2560x1440)", "4K (3840x2160)"])
        self.cmb_res.setCurrentText(self.config["resolution"])
        f_grid.addWidget(self.cmb_res, 4, 1)

        # 5. Target FPS
        lbl_fps = QLabel("Target Frame Rate (FPS):")
        f_grid.addWidget(lbl_fps, 5, 0, Qt.AlignVCenter)
        self.spn_fps = QSpinBox()
        self.spn_fps.setRange(5, 60)
        self.spn_fps.setValue(self.config["fps"])
        f_grid.addWidget(self.spn_fps, 5, 1)

        # 6. Motion Sensitivity
        lbl_mot = QLabel("Motion Sensitivity (%):")
        f_grid.addWidget(lbl_mot, 6, 0, Qt.AlignVCenter)
        self.sld_motion = QSlider(Qt.Horizontal)
        self.sld_motion.setRange(0, 100)
        self.sld_motion.setValue(self.config["motion_sensitivity"])
        f_grid.addWidget(self.sld_motion, 6, 1)

        # 7. Privacy Mode per device
        lbl_priv = QLabel("Per-Device Privacy Mode:")
        f_grid.addWidget(lbl_priv, 7, 0, Qt.AlignVCenter)
        self.chk_priv = QCheckBox("Disable Feed && Recording")
        self.chk_priv.setChecked(self.config["privacy"])
        f_grid.addWidget(self.chk_priv, 7, 1)

        scroll.setWidget(form_frame)
        layout.addWidget(scroll, 1)

        # Footer Buttons
        btn_box = QHBoxLayout()
        btn_cancel = QPushButton("Cancel")
        btn_cancel_style = "background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 6px 16px; border-radius: 8px;" if self.is_dark_mode else "background: #e2e8f0; color: #0f172a; border: 1px solid #cbd5e1; padding: 6px 16px; border-radius: 8px;"
        btn_cancel.setStyleSheet(btn_cancel_style)
        btn_cancel.clicked.connect(self.reject)

        btn_save = QPushButton("💾 Save Device Settings")
        btn_save.setCursor(Qt.PointingHandCursor)
        btn_save.clicked.connect(self.save_settings)

        btn_box.addWidget(btn_cancel)
        btn_box.addStretch()
        btn_box.addWidget(btn_save)
        layout.addLayout(btn_box)

    def save_settings(self):
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["name"] = self.edit_name.text()
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["passcode"] = self.edit_passcode.text()
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["rtsp_url"] = self.edit_rtsp.text()
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["resolution"] = self.cmb_res.currentText()
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["fps"] = self.spn_fps.value()
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["motion_sensitivity"] = self.sld_motion.value()
        DEV_TEMPORARY_DEVICE_DB[self.cam_id]["privacy"] = self.chk_priv.isChecked()

        self.accept()


# ==========================================
# 3. EXPANDED SINGLE-CAMERA FOCUS VIEW PAGE
# ==========================================
class ExpandedCameraViewPage(QWidget):
    """Full Expanded Single-Camera Focus View with Dynamic Hardware Capabilities & Keyboard Controls."""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.cam_id = "cam-01"
        self.config = DEV_TEMPORARY_DEVICE_DB[self.cam_id]
        self.is_playing = True
        self.is_muted = False
        
        self.setFocusPolicy(Qt.StrongFocus)
        self.init_ui()

    def set_camera(self, cam_id):
        self.cam_id = cam_id
        self.config = DEV_TEMPORARY_DEVICE_DB[cam_id]
        self.lbl_title.setText(f"🔍 Focus View: {self.config['name']} ({self.cam_id})")
        self.lbl_badge.setText(self.config["type"])
        self.lbl_canvas_text.setText(f"[ Live Stream • {self.config['resolution']} • {self.config['fps']}FPS ]\n{self.config['rtsp_url']}")
        
        caps = self.config.get("capabilities", {})
        has_ptz = caps.get("has_ptz", False)
        has_zoom = caps.get("has_zoom", False)
        has_intercom = caps.get("has_intercom", False)

        self.ptz_frame.setEnabled(has_ptz)
        if has_ptz:
            self.lbl_ptz_status.setText("🕹️ PTZ Pan-Tilt Controls")
            self.lbl_ptz_status.setStyleSheet("color: #d4aaff;" if self.main_window.is_dark_mode else "color: #7c3aed;")
        else:
            self.lbl_ptz_status.setText("🔒 Fixed Lens — No PTZ Support")
            self.lbl_ptz_status.setStyleSheet("color: #6b7280;")

        self.btn_z_in.setEnabled(has_zoom)
        self.btn_z_out.setEnabled(has_zoom)

        self.btn_talk.setEnabled(has_intercom)
        if has_intercom:
            self.btn_talk.setText("🎙️ HOLD TO TALK (Intercom)")
            self.btn_talk.setStyleSheet("background: linear-gradient(45deg, #ff007f, #8a2be2); color: #ffffff; border: none; padding: 8px; border-radius: 8px; font-weight: bold; min-height: 32px;")
        else:
            self.btn_talk.setText("🚫 Intercom Unavailable")
            self.btn_talk.setStyleSheet("background: #1a102a; color: #6b7280; border: 1px solid #371d5a; padding: 8px; border-radius: 8px; min-height: 32px;")

        self.setFocus()

    def highlight_button_glow(self, btn, original_style):
        glow_style = original_style + " background: #ff007f !important; color: #ffffff !important; border: 2px solid #ffffff !important;"
        btn.setStyleSheet(glow_style)
        QTimer.singleShot(350, lambda: btn.setStyleSheet(original_style))

    def keyPressEvent(self, event: QKeyEvent):
        caps = self.config.get("capabilities", {})
        key = event.key()

        if key == Qt.Key_Escape:
            self.main_window.switch_page(0)
        elif key == Qt.Key_Space:
            self.highlight_button_glow(self.btn_play_pause, self.btn_play_pause.styleSheet())
            self.toggle_play_pause()
        elif key == Qt.Key_M:
            self.highlight_button_glow(self.btn_mute, self.btn_mute.styleSheet())
            self.toggle_mute()
        elif key == Qt.Key_P:
            self.config["privacy"] = not self.config["privacy"]
            self.set_camera(self.cam_id)
            self.trigger_ptz_action("Privacy Toggle [P]", btn=None)
        elif caps.get("has_ptz", False):
            if key == Qt.Key_Up:
                self.trigger_ptz_action("Tilt Up (▲)", btn=self.btn_up)
            elif key == Qt.Key_Down:
                self.trigger_ptz_action("Tilt Down (▼)", btn=self.btn_down)
            elif key == Qt.Key_Left:
                self.trigger_ptz_action("Pan Left (◀)", btn=self.btn_left)
            elif key == Qt.Key_Right:
                self.trigger_ptz_action("Pan Right (▶)", btn=self.btn_right)
        elif caps.get("has_zoom", False):
            if key in (Qt.Key_Plus, Qt.Key_Equal):
                self.trigger_ptz_action("Zoom In (+)", btn=self.btn_z_in)
            elif key == Qt.Key_Minus:
                self.trigger_ptz_action("Zoom Out (-)", btn=self.btn_z_out)
        else:
            super().keyPressEvent(event)

    def trigger_ptz_action(self, action_name, btn=None):
        if btn and hasattr(self, 'ptz_btn_style'):
            self.highlight_button_glow(btn, getattr(btn, '_orig_style', self.ptz_btn_style))

        self.hud_active_tag.setText(f"⚡ CONTROL ACTIVE: [{action_name}]")
        self.hud_active_tag.setStyleSheet("color: #ffffff; background: #ff007f; padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 10px;")
        
        self.lbl_canvas_text.setText(f"[ Action Triggered: {action_name} ]\n{self.config['rtsp_url']}")
        
        QTimer.singleShot(1600, lambda: (
            self.hud_active_tag.setText("⚡ Control Ready (Arrows / +/- / Space)"),
            self.hud_active_tag.setStyleSheet("color: #d4aaff; background: rgba(0,0,0,0.6); padding: 4px 10px; border-radius: 6px; font-size: 9px;"),
            self.lbl_canvas_text.setText(f"[ Live Stream • {self.config['resolution']} • {self.config['fps']}FPS ]\n{self.config['rtsp_url']}")
        ))

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # 1. Header Toolbar
        top_bar = QHBoxLayout()
        btn_back = QPushButton("⬅️ Back to Camera Grid [Esc]")
        btn_back.setCursor(Qt.PointingHandCursor)
        btn_back.setStyleSheet("background: #1a102a; color: #d4aaff; border: 1px solid #371d5a; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 11px; min-height: 28px;")
        btn_back.clicked.connect(lambda: self.main_window.switch_page(0))

        self.lbl_title = QLabel(f"🔍 Focus View: {self.config['name']} ({self.cam_id})")
        self.lbl_title.setFont(QFont("sans-serif", 13, QFont.Bold))
        self.lbl_title.setStyleSheet("min-height: 24px; background: transparent;")

        self.lbl_badge = QLabel(self.config["type"])
        self.lbl_badge.setFont(QFont("sans-serif", 8, QFont.Bold))
        self.lbl_badge.setStyleSheet("color: #34d399; background: #064e3b; padding: 2px 8px; border-radius: 4px;")

        btn_popout_exp = QPushButton("🗗 Pop Out Window")
        btn_popout_exp.setCursor(Qt.PointingHandCursor)
        btn_popout_exp.setStyleSheet("background: #3b0764; color: #ff007f; border: 1px solid #831843; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 11px; min-height: 28px;")
        btn_popout_exp.clicked.connect(lambda: self.main_window.open_popout_window(self.cam_id))

        btn_dev_settings = QPushButton("⚙️ Per-Device Settings")
        btn_dev_settings.setCursor(Qt.PointingHandCursor)
        btn_dev_settings.setStyleSheet("background: #2b1128; color: #f472b6; border: 1px solid #831843; padding: 6px 14px; border-radius: 8px; font-weight: bold; font-size: 11px; min-height: 28px;")
        btn_dev_settings.clicked.connect(self.open_current_settings)

        top_bar.addWidget(btn_back)
        top_bar.addSpacing(12)
        top_bar.addWidget(self.lbl_title)
        top_bar.addWidget(self.lbl_badge)
        top_bar.addStretch()
        top_bar.addWidget(btn_popout_exp)
        top_bar.addWidget(btn_dev_settings)
        layout.addLayout(top_bar)

        # 2. Main Center Body
        center_split = QHBoxLayout()
        center_split.setSpacing(12)

        # Viewfinder Container
        self.vf_frame = QFrame()
        self.vf_frame.setObjectName("viewfinderFrame")
        self.vf_frame.setStyleSheet("QFrame#viewfinderFrame { background-color: #030105; border: 2px solid #201235; border-radius: 14px; }")
        vf_layout = QVBoxLayout(self.vf_frame)
        vf_layout.setContentsMargins(16, 16, 16, 16)

        hud_top = QHBoxLayout()
        hud_rec = QLabel("🔴 LIVE REC • H.265")
        hud_rec.setStyleSheet("color: #ef4444; background: rgba(0,0,0,0.6); padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 10px;")
        hud_ai = QLabel("⚡ YOLOv8: Person Detected (94%)")
        hud_ai.setStyleSheet("color: #34d399; background: rgba(0,0,0,0.6); padding: 4px 10px; border-radius: 6px; font-weight: bold; font-size: 10px;")
        
        self.hud_active_tag = QLabel("⚡ Control Ready (Arrows / +/- / Space)")
        self.hud_active_tag.setStyleSheet("color: #d4aaff; background: rgba(0,0,0,0.6); padding: 4px 10px; border-radius: 6px; font-size: 9px;")
        
        hud_top.addWidget(hud_rec)
        hud_top.addWidget(hud_ai)
        hud_top.addStretch()
        hud_top.addWidget(self.hud_active_tag)
        vf_layout.addLayout(hud_top)

        vf_layout.addStretch()
        self.canvas_icon = QLabel("📹")
        self.canvas_icon.setFont(QFont("sans-serif", 48))
        self.canvas_icon.setAlignment(Qt.AlignCenter)
        self.canvas_icon.setStyleSheet("background: transparent; color: #ffffff;")
        
        self.lbl_canvas_text = QLabel(f"[ Live Stream • {self.config['resolution']} • {self.config['fps']}FPS ]\n{self.config['rtsp_url']}")
        self.lbl_canvas_text.setFont(QFont("sans-serif", 10))
        self.lbl_canvas_text.setStyleSheet("color: #9ba1a6; background: transparent;")
        self.lbl_canvas_text.setAlignment(Qt.AlignCenter)

        vf_layout.addWidget(self.canvas_icon)
        vf_layout.addWidget(self.lbl_canvas_text)
        vf_layout.addStretch()

        center_split.addWidget(self.vf_frame, 3)

        # Right Control Drawer
        ctrl_panel = QFrame()
        ctrl_panel.setObjectName("ctrlPanel")
        ctrl_panel.setFixedWidth(280)
        ctrl_panel.setStyleSheet("QFrame#ctrlPanel { border-radius: 14px; padding: 12px; }")
        cp_layout = QVBoxLayout(ctrl_panel)
        cp_layout.setSpacing(12)

        self.lbl_ptz_status = QLabel("🕹️ PTZ Pan-Tilt Controls")
        self.lbl_ptz_status.setFont(QFont("sans-serif", 11, QFont.Bold))
        self.lbl_ptz_status.setStyleSheet("background: transparent;")
        cp_layout.addWidget(self.lbl_ptz_status)

        self.ptz_frame = QFrame()
        self.ptz_frame.setStyleSheet("background: transparent; border: none;")
        ptz_grid = QGridLayout(self.ptz_frame)
        ptz_grid.setContentsMargins(0, 0, 0, 0)
        ptz_grid.setSpacing(6)

        self.btn_up = QPushButton("▲")
        self.btn_down = QPushButton("▼")
        self.btn_left = QPushButton("◀")
        self.btn_right = QPushButton("▶")
        self.btn_home = QPushButton("🏠")
        
        self.ptz_btn_style = "background: #1a102a; color: #ffffff; border: 1px solid #371d5a; border-radius: 6px; font-weight: bold; min-height: 32px; font-size: 13px;"
        self.btn_up.setStyleSheet(self.ptz_btn_style)
        self.btn_down.setStyleSheet(self.ptz_btn_style)
        self.btn_left.setStyleSheet(self.ptz_btn_style)
        self.btn_right.setStyleSheet(self.ptz_btn_style)
        self.btn_home.setStyleSheet("background: #8a2be2; color: #ffffff; border: none; border-radius: 6px; font-weight: bold; min-height: 32px;")

        self.btn_up.clicked.connect(lambda: self.trigger_ptz_action("Tilt Up (▲)", self.btn_up))
        self.btn_down.clicked.connect(lambda: self.trigger_ptz_action("Tilt Down (▼)", self.btn_down))
        self.btn_left.clicked.connect(lambda: self.trigger_ptz_action("Pan Left (◀)", self.btn_left))
        self.btn_right.clicked.connect(lambda: self.trigger_ptz_action("Pan Right (▶)", self.btn_right))
        self.btn_home.clicked.connect(lambda: self.trigger_ptz_action("Return to Home Position", self.btn_home))

        ptz_grid.addWidget(self.btn_up, 0, 1)
        ptz_grid.addWidget(self.btn_left, 1, 0)
        ptz_grid.addWidget(self.btn_home, 1, 1)
        ptz_grid.addWidget(self.btn_right, 1, 2)
        ptz_grid.addWidget(self.btn_down, 2, 1)
        cp_layout.addWidget(self.ptz_frame)

        zoom_box = QHBoxLayout()
        self.btn_z_in = QPushButton("🔍 Zoom +")
        self.btn_z_out = QPushButton("🔍 Zoom -")
        self.zoom_btn_style = "background: #1e1233; color: #d4aaff; border: 1px solid #371d5a; border-radius: 6px; padding: 6px; min-height: 28px;"
        self.btn_z_in.setStyleSheet(self.zoom_btn_style)
        self.btn_z_out.setStyleSheet(self.zoom_btn_style)
        self.btn_z_in.clicked.connect(lambda: self.trigger_ptz_action("Zoom In (+)", self.btn_z_in))
        self.btn_z_out.clicked.connect(lambda: self.trigger_ptz_action("Zoom Out (-)", self.btn_z_out))
        
        zoom_box.addWidget(self.btn_z_in)
        zoom_box.addWidget(self.btn_z_out)
        cp_layout.addLayout(zoom_box)

        lbl_pre = QLabel("Presets:")
        lbl_pre.setStyleSheet("font-size: 10px; font-weight: bold; background: transparent;")
        cp_layout.addWidget(lbl_pre)
        
        pre_box = QHBoxLayout()
        for p_num in ["Preset 1", "Preset 2", "Preset 3"]:
            b_pre = QPushButton(p_num)
            b_pre.setStyleSheet("background: #160f24; color: #34d399; border: 1px solid #064e3b; border-radius: 4px; font-size: 9px; min-height: 24px;")
            b_pre.clicked.connect(lambda _, name=p_num, btn_target=b_pre: self.trigger_ptz_action(f"Go to {name}", btn_target))
            pre_box.addWidget(b_pre)
        cp_layout.addLayout(pre_box)

        cp_layout.addSpacing(6)

        lbl_audio = QLabel("🎙️ Audio & Intercom")
        lbl_audio.setFont(QFont("sans-serif", 10, QFont.Bold))
        lbl_audio.setStyleSheet("background: transparent;")
        cp_layout.addWidget(lbl_audio)

        self.btn_talk = QPushButton("🎙️ HOLD TO TALK (Intercom)")
        self.btn_talk.setCursor(Qt.PointingHandCursor)
        cp_layout.addWidget(self.btn_talk)

        self.btn_mute = QPushButton("🔊 Speaker Active [M]")
        self.btn_mute.setCursor(Qt.PointingHandCursor)
        self.btn_mute.setStyleSheet("background: #1a102a; color: #34d399; border: 1px solid #371d5a; border-radius: 6px; padding: 4px; font-size: 10px; min-height: 26px;")
        self.btn_mute.clicked.connect(self.toggle_mute)
        cp_layout.addWidget(self.btn_mute)

        cp_layout.addStretch()
        center_split.addWidget(ctrl_panel)
        layout.addLayout(center_split, 1)

        # 3. Bottom Playback Scrubbing Timeline Bar
        scrub_card = QFrame()
        scrub_card.setObjectName("scrubCard")
        scrub_card.setStyleSheet("QFrame#scrubCard { border-radius: 12px; padding: 10px 14px; }")
        sc_layout = QVBoxLayout(scrub_card)
        sc_layout.setSpacing(6)

        sc_head = QHBoxLayout()
        sc_title = QLabel("🎞️ Local NVMe 15-Minute Rolling Ring Buffer")
        sc_title.setFont(QFont("sans-serif", 10, QFont.Bold))
        sc_title.setStyleSheet("background: transparent;")
        
        self.sc_pos = QLabel("LIVE STREAM (00:00)")
        self.sc_pos.setStyleSheet("color: #ef4444; font-weight: bold; font-size: 10px; background: transparent;")
        
        sc_head.addWidget(sc_title)
        sc_head.addStretch()
        sc_head.addWidget(self.sc_pos)
        sc_layout.addLayout(sc_head)

        self.scrub_slider = QSlider(Qt.Horizontal)
        self.scrub_slider.setMinimum(-900)
        self.scrub_slider.setMaximum(0)
        self.scrub_slider.setValue(0)
        self.scrub_slider.valueChanged.connect(self.update_scrub_label)
        sc_layout.addWidget(self.scrub_slider)

        sc_ctrl = QHBoxLayout()
        btn_rew = QPushButton("⏪ -10s")
        self.btn_play_pause = QPushButton("⏸ Pause [Space]")
        btn_ff = QPushButton("⏩ LIVE")

        s_btn_style = "background: #1a102a; color: #d4aaff; border: 1px solid #371d5a; padding: 4px 10px; border-radius: 4px; font-size: 10px; min-height: 24px;"
        btn_rew.setStyleSheet(s_btn_style)
        self.btn_play_pause.setStyleSheet(s_btn_style)
        self.btn_play_pause.clicked.connect(self.toggle_play_pause)
        
        btn_ff.setStyleSheet("background: #3b0764; color: #ff007f; border: 1px solid #831843; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 10px; min-height: 24px;")
        btn_ff.clicked.connect(lambda: self.scrub_slider.setValue(0))

        sc_ctrl.addWidget(btn_rew)
        sc_ctrl.addWidget(self.btn_play_pause)
        sc_ctrl.addWidget(btn_ff)
        sc_ctrl.addStretch()

        ev_tag = QLabel("AI Event Markers: 📍 11:42 AM (Person)  |  📍 11:38 AM (Vehicle)")
        ev_tag.setStyleSheet("color: #34d399; font-size: 10px; background: transparent;")
        sc_ctrl.addWidget(ev_tag)
        sc_layout.addLayout(sc_ctrl)

        layout.addWidget(scrub_card)

    def toggle_mute(self):
        self.is_muted = not self.is_muted
        if self.is_muted:
            self.btn_mute.setText("🔇 Speaker Muted [M]")
            self.btn_mute.setStyleSheet("background: #2b1128; color: #f472b6; border: 1px solid #831843; border-radius: 6px; padding: 4px; font-size: 10px; min-height: 26px;")
        else:
            self.btn_mute.setText("🔊 Speaker Active [M]")
            self.btn_mute.setStyleSheet("background: #1a102a; color: #34d399; border: 1px solid #371d5a; border-radius: 6px; padding: 4px; font-size: 10px; min-height: 26px;")

    def toggle_play_pause(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.btn_play_pause.setText("⏸ Pause [Space]")
        else:
            self.btn_play_pause.setText("▶ Play [Space]")

    def update_scrub_label(self, val):
        if val == 0:
            self.sc_pos.setText("LIVE STREAM (00:00)")
            self.sc_pos.setStyleSheet("color: #ef4444; font-weight: bold; font-size: 10px; background: transparent;")
        else:
            mins = abs(val) // 60
            secs = abs(val) % 60
            self.sc_pos.setText(f"REWIND PLAYBACK: -{mins:02d}:{secs:02d}")
            self.sc_pos.setStyleSheet("color: #f59e0b; font-weight: bold; font-size: 10px; background: transparent;")

    def open_current_settings(self):
        dlg = PerDeviceSettingsDialog(self.cam_id, self, is_dark_mode=self.main_window.is_dark_mode)
        if dlg.exec():
            self.set_camera(self.cam_id)


# ==========================================
# 3.5 POP-OUT CAMERA GROUP WINDOW (MULTI-MONITOR)
# ==========================================
class PopoutCameraGroupWindow(QMainWindow):
    """
    Independent Detachable Window for Multi-Monitor Security Stations.
    Supports Camera Grouping (Chrome-style tabbed or sub-grid split views).
    """

    def __init__(self, group_name="Monitor 2 Pop-Out Group", main_window=None):
        super().__init__()
        self.main_window = main_window
        self.group_name = group_name
        self.cam_ids = []
        self.view_mode = "grid"
        self.is_fullscreen = False

        self.setWindowTitle(f"🦊 Fennec Cameras — Pop-Out Workspace: {self.group_name}")
        self.resize(920, 620)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        tb = QHBoxLayout()
        self.lbl_title = QLabel(f"🗗 Group: {self.group_name}")
        self.lbl_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        
        self.btn_mode_grid = QPushButton("🗂️ Sub-Grid View")
        self.btn_mode_grid.setCursor(Qt.PointingHandCursor)
        self.btn_mode_grid.clicked.connect(lambda: self.set_view_mode("grid"))

        self.btn_mode_tabs = QPushButton("📑 Tabbed View")
        self.btn_mode_tabs.setCursor(Qt.PointingHandCursor)
        self.btn_mode_tabs.clicked.connect(lambda: self.set_view_mode("tabbed"))

        self.cmb_add_cam = QComboBox()
        self.cmb_add_cam.addItem("➕ Add Camera to Group...")
        for cid, cfg in DEV_TEMPORARY_DEVICE_DB.items():
            self.cmb_add_cam.addItem(f"{cfg['name']} ({cid})", cid)
        self.cmb_add_cam.currentIndexChanged.connect(self.on_add_cam_selected)

        self.btn_fullscreen = QPushButton("📺 Fullscreen [F11]")
        self.btn_fullscreen.setCursor(Qt.PointingHandCursor)
        self.btn_fullscreen.clicked.connect(self.toggle_fullscreen)

        self.btn_merge = QPushButton("🔗 Merge Window")
        self.btn_merge.setToolTip("Hover window over another pop-out or click to merge groups")
        self.btn_merge.setCursor(Qt.PointingHandCursor)
        self.btn_merge.clicked.connect(self.prompt_merge_window)

        btn_dock = QPushButton("📥 Dock Back")
        btn_dock.setCursor(Qt.PointingHandCursor)
        btn_dock.clicked.connect(self.close)

        tb.addWidget(self.lbl_title)
        tb.addSpacing(10)
        tb.addWidget(self.btn_mode_grid)
        tb.addWidget(self.btn_mode_tabs)
        tb.addSpacing(15)
        tb.addWidget(self.cmb_add_cam)
        tb.addStretch()
        tb.addWidget(self.btn_merge)
        tb.addWidget(self.btn_fullscreen)
        tb.addWidget(btn_dock)

        main_layout.addLayout(tb)

        self.container_frame = QFrame()
        self.container_frame.setObjectName("popoutContainer")
        self.container_layout = QVBoxLayout(self.container_frame)
        self.container_layout.setContentsMargins(8, 8, 8, 8)

        self.grid_widget = QWidget()
        self.sub_grid_layout = QGridLayout(self.grid_widget)
        self.sub_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.sub_grid_layout.setSpacing(8)

        self.tab_widget = QWidget()
        tab_layout = QVBoxLayout(self.tab_widget)
        tab_layout.setContentsMargins(0, 0, 0, 0)
        
        self.tab_bar = QTabBar()
        self.tab_bar.setCursor(Qt.PointingHandCursor)
        self.tab_bar.currentChanged.connect(self.on_tab_changed)
        
        self.tab_stack = QStackedWidget()
        tab_layout.addWidget(self.tab_bar)
        tab_layout.addWidget(self.tab_stack, 1)

        main_layout.addWidget(self.container_frame, 1)
        self.update_styles()

    def moveEvent(self, event):
        super().moveEvent(event)
        if not hasattr(self, '_drop_timer'):
            self._drop_timer = QTimer(self)
            self._drop_timer.setSingleShot(True)
            self._drop_timer.timeout.connect(self.detect_window_overlap)
        self._drop_timer.start(200)

    def detect_window_overlap(self):
        if not self.main_window or not hasattr(self.main_window, 'active_popouts'):
            return
        
        # Only auto-group when the mouse click/drag event has finished (mouse button released)
        if QApplication.mouseButtons() != Qt.NoButton:
            return

        my_geo = self.geometry()
        center_pt = my_geo.center()

        for other in self.main_window.active_popouts:
            if other != self and other.isVisible() and len(other.cam_ids) > 0:
                if other.geometry().contains(center_pt) or my_geo.intersects(other.geometry()):
                    self.merge_into(other)
                    break

    def merge_into(self, target_window):
        for cid in list(self.cam_ids):
            target_window.add_camera(cid)
        target_window.raise_()
        target_window.activateWindow()
        
        self.cam_ids.clear()
        if self.main_window and hasattr(self.main_window, 'active_popouts'):
            if self in self.main_window.active_popouts:
                self.main_window.active_popouts.remove(self)

        self.close()
        self.deleteLater()

    def prompt_merge_window(self):
        if not self.main_window or not hasattr(self.main_window, 'active_popouts'):
            return
        other_wins = [w for w in self.main_window.active_popouts if w != self and w.isVisible()]
        if not other_wins:
            QMessageBox.information(self, "Merge Windows", "No other active pop-out windows open to merge with.")
            return
        
        target = other_wins[0]
        self.merge_into(target)

    def add_camera(self, cam_id):
        if cam_id not in self.cam_ids:
            self.cam_ids.append(cam_id)
            self.refresh_group_views()

    def remove_camera(self, cam_id):
        if cam_id in self.cam_ids:
            self.cam_ids.remove(cam_id)
            self.refresh_group_views()

    def set_view_mode(self, mode):
        self.view_mode = mode
        self.refresh_group_views()

    def refresh_group_views(self):
        for i in reversed(range(self.sub_grid_layout.count())):
            w = self.sub_grid_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        while self.tab_bar.count() > 0:
            self.tab_bar.removeTab(0)
        while self.tab_stack.count() > 0:
            w = self.tab_stack.widget(0)
            self.tab_stack.removeWidget(w)

        for i in reversed(range(self.container_layout.count())):
            w = self.container_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        if not self.cam_ids:
            empty_lbl = QLabel("No cameras in this pop-out group window.\nUse the '➕ Add Camera' dropdown above to add live feeds.")
            empty_lbl.setAlignment(Qt.AlignCenter)
            empty_lbl.setStyleSheet("color: #6b7280; font-size: 13px; font-weight: bold;")
            self.container_layout.addWidget(empty_lbl)
            return

        if self.view_mode == "grid":
            cols = 2 if len(self.cam_ids) > 1 else 1
            for idx, cid in enumerate(self.cam_ids):
                row = idx // cols
                col = idx % cols
                tile = LiveCameraWidget(cid, self.main_window.page_live_grid if self.main_window else None)
                self.sub_grid_layout.addWidget(tile, row, col)
            self.container_layout.addWidget(self.grid_widget)
        else:
            for cid in self.cam_ids:
                cfg = DEV_TEMPORARY_DEVICE_DB.get(cid, {})
                title = f"📹 {cfg.get('name', cid)}"
                self.tab_bar.addTab(title)
                tile = LiveCameraWidget(cid, self.main_window.page_live_grid if self.main_window else None)
                self.tab_stack.addWidget(tile)
            self.container_layout.addWidget(self.tab_widget)

        self.update_styles()

    def on_tab_changed(self, index):
        if index >= 0:
            self.tab_stack.setCurrentIndex(index)

    def on_add_cam_selected(self, index):
        if index > 0:
            cid = self.cmb_add_cam.itemData(index)
            if cid:
                self.add_camera(cid)
            self.cmb_add_cam.setCurrentIndex(0)

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.showFullScreen()
            self.btn_fullscreen.setText("🗗 Windowed [Esc]")
        else:
            self.showNormal()
            self.btn_fullscreen.setText("📺 Fullscreen [F11]")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            self.toggle_fullscreen()
        elif event.key() == Qt.Key_Escape and self.is_fullscreen:
            self.toggle_fullscreen()
        else:
            super().keyPressEvent(event)

    def update_styles(self):
        is_dark = self.main_window.is_dark_mode if self.main_window else True
        if is_dark:
            self.setStyleSheet("background-color: #0d0714; color: #ffffff;")
            self.lbl_title.setStyleSheet("color: #ff007f;")
            self.container_frame.setStyleSheet("QFrame#popoutContainer { background-color: #080410; border-radius: 10px; border: 1px solid #201235; }")
            self.btn_mode_grid.setStyleSheet("background: #ff007f; color: #ffffff; border: none; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 10px;" if self.view_mode == "grid" else "background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 5px 12px; border-radius: 6px; font-size: 10px;")
            self.btn_mode_tabs.setStyleSheet("background: #ff007f; color: #ffffff; border: none; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 10px;" if self.view_mode == "tabbed" else "background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 5px 12px; border-radius: 6px; font-size: 10px;")
            self.btn_fullscreen.setStyleSheet("background: #3b0764; color: #d4aaff; border: 1px solid #831843; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 10px;")
            self.tab_bar.setStyleSheet("QTabBar::tab { background: #1a102a; color: #9ba1a6; padding: 8px 16px; border-top-left-radius: 6px; border-top-right-radius: 6px; } QTabBar::tab:selected { background: #ff007f; color: #ffffff; font-weight: bold; }")
        else:
            self.setStyleSheet("background-color: #f8fafc; color: #0f172a;")
            self.lbl_title.setStyleSheet("color: #7c3aed;")
            self.container_frame.setStyleSheet("QFrame#popoutContainer { background-color: #ffffff; border-radius: 10px; border: 1px solid #cbd5e1; }")
            self.btn_mode_grid.setStyleSheet("background: #7c3aed; color: #ffffff; border: none; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 10px;" if self.view_mode == "grid" else "background: #e2e8f0; color: #475569; border: 1px solid #cbd5e1; padding: 5px 12px; border-radius: 6px; font-size: 10px;")
            self.btn_mode_tabs.setStyleSheet("background: #7c3aed; color: #ffffff; border: none; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 10px;" if self.view_mode == "tabbed" else "background: #e2e8f0; color: #475569; border: 1px solid #cbd5e1; padding: 5px 12px; border-radius: 6px; font-size: 10px;")
            self.btn_fullscreen.setStyleSheet("background: #ffffff; color: #7c3aed; border: 1px solid #cbd5e1; padding: 5px 12px; border-radius: 6px; font-weight: bold; font-size: 10px;")
            self.tab_bar.setStyleSheet("QTabBar::tab { background: #e2e8f0; color: #475569; padding: 8px 16px; border-top-left-radius: 6px; border-top-right-radius: 6px; } QTabBar::tab:selected { background: #7c3aed; color: #ffffff; font-weight: bold; }")


# ==========================================
# 4. LIVE CAMERA WIDGET & GRID PAGE
# ==========================================
class LiveCameraWidget(QFrame):
    """Interactive Live Stream Grid Tile with Expand & Active Selection Glow."""

    def __init__(self, cam_id, parent_grid=None):
        super().__init__()
        self.cam_id = cam_id
        self.parent_grid = parent_grid
        self.config = DEV_TEMPORARY_DEVICE_DB[cam_id]
        self.is_recording = True
        self.is_selected = False

        self.setObjectName("camTile")
        self.setCursor(Qt.PointingHandCursor)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        header = QHBoxLayout()
        self.name_label = QLabel(self.config["name"])
        self.name_label.setFont(QFont("sans-serif", 10, QFont.Bold))
        self.name_label.setStyleSheet("border: none; min-height: 20px; background: transparent;")
        
        self.badge = QLabel(self.config["type"])
        self.badge.setFont(QFont("sans-serif", 8, QFont.Bold))
        self.badge.setStyleSheet("color: #34d399; background: #064e3b; padding: 2px 6px; border-radius: 4px; border: none;")
        
        self.sel_tag = QLabel("")
        self.sel_tag.setFont(QFont("sans-serif", 8, QFont.Bold))

        btn_dev_settings = QPushButton("⚙️")
        btn_dev_settings.setToolTip("Per-Device Settings && Passcode")
        btn_dev_settings.setCursor(Qt.PointingHandCursor)
        btn_dev_settings.setStyleSheet("background: #1a102a; color: #d4aaff; border: 1px solid #371d5a; border-radius: 4px; padding: 2px 6px; font-size: 10px; min-height: 22px;")
        btn_dev_settings.clicked.connect(self.open_device_settings)

        header.addWidget(self.name_label)
        header.addWidget(self.sel_tag)
        header.addStretch()
        header.addWidget(self.badge)
        header.addWidget(btn_dev_settings)
        layout.addLayout(header)

        # Viewfinder Canvas
        self.viewfinder = QFrame()
        self.viewfinder.setObjectName("gridCanvas")
        self.viewfinder.setStyleSheet("QFrame#gridCanvas { background-color: #040207; border-radius: 8px; border: 1px solid #1a102a; }")
        vf_layout = QVBoxLayout(self.viewfinder)
        
        self.icon_label = QLabel("📹")
        self.icon_label.setFont(QFont("sans-serif", 24))
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setStyleSheet("border: none; background: transparent; color: #ffffff;")
        
        self.vf_text = QLabel(f"[ {self.config['resolution']} • {self.config['fps']}FPS ]\n{self.config['rtsp_url']}")
        self.vf_text.setFont(QFont("sans-serif", 9))
        self.vf_text.setStyleSheet("color: #6b7280; border: none; background: transparent;")
        self.vf_text.setAlignment(Qt.AlignCenter)
        
        vf_layout.addWidget(self.icon_label)
        vf_layout.addWidget(self.vf_text)
        layout.addWidget(self.viewfinder)

        controls = QHBoxLayout()
        self.rec_status = QLabel("🔴 REC")
        self.rec_status.setFont(QFont("sans-serif", 8, QFont.Bold))
        self.rec_status.setStyleSheet("color: #ef4444; border: none; background: transparent;")

        btn_popout = QPushButton("🗗 Pop Out")
        btn_popout.setCursor(Qt.PointingHandCursor)
        btn_popout.setStyleSheet("background: #3b0764; color: #ff007f; border: none; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 10px; min-height: 22px;")
        btn_popout.clicked.connect(self.popout_view)

        btn_expand = QPushButton("🔍 Expand View")
        btn_expand.setCursor(Qt.PointingHandCursor)
        btn_expand.setStyleSheet("background: #8a2be2; color: #ffffff; border: none; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 10px; min-height: 22px;")
        btn_expand.clicked.connect(self.expand_view)
        
        btn_snap = QPushButton("📸 Snap")
        btn_snap.setCursor(Qt.PointingHandCursor)
        btn_snap.setStyleSheet("background: #1e1233; color: #d4aaff; border: none; padding: 4px 8px; border-radius: 4px; font-size: 10px; min-height: 22px;")
        btn_snap.clicked.connect(self.take_snapshot)

        self.btn_rec_toggle = QPushButton("Pause")
        self.btn_rec_toggle.setCursor(Qt.PointingHandCursor)
        self.btn_rec_toggle.setStyleSheet("background: #2b1128; color: #f472b6; border: none; padding: 4px 8px; border-radius: 4px; font-size: 10px; min-height: 22px;")
        self.btn_rec_toggle.clicked.connect(self.toggle_rec)

        controls.addWidget(self.rec_status)
        controls.addStretch()
        controls.addWidget(btn_popout)
        controls.addWidget(btn_expand)
        controls.addWidget(btn_snap)
        controls.addWidget(self.btn_rec_toggle)
        layout.addLayout(controls)

    def mousePressEvent(self, event):
        if self.parent_grid:
            self.parent_grid.select_tile(self.cam_id)
        super().mousePressEvent(event)

    def popout_view(self):
        if self.parent_grid and self.parent_grid.main_window:
            self.parent_grid.main_window.open_popout_window(self.cam_id)
        elif self.window() and hasattr(self.window(), 'main_window') and self.window().main_window:
            self.window().main_window.open_popout_window(self.cam_id)

    def set_tile_selected(self, selected):
        self.is_selected = selected
        if selected:
            self.sel_tag.setText(" [ACTIVE SELECTION] ")
            self.sel_tag.setStyleSheet("color: #ffffff; background: #ff007f; padding: 2px 6px; border-radius: 4px;")
            self.setStyleSheet("""
                QFrame#camTile {
                    border: 3px solid #ff007f !important;
                    border-radius: 12px;
                }
            """)
        else:
            self.sel_tag.setText("")
            self.setStyleSheet("""
                QFrame#camTile {
                    border-radius: 12px;
                }
            """)

    def expand_view(self):
        if self.parent_grid and self.parent_grid.main_window:
            self.parent_grid.main_window.open_expanded_camera(self.cam_id)

    def refresh_from_config(self):
        self.config = DEV_TEMPORARY_DEVICE_DB[self.cam_id]
        self.name_label.setText(self.config["name"])
        self.badge.setText(self.config["type"])
        
        if self.config["privacy"]:
            self.icon_label.setText("🔒")
            self.vf_text.setText("[ PER-DEVICE PRIVACY ACTIVE - FEED DISABLED ]")
            self.rec_status.setText("🚫 OFF")
            self.rec_status.setStyleSheet("color: #6b7280; border: none; background: transparent;")
        else:
            self.icon_label.setText("📹")
            self.vf_text.setText(f"[ {self.config['resolution']} • {self.config['fps']}FPS ]\n{self.config['rtsp_url']}")
            if self.is_recording:
                self.rec_status.setText("🔴 REC")
                self.rec_status.setStyleSheet("color: #ef4444; border: none; background: transparent;")

    def open_device_settings(self):
        is_dark = True
        if self.parent_grid and self.parent_grid.main_window:
            is_dark = self.parent_grid.main_window.is_dark_mode
        dlg = PerDeviceSettingsDialog(self.cam_id, self, is_dark_mode=is_dark)
        if dlg.exec():
            self.refresh_from_config()

    def take_snapshot(self):
        self.vf_text.setText(f"[ Snapshot Saved to /tmp/fennec_snaps/{self.cam_id}_snap.jpg ]")
        QTimer.singleShot(2500, self.refresh_from_config)

    def toggle_rec(self):
        self.is_recording = not self.is_recording
        if self.is_recording:
            self.rec_status.setText("🔴 REC")
            self.rec_status.setStyleSheet("color: #ef4444; border: none; background: transparent;")
            self.btn_rec_toggle.setText("Pause")
        else:
            self.rec_status.setText("⏸ PAUSED")
            self.rec_status.setStyleSheet("color: #f59e0b; border: none; background: transparent;")
            self.btn_rec_toggle.setText("Resume")

    def set_privacy_mode(self, enabled):
        if enabled:
            self.icon_label.setText("🔒")
            self.vf_text.setText("[ GLOBAL PRIVACY MODE ACTIVE - CAMERA OFF ]")
            self.rec_status.setText("🚫 OFF")
            self.rec_status.setStyleSheet("color: #6b7280; border: none; background: transparent;")
        else:
            self.refresh_from_config()


class LiveGridPage(QWidget):
    """Main Camera Stream Grid Page with Explicit Tile Selection, Pagination & Auto-Tour Carousel Engine."""

    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.selected_cam_id = "cam-01"
        self.active_grid_mode = "2x2"
        self.current_page = 0

        self.tour_intervals = [0, 5, 10, 30]
        self.tour_idx = 0
        self.tour_timer = QTimer(self)
        self.tour_timer.timeout.connect(self.next_page)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        toolbar = QHBoxLayout()
        
        lbl_layout = QLabel("Grid Layout:")
        lbl_layout.setFont(QFont("sans-serif", 10, QFont.Bold))
        toolbar.addWidget(lbl_layout)

        self.btn_2x2 = QPushButton("✓ 2x2 (4 Cams)")
        self.btn_2x2.setCursor(Qt.PointingHandCursor)
        self.btn_2x2.clicked.connect(lambda: self.set_grid_layout("2x2"))
        toolbar.addWidget(self.btn_2x2)

        self.btn_3x3 = QPushButton("3x3 (9 Cams)")
        self.btn_3x3.setCursor(Qt.PointingHandCursor)
        self.btn_3x3.clicked.connect(lambda: self.set_grid_layout("3x3"))
        toolbar.addWidget(self.btn_3x3)

        toolbar.addSpacing(10)

        # Pagination Bar
        self.btn_prev_page = QPushButton("⬅️ Prev")
        self.btn_prev_page.setCursor(Qt.PointingHandCursor)
        self.btn_prev_page.clicked.connect(self.prev_page)

        self.lbl_page_info = QLabel("Page 1 of 1")
        self.lbl_page_info.setFont(QFont("sans-serif", 9, QFont.Bold))

        self.btn_next_page = QPushButton("Next ➡️")
        self.btn_next_page.setCursor(Qt.PointingHandCursor)
        self.btn_next_page.clicked.connect(self.next_page)

        toolbar.addWidget(self.btn_prev_page)
        toolbar.addWidget(self.lbl_page_info)
        toolbar.addWidget(self.btn_next_page)

        toolbar.addSpacing(10)

        # Auto-Tour Timer Switcher
        self.btn_auto_tour = QPushButton("🔄 Auto-Tour: OFF")
        self.btn_auto_tour.setCursor(Qt.PointingHandCursor)
        self.btn_auto_tour.setStyleSheet("background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 6px 12px; border-radius: 6px; font-size: 11px; min-height: 28px;")
        self.btn_auto_tour.clicked.connect(self.cycle_auto_tour)
        toolbar.addWidget(self.btn_auto_tour)

        toolbar.addSpacing(10)

        self.btn_privacy = QPushButton("🛡️ Global Privacy: OFF")
        self.btn_privacy.setCursor(Qt.PointingHandCursor)
        self.btn_privacy.setStyleSheet("background: #161026; color: #10b981; border: 1px solid #059669; padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
        self.btn_privacy.clicked.connect(self.toggle_privacy)
        toolbar.addWidget(self.btn_privacy)

        self.btn_siren = QPushButton("🚨 Emergency Siren")
        self.btn_siren.setCursor(Qt.PointingHandCursor)
        self.btn_siren.setStyleSheet("background: #3b0764; color: #f43f5e; border: 1px solid #e11d48; padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
        self.btn_siren.clicked.connect(self.trigger_siren)
        toolbar.addWidget(self.btn_siren)

        toolbar.addStretch()

        self.btn_snap_all = QPushButton("📸 Snapshot All")
        self.btn_snap_all.setCursor(Qt.PointingHandCursor)
        self.btn_snap_all.setStyleSheet("background: #1a102a; color: #ffffff; border: 1px solid #371d5a; padding: 6px 12px; border-radius: 6px; font-size: 11px; min-height: 28px;")
        self.btn_snap_all.clicked.connect(self.take_snapshot_all)
        toolbar.addWidget(self.btn_snap_all)

        layout.addLayout(toolbar)

        grid_frame = QFrame()
        grid_frame.setObjectName("gridFrame")
        grid_frame.setStyleSheet("QFrame#gridFrame { border-radius: 14px; }")
        self.grid_layout = QGridLayout(grid_frame)
        self.grid_layout.setContentsMargins(10, 10, 10, 10)
        self.grid_layout.setSpacing(10)

        self.cam_widgets = {}
        all_cams = list(DEV_TEMPORARY_DEVICE_DB.keys())
        for cid in all_cams:
            widget = LiveCameraWidget(cid, self)
            self.cam_widgets[cid] = widget

        layout.addWidget(grid_frame, 1)
        self.set_grid_layout("2x2")

    def select_tile(self, cam_id):
        self.selected_cam_id = cam_id
        for cid, widget in self.cam_widgets.items():
            widget.set_tile_selected(cid == cam_id)

    def update_layout_button_styles(self):
        is_dark = self.main_window.is_dark_mode if self.main_window else True
        btn_nav_style = "background: #1a102a; color: #d4aaff; border: 1px solid #371d5a; padding: 5px 10px; border-radius: 6px; font-size: 11px; min-height: 26px;" if is_dark else "background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; padding: 5px 10px; border-radius: 6px; font-size: 11px; min-height: 26px;"
        self.btn_prev_page.setStyleSheet(btn_nav_style)
        self.btn_next_page.setStyleSheet(btn_nav_style)
        self.lbl_page_info.setStyleSheet("color: #d4aaff; padding: 0 6px;" if is_dark else "color: #7c3aed; padding: 0 6px;")

        if self.active_grid_mode == "2x2":
            self.btn_2x2.setText("✓ 2x2 (4 Cams)")
            self.btn_3x3.setText("3x3 (9 Cams)")
            if is_dark:
                self.btn_2x2.setStyleSheet("background: #ff007f; color: #ffffff; border: 2px solid #ffffff; padding: 6px 14px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
                self.btn_3x3.setStyleSheet("background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 6px 14px; border-radius: 6px; font-size: 11px; min-height: 28px;")
            else:
                self.btn_2x2.setStyleSheet("background: #7c3aed; color: #ffffff; border: 2px solid #5b21b6; padding: 6px 14px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
                self.btn_3x3.setStyleSheet("background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; padding: 6px 14px; border-radius: 6px; font-size: 11px; min-height: 28px;")
        else:
            self.btn_2x2.setText("2x2 (4 Cams)")
            self.btn_3x3.setText("✓ 3x3 (9 Cams)")
            if is_dark:
                self.btn_3x3.setStyleSheet("background: #ff007f; color: #ffffff; border: 2px solid #ffffff; padding: 6px 14px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
                self.btn_2x2.setStyleSheet("background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 6px 14px; border-radius: 6px; font-size: 11px; min-height: 28px;")
            else:
                self.btn_3x3.setStyleSheet("background: #7c3aed; color: #ffffff; border: 2px solid #5b21b6; padding: 6px 14px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
                self.btn_2x2.setStyleSheet("background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; padding: 6px 14px; border-radius: 6px; font-size: 11px; min-height: 28px;")

    def set_grid_layout(self, mode):
        self.active_grid_mode = mode
        self.current_page = 0
        self.render_current_page()

    def render_current_page(self):
        self.update_layout_button_styles()

        for cid, w in self.cam_widgets.items():
            self.grid_layout.removeWidget(w)
            w.hide()

        all_keys = list(self.cam_widgets.keys())
        page_size = 4 if self.active_grid_mode == "2x2" else 9
        total_pages = max(1, (len(all_keys) + page_size - 1) // page_size)

        if self.current_page >= total_pages:
            self.current_page = 0

        start_idx = self.current_page * page_size
        end_idx = min(len(all_keys), start_idx + page_size)
        page_keys = all_keys[start_idx:end_idx]

        cols = 2 if self.active_grid_mode == "2x2" else 3
        for idx, cid in enumerate(page_keys):
            row = idx // cols
            col = idx % cols
            w = self.cam_widgets[cid]
            w.show()
            self.grid_layout.addWidget(w, row, col)

        self.lbl_page_info.setText(f"Page {self.current_page + 1}/{total_pages} ({start_idx + 1}-{end_idx} of {len(all_keys)})")
        self.btn_prev_page.setEnabled(total_pages > 1)
        self.btn_next_page.setEnabled(total_pages > 1)

        self.select_tile(self.selected_cam_id)

    def prev_page(self):
        all_keys = list(self.cam_widgets.keys())
        page_size = 4 if self.active_grid_mode == "2x2" else 9
        total_pages = max(1, (len(all_keys) + page_size - 1) // page_size)
        self.current_page = (self.current_page - 1) % total_pages
        self.render_current_page()

    def next_page(self):
        all_keys = list(self.cam_widgets.keys())
        page_size = 4 if self.active_grid_mode == "2x2" else 9
        total_pages = max(1, (len(all_keys) + page_size - 1) // page_size)
        self.current_page = (self.current_page + 1) % total_pages
        self.render_current_page()

    def cycle_auto_tour(self):
        self.tour_idx = (self.tour_idx + 1) % len(self.tour_intervals)
        seconds = self.tour_intervals[self.tour_idx]
        if seconds == 0:
            self.tour_timer.stop()
            self.btn_auto_tour.setText("🔄 Auto-Tour: OFF")
            self.btn_auto_tour.setStyleSheet("background: #1a102a; color: #9ba1a6; border: 1px solid #371d5a; padding: 6px 12px; border-radius: 6px; font-size: 11px; min-height: 28px;")
        else:
            self.tour_timer.start(seconds * 1000)
            self.btn_auto_tour.setText(f"🟢 AUTO-TOUR: {seconds}s Cycling")
            self.btn_auto_tour.setStyleSheet("background: #064e3b; color: #34d399; border: 1px solid #059669; padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")

    def take_snapshot_all(self):
        all_keys = list(self.cam_widgets.keys())
        page_size = 4 if self.active_grid_mode == "2x2" else 9
        start_idx = self.current_page * page_size
        end_idx = min(len(all_keys), start_idx + page_size)
        for cid in all_keys[start_idx:end_idx]:
            self.cam_widgets[cid].take_snapshot()

    def toggle_privacy(self):
        is_active = "OFF" in self.btn_privacy.text()
        if is_active:
            self.btn_privacy.setText("🛡️ Global Privacy: ACTIVE")
            self.btn_privacy.setStyleSheet("background: #991b1b; color: #ffffff; border: 1px solid #ef4444; padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
            for w in self.cam_widgets.values():
                w.set_privacy_mode(True)
        else:
            self.btn_privacy.setText("🛡️ Global Privacy: OFF")
            self.btn_privacy.setStyleSheet("background: #161026; color: #10b981; border: 1px solid #059669; padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 11px; min-height: 28px;")
            for w in self.cam_widgets.values():
                w.set_privacy_mode(False)

    def trigger_siren(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Emergency Alert")
        msg.setText("🚨 High-decibel local emergency siren triggered on all node speakers!")
        if self.main_window and self.main_window.is_dark_mode:
            msg.setStyleSheet("background-color: #1a0a2a; color: #ffffff;")
        else:
            msg.setStyleSheet("background-color: #ffffff; color: #000000;")
        msg.exec()


# ==========================================
# 5. MOBILE NODES PAGE
# ==========================================
class MobileNodesPage(QWidget):
    """Mobile Phone Camera Nodes Management Page with Per-Device Passcodes."""

    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)

        header = QHBoxLayout()
        title_box = QVBoxLayout()
        title = QLabel("📱 Mobile Phone Camera Nodes")
        title.setFont(QFont("sans-serif", 14, QFont.Bold))
        subtitle = QLabel("Repurposed Android && iOS devices functioning as low-power edge IP RTSP nodes.")
        subtitle.setObjectName("subTitleLabel")
        title_box.addWidget(title)
        title_box.addWidget(subtitle)

        btn_pair = QPushButton("➕ Pair New Phone Node (QR Code)")
        btn_pair.setObjectName("btnPair")
        btn_pair.setCursor(Qt.PointingHandCursor)
        btn_pair.clicked.connect(self.show_qr_dialog)

        header.addLayout(title_box)
        header.addStretch()
        header.addWidget(btn_pair)
        layout.addLayout(header)

        banner = QFrame()
        banner.setObjectName("swellBanner")
        banner_layout = QHBoxLayout(banner)

        b_icon = QLabel("🔋")
        b_icon.setFont(QFont("sans-serif", 20))
        
        b_info = QVBoxLayout()
        b_title = QLabel("Battery Swell Protection Engine (80% Charge Cap)")
        b_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        b_title.setStyleSheet("color: #059669;" if (self.main_window and not self.main_window.is_dark_mode) else "color: #34d399;")
        
        b_desc = QLabel("Prevents lithium battery degradation by cutting off AC power toggles via smart plug when node battery hits 80%.")
        b_desc.setObjectName("subTitleLabel")
        b_info.addWidget(b_title)
        b_info.addWidget(b_desc)

        swell_toggle = QCheckBox("Enable Protection")
        swell_toggle.setChecked(True)
        swell_toggle.setStyleSheet("font-weight: bold; font-size: 11px;")

        banner_layout.addWidget(b_icon)
        banner_layout.addLayout(b_info)
        banner_layout.addStretch()
        banner_layout.addWidget(swell_toggle)
        layout.addWidget(banner)

        nodes_scroll = QScrollArea()
        nodes_scroll.setWidgetResizable(True)
        nodes_scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        nodes_container = QWidget()
        nc_layout = QVBoxLayout(nodes_container)
        nc_layout.setContentsMargins(0, 0, 0, 0)
        nc_layout.setSpacing(10)

        paired_devices = [
            ("cam-02", "Driveway Node", "Galaxy S24 (Android 14)", "192.168.1.105", "PIN: 4490", "Battery: 78% (Thermal: 34°C)", "Online • 4K 24FPS"),
            ("cam-05", "Backyard Node", "Pixel 7 Pro (Android 14)", "192.168.1.112", "PIN: 9102", "Battery: 80% (Capped)", "Online • 1080p 30FPS"),
            ("cam-06", "Hallway Backup", "iPhone 11 (iOS 17)", "192.168.1.140", "PIN: 3311", "Battery: 92% (Warning)", "Standby • Low Power")
        ]

        for cid, name, model, ip, pin, batt, status in paired_devices:
            card = QFrame()
            card.setObjectName("nodeCard")
            c_layout = QHBoxLayout(card)

            d_info = QVBoxLayout()
            d_name = QLabel(f"{name} — {model}")
            d_name.setFont(QFont("sans-serif", 11, QFont.Bold))
            
            d_details = QLabel(f"IP: {ip}  |  {pin}  |  {batt}  |  Status: {status}")
            d_details.setObjectName("detailLabel")
            
            d_info.addWidget(d_name)
            d_info.addWidget(d_details)

            btn_exp = QPushButton("🔍 Focus View")
            btn_exp.setObjectName("btnPrimaryAction")
            btn_exp.setCursor(Qt.PointingHandCursor)
            btn_exp.clicked.connect(lambda _, target_id=cid: self.open_expanded(target_id))

            btn_cfg = QPushButton("⚙️ Passcode && Settings")
            btn_cfg.setObjectName("btnSecondaryAction")
            btn_cfg.setCursor(Qt.PointingHandCursor)
            btn_cfg.clicked.connect(lambda _, target_id=cid: self.open_device_dialog(target_id))

            c_layout.addLayout(d_info)
            c_layout.addStretch()
            c_layout.addWidget(btn_exp)
            c_layout.addWidget(btn_cfg)
            nc_layout.addWidget(card)

        nc_layout.addStretch()
        nodes_scroll.setWidget(nodes_container)
        layout.addWidget(nodes_scroll, 1)

    def open_expanded(self, cid):
        if self.main_window:
            self.main_window.open_expanded_camera(cid)

    def open_device_dialog(self, cid):
        is_dark = True
        if self.main_window:
            is_dark = self.main_window.is_dark_mode
        if cid in DEV_TEMPORARY_DEVICE_DB:
            dlg = PerDeviceSettingsDialog(cid, self, is_dark_mode=is_dark)
            dlg.exec()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Node Settings")
            msg.setText(f"📱 Selected mobile node ({cid}) settings opened.")
            msg.setStyleSheet("background-color: #1a0a2a; color: #ffffff;")
            msg.exec()

    def show_qr_dialog(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Pair Mobile Camera Node")
        msg.setText("📱 Scan QR Code on Mobile App:\n\n[ QR CODE: fennec://pair?token=8a2be2_offlinerelease&pin=4490 ]\n\nEnsure mobile device is connected to the same OpenWrt WiFi network.")
        msg.setStyleSheet("background-color: #1a0a2a; color: #ffffff;")
        msg.exec()


# ==========================================
# 6. TIERED STORAGE & NAS PAGE
# ==========================================
class StorageNASPage(QWidget):
    """Tiered Storage & NAS Mount Configuration Page."""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        title = QLabel("💾 Tiered Storage && NAS Mounts")
        title.setFont(QFont("sans-serif", 14, QFont.Bold))
        layout.addWidget(title)

        denial_card = QFrame()
        denial_card.setObjectName("denialCard")
        dc_layout = QHBoxLayout(denial_card)
        
        warn_icon = QLabel("⚠️")
        warn_icon.setFont(QFont("sans-serif", 20))
        
        dc_info = QVBoxLayout()
        dc_title = QLabel("16GB Auto-Denial Internal Flash Protection Rule")
        dc_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        dc_title.setStyleSheet("color: #f43f5e; background: transparent;")
        dc_desc = QLabel("Internal OS eMMC/SATA drives <= 16GB strictly refuse full continuous NVR recording to prevent Wear-Out failure.")
        dc_desc.setObjectName("subTitleLabel")
        dc_info.addWidget(dc_title)
        dc_info.addWidget(dc_desc)

        denial_toggle = QCheckBox("Enforce Hard Limit")
        denial_toggle.setChecked(True)
        denial_toggle.setStyleSheet("font-weight: bold; font-size: 11px; background: transparent;")

        dc_layout.addWidget(warn_icon)
        dc_layout.addLayout(dc_info)
        dc_layout.addStretch()
        dc_layout.addWidget(denial_toggle)
        layout.addWidget(denial_card)

        nvme_box = QFrame()
        nvme_box.setObjectName("nvmeBox")
        nb_layout = QVBoxLayout(nvme_box)

        nb_header = QHBoxLayout()
        nb_title = QLabel("Local NVMe Rolling Ring Buffer (5-15 min High-FPS Retention)")
        nb_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        nb_usage = QLabel("3.2 GB / 64 GB (5% Used)")
        nb_usage.setStyleSheet("color: #34d399; font-weight: bold; font-size: 10px; background: transparent;")
        nb_header.addWidget(nb_title)
        nb_header.addStretch()
        nb_header.addWidget(nb_usage)
        nb_layout.addLayout(nb_header)

        pbar = QProgressBar()
        pbar.setFixedHeight(10)
        pbar.setValue(5)
        pbar.setTextVisible(False)
        pbar.setStyleSheet("""
            QProgressBar { background: #1a102a; border-radius: 5px; }
            QProgressBar::chunk { background: #8a2be2; border-radius: 5px; }
        """)
        nb_layout.addWidget(pbar)
        layout.addWidget(nvme_box)

        nas_box = QFrame()
        nas_box.setObjectName("nasBox")
        nas_layout = QVBoxLayout(nas_box)

        nas_title = QLabel("🌐 External Network Attached Storage (TrueNAS / Unraid / NFS / SMB)")
        nas_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        nas_title.setObjectName("sectionHeader")
        nas_layout.addWidget(nas_title)

        form_layout = QGridLayout()
        form_layout.setSpacing(10)

        form_layout.addWidget(QLabel("NAS Host/IP:"), 0, 0)
        self.input_nas_ip = QLineEdit("192.168.1.200")
        form_layout.addWidget(self.input_nas_ip, 0, 1)

        form_layout.addWidget(QLabel("Share Protocol:"), 0, 2)
        self.radio_nfs = QRadioButton("NFS v4 (Recommended)")
        self.radio_nfs.setChecked(True)
        form_layout.addWidget(self.radio_nfs, 0, 3)

        form_layout.addWidget(QLabel("Mount Path:"), 1, 0)
        self.input_mount = QLineEdit("/mnt/truenas/fennec_cams")
        form_layout.addWidget(self.input_mount, 1, 1, 1, 3)

        nas_layout.addLayout(form_layout)

        btn_test_nas = QPushButton("🔌 Test && Mount Remote Storage")
        btn_test_nas.setObjectName("btnPrimaryAction")
        btn_test_nas.setCursor(Qt.PointingHandCursor)
        btn_test_nas.clicked.connect(self.test_nas_connection)
        nas_layout.addWidget(btn_test_nas)

        layout.addWidget(nas_box)
        layout.addStretch()

    def test_nas_connection(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("NAS Mount Test")
        msg.setText(f"✅ Connection Successful!\n\nTarget Path: {self.input_mount.text()}\nHost: {self.input_nas_ip.text()}\nFree Capacity: 1.8 TB")
        msg.setStyleSheet("background-color: #1a0a2a; color: #ffffff;")
        msg.exec()


# ==========================================
# 7. OPENWRT MESH PAGE
# ==========================================
class OpenWrtMeshPage(QWidget):
    """OpenWrt Router P2P Mesh Page."""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        title = QLabel("📡 OpenWrt Mesh && WireGuard Peer Network")
        title.setFont(QFont("sans-serif", 14, QFont.Bold))
        layout.addWidget(title)

        qos_card = QFrame()
        qos_card.setObjectName("qosCard")
        q_layout = QVBoxLayout(qos_card)

        q_head = QHBoxLayout()
        q_title = QLabel("Mesh Video Traffic QoS Limit (Mbps)")
        q_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        self.q_val = QLabel("25 Mbps")
        self.q_val.setStyleSheet("color: #ff007f; font-weight: bold; background: transparent;")
        q_head.addWidget(q_title)
        q_head.addStretch()
        q_head.addWidget(self.q_val)
        q_layout.addLayout(q_head)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(5)
        slider.setMaximum(100)
        slider.setValue(25)
        slider.valueChanged.connect(lambda v: self.q_val.setText(f"{v} Mbps"))
        q_layout.addWidget(slider)

        layout.addWidget(qos_card)

        peer_box = QFrame()
        peer_box.setObjectName("peerBox")
        p_layout = QVBoxLayout(peer_box)

        p_title = QLabel("🔒 WireGuard Active Mesh Tunnel Peers")
        p_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        p_title.setObjectName("sectionHeader")
        p_layout.addWidget(p_title)

        peers = [
            ("Router-North (OpenWrt 23.05)", "10.8.0.1", "PSK Passcode Protected", "Latency: 2ms"),
            ("Outdoor Relay Node", "10.8.0.4", "PSK Passcode Protected", "Latency: 8ms"),
            ("Garage Access Point", "10.8.0.9", "PSK Passcode Protected", "Latency: 4ms")
        ]

        for p_name, p_ip, p_psk, p_stat in peers:
            p_row = QHBoxLayout()
            p_lbl = QLabel(f"● {p_name} ({p_ip})")
            p_lbl.setStyleSheet("color: #34d399; font-weight: bold; font-size: 11px; background: transparent;")
            p_info = QLabel(f"{p_psk} • {p_stat}")
            p_info.setObjectName("detailLabel")
            p_row.addWidget(p_lbl)
            p_row.addStretch()
            p_row.addWidget(p_info)
            p_layout.addLayout(p_row)

        layout.addWidget(peer_box)
        layout.addStretch()


# ==========================================
# 8. LOCAL EDGE AI PAGE
# ==========================================
class LocalEdgeAIPage(QWidget):
    """Local YOLOv8 Edge AI Detection Settings."""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        title = QLabel("⚡ Local Edge AI (YOLOv8 && NPU Acceleration)")
        title.setFont(QFont("sans-serif", 14, QFont.Bold))
        layout.addWidget(title)

        conf_card = QFrame()
        conf_card.setObjectName("confCard")
        c_layout = QVBoxLayout(conf_card)

        c_head = QHBoxLayout()
        c_title = QLabel("Detection Confidence Threshold")
        c_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        self.c_val = QLabel("70%")
        self.c_val.setStyleSheet("color: #34d399; font-weight: bold; background: transparent;")
        c_head.addWidget(c_title)
        c_head.addStretch()
        c_head.addWidget(self.c_val)
        c_layout.addLayout(c_head)

        conf_slider = QSlider(Qt.Horizontal)
        conf_slider.setMinimum(30)
        conf_slider.setMaximum(95)
        conf_slider.setValue(70)
        conf_slider.valueChanged.connect(lambda v: self.c_val.setText(f"{v}%"))
        c_layout.addWidget(conf_slider)

        layout.addWidget(conf_card)

        target_box = QFrame()
        target_box.setObjectName("targetBox")
        t_layout = QVBoxLayout(target_box)

        t_title = QLabel("🎯 Detected Target Classes (Local NPU/CPU Processing)")
        t_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        t_title.setObjectName("sectionHeader")
        t_layout.addWidget(t_title)

        grid = QGridLayout()
        classes = ["👤 Person / Human", "🚗 Vehicle / Car", "🐕 Pets / Animals", "📦 Package Delivery", "🚪 Door Open/Close"]
        for idx, cls_name in enumerate(classes):
            chk = QCheckBox(cls_name)
            chk.setChecked(True)
            chk.setStyleSheet("font-size: 11px; background: transparent;")
            grid.addWidget(chk, idx // 2, idx % 2)
        t_layout.addLayout(grid)

        layout.addWidget(target_box)
        layout.addStretch()


# ==========================================
# 9. SYSTEM HEALTH PAGE
# ==========================================
class SystemHealthPage(QWidget):
    """Intel N150 / Pentium Gold Hardware Diagnostics & Log Output."""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        title = QLabel("📊 System Health && Runtime Diagnostics")
        title.setFont(QFont("sans-serif", 14, QFont.Bold))
        layout.addWidget(title)

        hw_box = QFrame()
        hw_box.setObjectName("hwBox")
        h_layout = QVBoxLayout(hw_box)

        h_title = QLabel("🖥️ Target Low-Power Hardware: Intel N150 / Pentium 6500Y")
        h_title.setFont(QFont("sans-serif", 11, QFont.Bold))
        h_title.setStyleSheet("color: #34d399; background: transparent;")
        h_layout.addWidget(h_title)

        m_grid = QGridLayout()
        m_grid.addWidget(QLabel("CPU Usage: 14% (4-Cores Active)"), 0, 0)
        m_grid.addWidget(QLabel("RAM Usage: 1.2 GB / 8.0 GB"), 0, 1)
        m_grid.addWidget(QLabel("Bound Port: 8081 (HTTP API Local)"), 1, 0)
        m_grid.addWidget(QLabel("CPU Temp: 41°C (Fanless OK)"), 1, 1)
        
        for i in range(m_grid.count()):
            m_grid.itemAt(i).widget().setObjectName("detailLabel")
        h_layout.addLayout(m_grid)

        layout.addWidget(hw_box)

        log_box = QFrame()
        log_box.setObjectName("logBox")
        l_layout = QVBoxLayout(log_box)

        l_head = QHBoxLayout()
        l_title = QLabel("📜 Live Application Logs (Port 8081 / Drivers / Passcodes)")
        l_title.setFont(QFont("sans-serif", 10, QFont.Bold))
        l_head.addWidget(l_title)
        l_head.addStretch()

        btn_clear = QPushButton("Clear")
        btn_clear.setStyleSheet("background: #1a102a; color: #9ba1a6; border: none; padding: 2px 8px; border-radius: 4px; font-size: 9px;")
        l_head.addWidget(btn_clear)
        l_layout.addLayout(l_head)

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setStyleSheet("background-color: #030105; color: #34d399; font-family: monospace; font-size: 10px; border: none;")
        self.log_text.setText(
            "[INFO] Fennec NVR Engine Initialized successfully.\n"
            "[INFO] Master System PIN active (PIN verification ready).\n"
            "[INFO] Listening for HTTP API connections on http://127.0.0.1:8081\n"
            "[INFO] Active selection indicators enabled (Accent Left Bar, Neon Tile Border)."
        )
        l_layout.addWidget(self.log_text)

        layout.addWidget(log_box, 1)


# ==========================================
# 10. MAIN APPLICATION DASHBOARD WINDOW
# ==========================================
class MainDashboardWindow(QMainWindow):
    """Main Application Window with Clear Active Selection Indicators & QSS Theme Engine."""

    DARK_STYLESHEET = """
        QMainWindow, QWidget {
            background-color: #06020a;
            color: #f8f9fa;
            font-family: 'sans-serif';
        }
        QFrame#sidebarFrame, QFrame#gridFrame, QFrame#nodeCard, QFrame#denialCard, QFrame#nvmeBox, QFrame#nasBox, QFrame#qosCard, QFrame#peerBox, QFrame#confCard, QFrame#targetBox, QFrame#hwBox, QFrame#logBox, QFrame#swellBanner, QFrame#ctrlPanel, QFrame#scrubCard {
            background-color: #0c0714;
            border: 1px solid #201235;
            border-radius: 12px;
        }
        QFrame#camTile {
            background-color: #0b0612;
            border: 1px solid #281640;
            border-radius: 12px;
        }
        QLabel {
            color: #ffffff;
            background: transparent;
        }
        QLabel#subTitleLabel, QLabel#detailLabel {
            color: #9ba1a6;
            background: transparent;
        }
        QLabel#sectionHeader {
            color: #d4aaff;
            background: transparent;
        }
        QLineEdit, QComboBox, QSpinBox {
            background-color: #1a102a;
            border: 1px solid #371d5a;
            color: #ffffff;
            padding: 6px;
            border-radius: 6px;
        }
        QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QPushButton:focus {
            border: 2px solid #ff007f;
        }
        QPushButton#btnPair, QPushButton#btnPrimaryAction {
            background: linear-gradient(45deg, #ff007f, #8a2be2);
            color: #ffffff;
            border: none;
            padding: 6px 14px;
            border-radius: 6px;
            font-weight: bold;
            min-height: 28px;
        }
        QPushButton#btnSecondaryAction {
            background: #1a102a;
            color: #d4aaff;
            border: 1px solid #371d5a;
            padding: 6px 14px;
            border-radius: 6px;
            min-height: 28px;
        }
    """

    LIGHT_STYLESHEET = """
        QMainWindow, QWidget {
            background-color: #f1f5f9;
            color: #0f172a;
            font-family: 'sans-serif';
        }
        QFrame#sidebarFrame, QFrame#gridFrame, QFrame#nodeCard, QFrame#denialCard, QFrame#nvmeBox, QFrame#nasBox, QFrame#qosCard, QFrame#peerBox, QFrame#confCard, QFrame#targetBox, QFrame#hwBox, QFrame#logBox, QFrame#swellBanner, QFrame#ctrlPanel, QFrame#scrubCard {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
        }
        QFrame#camTile {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
        }
        QLabel {
            color: #0f172a;
            background: transparent;
        }
        QLabel#subTitleLabel, QLabel#detailLabel {
            color: #475569;
            background: transparent;
        }
        QLabel#sectionHeader {
            color: #6d28d9;
            background: transparent;
        }
        QLineEdit, QComboBox, QSpinBox {
            background-color: #ffffff;
            border: 1px solid #cbd5e1;
            color: #0f172a;
            padding: 6px;
            border-radius: 6px;
        }
        QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QPushButton:focus {
            border: 2px solid #7c3aed;
        }
        QPushButton#btnPair, QPushButton#btnPrimaryAction {
            background: #7c3aed;
            color: #ffffff;
            border: none;
            padding: 6px 14px;
            border-radius: 6px;
            font-weight: bold;
            min-height: 28px;
        }
        QPushButton#btnSecondaryAction {
            background: #f1f5f9;
            color: #0f172a;
            border: 1px solid #cbd5e1;
            padding: 6px 14px;
            border-radius: 6px;
            min-height: 28px;
        }
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fennec Cameras - Linux NVR Desktop Application")
        self.resize(1180, 760)
        self.is_dark_mode = True  # ALWAYS START IN DARK MODE BY DEFAULT
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(14)

        # 1. Top Navbar
        navbar = QHBoxLayout()
        brand = QLabel("🦊 FENNEC CAMERAS")
        brand.setFont(QFont("sans-serif", 16, QFont.Bold))
        
        self.status_tag = QLabel("100% OFFLINE • ZERO CLOUD")
        self.status_tag.setFont(QFont("sans-serif", 9, QFont.Bold))

        navbar.addWidget(brand)
        navbar.addSpacing(12)
        navbar.addWidget(self.status_tag)
        navbar.addStretch()

        self.btn_theme = QPushButton("🌙 Dark Mode")
        self.btn_theme.setCursor(Qt.PointingHandCursor)
        self.btn_theme.clicked.connect(self.toggle_theme)
        navbar.addWidget(self.btn_theme)

        self.btn_settings = QPushButton("🔑 Master Passcode")
        self.btn_settings.setCursor(Qt.PointingHandCursor)
        self.btn_settings.clicked.connect(self.prompt_master_passcode)
        navbar.addWidget(self.btn_settings)

        main_layout.addLayout(navbar)

        # 2. Body (Sidebar Navigation + Stacked Content Pages)
        body = QHBoxLayout()
        body.setSpacing(16)

        sidebar = QFrame()
        sidebar.setObjectName("sidebarFrame")
        sidebar.setFixedWidth(230)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(10, 15, 10, 15)
        sb_layout.setSpacing(6)

        self.stack = QStackedWidget()

        self.page_live_grid = LiveGridPage(self)
        self.page_expanded_view = ExpandedCameraViewPage(self)
        self.page_mobile_nodes = MobileNodesPage(self)
        self.page_storage_nas = StorageNASPage()
        self.page_openwrt_mesh = OpenWrtMeshPage()
        self.page_edge_ai = LocalEdgeAIPage()
        self.page_system_health = SystemHealthPage()

        self.stack.addWidget(self.page_live_grid)
        self.stack.addWidget(self.page_mobile_nodes)
        self.stack.addWidget(self.page_storage_nas)
        self.stack.addWidget(self.page_openwrt_mesh)
        self.stack.addWidget(self.page_edge_ai)
        self.stack.addWidget(self.page_system_health)
        self.stack.addWidget(self.page_expanded_view)

        self.nav_buttons = []
        self.nav_labels = [
            ("📺 Live Camera Grid", 0),
            ("📱 Mobile Nodes", 1),
            ("💾 Tiered Storage && NAS", 2),
            ("📡 OpenWrt Mesh", 3),
            ("⚡ Local Edge AI", 4),
            ("📊 System Health", 5),
        ]

        for text, index in self.nav_labels:
            btn = QPushButton(text)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda _, idx=index: self.switch_page(idx))
            sb_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        sb_layout.addStretch()
        body.addWidget(sidebar)
        body.addWidget(self.stack, 1)
        main_layout.addLayout(body, 1)

        # 3. Bottom Status Bar
        footer = QHBoxLayout()
        info_label = QLabel("Maintainer Hardware: Intel N150 / Pentium 6500Y • Bound Port: 8081 • Selection Highlights Active")
        info_label.setFont(QFont("sans-serif", 9))
        info_label.setStyleSheet("color: #6b7280; background: transparent;")

        footer.addWidget(info_label)
        footer.addStretch()
        main_layout.addLayout(footer)

        self.setCentralWidget(main_widget)
        self.apply_theme()
        self.update_nav_styles(0)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            self.setStyleSheet(self.DARK_STYLESHEET)
            self.btn_theme.setText("🌙 Dark Mode")
            self.btn_theme.setStyleSheet("background: #1a102a; border: 1px solid #371d5a; color: #ffffff; padding: 6px 14px; border-radius: 8px; font-size: 11px; font-weight: bold; min-height: 28px;")
            self.btn_settings.setStyleSheet("background: #1a102a; border: 1px solid #371d5a; color: #d4aaff; padding: 6px 14px; border-radius: 8px; font-size: 11px; font-weight: bold; min-height: 28px;")
            self.status_tag.setStyleSheet("color: #34d399; background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); padding: 4px 10px; border-radius: 12px;")
        else:
            self.setStyleSheet(self.LIGHT_STYLESHEET)
            self.btn_theme.setText("☀️ Light Mode")
            self.btn_theme.setStyleSheet("background: #ffffff; border: 1px solid #cbd5e1; color: #0f172a; padding: 6px 14px; border-radius: 8px; font-size: 11px; font-weight: bold; min-height: 28px;")
            self.btn_settings.setStyleSheet("background: #ffffff; border: 1px solid #cbd5e1; color: #7c3aed; padding: 6px 14px; border-radius: 8px; font-size: 11px; font-weight: bold; min-height: 28px;")
            self.status_tag.setStyleSheet("color: #047857; background: #d1fae5; border: 1px solid #a7f3d0; padding: 4px 10px; border-radius: 12px;")
        self.update_nav_styles(self.stack.currentIndex())
        if hasattr(self, 'page_live_grid'):
            self.page_live_grid.update_layout_button_styles()
        if hasattr(self, 'active_popouts'):
            for win in self.active_popouts:
                if win.isVisible():
                    win.update_styles()

    def open_popout_window(self, cam_id):
        if not hasattr(self, 'active_popouts'):
            self.active_popouts = []

        cfg = DEV_TEMPORARY_DEVICE_DB.get(cam_id, {})
        cam_name = cfg.get("name", cam_id)

        popout_win = PopoutCameraGroupWindow(cam_name, self)
        popout_win.add_camera(cam_id)
        self.active_popouts.append(popout_win)
        popout_win.show()
        popout_win.raise_()
        popout_win.activateWindow()

    def open_expanded_camera(self, cam_id):
        self.page_expanded_view.set_camera(cam_id)
        self.stack.setCurrentIndex(6)
        self.update_nav_styles(-1)

    def prompt_master_passcode(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Master System Passcode")
        msg.setText("🔑 Master System PIN: '1234'\n\nNode Passcode Access: Authorized.")
        if self.is_dark_mode:
            msg.setStyleSheet("background-color: #1a0a2a; color: #ffffff;")
        else:
            msg.setStyleSheet("background-color: #ffffff; color: #0f172a;")
        msg.exec()

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        self.update_nav_styles(index)

    def update_nav_styles(self, active_index):
        for idx, btn in enumerate(self.nav_buttons):
            orig_text, _ = self.nav_labels[idx]
            if idx == active_index:
                btn.setText(f"▶  {orig_text}")
                if self.is_dark_mode:
                    btn.setStyleSheet("background: #2b1128; color: #ffffff; border: none; border-left: 5px solid #ff007f; padding: 10px; border-radius: 8px; text-align: left; font-weight: bold; font-size: 11px; min-height: 32px;")
                else:
                    btn.setStyleSheet("background: #f1f5f9; color: #7c3aed; border: 1px solid #cbd5e1; border-left: 5px solid #7c3aed; padding: 10px; border-radius: 8px; text-align: left; font-weight: bold; font-size: 11px; min-height: 32px;")
            else:
                btn.setText(orig_text)
                if self.is_dark_mode:
                    btn.setStyleSheet("background: transparent; color: #9ba1a6; border: none; padding: 10px; border-radius: 8px; text-align: left; font-size: 11px; min-height: 32px;")
                else:
                    btn.setStyleSheet("background: transparent; color: #334155; border: none; padding: 10px; border-radius: 8px; text-align: left; font-size: 11px; min-height: 32px;")


def launch():
    app = QApplication(sys.argv)
    
    splash = SplashScreen()
    main_win = MainDashboardWindow()

    splash.finished.connect(lambda: (splash.close(), main_win.show()))
    splash.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    launch()
