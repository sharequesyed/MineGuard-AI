import React, { useState, useEffect } from 'react';
import { StatCard } from '../components/ui/StatCard';
import { DemoControlBar } from '../components/ui/DemoControlBar';
import { MineMap } from '../components/dashboard/MineMap';
import { AIInsightPanel } from '../components/dashboard/AIInsightPanel';
import { AlertPanel } from '../components/dashboard/AlertPanel';
import { SensorCard } from '../components/dashboard/SensorCard';
import { SensorCharts } from '../components/dashboard/SensorCharts';
import { NodeDetailModal } from '../components/dashboard/NodeDetailModal';
import { SENSOR_NODES_CONFIG, getRiskLevel } from '../utils/constants';
import { useDemoMode } from '../context/DemoContext';
import { ShieldAlert, Cpu, AlertTriangle, Radio, RefreshCw } from 'lucide-react';
import confetti from 'canvas-confetti';

export const DashboardPage = () => {
  const { demoMode } = useDemoMode();
  const [selectedNodeId, setSelectedNodeId] = useState(null);
  const [lastUpdated, setLastUpdated] = useState('Just now');

  // Simulated continuous sensor data state for 6 nodes
  const [nodesData, setNodesData] = useState(() => {
    const initial = {};
    SENSOR_NODES_CONFIG.forEach((cfg, idx) => {
      initial[cfg.id] = {
        tilt: 0.6 + idx * 0.1,
        displacement: 1.1 + idx * 0.3,
        crack_width: 0.2 + idx * 0.1,
        vibration: 0.05 + idx * 0.02,
        load_change: 2.0 + idx * 1.5,
        temperature: 27.5 + idx * 0.4,
        humidity: 78.0,
        battery: 98 - idx,
        risk_score: 12 + idx * 3,
        risk_level: 'LOW'
      };
    });
    return initial;
  });

  const [alerts, setAlerts] = useState([
    {
      id: 'ALT-101',
      node_id: 'N5',
      level: 'MEDIUM',
      score: 42,
      reason: 'Elevated Tilt Drift Rate',
      details: 'Node N5 detected +0.45°/min tilt acceleration in Panel C.',
      timestamp: '10:14:02 AM'
    }
  ]);

  // Live sensor tick simulation adapting dynamically to demoMode
  useEffect(() => {
    const interval = setInterval(() => {
      setNodesData((prev) => {
        const next = { ...prev };
        SENSOR_NODES_CONFIG.forEach((cfg) => {
          const current = prev[cfg.id] || {};
          let t = current.tilt || 0.8;
          let d = current.displacement || 1.2;
          let c = current.crack_width || 0.2;
          let v = current.vibration || 0.08;
          let l = current.load_change || 3.0;

          if (demoMode === 'NORMAL') {
            // Stable baseline micro-fluctuations
            t = Math.max(0.1, t + (Math.random() - 0.5) * 0.05);
            d = Math.max(0.2, d + (Math.random() - 0.5) * 0.1);
            c = Math.max(0.0, c + (Math.random() - 0.5) * 0.02);
            v = Math.max(0.02, v + (Math.random() - 0.5) * 0.01);
            l = Math.max(-2.0, l + (Math.random() - 0.5) * 0.5);
          } else if (demoMode === 'WARNING') {
            // Progressive upward drift (Warning)
            t += Math.random() * 0.15;
            d += Math.random() * 0.35;
            c += Math.random() * 0.08;
            v += Math.random() * 0.04;
            l += Math.random() * 2.0;
          } else if (demoMode === 'SUBSIDENCE') {
            // Severe Hazard Acceleration (Emergency Mode)
            if (cfg.id === 'N5' || cfg.id === 'N3') {
              t += Math.random() * 0.6;
              d += Math.random() * 1.5;
              c += Math.random() * 0.4;
              v += Math.random() * 0.2;
              l += Math.random() * 8.0;
            } else {
              t += Math.random() * 0.2;
              d += Math.random() * 0.4;
            }
          }

          // Calculate instant risk score
          const rawScore = t * 3.5 + d * 1.8 + c * 3.0 + v * 15.0 + l * 0.3;
          const riskScore = Math.min(100, Math.round(rawScore));
          const riskLevel = getRiskLevel(riskScore);

          next[cfg.id] = {
            tilt: parseFloat(t.toFixed(2)),
            displacement: parseFloat(d.toFixed(2)),
            crack_width: parseFloat(c.toFixed(2)),
            vibration: parseFloat(v.toFixed(3)),
            load_change: parseFloat(l.toFixed(1)),
            temperature: parseFloat((28 + Math.random()).toFixed(1)),
            humidity: 82.0,
            battery: current.battery || 95,
            risk_score: riskScore,
            risk_level: riskLevel
          };
        });

        // Trigger Alert if N5 or N3 hits HIGH or CRITICAL
        const n5 = next['N5'];
        if (n5 && (n5.risk_level === 'HIGH' || n5.risk_level === 'CRITICAL')) {
          const exists = alerts.some((a) => a.node_id === 'N5' && a.score === n5.risk_score);
          if (!exists) {
            setAlerts((prevAlerts) => [
              {
                id: `ALT-${Date.now().toString().slice(-4)}`,
                node_id: 'N5',
                level: n5.risk_level,
                score: n5.risk_score,
                reason: n5.risk_level === 'CRITICAL' ? 'SEVERE SUBSIDENCE RISK' : 'Accelerating Roof Displacement',
                details: `Node N5 registered ${n5.displacement}mm displacement and ${n5.tilt}° tilt angle change.`,
                timestamp: new Date().toLocaleTimeString()
              },
              ...prevAlerts.slice(0, 8)
            ]);
          }
        }

        return next;
      });

      setLastUpdated(new Date().toLocaleTimeString());
    }, 2000);

    return () => clearInterval(interval);
  }, [demoMode]);

  // Overall mine highest risk score
  const maxRiskScore = Math.max(...Object.values(nodesData).map((n) => n.risk_score || 0));
  const overallMineLevel = getRiskLevel(maxRiskScore);
  const highRiskCount = Object.values(nodesData).filter((n) => n.risk_level === 'HIGH' || n.risk_level === 'CRITICAL').length;

  // Chart trend mock array
  const trendHistory = [
    { time: '10:00 AM', N1_displacement: 1.1, N3_displacement: 1.4, N5_displacement: 2.1, N1_tilt: 0.5, N3_tilt: 0.8, N5_tilt: 1.2, N5_risk_score: 18 },
    { time: '10:05 AM', N1_displacement: 1.2, N3_displacement: 1.6, N5_displacement: 3.4, N1_tilt: 0.6, N3_tilt: 0.9, N5_tilt: 1.8, N5_risk_score: 32 },
    { time: '10:10 AM', N1_displacement: 1.3, N3_displacement: 1.9, N5_displacement: 6.8, N1_tilt: 0.7, N3_tilt: 1.1, N5_tilt: 2.9, N5_risk_score: 58 },
    { time: '10:15 AM', N1_displacement: nodesData.N1?.displacement || 1.4, N3_displacement: nodesData.N3?.displacement || 2.2, N5_displacement: nodesData.N5?.displacement || 12.4, N1_tilt: nodesData.N1?.tilt || 0.8, N3_tilt: nodesData.N3?.tilt || 1.3, N5_tilt: nodesData.N5?.tilt || 4.2, N5_risk_score: maxRiskScore }
  ];

  const handleAcknowledgeAlert = (id) => {
    setAlerts((prev) => prev.filter((a) => a.id !== id));
  };

  return (
    <div className="space-y-6">
      {/* SIH Emergency Demo Controller */}
      <DemoControlBar />

      {/* Summary KPI Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        <StatCard
          title="Overall Mine Risk"
          value={`${maxRiskScore}`}
          unit="/ 100"
          subtitle={`Level: ${overallMineLevel}`}
          icon={ShieldAlert}
          statusColor={overallMineLevel === 'CRITICAL' ? 'text-rose-500 animate-pulse' : overallMineLevel === 'HIGH' ? 'text-orange-500' : 'text-emerald-500'}
        />

        <StatCard
          title="Active Telemetry Nodes"
          value="6 / 6"
          subtitle="All LoRa Nodes Online"
          icon={Cpu}
          statusColor="text-indigo-600 dark:text-indigo-400"
        />

        <StatCard
          title="High Risk Zones"
          value={`${highRiskCount}`}
          subtitle={highRiskCount > 0 ? 'Panel C Underground Seam' : 'All Zones Safe'}
          icon={AlertTriangle}
          statusColor={highRiskCount > 0 ? 'text-rose-500' : 'text-slate-900 dark:text-white'}
        />

        <StatCard
          title="Active Warnings"
          value={`${alerts.length}`}
          subtitle="Early warning alerts"
          icon={Radio}
          statusColor={alerts.length > 0 ? 'text-amber-500' : 'text-slate-900 dark:text-white'}
        />

        <StatCard
          title="Last Telemetry Sync"
          value={lastUpdated}
          subtitle="Real-time 2s poll"
          icon={RefreshCw}
          statusColor="text-slate-700 dark:text-slate-200"
        />
      </div>

      {/* Main Grid: Mine Map & AI Predictor */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Leaflet Underground Mine Map */}
        <div className="lg:col-span-7">
          <div className="glass-panel rounded-xl p-4">
            <div className="flex items-center justify-between mb-3">
              <div>
                <h3 className="font-extrabold text-base text-slate-900 dark:text-white">
                  Underground Seam Geo-spatial Map
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  Live sensor nodes N1–N6 & active deformation zone overlay
                </p>
              </div>
              <span className="text-xs text-slate-400 font-mono">Jharia Coalfield #4</span>
            </div>
            <MineMap nodesData={nodesData} onSelectNode={(id) => setSelectedNodeId(id)} />
          </div>
        </div>

        {/* AI Prediction & Insight Panel */}
        <div className="lg:col-span-5 flex">
          <AIInsightPanel riskScore={maxRiskScore} riskLevel={overallMineLevel} />
        </div>
      </div>

      {/* Charts & Early Warning Panel Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div className="lg:col-span-7">
          <SensorCharts historyData={trendHistory} />
        </div>

        <div className="lg:col-span-5 flex">
          <AlertPanel alerts={alerts} onAcknowledge={handleAcknowledgeAlert} />
        </div>
      </div>

      {/* Live Telemetric Sensor Cards Grid (Nodes N1 to N6) */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <div>
            <h3 className="font-extrabold text-lg text-slate-900 dark:text-white">
              Underground Telemetry Node Array
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              Real-time MPU6050 tilt, displacement, crack width, vibration, load stress, & battery
            </p>
          </div>
          <span className="text-xs text-slate-400 font-mono">6 Nodes Connected</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {SENSOR_NODES_CONFIG.map((nodeCfg) => (
            <SensorCard
              key={nodeCfg.id}
              nodeConfig={nodeCfg}
              sensorData={nodesData[nodeCfg.id]}
              onSelectNode={(id) => setSelectedNodeId(id)}
            />
          ))}
        </div>
      </div>

      {/* Node Detail Popup Modal */}
      {selectedNodeId && (
        <NodeDetailModal
          nodeId={selectedNodeId}
          nodeData={nodesData[selectedNodeId]}
          onClose={() => setSelectedNodeId(null)}
        />
      )}
    </div>
  );
};
