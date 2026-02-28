'use client';

import { motion, useScroll, useTransform } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import React, { useRef } from 'react';
import { BentoGrid, BentoGridItem } from '@/components/BentoGrid'; // Adjust path if needed

const SectionWrapper = ({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) => {
  const ref = useRef(null);
  return (
    <motion.section
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.3 }}
      transition={{ duration: 0.8, ease: 'anticipate', delay }}
      className="w-full max-w-7xl mx-auto py-16 px-8"
    >
      {children}
    </motion.section>
  );
};

export default function Home() {
  const heroRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: heroRef,
    offset: ['start end', 'end start'],
  });

  const heroImageY = useTransform(scrollYProgress, [0, 1], [-100, 100]); // Parallax for hero image

  const productFeatures = [
    {
      title: "Lumina Rest™ AI Mask",
      description: (
        <>
          AI-driven soundscapes, bio-feedback monitoring, and light therapy for optimized sleep.
          <span className="block mt-2 text-digital-teal font-bold text-2xl">$129.99</span>
        </>
      ),
      header: (
        <motion.div style={{ y: heroImageY }} className="relative w-full h-full flex items-center justify-center p-4">
          <Image
            src="/lumina-rest-mask.png"
            alt="Lumina Rest AI Mask 3D"
            width={500}
            height={500}
            priority
            placeholder="blur"
            blurDataURL="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
            className="rounded-xl shadow-2xl"
          />
        </motion.div>
      ),
      icon: <LampIcon className="h-4 w-4 text-digital-teal" />,
      isLarge: true,
    },
    {
      title: "Adaptive Soundscapes",
      description: "Personalized audio environments for deeper, uninterrupted rest.",
      header: (
        <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-midnight-blue to-dark-charcoal/[0.7] flex-col items-center justify-center p-4">
          <MicrophoneIcon className="h-10 w-10 text-soft-lavender mb-2" />
          <p className="text-soft-lavender text-sm text-center">AI Audio Engine</p>
        </div>
      ),
      icon: <AudioWaveIcon className="h-4 w-4 text-digital-teal" />,
    },
    {
      title: "Bio-Feedback Monitoring",
      description: "Real-time data on sleep stages, heart rate, and oxygen levels.",
      header: (
        <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-midnight-blue to-dark-charcoal/[0.7] flex-col items-center justify-center p-4">
          <HeartRateIcon className="h-10 w-10 text-soft-lavender mb-2" />
          <p className="text-soft-lavender text-sm text-center">Precision Sensors</p>
        </div>
      ),
      icon: <MonitorIcon className="h-4 w-4 text-digital-teal" />,
    },
    {
      title: "Light Therapy Sync",
      description: "Gentle dawn simulation and sunset hues for natural wake/sleep cycles.",
      header: (
        <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-midnight-blue to-dark-charcoal/[0.7] flex-col items-center justify-center p-4">
          <SunIcon className="h-10 w-10 text-soft-lavender mb-2" />
          <p className="text-soft-lavender text-sm text-center">Circadian Rhythms</p>
        </div>
      ),
      icon: <LightbulbIcon className="h-4 w-4 text-digital-teal" />,
    },
    {
      title: "Ergonomic Comfort",
      description: "Lightweight, breathable materials designed for all-night wear.",
      header: (
        <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-midnight-blue to-dark-charcoal/[0.7] flex-col items-center justify-center p-4">
          <PillowIcon className="h-10 w-10 text-soft-lavender mb-2" />
          <p className="text-soft-lavender text-sm text-center">Adaptive Fit</p>
        </div>
      ),
      icon: <ComfortIcon className="h-4 w-4 text-digital-teal" />,
    },
    {
      title: "Coming Soon: Lumina Bio-Sensor Pad",
      description: "Advanced sleep tracking and environmental monitoring. Get notified!",
      header: (
        <div className="flex flex-1 w-full h-full min-h-[6rem] rounded-xl bg-gradient-to-br from-midnight-blue to-dark-charcoal/[0.7] flex-col items-center justify-center p-4">
          <BellIcon className="h-10 w-10 text-digital-teal mb-2 animate-bounce" />
          <p className="text-digital-teal text-xl font-bold text-center">Coming Soon!</p>
          <button className="mt-4 bg-digital-teal text-midnight-blue px-6 py-2 rounded-full font-semibold hover:bg-opacity-90 transition-colors btn-glow"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}>
            Notify Me
          </button>
        </div>
      ),
      icon: <StarIcon className="h-4 w-4 text-digital-teal" />,
    },
  ];

  return (
    <>
      <header className="fixed top-0 left-0 right-0 z-50 p-4 backdrop-blur-md bg-midnight-blue/[0.2] border-b border-soft-lavender/[0.1]">
        <nav className="max-w-7xl mx-auto flex justify-between items-center">
          <Link href="/">
            <h1 className="font-heading text-xl font-bold text-digital-teal">LUMINA SLEEP</h1>
          </Link>
          <ul className="flex space-x-6">
            <li><Link href="#products" className="text-soft-lavender hover:text-digital-teal transition-colors">Products</Link></li>
            <li><Link href="#about" className="text-soft-lavender hover:text-digital-teal transition-colors">About Us</Link></li>
            <li><Link href="#contact" className="text-soft-lavender hover:text-digital-teal transition-colors">Contact</Link></li>
          </ul>
        </nav>
      </header>

      <main className="flex min-h-screen flex-col items-center justify-center pt-24 text-soft-lavender">
        {/* Hero Section */}
        <SectionWrapper>
          <motion.div
            ref={heroRef}
            className="text-center max-w-4xl mb-12"
          >
            <h1 className="font-heading text-[clamp(2.5rem,7vw,5rem)] font-bold mb-4 text-digital-teal leading-tight">
              LUMINA SLEEP
            </h1>
            <p className="text-[clamp(1rem,2.5vw,1.5rem)] mb-8 font-sans leading-relaxed text-soft-lavender/[0.9]">
              Restorative Intelligence. Unlock Your Best Sleep. Every Night.
            </p>
            <Link href="#products">
              <motion.button
                whileHover={{ scale: 1.05, boxShadow: "0 0 20px rgba(0, 128, 128, 0.7)" }}
                whileTap={{ scale: 0.95 }}
                className="btn-glow bg-digital-teal text-midnight-blue px-10 py-4 rounded-full text-lg font-semibold shadow-lg transition-all duration-300"
              >
                Explore the Lumina Rest™ Mask
              </motion.button>
            </Link>
          </motion.div>

          {/* Social Proof Ticker */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.5, ease: 'anticipate' }}
            className="flex justify-center items-center flex-wrap gap-x-8 gap-y-4 mt-12 opacity-60"
          >
            <span className="text-sm text-soft-lavender/[0.5]">As seen in:</span>
            <Image src="/logos/techcrunch-mono.svg" alt="TechCrunch" width={100} height={20} className="grayscale opacity-70" />
            <Image src="/logos/wired-mono.svg" alt="Wired" width={70} height={20} className="grayscale opacity-70" />
            <Image src="/logos/fastcompany-mono.svg" alt="Fast Company" width={120} height={20} className="grayscale opacity-70" />
          </motion.div>
        </SectionWrapper>

        {/* Bento Grid Product Section */}
        <SectionWrapper delay={0.3}>
          <h2 id="products" className="text-center font-heading text-[clamp(2rem,6vw,4rem)] font-bold mb-16 text-soft-lavender leading-tight">
            PRODUCTS & INNOVATION
          </h2>
          <BentoGrid className="max-w-6xl mx-auto">
            {productFeatures.map((item, i) => (
              <BentoGridItem
                key={i}
                title={item.title}
                description={item.description}
                header={item.header}
                icon={item.icon}
                className={item.isLarge ? "md:col-span-2" : ""}
                isLarge={item.isLarge}
              />
            ))}
          </BentoGrid>
        </SectionWrapper>

        {/* About Us Section - Placeholder */}
        <SectionWrapper delay={0.5}>
          <h2 id="about" className="text-center font-heading text-[clamp(2rem,6vw,4rem)] font-bold mb-8 text-soft-lavender leading-tight">
            OUR VISION
          </h2>
          <p className="max-w-3xl text-center text-[clamp(0.9rem,2vw,1.1rem)] text-soft-lavender/[0.8]">
            At Lumina Sleep, we believe that true well-being begins with restorative sleep. 
            Our mission is to harness cutting-edge AI and bio-feedback technology to create 
            personalized sleep experiences that empower you to wake up revitalized, every single day.
          </p>
        </SectionWrapper>

        {/* Contact Section - Placeholder */}
        <SectionWrapper delay={0.7}>
          <h2 id="contact" className="text-center font-heading text-[clamp(2rem,6vw,4rem)] font-bold mb-8 text-soft-lavender leading-tight">
            CONNECT WITH US
          </h2>
          <p className="max-w-3xl text-center text-[clamp(0.9rem,2vw,1.1rem)] text-soft-lavender/[0.8]">
            Have questions or want to learn more? Reach out to our team.
          </p>
          <div className="flex justify-center mt-8">
            <motion.button
              whileHover={{ scale: 1.05, boxShadow: "0 0 20px rgba(0, 128, 128, 0.7)" }}
              whileTap={{ scale: 0.95 }}
              className="btn-glow bg-digital-teal text-midnight-blue px-8 py-3 rounded-full text-lg font-semibold shadow-lg transition-all duration-300"
            >
              Contact Support
            </motion.button>
          </div>
        </SectionWrapper>
      </main>

      <footer className="w-full py-8 text-center text-sm text-soft-lavender/[0.6] bg-midnight-blue/[0.3] backdrop-blur-sm border-t border-soft-lavender/[0.1]">
        &copy; {new Date().getFullYear()} Lumina Sleep. All rights reserved.
      </footer>
    </>
  );
}

