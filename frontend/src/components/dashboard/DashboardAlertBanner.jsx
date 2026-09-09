import React, { useState, useEffect, useRef } from 'react';
import { AlertTriangle, ShieldAlert, Siren, Volume2, VolumeX, CheckCircle, X, Send, Monitor, Bell } from 'lucide-react';
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

  // Function to dispatch Native Computer Desktop Notification
  const triggerComputerNotification = (force = false) => {
    if (typeof window === 'undefined' || !('Notification' in window)) {
      alert('Browser does not support Native Computer Desktop Notifications.');
      return;
    }

    const dispatch = () => {
      const now = Date.now();
      // Throttle automatic desktop notifications to once every 12 seconds unless forced
      if (!force && now - lastNotificationTimeRef.current < 12000) return;
      lastNotificationTimeRef.current = now;

      const title = isCritical
        ? `🚨 CRITICAL MINE SUBSIDENCE HAZARD - Node ${targetNodeId}`
        : `⚠️ WARNING: Mine Strata Acceleration - Node ${targetNodeId}`;

      const options = {
        body: isCritical
          ? `[EMERGENCY ALERT] Node ${targetNodeId} in Panel C registered ${targetData.displacement || 12.8}mm displacement & ${targetData.tilt || 4.5}° tilt. High risk of immediate roof fall!`
          : `[WARNING ALERT] Elevated tilt rate (${targetData.tilt || 1.8}°) and displacement (${targetData.displacement || 3.5}mm) registered at Panel C.`,
        icon: '/favicon.svg',
        tag: `mineguard-${isCritical ? 'critical' : 'warning'}-${targetNodeId}`,
        requireInteraction: isCritical
      };

      try {
        const notif = new Notification(title, options);
        notif.onclick = () => {
          window.focus();
        };
        setDesktopNotified(true);
      } catch (err) {
        console.warn('Could not launch computer desktop notification:', err);
      }
    };

    if (Notification.permission === 'granted') {
      dispatch();
    } else if (Notification.permission !== 'denied') {
      Notification.requestPermission().then((perm) => {
        setPermissionStatus(perm);
        if (perm === 'granted') {
          dispatch();
        }
      });
    } else {
      alert('Desktop notification permission was denied in your browser settings. Please enable notifications for this site to receive computer alerts.');
    }
  };

  // Auto-send Computer Desktop Notification when alert state triggers/changes
  useEffect(() => {
    if (isCritical || isWarning) {
      setDismissed(false);
      setSmsSent(false);
      triggerComputerNotification(false);
    }
  }, [isCritical, isWarning, demoMode, maxRiskScore]);

  // Audio Siren Synthesis using Web Audio API
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

      // Dual-tone siren sweep
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

  // Clean up audio on unmount
  useEffect(() => {
    return () => {
      stopSiren();
    };
  }, []);

  // Handle SMS simulation
  const handleSendSMS = () => {
    setSmsSent(true);
    setTimeout(() => {
      alert(`[SMS GATEWAY DISPATCHED]\n\nEmergency SMS alert broadcasted to Mine Safety Director & DGMS Authority:\n"HAZARD WARNING: MineGuard AI detected risk score ${maxRiskScore} at Panel C. Subsidence alert active."`);
    }, 200);
  };

  // If no alert condition or user dismissed, don't show active alert banner
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

              <span className="text-xs font-mono text-slate-300 bg-black/40 px-2 py-0.5 rounded-md border border-white/10 flex items-center gap-1">
                <Bell className="w-3 h-3 text-amber-400" /> PC Notification Active
              </span>
            </div>

            <h3 className="text-base sm:text-lg font-black tracking-tight text-white flex items-center gap-2">
              {isCritical
                ? `CRITICAL SUBSIDENCE ALERT — Node ${targetNodeId} (${targetData.risk_score || maxRiskScore}/100 Risk Score)`
                : `WARNING ALERT — Strata Drift Acceleration at Node ${targetNodeId}`}
            </h3>

            <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
              {isCritical ? (
                <span>
                  High-velocity displacement (<strong>{targetData.displacement || 12.8}mm</strong>) & tilt (<strong>{targetData.tilt || 4.5}°</strong>) registered at <strong>Panel C High Stress Zone</strong>. High probability of immediate roof fall! Computer desktop alert dispatched.
                </span>
              ) : (
                <span>
                  Elevated tilt angle change (<strong>{targetData.tilt || 1.8}°</strong>) and displacement rate (<strong>{targetData.displacement || 3.5}mm</strong>) detected. Computer warning alert active.
                </span>
              )}
            </p>
          </div>
        </div>

        {/* Right Side: Interactive Action Buttons */}
        <div className="flex items-center gap-2 flex-wrap w-full md:w-auto justify-end flex-shrink-0 pt-2 md:pt-0 border-t md:border-t-0 border-white/10">
          <button
            onClick={() => triggerComputerNotification(true)}
            className="px-3 py-2 rounded-lg text-xs font-black transition-all flex items-center gap-1.5 cursor-pointer shadow-md bg-indigo-600 hover:bg-indigo-500 text-white border border-indigo-400"
            title="Push Native Computer Desktop Notification Alert"
          >
            <Monitor className="w-4 h-4 text-white animate-pulse" />
            <span>{desktopNotified ? 'Resend PC Alert' : 'Send PC Notification'}</span>
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
