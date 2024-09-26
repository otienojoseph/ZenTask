import { assets } from "../../assets/assets";
import "./download.css";

function Download() {
	return (
		<div>
			<div className="app-download" id="app-download">
				<p>
					For Better Experience Download <br /> ZenTask App
				</p>
				<div className="app-download-platform">
					<img src={assets.play_store} alt="" />
					<img src={assets.app_store} alt="" />
				</div>
			</div>
		</div>
	);
}

export default Download;
