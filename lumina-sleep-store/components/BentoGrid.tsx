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
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ['start end', 'end start'],
  });

  const y = useTransform(scrollYProgress, [0, 1], [-50, 50]); // Parallax effect

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.3 }}
      transition={{ duration: 0.8, ease: 'anticipate' }} // Staggered fade-in with anticipate easing
      className={cn(
        'row-span-1 relative rounded-xl group/bento hover:shadow-xl transition duration-200 shadow-input dark:shadow-none p-4 dark:bg-black dark:border-white/[0.2] bg-white border border-transparent justify-between flex flex-col space-y-4',
        // Glassmorphism effect
        'bg-opacity-20 backdrop-filter backdrop-blur-md border border-soft-lavender/[0.3] hover:border-digital-teal/[0.5]',
        className
      )}
    >
      {isLarge ? (
        <motion.div style={{ y }} className="relative w-full h-full flex items-center justify-center">
          {header}
        </motion.div>
      ) : (
        header
      )}
      <div className="group-hover/bento:translate-x-2 transition duration-200">
        {icon}
        <div className="font-sans font-bold text-soft-lavender text-lg mb-2 mt-2">{title}</div>
        <div className="font-sans font-normal text-soft-lavender/[0.7] text-sm">{description}</div>
      </div>
    </motion.div>
  );
};

export { BentoGrid, BentoGridItem };