import { useState } from "react";
import Navbar from "./components/navbar/Navbar";
import { Outlet } from "react-router-dom";
import Footer from "./components/footer/Footer";
import Login from "./components/login/Login";
import Download from "./components/download//Download";
import Hero from "./components/hero/Hero";

function App() {
	const [showLogin, setShowLogin] = useState(false);
	return (
		<>
			{showLogin ? <Login setShowLogin={setShowLogin} /> : <></>}
			<div className="wrapper">
				<Navbar setShowLogin={setShowLogin} />
				<Hero />
				<Download />
				<Footer />
				<Outlet />
			</div>
		</>
	);
}

export default App;
