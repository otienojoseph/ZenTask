import { assets } from "../../assets/assets";
import "./footer.css";

function Footer() {
	return (
		<div className="footer" id="footer">
			<div className="footer-content">
				<div className="footer-content-left">
					<img src={assets.logo} alt="" />
					<p>
						At ZenTask, we believe that everything and anything is possible with
						the right mindset, attitude and time management. You can literally
						Zen through it!
					</p>
					<div className="footer-social-icons">
						<img src={assets.facebook_icon} alt="" />
						<img src={assets.x_icon} alt="" />
						<img src={assets.linkedin_icon} alt="" />
					</div>
				</div>
				<div className="footer-content-center">
					<h2>Company</h2>
					<ul>
						<li>Home</li>
						<li>About us</li>
						<li>Privacy policy</li>
					</ul>
				</div>
				<div className="footer-content-right">
					<h2>CONTACT US</h2>
					<ul>
						<li>+01-234-56-789</li>
						<li>email@zentask.com</li>
					</ul>
				</div>
			</div>
			<hr />
			<p className="footer-copyright">
				Copyright 2024 © ZenTask.com - All Right Reserved.
			</p>
		</div>
	);
}

export default Footer;
