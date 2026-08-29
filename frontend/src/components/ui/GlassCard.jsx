import React from 'react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export const GlassCard = ({ children, className = '', hoverEffect = false, ...props }) => {
  return (
    <div
      className={twMerge(
        'glass-panel rounded-xl p-5 transition-all duration-300 relative overflow-hidden',
        hoverEffect && 'glass-panel-hover',
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
};
