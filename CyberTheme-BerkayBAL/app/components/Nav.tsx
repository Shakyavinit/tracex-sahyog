"use client";

import React from "react";
import Link from "next/link";

export default function Navbar() {
  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-[#0B0B1A]/80 backdrop-blur-md border-b border-white/10">
      <nav className="max-w-7xl mx-auto flex items-center justify-between px-8 py-4">
        {/* Logo */}
        <div className="flex items-center gap-2">
          <img src="/vercel.svg
          " alt="Reflex Logo" className="w-8 h-8" />
          <span className="text-white font-semibold text-xl">Zynex</span>
        </div>

        {/* Centered navigation */}
        <ul className="hidden md:flex items-center gap-10 text-gray-300 text-sm">
          <li>
            <Link href="#" className="hover:text-white transition">
              Solutions
            </Link>
          </li>
          <li>
            <Link href="#" className="hover:text-white transition">
              Pricing
            </Link>
          </li>
          <li>
            <Link href="#" className="hover:text-white transition">
              Company
            </Link>
          </li>
          <li>
            <Link href="#" className="hover:text-white transition">
              Blog
            </Link>
          </li>
          <li>
            <Link href="#" className="hover:text-white transition">
              Contact
            </Link>
          </li>
        </ul>

        {/* Right side buttons */}
        <div className="flex items-center gap-4">
          <Link
            href="#"
            className="text-gray-300 hover:text-white transition text-sm"
          >
            Login
          </Link>
          <Link
            href="#"
            className="px-4 py-2 rounded-md bg-purple-600 hover:bg-purple-700 text-white text-sm transition"
          >
            Start Free Trial
          </Link>
        </div>
      </nav>
    </header>
  );
}
