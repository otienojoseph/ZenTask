import { useState } from "react";
import Navbar from "./components/navbar/Navbar";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import Home from "./home/Home";
import Footer from "./components/footer/Footer";
import Login from "./components/login/Login";

function App() {
	const [showLogin, setShowLogin] = useState(false);
	return (
		<>
			{showLogin ? <Login setShowLogin={setShowLogin} /> : <></>}
			<div className="app">
				<Navbar setShowLogin={setShowLogin} />
				<BrowserRouter>
					<Routes>
						<Route path="/" element={<Home />} />
					</Routes>
				</BrowserRouter>
			</div>
			<Footer />
		</>
	);
}

export default App;
