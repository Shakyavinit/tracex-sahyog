import React from 'react'
import { FaFacebookF } from 'react-icons/fa';
import { FaBehance } from 'react-icons/fa';
import { FaInstagram } from 'react-icons/fa';
import { FaDribbble } from 'react-icons/fa';


const Footer = () => {
  return (
     <footer className="bg-[#030014] text-gray-300 py-16">
  <div className="w-[1200px] mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-8">
 
    <div className="flex flex-col gap-4">

          <div className="flex items-center gap-2">
          <img src="/vercel.svg
          " alt="Reflex Logo" className="w-12 h-12" />
          <span className="text-white font-semibold text-[24px]">Zynex</span>
        </div> 
      
      <p className="text-gray-400">
        Protecting your digital world with cutting-edge solutions.
      </p>
   
      <div className="flex gap-4 mt-4">
        <a href="#"><FaFacebookF/> </a>
        <a href="#"><FaInstagram/> </a>
        <a href="#"><FaDribbble/> </a>
        <a href="#"><FaBehance/></a>
      </div>
    </div>

 
    <div className="flex flex-col gap-2">
      <h3 className="text-xl font-semibold text-white mb-2">Solutions</h3>
      <a href="#" className="hover:text-white transition">Threat Detection</a>
      <a href="#" className="hover:text-white transition">Endpoint Protection</a>
      <a href="#" className="hover:text-white transition">Cloud Security</a>
      <a href="#" className="hover:text-white transition">Network Monitoring</a>
    </div>

   
    <div className="flex flex-col gap-2">
      <h3 className="text-xl font-semibold text-white mb-2">Resources</h3>
      <a href="#" className="hover:text-white transition">Case Studies</a>
      <a href="#" className="hover:text-white transition">Blog & Insights</a>
      <a href="#" className="hover:text-white transition">Security Reports</a>
      <a href="#" className="hover:text-white transition">Compliance Center</a>
    </div>
 
    <div className="flex flex-col gap-2">
      <h3 className="text-xl font-semibold text-white mb-2">About Us</h3>
      <a href="#" className="hover:text-white transition">Careers</a>
      <a href="#" className="hover:text-white transition">Partners</a>
      <a href="#" className="hover:text-white transition">Contact</a>
 
    </div>

  </div>

 
  <div className="mt-12 max-w-2xl mx-auto px-6 text-center">
    <h4 className="text-xl font-semibold text-white mb-4">Stay Updated</h4>
    <form className="flex flex-col sm:flex-row gap-4 justify-center">
      <input 
        type="email" 
        placeholder="Enter your email address" 
        className="px-4 py-3 rounded-lg bg-[#1f1c2e] border border-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500 text-white w-full sm:w-auto flex-1"
      />
      <button type="submit" className="bg-purple-600 hover:bg-purple-700 text-white font-semibold px-6 py-3 rounded-lg transition">
      Subscribe
      </button>
    </form>
  </div>

  {/* Alt Kısım */}
  <div className="mt-12 border-t border-gray-700 pt-6 text-center text-gray-500 text-sm">
    &copy; 2025 Zynex Security. All rights reserved.
  </div>
</footer>

  )
}

export default Footer