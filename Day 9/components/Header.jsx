import { Link } from "react-router-dom";

function Header() {
  return (
    <div className="bg-slate-900 p-4">
      <div className="flex gap-6">

        <Link to="/">Home</Link>

        <Link to="/marketplace">
          Marketplace
        </Link>

        <Link to="/agent">
          AgentAI
        </Link>

        <Link to="/settings">
          Settings
        </Link>

      </div>
    </div>
  );
}

export default Header;