import React from 'react';
import { ShieldAlert, Cpu, Radio, Brain, Activity, MapPin, ChevronRight, CheckCircle2, ArrowRight } from 'lucide-react';
import { GlassCard } from '../components/ui/GlassCard';

export const LandingPage = ({ onLaunchDashboard }) => {
  return (
    <div className="space-y-16 py-6 max-w-6xl mx-auto">
      {/* Hero Section */}
      <section className="text-center space-y-6 py-12 relative">
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 text-indigo-700 dark:text-indigo-300 border border-indigo-500/20 text-xs font-bold uppercase tracking-wider mb-2">
          <ShieldAlert className="w-4 h-4 text-indigo-600 animate-pulse" />
          Smart India Hackathon 2026 Project (ID: SIH26025)
        </div>

        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight text-slate-900 dark:text-white max-w-4xl mx-auto leading-tight">
          AI-Enabled Low-Cost Real-Time <br />
          <span className="bg-gradient-to-r from-indigo-600 via-sky-500 to-purple-600 bg-clip-text text-transparent">
            Mine Subsidence Monitoring
          </span> & Early Warning System
        </h1>

        <p className="text-base sm:text-lg text-slate-600 dark:text-slate-300 max-w-2xl mx-auto font-medium">
          MineGuard AI protects underground coal miners in India by utilizing low-cost ESP32 LoRa sensor nodes, progressive geotechnical deformation analytics, and Random Forest machine learning.
        </p>

        <div className="flex items-center justify-center gap-4 pt-4">
          <button
            onClick={onLaunchDashboard}
            className="px-6 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm shadow-xl shadow-indigo-600/30 transition-all transform hover:-translate-y-0.5 flex items-center gap-2 cursor-pointer"
          >
            <span>Launch Live Monitoring Dashboard</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </section>

      {/* Core System Flow Diagram Section */}
      <section className="space-y-6">
        <div className="text-center">
          <h2 className="text-2xl font-extrabold text-slate-900 dark:text-white">
            End-to-End System Architecture
          </h2>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
            From underground sensor nodes to real-time risk classification & early warning sirens
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-8 gap-2">
          {[
            { step: '01', title: 'Sensors', desc: 'MPU6050, Strain, Vibration' },
            { step: '02', title: 'ESP32 Node', desc: 'Embedded Microcontroller' },
            { step: '03', title: 'LoRa Link', desc: '868MHz Long Range' },
            { step: '04', title: 'Gateway', desc: 'Ingestion Receiver' },
            { step: '05', title: 'FastAPI Backend', desc: 'REST & WebSocket API' },
            { step: '06', title: 'Database', desc: 'SQLite / TimescaleDB' },
            { step: '07', title: 'AI Risk Engine', desc: 'Scikit-learn Model' },
            { step: '08', title: 'Early Warning', desc: 'Dashboard & Sirens' },
          ].map((s, idx) => (
            <GlassCard key={idx} className="p-3 text-center flex flex-col justify-between">
              <span className="text-[10px] font-extrabold text-indigo-500 font-mono">{s.step}</span>
              <div className="my-1">
                <div className="font-bold text-xs text-slate-900 dark:text-white">{s.title}</div>
                <div className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">{s.desc}</div>
              </div>
              <ChevronRight className="w-3.5 h-3.5 text-slate-300 mx-auto hidden lg:block" />
            </GlassCard>
          ))}
        </div>
      </section>

      {/* Key Innovation Highlights */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <GlassCard hoverEffect className="space-y-3">
          <div className="p-3 rounded-xl bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 w-fit">
            <Radio className="w-6 h-6" />
          </div>
          <h3 className="font-extrabold text-lg text-slate-900 dark:text-white">Low-Cost LoRa Mesh</h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            Eliminates high cabling costs in deep underground coal mines using long-range 868MHz LoRa radio telemetry operating reliably through rock strata.
          </p>
        </GlassCard>

        <GlassCard hoverEffect className="space-y-3">
          <div className="p-3 rounded-xl bg-sky-500/10 text-sky-600 dark:text-sky-400 w-fit">
            <Brain className="w-6 h-6" />
          </div>
          <h3 className="font-extrabold text-lg text-slate-900 dark:text-white">Predictive AI Model</h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            Random Forest ML engine correlates 10 telemetry variables including 5-minute displacement velocity ($\Delta disp/\Delta t$) to predict subsidence prior to roof collapse.
          </p>
        </GlassCard>

        <GlassCard hoverEffect className="space-y-3">
          <div className="p-3 rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400 w-fit">
            <Activity className="w-6 h-6" />
          </div>
          <h3 className="font-extrabold text-lg text-slate-900 dark:text-white">SIH Emergency Simulator</h3>
          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
            Includes an interactive SIH Demo bar enabling judges to trigger Normal, Warning Drift, and Subsidence emergency events with visual node isolation.
          </p>
        </GlassCard>
      </section>

      {/* Team Credits Section */}
      <section className="glass-panel rounded-2xl p-6">
        <div className="text-center mb-6">
          <h2 className="text-2xl font-extrabold text-slate-900 dark:text-white">Team MineNova6</h2>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Smart India Hackathon 2026 Core Engineering Team
          </p>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-center">
          {[
            { name: 'Shareque', role: 'Team Leader & Tech Lead' },
            { name: 'Monika', role: 'Research & Documentation' },
            { name: 'Aditya', role: 'UI/UX Design Lead' },
            { name: 'Farhan', role: 'Frontend Engineer' },
            { name: 'Atharva', role: 'Backend API Lead' },
            { name: 'Affan', role: 'AI/ML & Data Lead' },
          ].map((m, idx) => (
            <div key={idx} className="p-3 rounded-xl bg-slate-100/60 dark:bg-slate-800/60 border border-slate-200/50 dark:border-slate-800">
              <div className="font-extrabold text-sm text-slate-900 dark:text-white">{m.name}</div>
              <div className="text-[10px] text-indigo-600 dark:text-indigo-400 font-semibold mt-0.5">{m.role}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};
