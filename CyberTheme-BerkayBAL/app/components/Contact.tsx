import React from 'react'

const Contact = () => {
    return (

 <form className="w-full max-w-[1200px] mx-auto bg-[#030016] p-8 rounded-xl shadow-lg text-white">
  <div className="flex flex-col md:flex-row gap-8 items-center relative">
    
    {/* Sol taraf: Form alanları */}
    <div className="flex-1 flex flex-col gap-4 ">
      <div className="flex flex-col md:flex-row gap-4">
        {/* Name */}
        <div className="flex-1">
          <label className="block mb-2 font-semibold text-lg  text-gray-600" htmlFor="name">Name, Surname</label>
          <input
            type="text"
            id="name"
            placeholder="Your name"
            className="w-full px-4 py-2 rounded-lg bg-[#1f1c2e] border border-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
          />
        </div>

        {/* Email */}
        <div className="flex-1">
          <label className="block mb-2 font-semibold text-lg  text-gray-600" htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            placeholder="Your email"
            className="w-full px-4 py-2 rounded-lg bg-[#1f1c2e] border border-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
          />
        </div>
      </div>

      {/* Subject */}<div className="flex flex-col md:flex-row gap-4">
      <div className="flex-2">
        <label className="block mb-2 text-gray-600 font-semibold text-lg" htmlFor="subject">Subject</label>
        <input
          type="text"
          id="subject"
          placeholder="Subject"
          className="w-full px-4 py-2 rounded-lg bg-[#1f1c2e] border border-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
        />
      </div>

        {/* phone */}
     <div className="flex-1">
            <label className="block mb-2 font-semibold  text-gray-600 text-lg" htmlFor="subject">Phone</label>
          <input
           type="text"
           id="phone"
            placeholder="0500 000 00 00"
           className="w-full px-4 py-2 rounded-lg bg-[#1f1c2e] border border-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
             />
      </div></div>


      {/* Message */}
      <div className="flex-1">
        <label className="block mb-2 font-semibold  text-gray-600 text-lg" htmlFor="message">Message</label>
        <textarea
          id="message"
          placeholder="Your message"
          className="w-full px-4 py-2 rounded-lg bg-[#1f1c2e] border border-gray-600 focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none h-32"
        ></textarea>
      </div>

      {/* Submit */}
      <button
        type="submit"
        className="mt-6 bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 rounded-lg transition"
      >
        Send Message
      </button>
    </div>

    {/* Sağ taraf: Görsel */}
    <div className="flex-1 flex justify-center items-start">
      <img src="/lock.png" alt="Contact Decor" className="w-full rounded-lg shadow-lg" />
    </div>

  <div className="absolute inset-0   opacity-80    flex items-center justify-center">
                <img
                    src="/vector.png"
                    alt="radar background"
                    className="w-[700px] md:w-[900px] opacity-100 z-10"
                />
            
               
            </div>
  </div> 


</form>




    )
}

export default Contact