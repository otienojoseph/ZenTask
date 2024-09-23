import { useState } from "react";
import { assets } from "../../assets/assets";
import "./LoginPopup.css";

function LoginPopup({ setShowLogin }) {
	const [currentState, setCurrentState] = useState("Login");
	return (
		<div className="login-popup" onClick={() => setShowLogin((prev) => !prev)}>
			<form className="login-popup-container">
				<div className="login-popup-title">
					<h2>{currentState}</h2>
					<img
						onClick={() => setShowLogin((prev) => !prev)}
						src={assets.cross_icon}
						alt=""
					/>
				</div>
				<div className="login-popup-input">
					{currentState === "Login" ? (
						<></>
					) : (
						<input type="text" placeholder="Fullname" required />
					)}
					<input type="email" placeholder="Your email" required />
					<input type="password" placeholder="Your password" required />
					<input type="password" placeholder="Confirm password" required />
				</div>
				<button>{currentState === "Sign Up" ? "Sign up" : "Login"}</button>
				<div className="login-popup-condition">
					<input type="checkbox" required />
					<p>By continuing, I agree to the terms of use & privacy policy.</p>
				</div>
				{currentState === "Login" ? (
					<p>
						Create a new account?{" "}
						<span onClick={() => setCurrentState("Sign Up")}>Click here</span>
					</p>
				) : (
					<p>
						Already have an account?{" "}
						<span onClick={() => setCurrentState("Login")}>Login here</span>
					</p>
				)}
			</form>
		</div>
	);
}

export default LoginPopup;
