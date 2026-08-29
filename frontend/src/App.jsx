import React, { useState } from 'react';
import { ThemeProvider } from './context/ThemeContext';
import { DemoProvider } from './context/DemoContext';
import { Header } from './components/dashboard/Header';
import { Sidebar } from './components/dashboard/Sidebar';
import { DashboardPage } from './pages/DashboardPage';
import { LandingPage } from './pages/LandingPage';
import { HistoryPage } from './pages/HistoryPage';
import { HealthPage } from './pages/HealthPage';
import { DocsPage } from './pages/DocsPage';

function MainLayout() {
  const [activeTab, setActiveTab] = useState('dashboard');

  return (
    <div className="bg-dot-matrix min-h-screen relative text-slate-900 dark:text-slate-100 flex flex-col selection:bg-indigo-500 selection:text-white">
      {/* Header */}
      <Header activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 lg:px-8 pb-12">
        {activeTab === 'landing' ? (
          <LandingPage onLaunchDashboard={() => setActiveTab('dashboard')} />
        ) : (
          <div className="flex flex-col lg:flex-row gap-6">
            <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
            <div className="flex-1 min-w-0">
              {activeTab === 'dashboard' && <DashboardPage />}
              {activeTab === 'map' && <DashboardPage />}
              {activeTab === 'analytics' && <DashboardPage />}
              {activeTab === 'alerts' && <HistoryPage />}
              {activeTab === 'health' && <HealthPage />}
              {activeTab === 'docs' && <DocsPage />}
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-200 dark:border-slate-800/80 py-4 text-center text-xs text-slate-400 dark:text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <span>MineGuard AI &copy; 2026 — Smart India Hackathon Prototype (SIH26025)</span>
          <span>Designed & Built by Team MineNova6</span>
        </div>
      </footer>
    </div>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <DemoProvider>
        <MainLayout />
      </DemoProvider>
    </ThemeProvider>
  );
}
