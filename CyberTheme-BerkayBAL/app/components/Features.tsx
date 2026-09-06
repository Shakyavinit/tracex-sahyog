"use client";

import React from "react";
import { PiFastForwardThin } from 'react-icons/pi';
import { FcDataProtection } from 'react-icons/fc';
import { VscWorkspaceTrusted } from 'react-icons/vsc';
 
import { VscSourceControl } from 'react-icons/vsc';
import { AiOutlineCompress } from 'react-icons/ai';
import { PiEscalatorUpThin } from 'react-icons/pi';
export default function Features() {
  return (
    <section className="relative py-0 pb-20 text-center    ">

         <div className="relative z-20 mb-12">
        <h1 className="text-5xl md:text-6xl font-bold text-white">
          Protecting Your <span className="text-purple-400">Digital World</span>
        </h1>
        <p className="text-gray-400 mt-4 text-lg">
          Advanced cybersecurity solutions to keep your business safe from evolving threats.
        </p>
      </div>



      
    <div className="max-w-6xl mx-auto px-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 divide-y sm:divide-y-0 sm:divide-x divide-white/5">

  <div className="relative flex flex-col items-center justify-center py-12 text-center border border-white/5 bg-linear-to-t from-transparent to-transparent hover:from-[#FFFFFF]/6 hover:to-[#FFFFFF]/0 transition-all duration-200 overflow-hidden">
    <h3 className="text-white font-semibold text-lg mb-2">
      <PiFastForwardThin className="w-12 h-12 mx-auto" /> Built for speed
    </h3>
    <p className="text-gray-400 text-sm max-w-xs">
      Instantly sync your notes across devices
    </p>
  </div>

  <div className="relative flex flex-col items-center justify-center py-12 text-center border border-white/5 bg-linear-to-t from-transparent to-transparent hover:from-[#FFFFFF]/6 hover:to-[#FFFFFF]/0 transition-all duration-200 overflow-hidden">
    <h3 className="text-white font-semibold text-lg mb-2">
      <FcDataProtection className="w-12 h-12 mx-auto" />Built for protection
    </h3>
    <p className="text-gray-400 text-sm max-w-xs">
      End-to-end encryption for all your data
    </p>
  </div>

  <div className="relative flex flex-col items-center justify-center py-12 text-center border border-white/5 bg-linear-to-t from-transparent to-transparent hover:from-[#FFFFFF]/6 hover:to-[#FFFFFF]/0 transition-all duration-200 overflow-hidden">
    <h3 className="text-white font-semibold text-lg mb-2">
     <VscWorkspaceTrusted className="w-12 h-12 mx-auto" /> Built for reliability
    </h3>
    <p className="text-gray-400 text-sm max-w-xs">
      99.99% uptime and global redundancy
    </p>
  </div>

  <div className="relative flex flex-col items-center justify-center py-12 text-center border border-white/5 bg-linear-to-t from-transparent to-transparent hover:from-[#FFFFFF]/6 hover:to-[#FFFFFF]/0 transition-all duration-200 overflow-hidden">
    <h3 className="text-white font-semibold text-lg mb-2">
  <PiEscalatorUpThin className="w-12 h-12 mx-auto" />    Built for scalability
    </h3>
    <p className="text-gray-400 text-sm max-w-xs">
      Cloud-native protection that grows with you
    </p>
  </div>

  <div className="relative flex flex-col items-center justify-center py-12 text-center border border-white/5 bg-linear-to-t from-transparent to-transparent hover:from-[#FFFFFF]/6 hover:to-[#FFFFFF]/0 transition-all duration-200 overflow-hidden">
    <h3 className="text-white font-semibold text-lg mb-2">
   <VscSourceControl className="w-12 h-12 mx-auto" />   Built for control
    </h3>
    <p className="text-gray-400 text-sm max-w-xs">
      Manage all devices from one secure dashboard
    </p>
  </div>

  <div className="relative flex flex-col items-center justify-center py-12 text-center border border-white/5 bg-linear-to-t from-transparent to-transparent hover:from-[#FFFFFF]/6 hover:to-[#FFFFFF]/0 transition-all duration-200 overflow-hidden">
    <h3 className="text-white font-semibold text-lg mb-2">
     <AiOutlineCompress className="w-12 h-12 mx-auto" /> Built for compliance
    </h3>
    <p className="text-gray-400 text-sm max-w-xs">
      GDPR, ISO27001, and SOC2 certified protection
    </p>
  </div>

</div>

    </section>
  );
}
