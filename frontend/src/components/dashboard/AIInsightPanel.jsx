import React from 'react';
import { GlassCard } from '../ui/GlassCard';
import { RiskGauge } from './RiskGauge';
import { RiskBadge } from '../ui/RiskBadge';
import { Brain, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { getRiskLevel } from '../../utils/constants';

export const AIInsightPanel = ({ riskScore = 18, riskLevel, factors = [] }) => {
  const level = riskLevel || getRiskLevel(riskScore);

  const defaultFactors = factors.length > 0 ? factors : [
    { factor: 'Tilt Angle Rate of Change', impact: riskScore > 50 ? 'High' : 'Low', weight: '34%' },
    { factor: 'Roof Displacement Velocity', impact: riskScore > 50 ? 'Critical' : 'Moderate', weight: '28%' },
    { factor: 'Crack Opening Width', impact: riskScore > 50 ? 'High' : 'Low', weight: '22%' },
    { factor: 'Ground Peak Acceleration', impact: 'Moderate', weight: '16%' }
  ];

  return (
    <GlassCard className="w-full flex flex-col justify-between">
      <div>
        <div className="flex items-center justify-between border-b border-slate-300/60 dark:border-slate-800/60 pb-3 mb-4">
          <div className="flex items-center gap-2">
            <div className="p-2 rounded-lg bg-indigo-100 text-indigo-700 dark:bg-indigo-950 dark:text-indigo-400">
              <Brain className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-black text-base text-slate-900 dark:text-white">
                AI Subsidence Predictor
              </h3>
              <p className="text-xs font-semibold text-slate-600 dark:text-slate-400">
                Random Forest & Gradient Boosting Inference Engine
              </p>
            </div>
          </div>
          <RiskBadge level={level} score={riskScore} size="lg" />
        </div>

        {/* Visual Risk Gauge */}
        <RiskGauge score={riskScore} level={level} />

        {/* Dynamic Prediction Summary Text */}
        <div className={`p-3 rounded-lg border text-xs my-4 ${
          level === 'CRITICAL' || level === 'HIGH'
            ? 'bg-rose-100 border-rose-400 text-rose-950 dark:bg-rose-950/60 dark:text-rose-200'
            : level === 'MEDIUM'
            ? 'bg-amber-100 border-amber-400 text-amber-950 dark:bg-amber-950/60 dark:text-amber-200'
            : 'bg-emerald-100 border-emerald-400 text-emerald-950 dark:bg-emerald-950/60 dark:text-emerald-200'
        }`}>
          <div className="flex items-start gap-2">
            {level === 'LOW' ? (
              <CheckCircle2 className="w-4 h-4 text-emerald-700 dark:text-emerald-400 flex-shrink-0 mt-0.5" />
            ) : (
              <AlertTriangle className="w-4 h-4 text-rose-700 dark:text-rose-400 flex-shrink-0 mt-0.5" />
            )}
            <div>
              <span className="font-extrabold text-xs">
                {level === 'LOW' && 'Stable Underground Conditions.'}
                {level === 'MEDIUM' && 'Caution: Elevated Strata Deformation Detected.'}
                {level === 'HIGH' && 'DANGER: Accelerating Roof Tilt & Displacement!'}
                {level === 'CRITICAL' && 'CRITICAL SUBSIDENCE RISK: Immediate Evacuation Advisory!'}
              </span>
              <p className="mt-1 text-[11px] font-semibold opacity-95">
                {level === 'LOW'
                  ? 'Sensor telemetry across all panels remains within normal geotechnical tolerance limits.'
                  : 'Multi-sensor correlation indicates structural roof deformation in Panel C. High rate of change detected.'}
              </p>
            </div>
          </div>
        </div>

        {/* Key Contributing Factors Breakdown */}
        <div className="mt-3">
          <span className="text-xs font-black uppercase tracking-wider text-slate-700 dark:text-slate-300 mb-2 block">
            Top Risk Contributing Factors:
          </span>
          <div className="space-y-2">
            {defaultFactors.map((f, idx) => (
              <div key={idx} className="flex items-center justify-between text-xs bg-slate-100 dark:bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700">
                <span className="text-slate-900 dark:text-slate-100 font-bold">{f.factor}</span>
                <div className="flex items-center gap-2">
                  <span className={`font-black ${
                    f.impact === 'Critical' ? 'text-rose-600' : f.impact === 'High' ? 'text-orange-600' : 'text-slate-600 dark:text-slate-400'
                  }`}>
                    {f.impact}
                  </span>
                  <span className="text-[10px] text-slate-500 dark:text-slate-400 font-mono font-bold">({f.weight})</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Model Specs */}
      <div className="mt-4 pt-3 border-t border-slate-300/60 dark:border-slate-800/60 flex items-center justify-between text-[11px] text-slate-600 dark:text-slate-400 font-bold">
        <span>Model: <strong className="text-slate-900 dark:text-white">RandomForestRegressor v1.2</strong></span>
        <span>Confidence: <strong className="text-slate-900 dark:text-white">94.2%</strong></span>
      </div>
    </GlassCard>
  );
};
