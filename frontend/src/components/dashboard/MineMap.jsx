import React from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle, Polygon } from 'react-leaflet';
import L from 'leaflet';
import { SENSOR_NODES_CONFIG, getRiskColor, getRiskLevel } from '../../utils/constants';
import { RiskBadge } from '../ui/RiskBadge';

// Custom Leaflet DivIcon for Mine Sensor Nodes
const createNodeIcon = (nodeId, level, score) => {
  const color = getRiskColor(level);
  const isDanger = level === 'HIGH' || level === 'CRITICAL';
  
  return L.divIcon({
    className: 'custom-mine-node',
    html: `
      <div class="relative flex items-center justify-center cursor-pointer">
        ${isDanger ? `<div class="absolute -inset-2 rounded-full opacity-75 animate-ping" style="background-color: ${color}"></div>` : ''}
        <div class="relative z-10 w-8 h-8 sm:w-9 sm:h-9 rounded-full flex items-center justify-center text-white font-black text-[11px] sm:text-xs shadow-lg border-2 border-white dark:border-slate-900 transition-transform duration-300 hover:scale-110" style="background-color: ${color}">
          ${nodeId}
        </div>
        <div class="absolute -bottom-5 whitespace-nowrap bg-slate-900/90 text-white text-[10px] font-mono px-1.5 py-0.5 rounded backdrop-blur-xs shadow-sm">
          ${score} pts
        </div>
      </div>
    `,
    iconSize: [36, 36],
    iconAnchor: [18, 18],
  });
};

export const MineMap = ({ nodesData = {}, onSelectNode }) => {
  // Center of underground coal mine (Jharia Coalfield simulation baseline)
  const mineCenter = [23.785, 86.427];

  // Polygon boundary for active underground excavation panel
  const highRiskPanelZone = [
    [23.784, 86.430],
    [23.789, 86.438],
    [23.783, 86.439],
    [23.780, 86.431]
  ];

  return (
    <div className="w-full h-[320px] sm:h-[420px] rounded-xl overflow-hidden relative shadow-inner border border-slate-200/80 dark:border-slate-800">
      <MapContainer center={mineCenter} zoom={15} scrollWheelZoom={false} className="w-full h-full">
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {/* Underground Active Extraction Zone Overlay */}
        <Polygon
          positions={highRiskPanelZone}
          pathOptions={{
            color: '#F97316',
            fillColor: '#F97316',
            fillOpacity: 0.15,
            dashArray: '6, 6',
            weight: 2
          }}
        />

        {/* Sensor Node Markers */}
        {SENSOR_NODES_CONFIG.map((cfg) => {
          const liveNode = nodesData[cfg.id] || {};
          const score = liveNode.risk_score !== undefined ? liveNode.risk_score : 15;
          const level = liveNode.risk_level || getRiskLevel(score);
          const icon = createNodeIcon(cfg.id, level, score);

          return (
            <React.Fragment key={cfg.id}>
              {/* Optional danger aura circle */}
              {(level === 'HIGH' || level === 'CRITICAL') && (
                <Circle
                  center={[cfg.lat, cfg.lng]}
                  radius={120}
                  pathOptions={{
                    color: getRiskColor(level),
                    fillColor: getRiskColor(level),
                    fillOpacity: 0.25
                  }}
                />
              )}

              <Marker
                position={[cfg.lat, cfg.lng]}
                icon={icon}
                eventHandlers={{
                  click: () => onSelectNode && onSelectNode(cfg.id),
                }}
              >
                <Popup className="mine-node-popup">
                  <div className="p-1 max-w-xs font-sans text-slate-800">
                    <div className="flex items-center justify-between gap-2 border-b pb-1.5 mb-2">
                      <strong className="text-xs font-bold">{cfg.name}</strong>
                      <RiskBadge level={level} score={score} size="sm" />
                    </div>
                    <p className="text-[11px] text-slate-500 mb-2">{cfg.location} (Depth: {cfg.depth})</p>

                    <div className="grid grid-cols-2 gap-1.5 text-[11px] bg-slate-50 p-2 rounded mb-2 border border-slate-100 font-medium">
                      <div>Tilt: <strong>{liveNode.tilt ?? 0.8}°</strong></div>
                      <div>Displacement: <strong>{liveNode.displacement ?? 1.2} mm</strong></div>
                      <div>Crack: <strong>{liveNode.crack_width ?? 0.2} mm</strong></div>
                      <div>Vibration: <strong>{liveNode.vibration ?? 0.08} g</strong></div>
                    </div>

                    <button
                      onClick={() => onSelectNode && onSelectNode(cfg.id)}
                      className="w-full py-1 bg-indigo-600 hover:bg-indigo-700 text-white rounded text-[11px] font-semibold transition cursor-pointer"
                    >
                      View Node Details & Trends
                    </button>
                  </div>
                </Popup>
              </Marker>
            </React.Fragment>
          );
        })}
      </MapContainer>

      {/* Map Legend Overlay */}
      <div className="absolute bottom-2 right-2 z-[400] glass-panel px-2.5 py-1.5 rounded-lg text-[10px] sm:text-xs flex items-center gap-2 sm:gap-3 backdrop-blur-md">
        <span className="font-bold text-slate-700 dark:text-slate-300 hidden sm:inline">Mine Seam:</span>
        <div className="flex items-center gap-1">
          <span className="w-2 h-2 rounded-full bg-emerald-500" />
          <span className="text-[10px] text-slate-700 dark:text-slate-300 font-bold">Low</span>
        </div>
        <div className="flex items-center gap-1">
          <span className="w-2 h-2 rounded-full bg-amber-500" />
          <span className="text-[10px] text-slate-700 dark:text-slate-300 font-bold">Med</span>
        </div>
        <div className="flex items-center gap-1">
          <span className="w-2 h-2 rounded-full bg-orange-500" />
          <span className="text-[10px] text-slate-700 dark:text-slate-300 font-bold">High</span>
        </div>
        <div className="flex items-center gap-1">
          <span className="w-2 h-2 rounded-full bg-rose-500 animate-ping" />
          <span className="text-[10px] text-slate-700 dark:text-slate-300 font-black">Critical</span>
        </div>
      </div>
    </div>
  );
};
