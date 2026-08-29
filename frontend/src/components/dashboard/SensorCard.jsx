import React from 'react';
import { GlassCard } from '../ui/GlassCard';
import { RiskBadge } from '../ui/RiskBadge';
import { Compass, MoveVertical, Split, Activity, Scale, Battery, Thermometer, ChevronRight } from 'lucide-react';
import { getRiskLevel } from '../../utils/constants';

export const SensorCard = ({ nodeConfig, sensorData = {}, onSelectNode }) => {
  const tilt = sensorData.tilt ?? 0.8;
  const displacement = sensorData.displacement ?? 1.2;
  const crackWidth = sensorData.crack_width ?? 0.2;
  const vibration = sensorData.vibration ?? 0.08;
  const loadChange = sensorData.load_change ?? 2.5;
  const battery = sensorData.battery ?? 95;
  const temp = sensorData.temperature ?? 28.4;

  const score = sensorData.risk_score ?? 15;
  const level = sensorData.risk_level || getRiskLevel(score);

  const metrics = [
    { label: 'Tilt', val: `${tilt}°`, icon: Compass, alert: tilt > 3.0 },
    { label: 'Displacement', val: `${displacement} mm`, icon: MoveVertical, alert: displacement > 8.0 },
    { label: 'Crack Width', val: `${crackWidth} mm`, icon: Split, alert: crackWidth > 3.0 },
    { label: 'Vibration', val: `${vibration} g`, icon: Activity, alert: vibration > 0.5 },
    { label: 'Load Change', val: `${loadChange} kg`, icon: Scale, alert: loadChange > 30.0 },
    { label: 'Temp / Hum', val: `${temp}°C`, icon: Thermometer, alert: false },
  ];

  return (
    <GlassCard hoverEffect className="flex flex-col justify-between group">
      <div>
        {/* Node Header */}
        <div className="flex items-start justify-between gap-2 mb-3">
          <div>
            <div className="flex items-center gap-2">
              <span className="font-black text-sm text-slate-900 dark:text-white">
                {nodeConfig.id}
              </span>
              <span className="text-xs text-slate-700 dark:text-slate-300 font-bold truncate max-w-[140px]">
                {nodeConfig.name}
              </span>
            </div>
            <p className="text-[11px] text-slate-600 dark:text-slate-400 font-mono font-medium mt-0.5">
              {nodeConfig.depth} | {nodeConfig.location}
            </p>
          </div>
          <RiskBadge level={level} score={score} size="sm" />
        </div>

        {/* Sensor Data Grid */}
        <div className="grid grid-cols-2 gap-2 my-3">
          {metrics.map((m, idx) => {
            const Icon = m.icon;
            return (
              <div
                key={idx}
                className={`p-2 rounded-lg border text-xs flex items-center gap-2 ${
                  m.alert
                    ? 'bg-rose-500/15 border-rose-400 text-rose-900 dark:text-rose-300 font-bold'
                    : 'bg-slate-100 dark:bg-slate-800/80 border-slate-200 dark:border-slate-700 text-slate-900 dark:text-slate-100'
                }`}
              >
                <Icon className={`w-3.5 h-3.5 ${m.alert ? 'text-rose-600 animate-pulse' : 'text-slate-500 dark:text-slate-400'}`} />
                <div>
                  <div className="text-[10px] text-slate-600 dark:text-slate-400 font-bold leading-none">{m.label}</div>
                  <div className="font-black text-xs mt-0.5 text-slate-900 dark:text-white">{m.val}</div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Footer Info & Action */}
      <div className="pt-2 border-t border-slate-300/60 dark:border-slate-800/60 flex items-center justify-between text-[11px] text-slate-600 dark:text-slate-400 font-bold">
        <div className="flex items-center gap-1">
          <Battery className={`w-3.5 h-3.5 ${battery < 20 ? 'text-rose-600' : 'text-emerald-600'}`} />
          <span>{battery}%</span>
        </div>

        <button
          onClick={() => onSelectNode && onSelectNode(nodeConfig.id)}
          className="flex items-center gap-1 text-indigo-700 dark:text-indigo-400 font-extrabold hover:underline cursor-pointer"
        >
          <span>Node Details</span>
          <ChevronRight className="w-3.5 h-3.5 group-hover:translate-x-0.5 transition-transform" />
        </button>
      </div>
    </GlassCard>
  );
};
