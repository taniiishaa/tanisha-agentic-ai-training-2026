function Home() {
  return (
    <div className="h-[90vh] p-4">
      <h1 className="text-3xl font-bold mb-4">Agent AI</h1>

      <div className="bg-slate-800 rounded-lg p-4 h-[80vh] flex flex-col">
        
        <div className="bg-slate-700 p-3 rounded mb-4 w-fit max-w-[80%]">
          AI: Hello!
        </div>

        <div className="flex justify-end mb-4">
          <div className="bg-cyan-600 p-3 rounded w-fit max-w-[80%]">
            User: Hello!
          </div>
        </div>

        <div className="bg-slate-700 p-3 rounded w-fit max-w-[80%]">
          AI: How can I help you today?
        </div>

      </div>
    </div>
  );
}

export default Home;