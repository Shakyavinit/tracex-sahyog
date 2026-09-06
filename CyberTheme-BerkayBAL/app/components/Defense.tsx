import React from 'react'

const Defense = () => {
    return (
        <section className="relative py-30 text-center    ">

            <div className="relative z-20 mb-0">
                <h1 className="text-5xl md:text-6xl font-bold text-white">
                    Protecting Your  Digital World
                </h1>
                <p className="text-gray-400 mt-4 text-lg ">
                Our platform uses machine learning, predictive analytics, and behavioral modeling to<br />   anticipate threats before they occur.

                </p>
            </div>

            <div className="flex    w-auto    mx-auto  items-center justify-center    overflow-hidden  ">
                <img
                    src="/defense.png"
                    alt="App Interface"
                    width={750}
                    height={500}
                    className="rounded-2xl"
                />
                <div className="absolute inset-0 bg-linear-to-t from-[#030016]/50 to-[#1D1C20]/0 pointer-events-none rounded-2xl"></div>
            </div>


            <div className="relative   overflow-hidden w-[1200px] mx-auto pl-2.5 ">
                {/* İlk satır sabit */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-0    rounded-t-lg overflow-hidden pr-2">
                    <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-center gap-2">
                        <button className="px-6 py-3 bg-purple-600 text-white rounded-lg hover:bg-[#1f1c2e] transition-colors">
                           Try For Free
                        </button>
                    </div>
                    <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-center gap-2">
                       <button className="px-6 py-3 bg-[#1f1c2e] text-white rounded-lg hover:bg-purple-700 transition-colors">
                           Get Contact
                        </button>
                    </div>
                </div>

                {/* Scrollable alan */}
                <div className="max-h-48  scroll-custom overflow-y-auto border border-t-0 border-[#1f1c2e]/80 rounded-b-lg    ">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-0">
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Multiplatform Windows®, macOS®, Android™, iOS®
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Scam Prevention & Detection
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Multi-Awarded Antivirus, Malware, Ransomware Protection
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Get anti-scam guidance, powered by AI
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Wi-Fi network security
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Protection against ransomware attacks
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Choose a VPN for more online privacy
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Cryptomining Protection
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Real-time threat detection and blocking
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Daily system health reports
                        </div>

                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />AI-powered intrusion analysis
                        </div>
                        <div className="p-4 border border-[#1f1c2e]/80 md:border-b-0 md:border-r flex items-center justify-start gap-2">
                            <img src="/verify2.png" width={30} height={30} />Advanced firewall & encryption
                        </div>

                    </div>
                    <div className="absolute inset-0 bg-linear-to-t from-white/5 to-[#ffffff]/0 pointer-events-none rounded-2xl"></div>   </div>
            </div>


        </section>
    )
}

export default Defense