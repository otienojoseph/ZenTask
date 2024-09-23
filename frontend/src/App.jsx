import { useState } from "react";
import Navbar from "./Components/Navbar/Navbar";
import Footer from "./Components/Footer/Footer";
import LoginPopup from "./Components/LoginPopup/LoginPopup";
import AppDownload from "./Components/AppDownload/AppDownload";
import { Outlet } from "react-router-dom";
import Header from "./Components/Header/Header";

function App() {
	const [showLogin, setShowLogin] = useState(false);
	return (
		<>
			{showLogin ? <LoginPopup setShowLogin={setShowLogin} /> : <></>}
			<div className="wrapper">
				<Navbar setShowLogin={setShowLogin} />
				<Header />
				<AppDownload />
				<Footer />
				<Outlet />
			</div>
		</>
	);
}

export default App;
