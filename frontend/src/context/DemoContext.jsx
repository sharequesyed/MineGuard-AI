import React, { createContext, useContext, useState } from 'react';

const DemoContext = createContext();

export const DemoProvider = ({ children }) => {
  const [demoMode, setDemoMode] = useState('NORMAL'); // 'NORMAL' | 'WARNING' | 'SUBSIDENCE'
  const [isSimulating, setIsSimulating] = useState(true);

  const triggerDemoMode = async (mode) => {
    setDemoMode(mode);
    try {
      await fetch('http://localhost:8000/api/demo/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mode })
      });
    } catch (err) {
      console.warn('Backend server not reached yet. Local state updated:', mode);
    }
  };

  return (
    <DemoContext.Provider value={{ demoMode, setDemoMode: triggerDemoMode, isSimulating, setIsSimulating }}>
      {children}
    </DemoContext.Provider>
  );
};

export const useDemoMode = () => useContext(DemoContext);
