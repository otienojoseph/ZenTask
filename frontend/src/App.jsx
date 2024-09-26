import { useState } from "react";
import Navbar from "./components/navbar/Navbar";
import Footer from "./components/footer/Footer";
import LoginPopup from "./components/login/Login";
import AppDownload from "./components/download/Download";
import { Outlet } from "react-router-dom";
import Hero from "./components/hero/Hero";

function App() {
	const [showLogin, setShowLogin] = useState(false);
	return (
		<>
			{showLogin ? <LoginPopup setShowLogin={setShowLogin} /> : <></>}
			<div className="wrapper">
				<Navbar setShowLogin={setShowLogin} />
				<Hero />
				<AppDownload />
				<Footer />
				<Outlet />
			</div>
		</>
	);
}

export default App;
