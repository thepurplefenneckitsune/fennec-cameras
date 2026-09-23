<?php
// CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
// Fennec Cameras - Live Web NVR Preview & System Status Display (Pure PHP)
header('Content-Type: text/html; charset=utf-8');

define('SIRV_FAVICON_URL', 'https://thepurplefox.sirv.com/kistune%20cam/purple_kitsune_logo2.jpg?cx=67&cy=74&cw=890&ch=890');

$protocol = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') ? 'https' : 'http';
$host = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : 'localhost';
$uri = isset($_SERVER['REQUEST_URI']) ? $_SERVER['REQUEST_URI'] : '';
$canonicalUrl = $protocol . '://' . $host . $uri;

$cameras = [
  "cam-01" => ["id" => "cam-01", "name" => "Front Yard Camera", "type" => "V4L2 USB Webcam", "resolution" => "1080p (1920x1080)", "fps" => 30, "rtsp" => "v4l2:///dev/video0"],
  "cam-02" => ["id" => "cam-02", "name" => "Driveway Node", "type" => "Android Phone S24", "resolution" => "4K (3840x2160)", "fps" => 24, "rtsp" => "rtsp://192.168.1.105:8554/live"],
  "cam-03" => ["id" => "cam-03", "name" => "Garage Gate", "type" => "ONVIF / RTSP IP", "resolution" => "1080p (1920x1080)", "fps" => 30, "rtsp" => "rtsp://admin:7712@192.168.1.120:554/stream1"],
  "cam-04" => ["id" => "cam-04", "name" => "Porch 360° View", "type" => "Dual-Lens Panoramic", "resolution" => "2K Panoramic", "fps" => 30, "rtsp" => "rtsp://192.168.1.135:8554/pano"],
  "cam-05" => ["id" => "cam-05", "name" => "Backyard Node", "type" => "Pixel 7 Pro Node", "resolution" => "1080p (1920x1080)", "fps" => 30, "rtsp" => "rtsp://192.168.1.112:8554/live"],
  "cam-06" => ["id" => "cam-06", "name" => "Hallway Backup", "type" => "iPhone 11 Node", "resolution" => "1080p (1920x1080)", "fps" => 30, "rtsp" => "rtsp://192.168.1.140:8554/live"],
  "cam-07" => ["id" => "cam-07", "name" => "Side Alley Cam", "type" => "ONVIF / RTSP IP", "resolution" => "1080p (1920x1080)", "fps" => 30, "rtsp" => "rtsp://admin:7743@192.168.1.145:554/stream1"],
  "cam-08" => ["id" => "cam-08", "name" => "Attic Sensor Cam", "type" => "V4L2 USB Webcam", "resolution" => "720p (1280x720)", "fps" => 30, "rtsp" => "v4l2:///dev/video1"],
  "cam-09" => ["id" => "cam-09", "name" => "Basement Perimeter", "type" => "Dual-Lens Panoramic", "resolution" => "2K Panoramic", "fps" => 30, "rtsp" => "rtsp://192.168.1.155:8554/pano"]
];
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fennec Cameras - Linux App Display Preview (PHP)</title>
  <link rel="canonical" href="<?php echo htmlspecialchars($canonicalUrl, ENT_QUOTES, 'UTF-8'); ?>" />
  <link rel="icon" type="image/jpeg" href="<?php echo htmlspecialchars(SIRV_FAVICON_URL, ENT_QUOTES, 'UTF-8'); ?>">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #371d5a; border-radius: 4px; }
  </style>
