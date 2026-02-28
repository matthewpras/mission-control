import type { Metadata } from "next";
import { Inter, Montserrat } from "next/font/google";
import "./globals.css";
import { cn } from "@/lib/utils";

const inter = Inter({ subsets: ["latin"], variable: '--font-sans' });
const montserrat = Montserrat({ subsets: ["latin"], variable: '--font-heading' });

export const metadata: Metadata = {
  title: "Lumina Sleep - Restorative Intelligence",
  description: "Optimize your sleep with Lumina Rest AI Mask. High-tech, bio-hacking, zen.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body
        className={cn(
          "min-h-screen bg-midnight-blue font-sans antialiased text-soft-lavender",
          inter.variable,
          montserrat.variable
        )}
      >
        {/* <Navbar /> */}
        {children}
      </body>
    </html>
  );
}