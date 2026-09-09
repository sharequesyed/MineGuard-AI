import React, { useState, useEffect } from 'react';
import { Activity, Radio, Clock, Bell } from 'lucide-react';
import { ThemeToggle } from '../ui/ThemeToggle';

export const Header = ({ activeTab, setActiveTab }) => {
  const [time, setTime] = useState(new Date().toLocaleTimeString());
  const [notifPermission, setNotifPermission] = useState(
    typeof window !== 'undefined' && 'Notification' in window ? Notification.permission : 'unsupported'
  );

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const handleTestDesktopNotification = () => {
    if (typeof window !== 'undefined' && 'Notification' in window) {
      if (Notification.permission === 'granted') {
        new Notification('MineGuard AI: Desktop Alert System Ready', {
          body: 'Native computer notifications are enabled. You will receive immediate PC alerts on Warning & Critical mine hazards.',
          icon: '/favicon.svg'
        });
      } else {
        Notification.requestPermission().then((perm) => {
          setNotifPermission(perm);
          if (perm === 'granted') {
            new Notification('MineGuard AI: Desktop Alert System Enabled', {
              body: 'Native computer notifications are now active.',
              icon: '/favicon.svg'
            });
          }
        });
      }
    } else {
      alert('Browser does not support desktop notifications.');
    }
  };

  return (
    <header className="glass-panel sticky top-0 z-40 border-b border-slate-300/80 dark:border-slate-800/80 px-3 sm:px-6 py-3 mb-4 sm:mb-6 flex flex-col md:flex-row items-center justify-between gap-3 shadow-sm">
      <div className="flex items-center gap-2.5 w-full md:w-auto justify-between md:justify-start">
        <div className="flex items-center gap-2.5">
          {/* Custom MineGuard AI Shield & Pulse Logo */}
          <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl overflow-hidden shadow-sm flex-shrink-0 bg-indigo-50 dark:bg-slate-900 flex items-center justify-center border border-indigo-200 dark:border-indigo-800">
            <img src="/favicon.svg" alt="MineGuard AI Logo" className="w-full h-full p-1 transform hover:scale-105 transition-transform" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-lg sm:text-xl font-black tracking-tight text-slate-900 dark:text-white">
                MineGuard AI
              </h1>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase bg-indigo-100 text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300 border border-indigo-300 dark:border-indigo-800">
                SIH26025
              </span>
            </div>
            <p className="text-[11px] sm:text-xs font-semibold text-slate-600 dark:text-slate-400">
              Real-Time Underground Mine Subsidence Monitoring System
            </p>
          </div>
        </div>

        <div className="md:hidden flex items-center gap-2 flex-shrink-0">
          <ThemeToggle />
        </div>
      </div>

      {/* System Status Indicators */}
      <div className="flex items-center gap-2 sm:gap-3 flex-wrap justify-start md:justify-end w-full md:w-auto text-[11px] sm:text-xs overflow-x-auto pb-1 md:pb-0">
        <button
          onClick={handleTestDesktopNotification}
          className="flex items-center gap-1.5 px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg bg-indigo-50 dark:bg-indigo-950/60 text-indigo-900 dark:text-indigo-200 border border-indigo-300 dark:border-indigo-800 font-bold hover:bg-indigo-100 dark:hover:bg-indigo-900 transition-colors cursor-pointer whitespace-nowrap shadow-xs"
          title="Click to enable or test Native Computer Desktop Notifications"
        >
          <Bell className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-indigo-600 dark:text-indigo-400 animate-bounce" />
          <span>PC Alerts: <strong className="text-indigo-700 dark:text-indigo-300">{notifPermission === 'granted' ? 'ACTIVE' : 'ENABLE'}</strong></span>
        </button>

        <div className="flex items-center gap-1.5 px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg bg-slate-200/70 dark:bg-slate-800/90 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700 font-bold whitespace-nowrap">
          <Radio className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-emerald-600 dark:text-emerald-400 animate-pulse" />
          <span>LoRa: <strong className="text-emerald-700 dark:text-emerald-400">ONLINE</strong></span>
        </div>

        <div className="flex items-center gap-1.5 px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg bg-slate-200/70 dark:bg-slate-800/90 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700 font-bold whitespace-nowrap">
          <Activity className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-indigo-600 dark:text-indigo-400" />
          <span>AI Engine: <strong className="text-indigo-700 dark:text-indigo-300">ACTIVE</strong></span>
        </div>

        <div className="flex items-center gap-1.5 px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg bg-slate-200/70 dark:bg-slate-800/90 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-700 font-mono font-bold whitespace-nowrap">
          <Clock className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-slate-600 dark:text-slate-400" />
          <span>{time}</span>
        </div>

        <div className="px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg bg-purple-100 dark:bg-purple-950/60 text-purple-900 dark:text-purple-200 border border-purple-300 dark:border-purple-800 font-black whitespace-nowrap">
          Team MineNova6
        </div>

        <div className="hidden md:block">
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
};
