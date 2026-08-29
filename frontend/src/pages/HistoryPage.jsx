import React, { useState } from 'react';
import { GlassCard } from '../components/ui/GlassCard';
import { RiskBadge } from '../components/ui/RiskBadge';
import { Search, Filter, Download, Database, History } from 'lucide-react';
import { SENSOR_NODES_CONFIG } from '../utils/constants';

export const HistoryPage = () => {
  const [selectedNode, setSelectedNode] = useState('ALL');
  const [search, setSearch] = useState('');

  // Sample historical telemetric logs
  const logs = [
    { id: 'LOG-908', time: '2026-08-29 10:14:00', node: 'N5', tilt: 4.8, disp: 14.2, crack: 5.1, vib: 0.82, risk: 84, level: 'CRITICAL' },
    { id: 'LOG-907', time: '2026-08-29 10:12:00', node: 'N5', tilt: 3.2, disp: 9.6, crack: 3.4, vib: 0.45, risk: 62, level: 'HIGH' },
    { id: 'LOG-906', time: '2026-08-29 10:10:00', node: 'N3', tilt: 1.8, disp: 4.1, crack: 1.2, vib: 0.22, risk: 36, level: 'MEDIUM' },
    { id: 'LOG-905', time: '2026-08-29 10:08:00', node: 'N1', tilt: 0.7, disp: 1.2, crack: 0.2, vib: 0.05, risk: 14, level: 'LOW' },
    { id: 'LOG-904', time: '2026-08-29 10:06:00', node: 'N2', tilt: 0.8, disp: 1.4, crack: 0.3, vib: 0.06, risk: 16, level: 'LOW' },
    { id: 'LOG-903', time: '2026-08-29 10:04:00', node: 'N4', tilt: 0.9, disp: 1.5, crack: 0.4, vib: 0.07, risk: 18, level: 'LOW' },
    { id: 'LOG-902', time: '2026-08-29 10:02:00', node: 'N6', tilt: 0.6, disp: 1.1, crack: 0.1, vib: 0.04, risk: 12, level: 'LOW' },
  ];

  const filteredLogs = logs.filter((l) => {
    const matchesNode = selectedNode === 'ALL' || l.node === selectedNode;
    const matchesSearch = l.node.toLowerCase().includes(search.toLowerCase()) || l.level.toLowerCase().includes(search.toLowerCase());
    return matchesNode && matchesSearch;
  });

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-2xl font-extrabold text-slate-900 dark:text-white">Historical Telemetry & Alert Logs</h2>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Query sensor readings and subsidence risk evaluations stored in database
          </p>
        </div>

        <button className="px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-200 text-xs font-semibold flex items-center gap-2 hover:bg-slate-300 dark:hover:bg-slate-700 transition cursor-pointer">
          <Download className="w-4 h-4" /> Export CSV Data
        </button>
      </div>

      {/* Filter Bar */}
      <GlassCard className="flex flex-col sm:flex-row items-center justify-between gap-3 p-4">
        <div className="flex items-center gap-2 w-full sm:w-auto">
          <Filter className="w-4 h-4 text-slate-400" />
          <span className="text-xs font-bold text-slate-600 dark:text-slate-300">Filter Node:</span>
          <select
            value={selectedNode}
            onChange={(e) => setSelectedNode(e.target.value)}
            className="px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-200 outline-none"
          >
            <option value="ALL">All Sensor Nodes (N1–N6)</option>
            {SENSOR_NODES_CONFIG.map((n) => (
              <option key={n.id} value={n.id}>{n.id} - {n.name}</option>
            ))}
          </select>
        </div>

        <div className="relative w-full sm:w-64">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-2.5" />
          <input
            type="text"
            placeholder="Search logs..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-9 pr-3 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs text-slate-900 dark:text-white outline-none"
          />
        </div>
      </GlassCard>

      {/* Table */}
      <GlassCard className="overflow-x-auto p-0">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="border-b border-slate-200/80 dark:border-slate-800 text-slate-400 font-bold uppercase tracking-wider bg-slate-50/50 dark:bg-slate-900/50">
              <th className="p-3.5">Log ID</th>
              <th className="p-3.5">Timestamp</th>
              <th className="p-3.5">Node</th>
              <th className="p-3.5">Tilt (°)</th>
              <th className="p-3.5">Disp. (mm)</th>
              <th className="p-3.5">Crack (mm)</th>
              <th className="p-3.5">Vib. (g)</th>
              <th className="p-3.5">Risk Score</th>
              <th className="p-3.5">Risk Classification</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-200/60 dark:divide-slate-800/60">
            {filteredLogs.map((log) => (
              <tr key={log.id} className="hover:bg-slate-50/60 dark:hover:bg-slate-800/40 transition">
                <td className="p-3.5 font-mono text-slate-400">{log.id}</td>
                <td className="p-3.5 text-slate-600 dark:text-slate-300 font-mono">{log.time}</td>
                <td className="p-3.5 font-bold text-slate-900 dark:text-white">{log.node}</td>
                <td className="p-3.5">{log.tilt}°</td>
                <td className="p-3.5 font-semibold text-slate-900 dark:text-white">{log.disp} mm</td>
                <td className="p-3.5">{log.crack} mm</td>
                <td className="p-3.5">{log.vib} g</td>
                <td className="p-3.5 font-extrabold">{log.risk}</td>
                <td className="p-3.5">
                  <RiskBadge level={log.level} score={log.risk} size="sm" />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </GlassCard>
    </div>
  );
};
