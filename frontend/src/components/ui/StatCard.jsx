import React from 'react';
import { GlassCard } from './GlassCard';

export const StatCard = ({ title, value, unit = '', subtitle, icon: Icon, trend, trendValue, statusColor = 'text-slate-900 dark:text-white' }) => {
  return (
    <GlassCard hoverEffect className="flex flex-col justify-between">
      <div className="flex items-center justify-between">
        <span className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400">
          {title}
        </span>
        {Icon && (
          <div className="p-2 rounded-lg bg-slate-200/80 dark:bg-slate-800 text-slate-800 dark:text-slate-200">
            <Icon className="w-5 h-5" />
          </div>
        )}
      </div>

      <div className="my-2">
        <div className="flex items-baseline gap-1">
          <span className={`text-2xl lg:text-3xl font-black tracking-tight ${statusColor}`}>
            {value}
          </span>
          {unit && <span className="text-xs font-bold text-slate-500 dark:text-slate-400">{unit}</span>}
        </div>

        {subtitle && (
          <p className="text-xs font-semibold text-slate-600 dark:text-slate-400 mt-1">{subtitle}</p>
        )}
      </div>

      {trend && (
        <div className="flex items-center gap-1.5 text-xs font-bold pt-2 border-t border-slate-300/60 dark:border-slate-800/60">
          <span className={trend === 'up' ? 'text-rose-600' : trend === 'down' ? 'text-emerald-600' : 'text-slate-600'}>
            {trend === 'up' ? '↑' : trend === 'down' ? '↓' : '→'} {trendValue}
          </span>
          <span className="text-slate-500">vs last hour</span>
        </div>
      )}
    </GlassCard>
  );
};
