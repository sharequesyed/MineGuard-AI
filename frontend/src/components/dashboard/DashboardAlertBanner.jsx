import React, { useState, useEffect, useRef } from 'react';
import { AlertTriangle, ShieldAlert, Siren, Volume2, VolumeX, CheckCircle, X, Send, Monitor, Bell, BellOff, Info } from 'lucide-react';
import { RiskBadge } from '../ui/RiskBadge';

export const DashboardAlertBanner = ({ nodesData = {}, maxRiskScore = 0, overallMineLevel = 'LOW', demoMode = 'NORMAL', onAcknowledgeAlert }) => {
  const [dismissed, setDismissed] = useState(false);
  const [sirenPlaying, setSirenPlaying] = useState(false);
  const [smsSent, setSmsSent] = useState(false);
  const [desktopNotified, setDesktopNotified] = useState(false);
  const [permissionStatus, setPermissionStatus] = useState(
    typeof window !== 'undefined' && 'Notification' in window ? Notification.permission : 'unsupported'
  );

  const audioCtxRef = useRef(null);
  const oscRef = useRef(null);
  const lastNotificationTimeRef = useRef(0);

  // Identify nodes that triggered Warning or Critical state
  const criticalNodes = Object.entries(nodesData).filter(([_, data]) => data.risk_level === 'CRITICAL');
  const warningNodes = Object.entries(nodesData).filter(([_, data]) => data.risk_level === 'HIGH' || data.risk_level === 'MEDIUM');

  const isCritical = overallMineLevel === 'CRITICAL' || criticalNodes.length > 0 || demoMode === 'SUBSIDENCE';
  const isWarning = !isCritical && (overallMineLevel === 'HIGH' || overallMineLevel === 'MEDIUM' || warningNodes.length > 0 || demoMode === 'WARNING');

  const activeNodeInfo = criticalNodes.length > 0
    ? criticalNodes[0]
    : warningNodes.length > 0
    ? warningNodes[0]
    : ['N5', nodesData['N5'] || {}];

  const targetNodeId = activeNodeInfo[0];
  const targetData = activeNodeInfo[1] || {};

  // Request browser Web Notification Permission explicitly
  const requestWebNotificationPermission = async () => {
    if (typeof window === 'undefined' || !('Notification' in window)) {
      alert('Browser does not support Web Desktop Notifications.');
      return 'unsupported';
    }

    try {
      const perm = await Notification.requestPermission();
      setPermissionStatus(perm);
      if (perm === 'granted') {
        // Dispatch test confirmation notification
        new Notification('MineGuard AI: Web Notifications Enabled', {
          body: 'You will receive immediate computer notifications containing full criticality details whenever Warning or Critical mine hazards occur.',
          icon: '/favicon.svg'
        });
      }
      return perm;
    } catch (e) {
      console.warn('Error requesting notification permission:', e);
      return Notification.permission;
    }
  };

  // Dispatch Native Web Desktop Notification with full criticality details
  const triggerComputerNotification = async (force = false) => {
    if (typeof window === 'undefined' || !('Notification' in window)) return;

    let currentPerm = Notification.permission;

    // Step 1: Take permission first if status is 'default'
    if (currentPerm === 'default') {
      currentPerm = await requestWebNotificationPermission();
    }

    if (currentPerm !== 'granted') {
      return;
    }

    const now = Date.now();
    // Throttle automatic background notifications to once every 10 seconds unless forced by button click
    if (!force && now - lastNotificationTimeRef.current < 10000) return;
    lastNotificationTimeRef.current = now;

    const riskScore = targetData.risk_score || maxRiskScore;
    const levelStr = isCritical ? 'CRITICAL EMERGENCY' : 'WARNING HAZARD';
    const locationStr = targetNodeId === 'N5' ? 'Panel C - High Stress Zone' : targetNodeId === 'N3' ? 'Panel B - Active Extraction' : 'Underground Mine Seam';

    const title = isCritical
      ? `🚨 [CRITICAL SUBSIDENCE HAZARD] Node ${targetNodeId}`
      : `⚠️ [WARNING STRAIN ALERT] Node ${targetNodeId}`;

    // Rich criticality details inside Web Notification body
    const bodyContent =
      `CRITICALITY INFO:\n` +
      `• Level: ${levelStr} (Risk Score: ${riskScore}/100)\n` +
      `• Location: ${locationStr}\n` +
      `• Displacement: ${targetData.displacement ?? 12.8}mm | Tilt: ${targetData.tilt ?? 4.5}°\n` +
      `• Crack Growth: ${targetData.crack_width ?? 5.2}mm | Load: +${targetData.load_change ?? 55.0}kN\n` +
      `• Required Action: ${isCritical ? 'IMMEDIATE UNDERGROUND EVACUATION REQUIRED!' : 'Increase strata monitoring & alert Panel C supervisor.'}`;

    const options = {
      body: bodyContent,
      icon: '/favicon.svg',
      tag: `mineguard-hazard-${isCritical ? 'critical' : 'warning'}-${targetNodeId}`,
      requireInteraction: isCritical, // Keeps critical notifications open on screen until clicked
      renotify: true
    };

    try {
      const notif = new Notification(title, options);
      notif.onclick = () => {
        window.focus();
      };
      setDesktopNotified(true);
    } catch (err) {
      console.warn('Failed to construct Web Notification:', err);
    }
  };

  // Auto-trigger permission & web notification when Warning or Critical hazard hits
  useEffect(() => {
    if (isCritical || isWarning) {
      setDismissed(false);
      setSmsSent(false);
      triggerComputerNotification(false);
    }
  }, [isCritical, isWarning, demoMode, maxRiskScore]);

  // Web Audio Siren Synthesis
  const toggleSiren = () => {
    if (sirenPlaying) {
      stopSiren();
    } else {
      startSiren();
    }
  };

  const startSiren = () => {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!audioCtxRef.current) {
        audioCtxRef.current = new AudioCtx();
      }
      const ctx = audioCtxRef.current;
      if (ctx.state === 'suspended') {
        ctx.resume();
      }

      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = isCritical ? 'sawtooth' : 'sine';
      osc.frequency.setValueAtTime(isCritical ? 880 : 587.33, ctx.currentTime);

      let toggle = false;
      const interval = setInterval(() => {
        if (!oscRef.current) {
          clearInterval(interval);
          return;
        }
        toggle = !toggle;
        osc.frequency.setValueAtTime(
          isCritical ? (toggle ? 950 : 650) : (toggle ? 620 : 520),
          ctx.currentTime
        );
      }, isCritical ? 250 : 500);

      gain.gain.setValueAtTime(0.15, ctx.currentTime);

      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      oscRef.current = osc;
      setSirenPlaying(true);
    } catch (e) {
      console.warn('Web Audio API requires user interaction:', e);
    }
  };

  const stopSiren = () => {
    if (oscRef.current) {
      try {
        oscRef.current.stop();
        oscRef.current.disconnect();
      } catch (e) {}
      oscRef.current = null;
    }
    setSirenPlaying(false);
  };

  useEffect(() => {
    return () => {
      stopSiren();
    };
  }, []);

  const handleSendSMS = () => {
    setSmsSent(true);
    setTimeout(() => {
      alert(`[SMS GATEWAY DISPATCHED]\n\nEmergency SMS alert broadcasted to Mine Safety Director & DGMS Authority:\n"HAZARD WARNING: MineGuard AI detected risk score ${maxRiskScore} at Panel C. Subsidence alert active."`);
    }, 200);
  };

  if ((!isCritical && !isWarning) || dismissed) {
    return null;
  }

  return (
    <div
      className={`rounded-xl p-4 mb-6 border shadow-lg transition-all duration-300 relative overflow-hidden ${
        isCritical
          ? 'bg-gradient-to-r from-rose-950/95 via-rose-900/95 to-red-950/95 border-rose-500 text-white shadow-rose-950/50 ring-2 ring-rose-500/50 animate-pulse'
          : 'bg-gradient-to-r from-amber-950/95 via-amber-900/95 to-orange-950/95 border-amber-500 text-white shadow-amber-950/50 ring-2 ring-amber-500/40'
      }`}
    >
      {/* Background Warning Glow Pulse */}
      <div className={`absolute -right-12 -top-12 w-48 h-48 rounded-full blur-3xl opacity-30 ${isCritical ? 'bg-rose-500' : 'bg-amber-500'}`} />

      <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        {/* Left Side: Alert Badge & Main Message */}
        <div className="flex items-start gap-3.5 flex-1">
          <div
            className={`p-3 rounded-xl flex-shrink-0 shadow-md ${
              isCritical
                ? 'bg-rose-600 text-white animate-bounce'
                : 'bg-amber-600 text-white animate-pulse'
            }`}
          >
            {isCritical ? <Siren className="w-7 h-7" /> : <AlertTriangle className="w-7 h-7" />}
          </div>

          <div className="space-y-1">
            <div className="flex items-center gap-2 flex-wrap">
              <span
                className={`px-2.5 py-0.5 rounded-full text-xs font-black uppercase tracking-wider ${
                  isCritical
                    ? 'bg-rose-500 text-white border border-rose-400'
                    : 'bg-amber-500 text-slate-950 border border-amber-300 font-extrabold'
                }`}
              >
                {isCritical ? '🚨 CRITICAL SUBSIDENCE HAZARD' : '⚠️ WARNING: ACCELERATED STRAIN DETECTED'}
              </span>

              <RiskBadge level={isCritical ? 'CRITICAL' : 'HIGH'} score={maxRiskScore} size="sm" />

              {permissionStatus === 'granted' ? (
                <span className="text-xs font-mono text-emerald-300 bg-emerald-950/80 px-2 py-0.5 rounded-md border border-emerald-500/30 flex items-center gap-1">
                  <Bell className="w-3 h-3 text-emerald-400" /> Web Notification Active
                </span>
              ) : (
                <button
                  onClick={requestWebNotificationPermission}
                  className="text-xs font-bold text-amber-200 bg-amber-950/90 hover:bg-amber-900 px-2.5 py-0.5 rounded-md border border-amber-400/50 flex items-center gap-1 cursor-pointer"
                >
                  <BellOff className="w-3 h-3 text-amber-300 animate-pulse" /> Grant Notification Permission
                </button>
              )}
            </div>

            <h3 className="text-base sm:text-lg font-black tracking-tight text-white flex items-center gap-2">
              {isCritical
                ? `CRITICAL SUBSIDENCE ALERT — Node ${targetNodeId} (${targetData.risk_score || maxRiskScore}/100 Risk Score)`
                : `WARNING ALERT — Strata Drift Acceleration at Node ${targetNodeId}`}
            </h3>

            {/* Criticality Info Summary Box */}
            <div className="bg-black/30 rounded-lg p-2.5 mt-1 border border-white/10 text-xs sm:text-sm text-slate-200 space-y-1">
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[11px] sm:text-xs">
                <div>Displacement: <strong className="text-amber-300">{targetData.displacement || 12.8}mm</strong></div>
                <div>Tilt Angle: <strong className="text-amber-300">{targetData.tilt || 4.5}°</strong></div>
                <div>Crack Width: <strong className="text-amber-300">{targetData.crack_width || 5.2}mm</strong></div>
                <div>Load Change: <strong className="text-amber-300">+{targetData.load_change || 55.0}kN</strong></div>
              </div>
              <p className="text-xs text-slate-300 border-t border-white/10 pt-1.5 flex items-center gap-1.5">
                <Info className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <span>
                  {isCritical
                    ? 'IMMEDIATE ACTION: Underground seam evacuation recommended. Web notification dispatched to computer desktop.'
                    : 'RECOMMENDED ACTION: Increase strata monitoring frequency & alert Panel C safety engineer.'}
                </span>
              </p>
            </div>
          </div>
        </div>

        {/* Right Side: Interactive Action Buttons */}
        <div className="flex items-center gap-2 flex-wrap w-full md:w-auto justify-end flex-shrink-0 pt-2 md:pt-0 border-t md:border-t-0 border-white/10">
          <button
            onClick={() => triggerComputerNotification(true)}
            className="px-3 py-2 rounded-lg text-xs font-black transition-all flex items-center gap-1.5 cursor-pointer shadow-md bg-indigo-600 hover:bg-indigo-500 text-white border border-indigo-400"
            title="Push Web Notification with Full Criticality Info to Computer Desktop"
          >
            <Monitor className="w-4 h-4 text-white animate-pulse" />
            <span>{desktopNotified ? 'Resend Web Notif' : 'Send Web Notif'}</span>
          </button>

          <button
            onClick={toggleSiren}
            className={`px-3 py-2 rounded-lg text-xs font-black transition-all flex items-center gap-1.5 cursor-pointer shadow-md ${
              sirenPlaying
                ? 'bg-rose-500 text-white ring-2 ring-white animate-pulse'
                : 'bg-white/15 hover:bg-white/25 text-white border border-white/20'
            }`}
            title="Toggle Emergency Underground Audio Siren"
          >
            {sirenPlaying ? <Volume2 className="w-4 h-4 text-white animate-bounce" /> : <VolumeX className="w-4 h-4 text-white" />}
            <span>{sirenPlaying ? 'Mute Siren' : 'Audio Alarm'}</span>
          </button>

          <button
            onClick={handleSendSMS}
            disabled={smsSent}
            className={`px-3 py-2 rounded-lg text-xs font-black transition-all flex items-center gap-1.5 cursor-pointer shadow-md ${
              smsSent
                ? 'bg-emerald-600 text-white opacity-90'
                : isCritical
                ? 'bg-rose-600 hover:bg-rose-500 text-white'
                : 'bg-amber-600 hover:bg-amber-500 text-white'
            }`}
          >
            {smsSent ? <CheckCircle className="w-4 h-4" /> : <Send className="w-4 h-4" />}
            <span>{smsSent ? 'SMS Sent' : 'Dispatch SMS'}</span>
          </button>

          <button
            onClick={() => {
              setDismissed(true);
              stopSiren();
              if (onAcknowledgeAlert) onAcknowledgeAlert();
            }}
            className="p-2 rounded-lg bg-white/10 hover:bg-white/20 text-slate-300 hover:text-white transition-colors cursor-pointer"
            title="Acknowledge & Dismiss Dashboard Alert"
          >
            <X className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
};
