import React from 'react';
import { GlassCard } from '../ui/GlassCard';
import { RiskBadge } from '../ui/RiskBadge';
import { Bell, ShieldAlert, CheckCircle, Clock } from 'lucide-react';

export const AlertPanel = ({ alerts = [], onAcknowledge }) => {
  return (
    <GlassCard className="w-full flex flex-col justify-between">
      <div>
        <div className="flex items-center justify-between border-b border-slate-200/60 dark:border-slate-800/60 pb-3 mb-3">
          <div className="flex items-center gap-2">
            <div className="p-2 rounded-lg bg-rose-500/10 text-rose-600 dark:text-rose-400">
              <Bell className="w-5 h-5 animate-bounce" />
            </div>
            <div>
              <h3 className="font-extrabold text-base text-slate-900 dark:text-white">
                Early Warning Alert Feed
              </h3>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                Automated hazard notifications & trigger events
              </p>
            </div>
          </div>
          <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/10 text-rose-600 border border-rose-500/20">
            {alerts.length} Active
          </span>
        </div>

        {/* Alert List Scrollable Container */}
        <div className="space-y-2.5 max-h-[300px] overflow-y-auto pr-1">
          {alerts.length === 0 ? (
            <div className="py-8 text-center text-slate-400 dark:text-slate-500 text-xs">
              <CheckCircle className="w-8 h-8 mx-auto mb-2 text-emerald-500 opacity-60" />
              <span>No active early warnings. All underground nodes operating normally.</span>
            </div>
          ) : (
            alerts.map((alert) => (
              <div
                key={alert.id}
                className={`p-3 rounded-lg border text-xs transition-all ${
                  alert.level === 'CRITICAL'
                    ? 'bg-rose-500/10 border-rose-500/30 text-slate-900 dark:text-white'
                    : alert.level === 'HIGH'
                    ? 'bg-orange-500/10 border-orange-500/30 text-slate-900 dark:text-white'
                    : 'bg-amber-500/10 border-amber-500/30 text-slate-900 dark:text-white'
                }`}
              >
                <div className="flex items-start justify-between gap-2 mb-1">
                  <div className="flex items-center gap-1.5 font-bold">
                    <ShieldAlert className="w-4 h-4 text-rose-500 flex-shrink-0" />
                    <span>Node {alert.node_id} — {alert.reason}</span>
                  </div>
                  <RiskBadge level={alert.level} score={alert.score} size="sm" />
                </div>

                <p className="text-[11px] text-slate-600 dark:text-slate-300 mb-2">
                  {alert.details || 'Accelerated roof displacement rate detected by LoRa telemetry node.'}
                </p>

                <div className="flex items-center justify-between text-[10px] text-slate-400 border-t border-slate-200/40 dark:border-slate-800/40 pt-1.5">
                  <span className="flex items-center gap-1 font-mono">
                    <Clock className="w-3 h-3" /> {alert.timestamp}
                  </span>
                  <button
                    onClick={() => onAcknowledge && onAcknowledge(alert.id)}
                    className="hover:underline text-indigo-600 dark:text-indigo-400 font-semibold cursor-pointer"
                  >
                    Acknowledge Alert
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      <div className="pt-3 mt-3 border-t border-slate-200/60 dark:border-slate-800/60 flex items-center justify-between text-[11px] text-slate-400">
        <span>Hardware Buzzer: <strong className="text-emerald-500">READY</strong></span>
        <span>SMS Gateway: <strong className="text-indigo-400">SIMULATED</strong></span>
      </div>
    </GlassCard>
  );
};
