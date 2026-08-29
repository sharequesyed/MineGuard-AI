import React from 'react';
import { Play, AlertTriangle, Flame, Volume2, VolumeX } from 'lucide-react';
import { useDemoMode } from '../../context/DemoContext';

export const DemoControlBar = () => {
  const { demoMode, setDemoMode } = useDemoMode();
  const [audioEnabled, setAudioEnabled] = React.useState(false);

  return (
    <div className="glass-panel rounded-xl p-3 sm:p-3.5 mb-6 border-indigo-300 dark:border-indigo-800 bg-gradient-to-r from-indigo-100/70 via-white to-purple-100/70 dark:from-indigo-950/40 dark:via-slate-900 dark:to-purple-950/40 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 shadow-md">
      <div className="flex items-center justify-between sm:justify-start gap-2">
        <div className="flex items-center gap-2 px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-black text-[11px] sm:text-xs shadow-sm flex-shrink-0">
          <span className="w-2 h-2 rounded-full bg-white animate-ping" />
          SIH DEMO MODE
        </div>
        <p className="text-[11px] sm:text-xs text-slate-800 dark:text-slate-200 font-bold leading-tight">
          Simulate underground stress conditions:
        </p>
      </div>

      <div className="grid grid-cols-3 sm:flex items-center gap-1.5 sm:gap-2">
        <button
          onClick={() => setDemoMode('NORMAL')}
          className={`px-2 py-2 sm:px-3.5 sm:py-1.5 rounded-lg text-[11px] sm:text-xs font-black transition-all flex items-center justify-center gap-1 cursor-pointer ${
            demoMode === 'NORMAL'
              ? 'bg-emerald-600 text-white shadow-md ring-2 ring-emerald-500'
              : 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 border border-slate-300 dark:border-slate-700'
          }`}
        >
          <Play className="w-3 h-3 sm:w-3.5 sm:h-3.5" />
          <span>Normal</span>
        </button>

        <button
          onClick={() => setDemoMode('WARNING')}
          className={`px-2 py-2 sm:px-3.5 sm:py-1.5 rounded-lg text-[11px] sm:text-xs font-black transition-all flex items-center justify-center gap-1 cursor-pointer ${
            demoMode === 'WARNING'
              ? 'bg-amber-600 text-white shadow-md ring-2 ring-amber-500'
              : 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-amber-50 dark:hover:bg-amber-950/40 border border-slate-300 dark:border-slate-700'
          }`}
        >
          <AlertTriangle className="w-3 h-3 sm:w-3.5 sm:h-3.5" />
          <span>Warning</span>
        </button>

        <button
          onClick={() => setDemoMode('SUBSIDENCE')}
          className={`px-2 py-2 sm:px-3.5 sm:py-1.5 rounded-lg text-[11px] sm:text-xs font-black transition-all flex items-center justify-center gap-1 cursor-pointer col-span-1 ${
            demoMode === 'SUBSIDENCE'
              ? 'bg-rose-600 text-white shadow-md ring-2 ring-rose-500 animate-pulse'
              : 'bg-white dark:bg-slate-800 text-rose-700 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 border border-rose-300 dark:border-rose-900'
          }`}
        >
          <Flame className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-rose-500 fill-rose-500" />
          <span>Hazard</span>
        </button>

        <button
          onClick={() => setAudioEnabled(!audioEnabled)}
          className={`hidden sm:flex p-1.5 rounded-lg text-xs border transition-all items-center justify-center cursor-pointer ${
            audioEnabled
              ? 'bg-indigo-600 text-white border-indigo-700'
              : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700'
          }`}
          title="Buzzer Audio Sound Simulation"
        >
          {audioEnabled ? <Volume2 className="w-4 h-4" /> : <VolumeX className="w-4 h-4" />}
        </button>
      </div>
    </div>
  );
};
