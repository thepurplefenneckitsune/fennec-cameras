<?php
// CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
// Fennec Cameras - Live Web NVR Preview & System Status Display
header('Content-Type: text/html; charset=utf-8');

define('SIRV_FAVICON_URL', 'https://thepurplefox.sirv.com/kistune%20cam/purple_kitsune_logo2.jpg?cx=67&cy=74&cw=890&ch=890');

$protocol = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') ? 'https' : 'http';
$host = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : 'localhost';
$uri = isset($_SERVER['REQUEST_URI']) ? $_SERVER['REQUEST_URI'] : '';
$canonicalUrl = $protocol . '://' . $host . $uri;
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fennec Cameras - Live NVR Web Preview & System Status</title>
  <meta name="description" content="Live interactive web preview display for Fennec Cameras Linux NVR Application. Feature multi-monitor pop-outs, camera grouping, auto-tour carousel, and edge AI.">
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

  <!-- Project Notifications Header Banner -->
  <div class="bg-gradient-to-r from-purple-900/90 via-pink-900/90 to-purple-900/90 border-b border-pink-500/40 px-4 py-3 text-xs text-pink-100 shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-pink-500 text-white uppercase tracking-wider animate-pulse">DEVELOPMENT UPDATE NOTIFICATION</span>
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
            FENNEC CAMERAS — NVR WEB PREVIEW
            <span class="text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 px-2 py-0.5 rounded-full font-extrabold">100% OFFLINE</span>
          </h1>
          <p class="text-xs text-purple-300/80">Interactive Web Showcase & Monitor Workstation Simulation</p>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <a href="public_cam_idea.php" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-[#140b22] text-pink-300 border border-[#371d5a] hover:bg-purple-900/40 transition">
          📋 Master Blueprint & Ideas
        </a>
        <a href="preview/camera_linux_app_preview.html" target="_blank" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-gradient-to-r from-pink-600 to-purple-600 text-white shadow-md hover:opacity-90 transition">
          🖥️ Open Fullscreen Display Preview ↗
        </a>
      </div>
    </div>
  </header>

  <!-- Content Container -->
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
            Linux Desktop NVR application display is being built! Current build status: <strong>Functional Prototype v0.9.4</strong>. Features PySide6/Qt6 native GUI, multi-monitor pop-outs with drag-release auto-grouping, 2x2/3x3 dynamic layout switching, auto-tour camera carousel, focus view with PTZ controls, and zero cloud lock-in.
          </p>
        </div>
        <div class="shrink-0 bg-emerald-950 text-emerald-400 border border-emerald-600 px-3 py-1.5 rounded-xl text-xs font-extrabold">
          ✓ 0 Personal Data • Verified Clean Build
        </div>
      </div>
    </div>

    <!-- Embedded Live Web Preview Display Container -->
    <div class="bg-[#140b22] border border-[#371d5a] rounded-2xl p-2 md:p-4 shadow-2xl space-y-3">
      <div class="flex items-center justify-between px-2">
        <div class="text-xs font-bold text-purple-300 flex items-center gap-2">
          <span>🖥️ Live Display Simulation</span>
          <span class="text-[10px] bg-purple-900 text-pink-300 px-2 py-0.5 rounded-full">Interactive Controls Enabled</span>
        </div>
        <a href="preview/camera_linux_app_preview.html" target="_blank" class="text-xs text-pink-400 font-bold hover:underline">
          Launch Standalone Window ↗
        </a>
      </div>
      
      <!-- Preview Frame -->
      <iframe src="preview/camera_linux_app_preview.html" class="w-full h-[620px] rounded-xl border border-[#371d5a] bg-[#0d0714]" loading="lazy"></iframe>
    </div>

  </main>

  <footer class="bg-[#140b22] border-t border-[#371d5a] py-4 text-center text-xs text-slate-500">
    Fennec Cameras Open Source Project • 100% Offline & Zero Cloud Subscription NVR
  </footer>

</body>
</html>
