import React from 'react';
import { GlassCard } from '../components/ui/GlassCard';
import { StatCard } from '../components/ui/StatCard';
import { Cpu, Radio, Wifi, Server, Battery, CheckCircle2, AlertCircle } from 'lucide-react';
import { SENSOR_NODES_CONFIG } from '../utils/constants';

export const HealthPage = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-extrabold text-slate-900 dark:text-white">LoRa Gateway & Hardware Health</h2>
        <p className="text-xs text-slate-500 dark:text-slate-400">
          Hardware node diagnostics, battery levels, packet reception rates, & backend API status
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="LoRa Gateway Status" value="ONLINE" subtitle="SX1276 868MHz Gateway" icon={Radio} statusColor="text-emerald-500" />
        <StatCard title="Packet Success Rate" value="99.8%" subtitle="0 dropped packets in 24h" icon={CheckCircle2} statusColor="text-indigo-600 dark:text-indigo-400" />
        <StatCard title="Average Node Battery" value="94%" subtitle="3.8V LiFePO4 cells" icon={Battery} statusColor="text-emerald-500" />
        <StatCard title="Backend API Health" value="HEALTHY" subtitle="FastAPI v0.110.0" icon={Server} statusColor="text-emerald-500" />
      </div>

      {/* Node Battery & Signal Strength Status */}
      <GlassCard className="space-y-4">
        <h3 className="font-extrabold text-base text-slate-900 dark:text-white">Underground LoRa Sensor Array Health</h3>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {SENSOR_NODES_CONFIG.map((n, idx) => {
            const bat = 98 - idx * 2;
            const rssi = -74 - idx * 3;
            return (
              <div key={n.id} className="p-4 rounded-xl bg-slate-100/60 dark:bg-slate-800/60 border border-slate-200/50 dark:border-slate-800 flex items-center justify-between">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-bold text-sm text-slate-900 dark:text-white">{n.id}</span>
                    <span className="text-xs text-slate-500">{n.name}</span>
                  </div>
                  <div className="text-[11px] text-slate-400 font-mono mt-1">RSSI: {rssi} dBm | SNR: +9.2 dB</div>
                </div>

                <div className="text-right">
                  <span className="inline-flex items-center gap-1 text-xs font-extrabold text-emerald-600 dark:text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20">
                    <Battery className="w-3.5 h-3.5" /> {bat}%
                  </span>
                  <div className="text-[10px] text-slate-400 mt-1">Status: OK</div>
                </div>
              </div>
            );
          })}
        </div>
      </GlassCard>
    </div>
  );
};
