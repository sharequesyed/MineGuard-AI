import React, { useState, useEffect } from 'react';
import { Activity, Radio, Clock } from 'lucide-react';
import { ThemeToggle } from '../ui/ThemeToggle';

export const Header = ({ activeTab, setActiveTab }) => {
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <header className="glass-panel sticky top-0 z-40 border-b border-slate-300/80 dark:border-slate-800/80 px-4 lg:px-8 py-3.5 mb-6 flex flex-col md:flex-row items-center justify-between gap-4 shadow-sm">
      <div className="flex items-center gap-3 w-full md:w-auto justify-between md:justify-start">
        <div className="flex items-center gap-3">
          {/* Custom MineGuard AI Shield & Pulse Logo */}
          <div className="w-10 h-10 rounded-xl overflow-hidden shadow-sm flex-shrink-0 bg-indigo-50 dark:bg-slate-900 flex items-center justify-center border border-indigo-200 dark:border-indigo-800">
            <img src="/favicon.svg" alt="MineGuard AI Logo" className="w-full h-full p-1 transform hover:scale-105 transition-transform" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-xl font-black tracking-tight text-slate-900 dark:text-white">
                MineGuard AI
              </h1>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-indigo-100 text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300 border border-indigo-300 dark:border-indigo-800">
                SIH26025
              </span>
            </div>
            <p className="text-xs font-semibold text-slate-600 dark:text-slate-400 hidden sm:block">
              Real-Time Underground Coal Mine Subsidence Monitoring & Early Warning System
            </p>
          </div>
        </div>

        <div className="md:hidden flex items-center gap-2">
          <ThemeToggle />
        </div>
      </div>

      {/* System Status Indicators */}
      <div className="flex items-center gap-3 flex-wrap justify-end w-full md:w-auto text-xs">
        <div className="hidden lg:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-200/70 dark:bg-slate-800/90 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700 font-bold">
          <Radio className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 animate-pulse" />
          <span>LoRa Gateway: <strong className="text-emerald-700 dark:text-emerald-400">ONLINE</strong></span>
        </div>

        <div className="hidden lg:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-200/70 dark:bg-slate-800/90 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700 font-bold">
          <Activity className="w-3.5 h-3.5 text-indigo-600 dark:text-indigo-400" />
          <span>AI Engine: <strong className="text-indigo-700 dark:text-indigo-300">ACTIVE</strong></span>
        </div>

        <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-200/70 dark:bg-slate-800/90 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-700 font-mono font-bold">
          <Clock className="w-3.5 h-3.5 text-slate-600 dark:text-slate-400" />
          <span>{time}</span>
        </div>

        <div className="px-3 py-1.5 rounded-lg bg-purple-100 dark:bg-purple-950/60 text-purple-900 dark:text-purple-200 border border-purple-300 dark:border-purple-800 font-black text-xs">
          Team MineNova6
        </div>

        <div className="hidden md:block">
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
};
