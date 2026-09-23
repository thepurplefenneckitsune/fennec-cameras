# HOW TO REMOVE TEMPORARY DEV IN-MEMORY STATE

This document outlines the steps to replace the temporary in-memory device state dictionary with persistent SQLite or JSON disk storage.

---

## Current Setup (Development Mode)

In [`desktop-core/ui/app.py`](file:///home/fox/Documents/second%20code%20folder/new%20camera%20app%20idea/desktop-core/ui/app.py), all device configurations, passcodes, RTSP endpoints, and hardware capabilities are stored in a runtime Python dictionary:

```python
DEV_TEMPORARY_DEVICE_DB = {
    "cam-01": { ... },
    "cam-02": { ... }
}
```

This temporary in-memory store allows rapid iteration and UI testing without creating database side-effects during development.

---

## 3-Step Migration to Persistent Storage

### Step 1: Replace `DEV_TEMPORARY_DEVICE_DB` with SQLite Database Helper

Create `desktop-core/storage/db.py`:

```python
import sqlite3
import json

DB_PATH = "/var/lib/fennec/fennec_config.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id TEXT PRIMARY KEY,
            name TEXT,
            type TEXT,
            ip TEXT,
            passcode TEXT,
            resolution TEXT,
            fps INTEGER,
            rtsp_url TEXT,
            privacy BOOLEAN,
            motion_sensitivity INTEGER,
            rec_schedule TEXT,
            capabilities TEXT
        )
    ''')
    conn.commit()
    conn.close()
```

### Step 2: Update Read Operations in `app.py`

Replace direct accesses to `DEV_TEMPORARY_DEVICE_DB[cam_id]` with a query function:

```python
def get_device_config(cam_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices WHERE id = ?", (cam_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "ip": row[3],
            "passcode": row[4],
            "resolution": row[5],
            "fps": row[6],
            "rtsp_url": row[7],
            "privacy": bool(row[8]),
            "motion_sensitivity": row[9],
            "rec_schedule": row[10],
            "capabilities": json.loads(row[11])
        }
    return None
```

### Step 3: Update `save_settings()` in `PerDeviceSettingsDialog`

Modify `save_settings()` to execute an `UPDATE` SQL statement:

```python
def save_settings(self):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE devices 
        SET name = ?, passcode = ?, rtsp_url = ?, resolution = ?, fps = ?, motion_sensitivity = ?, privacy = ?
        WHERE id = ?
    ''', (
        self.edit_name.text(),
        self.edit_passcode.text(),
        self.edit_rtsp.text(),
        self.cmb_res.currentText(),
        self.spn_fps.value(),
        self.sld_motion.value(),
        self.chk_priv.isChecked(),
        self.cam_id
    ))
    conn.commit()
    conn.close()
    self.accept()
```
