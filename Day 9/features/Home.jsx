function Home() {
  return (
    <div className="bg-[#000b4f] min-h-screen flex justify-center pt-12">

      <div className="w-[60rem] h-[42rem] bg-slate-900 rounded-2xl border border-slate-700">

        <div className="p-6 border-b border-slate-700">
          <h1 className="text-4xl font-bold text-white">
            AI Assistant
          </h1>

          <p className="text-green-500 text-lg mt-2">
            ● Online
          </p>
        </div>

        <div className="h-[28rem] p-6">

          <div className="bg-slate-700 text-white p-4 rounded-xl w-fit">
            Hello! How can I help you today?
          </div>

          <div className="flex justify-end mt-8">
            <div className="bg-cyan-500 text-white p-4 rounded-xl">
              Hello!
            </div>
          </div>

          <div className="mt-8">
            <div className="bg-slate-700 text-white p-4 rounded-xl w-fit">
              Nice to meet you.
            </div>
          </div>

        </div>

        <div className="border-t border-slate-700 p-4 flex gap-4">

          <input
            type="text"
            placeholder="Type a message..."
            className="flex-1 bg-slate-800 p-4 rounded-xl text-white"
          />

          <button className="bg-cyan-500 px-8 rounded-xl text-white">
            Send
          </button>

        </div>

      </div>

    </div>
  );
}

export default Home;