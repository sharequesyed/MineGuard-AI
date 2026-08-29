import React from 'react';
import { getRiskLevel, getRiskColor } from '../../utils/constants';

export const RiskGauge = ({ score = 15, level }) => {
  const currentLevel = level || getRiskLevel(score);
  const color = getRiskColor(currentLevel);

  // Gauge calculation for semi-circle (180 degrees)
  const radius = 70;
  const strokeWidth = 14;
  const circumference = Math.PI * radius; // Half circle
  const scorePercent = Math.min(Math.max(score, 0), 100) / 100;
  const strokeDashoffset = circumference - scorePercent * circumference;

  // Needle angle (-90deg to +90deg)
  const needleAngle = -90 + scorePercent * 180;

  return (
    <div className="flex flex-col items-center justify-center relative py-2">
      <svg className="w-48 h-28 overflow-visible" viewBox="0 0 180 100">
        <defs>
          <linearGradient id="gaugeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stopColor="#10B981" />
            <stop offset="33%" stopColor="#F59E0B" />
            <stop offset="66%" stopColor="#F97316" />
            <stop offset="100%" stopColor="#EF4444" />
          </linearGradient>
        </defs>

        {/* Background Track */}
        <path
          d="M 20 90 A 70 70 0 0 1 160 90"
          fill="none"
          stroke="currentColor"
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          className="text-slate-300 dark:text-slate-800"
        />

        {/* Active Arc */}
        <path
          d="M 20 90 A 70 70 0 0 1 160 90"
          fill="none"
          stroke="url(#gaugeGradient)"
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          className="transition-all duration-700 ease-out"
        />

        {/* Center Needle */}
        <g transform={`translate(90, 90) rotate(${needleAngle})`} className="transition-transform duration-700 ease-out">
          <line x1="0" y1="0" x2="0" y2="-62" stroke="#0F172A" strokeWidth="3.5" className="dark:stroke-slate-100" strokeLinecap="round" />
          <circle cx="0" cy="0" r="6" fill="#0F172A" className="dark:fill-slate-100" />
        </g>
      </svg>

      {/* Numerical Output */}
      <div className="text-center -mt-4">
        <div className="text-3xl font-black tracking-tight" style={{ color }}>
          {score}
          <span className="text-xs font-extrabold text-slate-500 dark:text-slate-400 ml-1">/ 100</span>
        </div>
        <div className="text-xs font-black uppercase tracking-widest text-slate-700 dark:text-slate-300 mt-0.5">
          SUBSIDENCE RISK
        </div>
      </div>
    </div>
  );
};
