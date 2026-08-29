import React from 'react';
import { LayoutDashboard, MapPin, BrainCircuit, BellRing, Cpu, FileText } from 'lucide-react';

export const Sidebar = ({ activeTab, setActiveTab }) => {
  const menuItems = [
    { id: 'dashboard', label: 'Live Monitoring', icon: LayoutDashboard },
    { id: 'map', label: 'Mine Underground Map', icon: MapPin },
    { id: 'analytics', label: 'AI Risk Analytics', icon: BrainCircuit },
    { id: 'alerts', label: 'Alert History', icon: BellRing },
    { id: 'health', label: 'LoRa & Hardware', icon: Cpu },
    { id: 'docs', label: 'SIH Project Docs', icon: FileText },
  ];

  return (
    <aside className="w-full lg:w-64 flex-shrink-0">
      <div className="glass-panel rounded-xl p-3 flex lg:flex-col gap-1.5 overflow-x-auto lg:overflow-visible shadow-xs">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;
          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-xs font-bold transition-all whitespace-nowrap cursor-pointer ${
                isActive
                  ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/20 dark:bg-indigo-600'
                  : 'text-slate-800 dark:text-slate-200 hover:bg-slate-200/80 dark:hover:bg-slate-800/80'
              }`}
            >
              <Icon className={`w-4 h-4 ${isActive ? 'text-white' : 'text-slate-600 dark:text-slate-400'}`} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </div>
    </aside>
  );
};
