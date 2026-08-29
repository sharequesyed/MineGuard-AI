import React, { useState } from 'react';
import { GlassCard } from '../ui/GlassCard';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, Legend } from 'recharts';

export const SensorCharts = ({ historyData = [] }) => {
  const [metric, setMetric] = useState('displacement');

  const metricConfigs = {
    displacement: { label: 'Displacement (mm)', color: '#6366F1', key: 'displacement', unit: 'mm' },
    tilt: { label: 'Tilt (°)', color: '#F59E0B', key: 'tilt', unit: '°' },
    vibration: { label: 'Vibration (g)', color: '#EC4899', key: 'vibration', unit: 'g' },
    crack_width: { label: 'Crack Width (mm)', color: '#F97316', key: 'crack_width', unit: 'mm' },
    risk_score: { label: 'AI Risk Score (0-100)', color: '#EF4444', key: 'risk_score', unit: 'pts' },
  };

  const currentCfg = metricConfigs[metric];

  return (
    <GlassCard className="w-full">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 mb-4">
        <div>
          <h3 className="font-extrabold text-base text-slate-900 dark:text-white">
            Real-Time Geotechnical Telemetry Trends
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Multi-node subsidence progression over time
          </p>
        </div>

        {/* Metric Selector Tabs */}
        <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-800 p-1 rounded-lg text-xs overflow-x-auto max-w-full">
          {Object.keys(metricConfigs).map((key) => (
            <button
              key={key}
              onClick={() => setMetric(key)}
              className={`px-2.5 py-1 rounded-md font-semibold transition cursor-pointer whitespace-nowrap ${
                metric === key
                  ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              {key === 'displacement' ? 'Displacement' : key === 'tilt' ? 'Tilt' : key === 'vibration' ? 'Vibration' : key === 'crack_width' ? 'Crack Width' : 'Risk Score'}
            </button>
          ))}
        </div>
      </div>

      {/* Recharts Line Chart */}
      <div className="h-72 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={historyData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" opacity={0.5} />
            <XAxis dataKey="time" stroke="#94A3B8" fontSize={11} />
            <YAxis stroke="#94A3B8" fontSize={11} />
            <Tooltip
              contentStyle={{
                backgroundColor: 'rgba(15, 23, 42, 0.9)',
                borderRadius: '8px',
                border: 'none',
                color: '#FFF',
                fontSize: '12px',
                boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.3)'
              }}
            />
            <Legend wrapperStyle={{ fontSize: '11px', paddingTop: '10px' }} />
            <Line
              type="monotone"
              dataKey={`N1_${currentCfg.key}`}
              name="Node N1"
              stroke="#6366F1"
              strokeWidth={2}
              dot={false}
            />
            <Line
              type="monotone"
              dataKey={`N3_${currentCfg.key}`}
              name="Node N3"
              stroke="#10B981"
              strokeWidth={2}
              dot={false}
            />
            <Line
              type="monotone"
              dataKey={`N5_${currentCfg.key}`}
              name="Node N5 (High Risk)"
              stroke="#EF4444"
              strokeWidth={2.5}
              dot={{ r: 3 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </GlassCard>
  );
};
