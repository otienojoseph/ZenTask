import { useState } from "react";
import Hero from "../components/hero/Hero";
import AppDownload from "../components/download/Download";
function Home() {
	//  const [category, setCategory] = useState('All')

	return (
		<div className="home" id="home">
			<Hero />
			<AppDownload />
		</div>
	);
}

export default Home;
