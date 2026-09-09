import React, { useState, useEffect } from 'react';
import { StatCard } from '../components/ui/StatCard';
import { DemoControlBar } from '../components/ui/DemoControlBar';
import { MineMap } from '../components/dashboard/MineMap';
import { AIInsightPanel } from '../components/dashboard/AIInsightPanel';
import { AlertPanel } from '../components/dashboard/AlertPanel';
import { SensorCard } from '../components/dashboard/SensorCard';
import { SensorCharts } from '../components/dashboard/SensorCharts';
import { NodeDetailModal } from '../components/dashboard/NodeDetailModal';
import { DashboardAlertBanner } from '../components/dashboard/DashboardAlertBanner';
import { SENSOR_NODES_CONFIG, getRiskLevel } from '../utils/constants';
import { useDemoMode } from '../context/DemoContext';
import { ShieldAlert, Cpu, AlertTriangle, Radio, RefreshCw } from 'lucide-react';

export const DashboardPage = () => {
  const { demoMode } = useDemoMode();
  const [selectedNodeId, setSelectedNodeId] = useState(null);
  const [lastUpdated, setLastUpdated] = useState('Just now');

  // Rolling history for Recharts line graph with dynamic real time X-axis
  const [trendHistory, setTrendHistory] = useState(() => {
    const now = Date.now();
    const initialPoints = [];
    for (let i = 7; i >= 0; i--) {
      const past = new Date(now - i * 15000);
      const timeStr = past.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      initialPoints.push({
        time: timeStr,
        N1_displacement: parseFloat((1.1 + Math.sin(i) * 0.1).toFixed(2)),
        N3_displacement: parseFloat((1.4 + Math.cos(i) * 0.2).toFixed(2)),
        N5_displacement: parseFloat((2.1 + (7 - i) * 0.4).toFixed(2)),
        N1_tilt: 0.5,
        N3_tilt: 0.8,
        N5_tilt: parseFloat((1.2 + (7 - i) * 0.3).toFixed(2)),
        N1_vibration: 0.05,
        N3_vibration: 0.08,
        N5_vibration: parseFloat((0.1 + (7 - i) * 0.05).toFixed(3)),
        N1_crack_width: 0.2,
        N3_crack_width: 0.4,
        N5_crack_width: parseFloat((0.3 + (7 - i) * 0.2).toFixed(2)),
        N5_risk_score: Math.min(100, 18 + (7 - i) * 8)
      });
    }
    return initialPoints;
  });

  // Calculate synchronized telemetric state from global Epoch time tick
  const computeSynchronizedNodes = (mode) => {
    const epochTick = Math.floor(Date.now() / 2500); // 2.5s synchronized global tick
    const next = {};

    SENSOR_NODES_CONFIG.forEach((cfg, idx) => {
      // Pseudo-deterministic sine/cosine wave based on epochTick & node index
      const wave1 = Math.sin(epochTick * 0.15 + idx * 1.5);
      const wave2 = Math.cos(epochTick * 0.2 + idx * 0.8);

      let t = 0.6 + idx * 0.15 + wave1 * 0.08;
      let d = 1.1 + idx * 0.35 + wave2 * 0.12;
      let c = 0.2 + idx * 0.1 + wave1 * 0.03;
      let v = 0.05 + idx * 0.02 + wave2 * 0.01;
      let l = 2.0 + idx * 1.5 + wave1 * 0.5;

      if (mode === 'WARNING') {
        // Warning Mode elevation
        t += 1.4 + (epochTick % 10) * 0.1;
        d += 3.2 + (epochTick % 10) * 0.25;
        c += 1.1 + (epochTick % 10) * 0.05;
        v += 0.25;
        l += 18.0;
      } else if (mode === 'SUBSIDENCE') {
        // Emergency Subsidence Mode
        if (cfg.id === 'N5' || cfg.id === 'N3') {
          t += 4.5 + (epochTick % 15) * 0.3;
          d += 12.8 + (epochTick % 15) * 0.8;
          c += 5.2 + (epochTick % 15) * 0.25;
          v += 0.85 + (epochTick % 10) * 0.05;
          l += 55.0;
        } else {
          t += 1.8;
          d += 3.5;
        }
      }

      t = Math.max(0.1, t);
      d = Math.max(0.2, d);
      c = Math.max(0.0, c);
      v = Math.max(0.01, v);

      const rawScore = t * 3.5 + d * 1.8 + c * 3.0 + v * 15.0 + l * 0.3;
      const riskScore = Math.min(100, Math.round(rawScore));
      const riskLevel = getRiskLevel(riskScore);

      next[cfg.id] = {
        tilt: parseFloat(t.toFixed(2)),
        displacement: parseFloat(d.toFixed(2)),
        crack_width: parseFloat(c.toFixed(2)),
        vibration: parseFloat(v.toFixed(3)),
        load_change: parseFloat(l.toFixed(1)),
        temperature: parseFloat((28.0 + wave1 * 0.5).toFixed(1)),
        humidity: 80.0,
        battery: Math.max(70, 98 - idx * 2),
        risk_score: riskScore,
        risk_level: riskLevel
      };
    });

    return next;
  };

  const [nodesData, setNodesData] = useState(() => computeSynchronizedNodes(demoMode));

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

  // Synchronized Telemetry Loop & Rolling Graph Update
  useEffect(() => {
    const updateTick = () => {
      const freshNodes = computeSynchronizedNodes(demoMode);
      setNodesData(freshNodes);

      const now = new Date();
      const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      setLastUpdated(timeStr);

      // Append new point to Recharts rolling history window
      const n1 = freshNodes['N1'] || {};
      const n3 = freshNodes['N3'] || {};
      const n5 = freshNodes['N5'] || {};

      setTrendHistory((prevHistory) => {
        const newPoint = {
          time: timeStr,
          N1_displacement: n1.displacement ?? 1.1,
          N3_displacement: n3.displacement ?? 1.4,
          N5_displacement: n5.displacement ?? 2.1,
          N1_tilt: n1.tilt ?? 0.5,
          N3_tilt: n3.tilt ?? 0.8,
          N5_tilt: n5.tilt ?? 1.2,
          N1_vibration: n1.vibration ?? 0.05,
          N3_vibration: n3.vibration ?? 0.08,
          N5_vibration: n5.vibration ?? 0.1,
          N1_crack_width: n1.crack_width ?? 0.2,
          N3_crack_width: n3.crack_width ?? 0.4,
          N5_crack_width: n5.crack_width ?? 0.5,
          N1_risk_score: n1.risk_score ?? 12,
          N3_risk_score: n3.risk_score ?? 18,
          N5_risk_score: n5.risk_score ?? 25
        };

        const updated = [...prevHistory, newPoint];
        // Keep max 10 data points in rolling queue
        if (updated.length > 10) {
          return updated.slice(updated.length - 10);
        }
        return updated;
      });

      // Auto-trigger alerts when any node hits score > 40 or MEDIUM, HIGH or CRITICAL level
      Object.entries(freshNodes).forEach(([nodeId, data]) => {
        if ((data.risk_score || 0) > 40 || (data.displacement || 0) > 40 || data.risk_level === 'MEDIUM' || data.risk_level === 'HIGH' || data.risk_level === 'CRITICAL') {
          setAlerts((prevAlerts) => {
            const exists = prevAlerts.some((a) => a.node_id === nodeId && a.score === data.risk_score);
            if (!exists) {
              return [
                {
                  id: `ALT-${Date.now().toString().slice(-4)}`,
                  node_id: nodeId,
                  level: data.risk_level,
                  score: data.risk_score,
                  reason:
                    data.risk_level === 'CRITICAL'
                      ? 'SEVERE SUBSIDENCE EMERGENCY'
                      : data.risk_level === 'HIGH'
                      ? 'Accelerating Roof Displacement'
                      : 'Elevated Tilt Drift Rate',
                  details: `Node ${nodeId} registered ${data.displacement}mm displacement and ${data.tilt}° tilt angle change in underground seam.`,
                  timestamp: timeStr
                },
                ...prevAlerts.slice(0, 8)
              ];
            }
            return prevAlerts;
          });
        }
      });
    };

    updateTick();
    const interval = setInterval(updateTick, 2500);
    return () => clearInterval(interval);
  }, [demoMode]);

  // Overall mine highest risk score
  const maxRiskScore = Math.max(...Object.values(nodesData).map((n) => n.risk_score || 0));
  const overallMineLevel = getRiskLevel(maxRiskScore);
  const highRiskCount = Object.values(nodesData).filter((n) => n.risk_level === 'HIGH' || n.risk_level === 'CRITICAL').length;

  const handleAcknowledgeAlert = (id) => {
    setAlerts((prev) => prev.filter((a) => a.id !== id));
  };

  return (
    <div className="space-y-6">
      {/* SIH Emergency Demo Controller */}
      <DemoControlBar />

      {/* Dynamic Warning & Critical Dashboard Alert Banner */}
      <DashboardAlertBanner
        nodesData={nodesData}
        maxRiskScore={maxRiskScore}
        overallMineLevel={overallMineLevel}
        demoMode={demoMode}
        onAcknowledgeAlert={() => {
          if (alerts.length > 0) {
            setAlerts((prev) => prev.slice(1));
          }
        }}
      />

      {/* Summary KPI Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        <StatCard
          title="Overall Mine Risk"
          value={`${maxRiskScore}`}
          unit="/ 100"
          subtitle={`Level: ${overallMineLevel}`}
          icon={ShieldAlert}
          statusColor={overallMineLevel === 'CRITICAL' ? 'text-rose-600 animate-pulse' : overallMineLevel === 'HIGH' ? 'text-orange-600' : 'text-emerald-600'}
        />

        <StatCard
          title="Active Telemetry Nodes"
          value="6 / 6"
          subtitle="All LoRa Nodes Online"
          icon={Cpu}
          statusColor="text-indigo-700 dark:text-indigo-400"
        />

        <StatCard
          title="High Risk Zones"
          value={`${highRiskCount}`}
          subtitle={highRiskCount > 0 ? 'Panel C Underground Seam' : 'All Zones Safe'}
          icon={AlertTriangle}
          statusColor={highRiskCount > 0 ? 'text-rose-600' : 'text-slate-900 dark:text-white'}
        />

        <StatCard
          title="Active Warnings"
          value={`${alerts.length}`}
          subtitle="Early warning alerts"
          icon={Radio}
          statusColor={alerts.length > 0 ? 'text-amber-600' : 'text-slate-900 dark:text-white'}
        />

        <StatCard
          title="Last Telemetry Sync"
          value={lastUpdated}
          subtitle="Real-time 2.5s poll"
          icon={RefreshCw}
          statusColor="text-slate-800 dark:text-slate-200"
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
