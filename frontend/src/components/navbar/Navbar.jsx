import { useState, useContext } from "react";
import { assets } from "../../assets/assets";
import "./navbar.css";

function Navbar({ setShowLogin }) {
	const [menu, setMenu] = useState("home");

	const isHome = location.pathname === "/";

	return (
		<div className="navbar" id="navbar">
			{isHome && (
				<div className="top">
					<a href="#navbar">Back To Top</a>
				</div>
			)}

			<a href="#header">
				<img src={assets.logo} alt="" className="logo" />
			</a>
			<ul className="navbar-menu">
				<a
					href="#header"
					onClick={() => setMenu("home")}
					className={menu === "home" ? "active" : ""}
				>
					Home
				</a>
				<a
					href="#app-download"
					onClick={() => setMenu("Mobile-App")}
					className={menu === "Mobile-App" ? "active" : ""}
				>
					Mobile-App
				</a>
				<a
					href="#footer"
					onClick={() => setMenu("contact-us")}
					className={menu === "contact-us" ? "active" : ""}
				>
					Contact Us
				</a>
			</ul>
			<div className="navbar-right">
				<img src={assets.search_icon} alt="" />
				<button onClick={() => setShowLogin(true)}>sign in</button>
			</div>
		</div>
	);
}

export default Navbar;
