import React from 'react';
import { X, Battery, Wifi, ShieldAlert, Activity, Compass, MoveVertical, Split, Scale } from 'lucide-react';
import { RiskBadge } from '../ui/RiskBadge';
import { SENSOR_NODES_CONFIG, getRiskLevel } from '../../utils/constants';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';

export const NodeDetailModal = ({ nodeId, nodeData = {}, onClose }) => {
  if (!nodeId) return null;

  const config = SENSOR_NODES_CONFIG.find((n) => n.id === nodeId) || {
    id: nodeId,
    name: `Node ${nodeId}`,
    location: 'Underground Seam Panel',
    depth: '210m'
  };

  const score = nodeData.risk_score ?? 15;
  const level = nodeData.risk_level || getRiskLevel(score);

  // Generate sample trend data for this node
  const trendData = [
    { time: '10:00', disp: nodeData.displacement ? nodeData.displacement * 0.4 : 1.2, tilt: 0.5 },
    { time: '10:05', disp: nodeData.displacement ? nodeData.displacement * 0.6 : 1.5, tilt: 0.7 },
    { time: '10:10', disp: nodeData.displacement ? nodeData.displacement * 0.8 : 2.1, tilt: 1.1 },
    { time: '10:15', disp: nodeData.displacement ?? 2.8, tilt: nodeData.tilt ?? 1.4 },
  ];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs">
      <div className="glass-panel w-full max-w-2xl rounded-2xl p-6 shadow-2xl relative animate-in fade-in zoom-in-95 duration-200 border-indigo-500/30">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-500 hover:text-slate-900 dark:hover:text-white transition cursor-pointer"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="flex items-center gap-3 mb-4">
          <div className="w-12 h-12 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-extrabold text-lg shadow-md">
            {config.id}
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-xl font-bold text-slate-900 dark:text-white">{config.name}</h2>
              <RiskBadge level={level} score={score} size="md" />
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              Location: {config.location} | Depth: {config.depth} | Telemetry: <strong>LoRa 868MHz</strong>
            </p>
          </div>
        </div>

        {/* Sensor Metrics Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 my-4">
          <div className="p-3 rounded-xl bg-slate-100/70 dark:bg-slate-800/70 border border-slate-200/60 dark:border-slate-800">
            <div className="flex items-center gap-1.5 text-xs text-slate-500 mb-1">
              <Compass className="w-4 h-4 text-indigo-500" /> Tilt Angle
            </div>
            <div className="text-lg font-extrabold text-slate-900 dark:text-white">{nodeData.tilt ?? 0.8}°</div>
          </div>

          <div className="p-3 rounded-xl bg-slate-100/70 dark:bg-slate-800/70 border border-slate-200/60 dark:border-slate-800">
            <div className="flex items-center gap-1.5 text-xs text-slate-500 mb-1">
              <MoveVertical className="w-4 h-4 text-emerald-500" /> Roof Disp.
            </div>
            <div className="text-lg font-extrabold text-slate-900 dark:text-white">{nodeData.displacement ?? 1.2} mm</div>
          </div>

          <div className="p-3 rounded-xl bg-slate-100/70 dark:bg-slate-800/70 border border-slate-200/60 dark:border-slate-800">
            <div className="flex items-center gap-1.5 text-xs text-slate-500 mb-1">
              <Split className="w-4 h-4 text-amber-500" /> Crack Width
            </div>
            <div className="text-lg font-extrabold text-slate-900 dark:text-white">{nodeData.crack_width ?? 0.2} mm</div>
          </div>

          <div className="p-3 rounded-xl bg-slate-100/70 dark:bg-slate-800/70 border border-slate-200/60 dark:border-slate-800">
            <div className="flex items-center gap-1.5 text-xs text-slate-500 mb-1">
              <Activity className="w-4 h-4 text-rose-500" /> Vibration
            </div>
            <div className="text-lg font-extrabold text-slate-900 dark:text-white">{nodeData.vibration ?? 0.08} g</div>
          </div>
        </div>

        {/* Node Historical Displacement Chart */}
        <div className="mt-4">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">
            Displacement Trend ({config.id})
          </h4>
          <div className="h-40 w-full bg-slate-50 dark:bg-slate-900/50 p-2 rounded-xl border border-slate-200 dark:border-slate-800">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={trendData}>
                <XAxis dataKey="time" stroke="#94A3B8" fontSize={10} />
                <YAxis stroke="#94A3B8" fontSize={10} />
                <Tooltip />
                <Line type="monotone" dataKey="disp" stroke="#6366F1" strokeWidth={2} name="Displacement (mm)" />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Modal Footer */}
        <div className="mt-5 pt-3 border-t border-slate-200/60 dark:border-slate-800/60 flex items-center justify-between text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <Battery className="w-4 h-4 text-emerald-500" />
            <span>Battery: <strong>{nodeData.battery ?? 94}% (3.82V)</strong></span>
          </div>
          <button
            onClick={onClose}
            className="px-4 py-1.5 bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 rounded-lg font-semibold hover:bg-slate-300 dark:hover:bg-slate-700 transition cursor-pointer"
          >
            Close Panel
          </button>
        </div>
      </div>
    </div>
  );
};
