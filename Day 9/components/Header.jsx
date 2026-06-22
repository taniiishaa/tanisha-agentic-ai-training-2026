import { Link } from "react-router-dom";

function Header() {
  return (
    <nav className="bg-slate-200 px-8 py-5 flex justify-between items-center">
      <h1 className="text-4xl font-bold text-teal-600">
        CodeNoids
      </h1>

      <div className="flex gap-10 text-xl font-semibold text-slate-700">
        <Link to="/">Home</Link>
        <Link to="/agent">Agentic AI</Link>
        <Link to="/marketplace">Marketplace</Link>
        <Link to="/settings">Settings</Link>
        <Link to="/about">AboutMe</Link>
      </div>
    </nav>
  );
}

export default Header;