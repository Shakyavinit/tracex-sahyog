import React from "react";

const Info = () => {
    return (
        <section className="relative flex flex-col items-center justify-center py-32 bg-[#030016] overflow-hidden">
            {/* Arka plan daire efekti */}
            <div className="absolute inset-0   pt-[200px] flex items-center justify-center">
                <img
                    src="/vector.png"
                    alt="radar background"
                    className="w-[700px] md:w-[900px] opacity-100 z-10"
                />
                {/* Ortadaki merkez ışık efekti */}
                <img
                    src="/leen.png"
                    alt="center glow"
                    className="absolute w-[700px] md:w-[700px] z-20"
                />
            </div>

            {/* Gradient overlay */}
            <div className="absolute inset-0 bg-linear-to-t from-[#030016] via-[#030016]/40 to-transparent z-30"></div>

            {/* İçerik */}
            <div className="relative z-40 text-center px-6">
                <h1 className="text-4xl md:text-6xl font-bold text-white mb-4">
                 Never Lose Information Again
                </h1>
                <p className="text-gray-300 max-w-2xl mx-auto text-lg">
                  Protect critical data with continuous backup, instant recovery, and global redundancy.
                </p>



            </div>
            <img
                src="/star.png"
                alt="App Interface"
                width={80}
                height={80}
                className="absolute z-40 ml-180 rounded-2xl shadow-2xl overflow-hidden"
            />
            <img
                src="/star.png"
                alt="App Interface"
                width={80}
                height={80}
                className="absolute z-40 mr-200  mt-[280px] rounded-2xl shadow-2xl overflow-hidden"
            />

            <div className="relative z-40 text-start px-6">
                <div className=" mt-10 flex flex-col md:flex-row justify-center gap-10  border-[#FFFFFF]/6 rounded-lg text-sm w-[800px] text-gray-400 border">
                    <div className="flex-1 ml-5 mt-5 mb-5">
                        <h3 className="font-semibold text-white text-3xl mb-1 ">AI-Driven Defense</h3>
                        <p className="text-gray-400 mt-4 text-lg">Predict and eliminate cyber threats using adaptive artificial intelligence.</p>
                    </div>

                  
                    <div className="flex-1 text-left mt-5 mb-5 mr-5">

                        <h3 className="font-semibold text-white text-3xl mb-1">Resilient Protection</h3>
                        <p className="text-gray-400 mt-4 text-lg">Ensure uninterrupted security with automated recovery and real-time monitoring.</p>
                    </div>
                </div></div>

        </section>
    );
};

export default Info;
