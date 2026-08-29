import React from 'react';
import { GlassCard } from '../components/ui/GlassCard';
import { FileText, Users, ShieldAlert, Cpu, CheckCircle } from 'lucide-react';

export const DocsPage = () => {
  return (
    <div className="space-y-6 max-w-5xl mx-auto">
      <div>
        <h2 className="text-2xl font-extrabold text-slate-900 dark:text-white">SIH 2026 Project Documentation</h2>
        <p className="text-xs text-slate-500 dark:text-slate-400">
          Problem Statement SIH26025 & Team MineNova6 Technical Specs
        </p>
      </div>

      <GlassCard className="space-y-4">
        <h3 className="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
          <ShieldAlert className="w-5 h-5 text-indigo-600" />
          Problem Statement Details
        </h3>
        <div className="text-xs text-slate-600 dark:text-slate-300 space-y-2 leading-relaxed">
          <p><strong>PS ID:</strong> SIH26025</p>
          <p><strong>Title:</strong> Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India.</p>
          <p><strong>Objective:</strong> Design and build an operational prototype that ingests multi-sensor telemetric data (tilt, displacement, crack width, vibration, load change), calculates continuous subsidence risk scores (0–100), isolates high-risk underground seams, and generates instant early warnings.</p>
        </div>
      </GlassCard>

      <GlassCard className="space-y-4">
        <h3 className="text-lg font-bold text-slate-900 dark:text-white flex items-center gap-2">
          <Users className="w-5 h-5 text-indigo-600" />
          Team Member Allocation (Team MineNova6)
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
          <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <strong>Shareque:</strong> Team Leader + Tech Lead + System Integration
          </div>
          <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <strong>Monika:</strong> Presentation + Documentation + Geotechnical Research
          </div>
          <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <strong>Aditya:</strong> UI/UX Design Lead
          </div>
          <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <strong>Farhan:</strong> Frontend React Engineer
          </div>
          <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <strong>Atharva:</strong> Backend FastAPI Lead
          </div>
          <div className="p-3 rounded-lg bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <strong>Affan:</strong> AI/ML & Data Lead
          </div>
        </div>
      </GlassCard>
    </div>
  );
};
