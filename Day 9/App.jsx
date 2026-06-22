import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import AboutMe from "./features/AboutMe";
import Home from "./features/Home";
import Marketplace from "./features/Marketplace";
import AgentAI from "./features/AgentAI";
import Settings from "./features/Settings";

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-slate-950 text-white">
        <Header />

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/agent" element={<AgentAI />} />
          <Route path="/marketplace" element={<Marketplace />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/about" element={<AboutMe />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;