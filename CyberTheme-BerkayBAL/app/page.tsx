import React from "react";
import Nav from "./components/Nav"
import Hero from "./components/Hero";
import Features from "./components/Features";
import Footer from "./components/Footer";
import Defense from "./components/Defense";
import Info from "./components/Info";
import Contact from "./components/Contact";

export default function Page() {
  return (
    <div className="min-h-screen bg-[#030016] text-white antialiased">
      <Nav />
      <main>
        <Hero />
        <Features />
        <Defense />
        <Info />
        <Contact />
      </main>
      <Footer />

    </div>
  );
}