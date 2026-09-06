"use client";

import Image from "next/image";

export default function Hero() {
  return (
    <section className="relative flex flex-col items-center text-center pt-32 pb-0 overflow-hidden bg-[#030016]">
   
      <div className="absolute inset-0 flex justify-center">
      
        <div className="absolute top-1/4 z-10 w-[700px] h-[700px] bg-[#0b0961] rounded-full blur-[140px] hidden sm:block" />
       
        <img
          src="/des85.jpg"
          alt="Background Graphic"
          className="absolute  top-60 -translate-y-[10%] w-[1200px] h-[700px] object-cover opacity-100"
        />
      </div>

     
      <div className="relative z-20">
        <h1 className="text-5xl md:text-6xl font-bold text-white">
          Protecting Your <span className="text-purple-400">Digital World</span>
        </h1>
        <p className="text-gray-400 mt-4 text-lg">
          Advanced cybersecurity solutions to keep your business safe from evolving threats.
        </p>
      </div>

  
      <div className="relative z-30 mt-24 mr-5">
        <img
          src="/lock.png"
          alt="Lock Icon"
          className="   w-[250px] sm:w-[400px]  object-contain drop-shadow-[0_0_40px_rgba(168,85,247,0.9)]"
        />
      </div>

 
      <div className="relative z-40 -mt-[140px] w-auto sm:w-[1200px] backdrop-filter backdrop-blur-sm   shadow-2xl rounded-2xl overflow-hidden  ">
        <Image
          src="/22sd.png"
          alt="App Interface"
          width={1200}
          height={750}
          className="rounded-2xl"
        />
          <div className="absolute inset-0 bg-linear-to-t from-[#030016] to-[#1D1C20]/0 pointer-events-none rounded-2xl"></div>
      </div>
    </section>
  );
}
