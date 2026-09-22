<?php
// CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE
// Fennec Cameras - Server Rack & NVR Hub Administration Console (Headless Server Admin)
header('Content-Type: text/html; charset=utf-8');

/**
 * Conflict-Free Auto-Port Relocation Protocol
 * Detects occupied default web ports (80, 8080, 8443) and auto-binds to 8081.
 */
function resolve_server_port($desired_port = 8080, $fallback_port = 8081) {
    $connection = @fsockopen('127.0.0.1', $desired_port, $errno, $errstr, 0.5);
    if (is_resource($connection)) {
        fclose($connection);
        return $fallback_port; // Desired port occupied by Home Assistant / Plex, relocate to 8081
    }
    return $desired_port;
}

$boundPort = resolve_server_port();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Headless Server NVR Admin Console - Fennec Cameras</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6 font-sans">
  <!-- CONCEPT CODE BANNER -->
  <div class="bg-indigo-950 border border-indigo-500/50 rounded-xl p-4 mb-6 text-center text-xs font-mono font-bold text-indigo-300 uppercase tracking-widest">
    ⚠️ CONCEPT CODE - UNTESTED ROADMAP PROTOTYPE — HEADLESS SERVER ADMIN CONSOLE
  </div>

  <div class="max-w-7xl mx-auto space-y-6">
    <header class="flex items-center justify-between border-b border-slate-800 pb-4">
      <div>
        <h1 class="text-2xl font-extrabold text-white flex items-center gap-2">
          <span>🖥️ Headless Server NVR Console</span>
        </h1>
        <p class="text-xs text-slate-400 mt-1">Bound to HTTP Port: <span class="text-indigo-400 font-bold"><?php echo $boundPort; ?></span> (Auto-Relocated)</p>
      </div>
      <div class="flex items-center gap-3">
        <span class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">LAN Core Active</span>
      </div>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-3">
        <h3 class="font-bold text-sm text-slate-200">Live Multi-Channel Grid & Timeline Scrubbing</h3>
        <div class="aspect-video bg-black rounded-lg flex items-center justify-center border border-slate-800">
          <p class="text-xs text-slate-500 italic">[ WebRTC Stream Grid Placeholder ]</p>
        </div>
      </div>

      <div class="bg-slate-900 border border-slate-800 rounded-xl p-4 space-y-4">
        <h3 class="font-bold text-sm text-slate-200">Tiered NAS Storage & Storage Node Qualifications</h3>
        <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 space-y-2 text-xs">
          <p class="text-slate-300 font-semibold">TrueNAS SMB/NFS Target: <span class="text-indigo-400">Connected</span></p>
          <p class="text-slate-400">Ring Buffer: 5-15 min rolling memory quota</p>
          <p class="text-rose-400 font-medium">Auto-Denial Engine: Reject drives &lt;16GB</p>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
