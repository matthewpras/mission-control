'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import React from 'react';
import { BentoGrid, BentoGridItem } from '@/components/BentoGrid';
import { 
  Zap, 
  Moon, 
  Brain, 
  Sun, 
  ShieldCheck, 
  ChevronRight,
  Activity,
  Music,
  Waves
} from 'lucide-react';

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.15,
      delayChildren: 0.2,
    },
  },
};

export default function Home() {
  const productFeatures = [
    {
      title: "Lumina Rest™ AI Mask",
      description: (
        <div className="space-y-4">
          <p className="text-lg">
            The world's most advanced sleep interface. AI-driven soundscapes, neural monitoring, and clinical-grade light therapy.
          </p>
          <div className="flex items-center gap-4">
            <span className="text-3xl font-bold text-digital-teal tracking-tighter">$129.99</span>
            <button className="bg-digital-teal text-midnight-blue px-6 py-2 rounded-full font-bold hover:scale-105 transition-transform">
              Pre-Order Now
            </button>
          </div>
        </div>
      ),
      header: (
        <div className="relative w-full h-[300px] flex items-center justify-center overflow-hidden">
          <motion.div
            animate={{ 
              y: [0, -10, 0],
              rotateZ: [0, 2, 0]
            }}
            transition={{ 
              duration: 5, 
              repeat: Infinity, 
              ease: "easeInOut" 
            }}
          >
            <Image
              src="/lumina-rest-mask.png"
              alt="Lumina Rest AI Mask 3D"
              width={400}
              height={400}
              priority
              className="drop-shadow-[0_20px_50px_rgba(45,212,191,0.3)] object-contain"
            />
          </motion.div>
          {/* Decorative glow behind the image */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-digital-teal/20 blur-[100px] rounded-full -z-10" />
        </div>
      ),
      icon: <Zap className="w-5 h-5 text-digital-teal" />,
      className: "md:col-span-2 md:row-span-2",
    },
    {
      title: "Neural Audio Engine",
      description: "Spatial soundscapes that adapt in real-time to your brainwave activity.",
      header: (
        <div className="h-24 flex items-center justify-center bg-gradient-to-br from-digital-teal/10 to-transparent rounded-xl mb-4">
          <Waves className="w-12 h-12 text-digital-teal animate-pulse" />
        </div>
      ),
      icon: <Music className="w-5 h-5 text-digital-teal" />,
    },
    {
      title: "Bio-Precision Sensors",
      description: "Clinical SpO2, Heart Rate Variability, and triple-axis neural tracking.",
      header: (
        <div className="h-24 flex items-center justify-center bg-gradient-to-br from-digital-teal/10 to-transparent rounded-xl mb-4">
          <Activity className="w-12 h-12 text-digital-teal" />
        </div>
      ),
      icon: <Brain className="w-5 h-5 text-digital-teal" />,
    },
    {
      title: "Circadian Sync",
      description: "660nm Red Light therapy to trigger natural melatonin production.",
      header: (
        <div className="h-24 flex items-center justify-center bg-gradient-to-br from-digital-teal/10 to-transparent rounded-xl mb-4">
          <Sun className="w-12 h-12 text-digital-teal" />
        </div>
      ),
      icon: <Zap className="w-5 h-5 text-digital-teal" />,
    },
    {
      title: "Deep Sleep Optimization",
      description: "Proven to increase REM duration by up to 24% through AI feedback.",
      header: (
        <div className="h-24 flex items-center justify-center bg-gradient-to-br from-digital-teal/10 to-transparent rounded-xl mb-4">
          <Moon className="w-12 h-12 text-digital-teal" />
        </div>
      ),
      icon: <ShieldCheck className="w-5 h-5 text-digital-teal" />,
    },
  ];

  return (
    <div className="relative min-h-screen">
      {/* Background elements */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-digital-teal/5 blur-[120px] rounded-full" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-blue-500/5 blur-[120px] rounded-full" />
      </div>

      <header className="fixed top-0 left-0 right-0 z-50 glass">
        <nav className="max-w-7xl mx-auto flex justify-between items-center py-4 px-8">
          <Link href="/" className="flex items-center gap-2 group">
            <div className="w-8 h-8 bg-digital-teal rounded-lg flex items-center justify-center group-hover:rotate-12 transition-transform">
              <Zap className="w-5 h-5 text-midnight-blue" />
            </div>
            <h1 className="font-heading text-xl font-bold tracking-tighter text-soft-lavender">LUMINA</h1>
          </Link>
          <ul className="hidden md:flex space-x-8">
            {['Technology', 'Science', 'Reviews', 'Support'].map((item) => (
              <li key={item}>
                <Link href={`#${item.toLowerCase()}`} className="text-sm font-medium text-soft-lavender/60 hover:text-digital-teal transition-colors uppercase tracking-widest">
                  {item}
                </Link>
              </li>
            ))}
          </ul>
          <button className="glass px-6 py-2 rounded-full text-xs font-bold uppercase tracking-widest hover:border-digital-teal/50 transition-all">
            Pre-Order
          </button>
        </nav>
      </header>

      <main className="relative pt-32 pb-20 px-6">
        {/* Hero Section */}
        <section className="max-w-7xl mx-auto text-center mb-32">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
          >
            <span className="inline-block glass px-4 py-1 rounded-full text-[10px] font-bold uppercase tracking-[0.3em] text-digital-teal mb-6">
              The Future of Rest
            </span>
            <h2 className="font-heading text-[clamp(3rem,10vw,8rem)] font-bold leading-none tracking-tighter mb-8 bg-gradient-to-b from-white to-white/40 bg-clip-text text-transparent">
              SLEEP<br />REINVENTED.
            </h2>
            <p className="max-w-2xl mx-auto text-lg md:text-xl text-soft-lavender/60 mb-12">
              Lumina Rest combines neuro-feedback with spatial acoustics to unlock your deepest recovery state.
            </p>
            <div className="flex flex-col md:flex-row items-center justify-center gap-6">
              <button className="w-full md:w-auto bg-digital-teal text-midnight-blue px-10 py-5 rounded-full font-bold text-lg hover:scale-105 transition-transform shadow-[0_0_30px_rgba(45,212,191,0.3)]">
                Experience Lumina
              </button>
              <button className="w-full md:w-auto glass px-10 py-5 rounded-full font-bold text-lg hover:border-digital-teal/50 transition-all">
                Watch the Film
              </button>
            </div>
          </motion.div>
        </section>

        {/* Bento Grid Section */}
        <section id="technology" className="max-w-7xl mx-auto">
          <div className="flex flex-col md:flex-row items-end justify-between mb-16 gap-4">
            <div className="max-w-2xl">
              <h3 className="font-heading text-4xl md:text-5xl font-bold mb-4 tracking-tighter">ENGINEERED FOR TRANQUILITY.</h3>
              <p className="text-soft-lavender/60 text-lg">Every component designed to disappear, leaving only pure restorative intelligence.</p>
            </div>
            <Link href="#" className="flex items-center gap-2 text-digital-teal font-bold uppercase tracking-widest text-sm hover:gap-4 transition-all">
              Full Specifications <ChevronRight className="w-4 h-4" />
            </Link>
          </div>

          <motion.div
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-100px" }}
          >
            <BentoGrid>
              {productFeatures.map((feature, i) => (
                <BentoGridItem
                  key={i}
                  title={feature.title}
                  description={feature.description}
                  header={feature.header}
                  icon={feature.icon}
                  className={feature.className}
                />
              ))}
            </BentoGrid>
          </motion.div>
        </section>

        {/* Brand Proof */}
        <section className="max-w-7xl mx-auto mt-40 border-t border-white/5 pt-20">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-12 opacity-30 grayscale hover:grayscale-0 transition-all duration-700">
            <div className="flex items-center justify-center h-12">
              <span className="font-heading font-black text-2xl">WIRED</span>
            </div>
            <div className="flex items-center justify-center h-12">
              <span className="font-heading font-black text-2xl">FORBES</span>
            </div>
            <div className="flex items-center justify-center h-12">
              <span className="font-heading font-black text-2xl">THE VERGE</span>
            </div>
            <div className="flex items-center justify-center h-12">
              <span className="font-heading font-black text-2xl">GQ</span>
            </div>
          </div>
        </section>
      </main>

      <footer className="max-w-7xl mx-auto py-20 px-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8">
        <div className="flex items-center gap-2">
          <div className="w-6 h-6 bg-digital-teal rounded flex items-center justify-center">
            <Zap className="w-4 h-4 text-midnight-blue" />
          </div>
          <span className="font-heading font-bold text-sm tracking-tighter">LUMINA SLEEP</span>
        </div>
        <div className="flex gap-8 text-xs font-bold uppercase tracking-[0.2em] text-soft-lavender/40">
          <Link href="#" className="hover:text-digital-teal transition-colors">Twitter</Link>
          <Link href="#" className="hover:text-digital-teal transition-colors">Instagram</Link>
          <Link href="#" className="hover:text-digital-teal transition-colors">Contact</Link>
        </div>
        <p className="text-xs text-soft-lavender/20 uppercase tracking-widest">
          © 2026 LUMINA SLEEP TECHNOLOGY. ALL RIGHTS RESERVED.
        </p>
      </footer>
    </div>
  );
}
