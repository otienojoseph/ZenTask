import { Outlet } from "react-router-dom";
import Footer from "../components/footer/Footer";
import Navbar from "../components/navbar/Navbar";

export default function Pomodoro() {
	return (
		<div>
			<Navbar />
			<h1>This is where the header goes</h1>
			<Outlet />
			<Footer />
		</div>
	);
}
