const BASE_URL = 'http://localhost:8000/api';

export const fetchDashboardSummary = async () => {
  try {
    const res = await fetch(`${BASE_URL}/dashboard/summary`);
    if (!res.ok) throw new Error('Network error');
    return await res.json();
  } catch (err) {
    return null; // Fallback to live generator in hook
  }
};

export const fetchLatestSensorReadings = async () => {
  try {
    const res = await fetch(`${BASE_URL}/sensors/latest`);
    if (!res.ok) throw new Error('Network error');
    return await res.json();
  } catch (err) {
    return null;
  }
};

export const fetchSensorHistory = async (nodeId, limit = 30) => {
  try {
    const res = await fetch(`${BASE_URL}/sensors/history?node_id=${nodeId}&limit=${limit}`);
    if (!res.ok) throw new Error('Network error');
    return await res.json();
  } catch (err) {
    return null;
  }
};

export const fetchAlerts = async (limit = 20) => {
  try {
    const res = await fetch(`${BASE_URL}/alerts?limit=${limit}`);
    if (!res.ok) throw new Error('Network error');
    return await res.json();
  } catch (err) {
    return null;
  }
};

export const triggerDemoModeAPI = async (mode) => {
  try {
    const res = await fetch(`${BASE_URL}/demo/mode`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mode })
    });
    return await res.json();
  } catch (err) {
    return { success: false, mode };
  }
};
