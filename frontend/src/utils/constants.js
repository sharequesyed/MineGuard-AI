export const RISK_THRESHOLDS = {
  LOW: { max: 25, label: 'LOW', color: '#10B981', bgClass: 'bg-emerald-500/10 text-emerald-600 border-emerald-500/20' },
  MEDIUM: { max: 50, label: 'MEDIUM', color: '#F59E0B', bgClass: 'bg-amber-500/10 text-amber-600 border-amber-500/20' },
  HIGH: { max: 75, label: 'HIGH', color: '#F97316', bgClass: 'bg-orange-500/10 text-orange-600 border-orange-500/20' },
  CRITICAL: { max: 100, label: 'CRITICAL', color: '#EF4444', bgClass: 'bg-rose-500/10 text-rose-600 border-rose-500/20' },
};

export const SENSOR_NODES_CONFIG = [
  { id: 'N1', name: 'Node N1 - Main Seam Entry', location: 'Panel A - North Drift', lat: 23.785, lng: 86.425, depth: '180m' },
  { id: 'N2', name: 'Node N2 - Pillar Line 4', location: 'Panel A - East Pillar', lat: 23.788, lng: 86.429, depth: '210m' },
  { id: 'N3', name: 'Node N3 - Goaf Edge South', location: 'Panel B - Active Extraction', lat: 23.782, lng: 86.432, depth: '240m' },
  { id: 'N4', name: 'Node N4 - Haulage Roadway', location: 'Panel B - Conveyor Belt 2', lat: 23.780, lng: 86.422, depth: '195m' },
  { id: 'N5', name: 'Node N5 - Roof Strata Junction', location: 'Panel C - High Stress Zone', lat: 23.786, lng: 86.436, depth: '260m' },
  { id: 'N6', name: 'Node N6 - Air Return Shaft', location: 'Shaft 2 - Ventilation Line', lat: 23.791, lng: 86.420, depth: '225m' },
];

export const getRiskLevel = (score) => {
  if (score < 25) return 'LOW';
  if (score < 50) return 'MEDIUM';
  if (score < 75) return 'HIGH';
  return 'CRITICAL';
};

export const getRiskColor = (level) => {
  switch (level) {
    case 'LOW': return '#10B981';
    case 'MEDIUM': return '#F59E0B';
    case 'HIGH': return '#F97316';
    case 'CRITICAL': return '#EF4444';
    default: return '#64748B';
  }
};
