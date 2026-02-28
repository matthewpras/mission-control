'use client';

import { motion, useScroll, useTransform } from 'framer-motion';
import Image from 'next/image';
import React, { useRef } from 'react';
import { cn } from '@/lib/utils'; // Assuming cn utility is available for class merging

interface BentoGridProps {
  children: React.ReactNode;
  className?: string;
}

interface BentoGridItemProps {
  className?: string;
  title: string;
  description: React.ReactNode;
  header: React.ReactNode;
  icon: React.ReactNode;
  isLarge?: boolean;
}

const BentoGrid = ({ className, children }: BentoGridProps) => {
  return (
    <div
      className={cn(
        'grid md:auto-rows-[18rem] grid-cols-1 md:grid-cols-3 gap-4 max-w-7xl mx-auto ',
        className
      )}
    >
      {children}
    </div>
  );
};

const BentoGridItem = ({
  className,
  title,
  description,
  header,
  icon,
  isLarge,
}: BentoGridItemProps) => {
  return (
    <motion.div
      variants={{
        hidden: { opacity: 0, y: 20 },
        visible: { opacity: 1, y: 0 }
      }}
      className={cn(
        'row-span-1 relative rounded-2xl group/bento transition duration-300 p-6 flex flex-col justify-between space-y-4',
        'glass glass-hover glow-effect',
        className
      )}
    >
      {header}
      <div className="group-hover/bento:translate-x-2 transition duration-300">
        <div className="flex items-center gap-2 mb-2">
          {icon}
          <div className="font-heading font-bold text-soft-lavender text-lg uppercase tracking-wider">{title}</div>
        </div>
        <div className="font-sans font-normal text-soft-lavender/70 text-sm leading-relaxed">{description}</div>
      </div>
    </motion.div>
  );
};

export { BentoGrid, BentoGridItem };