// Placeholder Icons (replace with actual SVG or component icons)
const LampIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M12 18v-5.25m0 0a6.002 6.002 0 0 0-7.878-3.65l-1.025.385M12 18a6.002 6.002 0 0 1 7.878-3.65l1.025.385M12 18V5.25m0 0a6.002 6.002 0 0 0-7.878-3.65l-1.025.385M12 18a6.002 6.002 0 0 1 7.878-3.65l1.025.385"
    />
  </svg>
);

const AudioWaveIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M19.114 5.66c.159.13.297.284.42.457.575.86.95 1.848.95 2.923 0 1.108-.407 2.128-1.121 2.973-.021.027-.043.054-.067.08m-.385.474c-.042.046-.08.096-.12.146M8.118 7.57a4.904 4.904 0 0 1 3.515-1.423c.966 0 1.897.291 2.684.82M6.11 10.82c.11.23.238.448.384.65M16 4.5h2.25V7.5M10.5 7.5V4.5M3.75 10.5h2.25m10.5-3V4.5M18 19.5l-1.5-1.5M4.5 19.5l1.5-1.5M18 10.5l-1.5 1.5M4.5 10.5l1.5 1.5"
    />
  </svg>
);

const HeartRateIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z"
    />
  </svg>
);

const MonitorIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M9 17.25v1.007a3 3 0 0 1-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0 1 15 18.257V17.25m6-12V15a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 15V5.25A2.25 2.25 0 0 1 5.25 3h13.5A2.25 2.25 0 0 1 21 5.25Z"
    />
  </svg>
);

const SunIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 21v-2.25m-6.364-.386 1.591-1.591M3 12H5.25m-.386-6.364 1.591 1.591M12 12a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"
    />
  </svg>
);

const LightbulbIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M12 18.75c-3.111 0-5.625-2.514-5.625-5.625V7.5m5.625 11.25a2.25 2.25 0 1 0 0 4.5 2.25 2.25 0 0 0 0-4.5ZM12 4.5v-.75a.75.75 0 0 0-1.5 0v.75m-5.25 6.375a4.5 4.5 0 0 1 1.493-1.85c.34-.143.654-.316.921-.504v-.199m7.65 0v.199c.267.189.581.362.921.504a4.5 4.5 0 0 1 1.493 1.85m-11.25 0s1.5.75 3.75.75 3.75-.75 3.75-.75M12 12.75h.008v.008H12v-.008Z"
    />
  </svg>
);

const PillowIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M16.898 8.042c1.077 0 2.247.168 3.102.583 1.05.517 1.777 1.63 1.777 2.946v3.193c0 .548-.113 1.076-.325 1.564-.173.407-.37.797-.584 1.162l-.089.152a.75.75 0 0 1-1.092.217l-2.063-1.838a1.5 1.5 0 0 0-2.195 0l-.865.772a.75.75 0 0 1-1.092.217l-.89-.792c-.172-.153-.342-.31-.5-.473a.75.75 0 0 0-1.092.217l-1.602 1.428a1.5 1.5 0 0 0-2.195 0l-.865.772a.75.75 0 0 1-1.092.217l-2.063-1.838a.75.75 0 0 1-1.092-.217l-.089-.152A6.476 6.476 0 0 1 3 14.766V11.57c0-1.316.727-2.429 1.777-2.946.855-.415 2.025-.583 3.102-.583h8.02Z"
    />
  </svg>
);

const ComfortIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M9.53 16.122a3 3 0 0 0-5.716 0L3 20.25h18l-1.014-4.128a3 3 0 0 0-5.716 0M11.999 15.659l-1.465-1.465c-.87-.87-.87-2.285 0-3.155l.732-.732a2.25 2.25 0 0 1 3.182 0l.732.732c.87.87.87 2.285 0 3.155l-1.465 1.465Z"
    />
  </svg>
);

const BellIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M9.53 16.122a3 3 0 0 0-5.716 0L3 20.25h18l-1.014-4.128a3 3 0 0 0-5.716 0M11.999 15.659l-1.465-1.465c-.87-.87-.87-2.285 0-3.155l.732-.732a2.25 2.25 0 0 1 3.182 0l.732.732c.87.87.87 2.285 0 3.155l-1.465 1.465Z"
    />
  </svg>
);

const StarIcon = ({ className }: { className?: string }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth="1.5"
    stroke="currentColor"
    className={className}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M11.48 3.499a.562.562 0 0 1 1.04 0l2.125 5.111a.563.563 0 0 0 .475.345l5.518.442c.499.04.701.663.321.988l-4.286 3.424a.563.563 0 0 0-.182.557l1.285 5.385a.562.562 0 0 1-.84.61l-4.725-2.885a.563.563 0 0 0-.586 0L6.982 20.54a.562.562 0 0 1-.84-.61l1.285-5.385a.562.562 0 0 0-.182-.557L3.499 10.42c-.38-.325-.178-.948.321-.988l5.518-.442a.563.563 0 0 0 .475-.345L11.48 3.5Z"
    />
  </svg>
);