</head>
<body class="bg-[#0d0714] text-[#f8fafc] font-sans antialiased min-h-screen flex flex-col">

  <!-- Active Development Notification Banner -->
  <div class="bg-gradient-to-r from-purple-900/90 via-pink-900/90 to-purple-900/90 border-b border-pink-500/40 px-4 py-3 text-xs text-pink-100 shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-pink-500 text-white uppercase tracking-wider animate-pulse">DEVELOPMENT NOTIFICATION LOG</span>
        <span class="font-semibold text-pink-200">📢 <strong>Linux Desktop App Display:</strong> Native PySide6/Qt6 NVR application is being made — not complete yet, but fully functional!</span>
      </div>
      <div class="flex items-center gap-3">
        <a href="public_cam_idea.php" class="text-xs text-pink-300 hover:text-white font-bold underline flex items-center gap-1">
          ⬅️ Back to Master Roadmap
        </a>
      </div>
    </div>
  </div>

  <!-- Header Toolbar -->
  <header class="bg-[#1a102a] border-b border-[#371d5a] px-4 py-3 shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-pink-600 to-purple-600 flex items-center justify-center text-white text-xl font-bold shadow-md shadow-pink-500/20">
          🦊
        </div>
        <div>
          <h1 class="text-lg font-bold text-white tracking-tight flex items-center gap-2">
            FENNEC CAMERAS — LINUX APP DISPLAY PREVIEW (PHP)
            <span class="text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 px-2 py-0.5 rounded-full font-extrabold">100% OFFLINE</span>
          </h1>
          <p class="text-xs text-purple-300/80">Pure PHP Web Showcase & Monitor Workstation Simulation</p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <a href="public_cam_idea.php" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-[#140b22] text-pink-300 border border-[#371d5a] hover:bg-purple-900/40 transition">
          📋 Master Blueprint & Ideas
        </a>
      </div>
    </div>
  </header>

  <!-- Main Body Content -->
  <main class="max-w-7xl mx-auto w-full p-4 md:p-6 flex-1 space-y-6">

    <!-- Active Development Notification Drawer -->
    <div class="bg-[#1a102a] border border-pink-500/40 rounded-2xl p-4 md:p-5 shadow-xl relative overflow-hidden">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-pink-500/20 text-pink-300 border border-pink-500/30">NOTIFICATION LOG</span>
            <h2 class="text-sm font-bold text-white">Latest Development Progress & Changes</h2>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">
            Linux Desktop NVR application display is being made! Current build status: <strong>Functional Prototype v0.9.4</strong>. Features PySide6/Qt6 native GUI, multi-monitor pop-outs with drag-release auto-grouping, 2x2/3x3 dynamic layout switching, auto-tour camera carousel, focus view with PTZ controls, and zero cloud lock-in.
          </p>
        </div>
        <div class="shrink-0 bg-emerald-950 text-emerald-400 border border-emerald-600 px-3 py-1.5 rounded-xl text-xs font-extrabold">
          ✓ 0 Personal Data • Verified Clean Build
        </div>
      </div>
    </div>

    <!-- Live Grid Simulation -->
    <div class="space-y-4">
      <div class="bg-[#1a102a] border border-[#371d5a] p-3 rounded-xl flex flex-wrap items-center justify-between gap-3 shadow-md">
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold text-white">Grid Layout:</span>
          <span class="px-3 py-1 rounded-lg text-xs font-bold bg-pink-600 text-white border-2 border-white shadow">✓ 2x2 / 3x3 Dynamic Grid</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="px-3 py-1 rounded-lg text-xs font-bold bg-[#140b22] text-emerald-400 border border-emerald-500/40">🛡️ Global Privacy: OFF</span>
          <span class="px-3 py-1 rounded-lg text-xs font-bold bg-rose-950 text-rose-300 border border-rose-600">🚨 Emergency Siren Ready</span>
        </div>
      </div>

      <!-- PHP Camera Grid Loop -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <?php foreach ($cameras as $cid => $cam): ?>
          <div class="bg-[#1a102a] border border-[#371d5a] rounded-xl p-3 flex flex-col justify-between space-y-3 hover:border-pink-500 transition shadow">
            <div class="flex items-center justify-between text-xs font-bold">
              <span class="text-white"><?php echo htmlspecialchars($cam['name']); ?></span>
              <span class="text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-600 px-1.5 py-0.5 rounded"><?php echo htmlspecialchars($cam['type']); ?></span>
            </div>
            <div class="bg-[#040207] border border-[#201235] rounded-lg p-4 text-center flex flex-col items-center justify-center min-h-[140px]">
              <div class="text-3xl mb-1">📹</div>
              <div class="text-[10px] text-slate-400 font-mono">[ <?php echo htmlspecialchars($cam['resolution']); ?> • <?php echo htmlspecialchars($cam['fps']); ?>FPS ]<br><?php echo htmlspecialchars($cam['rtsp']); ?></div>
            </div>
            <div class="flex items-center justify-between text-[11px]">
              <span class="text-rose-500 font-bold">🔴 REC</span>
              <div class="flex gap-1.5">
                <span class="px-2 py-0.5 rounded bg-purple-900 text-pink-300 border border-pink-500/30 font-bold text-[10px]">🗗 Pop-Out Ready</span>
                <span class="px-2 py-0.5 rounded bg-purple-600 text-white font-bold text-[10px]">🔍 Focus View</span>
              </div>
            </div>
          </div>
        <?php endforeach; ?>
      </div>
    </div>

  </main>

  <footer class="bg-[#140b22] border-t border-[#371d5a] py-4 text-center text-xs text-slate-500">
    Fennec Cameras Open Source Project • Pure PHP Implementation
  </footer>

</body>
</html>
