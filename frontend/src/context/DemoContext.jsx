import React, { createContext, useContext, useState, useEffect } from 'react';

const DemoContext = createContext();

export const DemoProvider = ({ children }) => {
  const [demoMode, setDemoModeState] = useState(() => {
    return localStorage.getItem('mineguard_demo_mode') || 'NORMAL';
  });
  const [isSimulating, setIsSimulating] = useState(true);

  // Cross-tab broadcast channel
  useEffect(() => {
    let bc;
    if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
      bc = new BroadcastChannel('mineguard_demo_channel');
      bc.onmessage = (event) => {
        if (event.data && event.data.mode) {
          setDemoModeState(event.data.mode);
        }
      };
    }
    return () => {
      if (bc) bc.close();
    };
  }, []);

  const triggerDemoMode = async (mode) => {
    setDemoModeState(mode);
    localStorage.setItem('mineguard_demo_mode', mode);

    // Broadcast to other tabs on same device
    if (typeof window !== 'undefined' && 'BroadcastChannel' in window) {
      try {
        const bc = new BroadcastChannel('mineguard_demo_channel');
        bc.postMessage({ mode });
        bc.close();
      } catch (e) {
        // ignore
      }
    }

    try {
      await fetch('http://localhost:8000/api/demo/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode })
      });
    } catch (err) {
      // Offline fallback
    }
  };

  return (
    <DemoContext.Provider value={{ demoMode, setDemoMode: triggerDemoMode, isSimulating, setIsSimulating }}>
      {children}
    </DemoContext.Provider>
  );
};

export const useDemoMode = () => useContext(DemoContext);
