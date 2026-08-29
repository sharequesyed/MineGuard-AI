import React from 'react';
import { getRiskLevel } from '../../utils/constants';

export const RiskBadge = ({ level, score, size = 'md' }) => {
  const finalLevel = level || (score !== undefined ? getRiskLevel(score) : 'LOW');

  const colorMap = {
    LOW: 'bg-emerald-500/15 text-emerald-700 dark:text-emerald-400 border-emerald-500/30',
    MEDIUM: 'bg-amber-500/15 text-amber-700 dark:text-amber-400 border-amber-500/30',
    HIGH: 'bg-orange-500/15 text-orange-700 dark:text-orange-400 border-orange-500/30',
    CRITICAL: 'bg-rose-500/20 text-rose-700 dark:text-rose-400 border-rose-500/40 animate-pulse',
  };

  const dotMap = {
    LOW: 'bg-emerald-500',
    MEDIUM: 'bg-amber-500',
    HIGH: 'bg-orange-500',
    CRITICAL: 'bg-rose-500 animate-ping',
  };

  const sizeMap = {
    sm: 'text-xs px-2 py-0.5 gap-1',
    md: 'text-xs font-semibold px-2.5 py-1 gap-1.5',
    lg: 'text-sm font-bold px-3.5 py-1.5 gap-2',
  };

  return (
    <span
      className={`inline-flex items-center rounded-full border backdrop-blur-sm shadow-xs ${colorMap[finalLevel] || colorMap.LOW} ${sizeMap[size]}`}
    >
      <span className={`w-2 h-2 rounded-full ${dotMap[finalLevel] || dotMap.LOW}`} />
      <span>{finalLevel}</span>
      {score !== undefined && <span className="opacity-80">({score})</span>}
    </span>
  );
};
