// // import {
// // 	Flex,
// // 	Spacer,
// // 	Box,
// // 	ButtonGroup,
// // 	Button,
// // 	Heading,
// // 	Container,
// // } from "@chakra-ui/react";

// // function App() {
// // 	return (
// // 		<Container maxW="container.lg" bg="gray.50">
// // 			<Box my="2">
// // 				<Flex minWidth="max-content" alignItems="center" gap="2">
// // 					<Box p="2" className="logo">
// // 						{/* <a href="#">Zen it!</a> */}
// // 						<Heading size="md" color="pink.500">
// // 							Zen it!
// // 						</Heading>
// // 					</Box>
// // 					<Spacer />
// // 					<ButtonGroup gap="2">
// // 						{/* <ul>
// // 							<li>
// // 								<a href="#">Settings</a>
// // 							</li>
// // 							<li>
// // 								<a href="#">Log Out</a>
// // 							</li>
// // 						</ul> */}
// // 						<Button colorScheme="teal">Settings</Button>
// // 						<Button colorScheme="teal">Log Out</Button>
// // 					</ButtonGroup>
// // 				</Flex>
// // 			</Box>
// // 			<div className="timer-container">
// // 				<div className="timer">
// // 					<span id="timer-display">00:00:00</span>
// // 					<button id="start-button">START</button>
// // 				</div>
// // 				<div className="break-buttons">
// // 					<button>Short Break</button>
// // 					<button>Long Break</button>
// // 				</div>
// // 			</div>

// // 			<div className="task-list">
// // 				<table>
// // 					<thead>
// // 						<tr>
// // 							<th>Task Title</th>
// // 							<th>Duration</th>
// // 						</tr>
// // 					</thead>
// // 					<tbody>
// // 						<tr>
// // 							<td>Pomodoro</td>
// // 							<td id="pomodoro-duration">00:00:00</td>
// // 						</tr>
// // 						<tr>
// // 							<td>Mindfulness</td>
// // 							<td id="mindfulness-duration">00:00:00</td>
// // 						</tr>
// // 						<tr>
// // 							<td>Meditation</td>
// // 							<td id="meditation-duration">00:00:00</td>
// // 						</tr>
// // 					</tbody>
// // 				</table>
// // 			</div>

// // 			<div className="controls">
// // 				<button id="play-button">
// // 					<i className="fa fa-play"></i>
// // 				</button>
// // 				<button id="pause-button">
// // 					<i className="fa fa-pause"></i>
// // 				</button>
// // 				<button id="reset-button">
// // 					<i className="fa fa-undo"></i>
// // 				</button>
// // 				<div className="sound-control">
// // 					<i className="fa fa-volume-up"></i>
// // 					<input type="range" min="0" max="100" />
// // 				</div>
// // 			</div>

// // 			<footer>
// // 				<p>
// // 					Motivational Quote - The finishing is more important than the
// // 					beginning
// // 				</p>
// // 			</footer>
// // 		</Container>
// // 	);
// // }

// // export default App;

// import React, {useState} from 'react'
// import Navbar from './Components/Navbar/Navbar'
// import { Route, Routes } from 'react-router-dom'
// import Home from './Home/Home'
// import Footer from './Components/Footer/Footer'
// import LoginPopup from './Components/LoginPopup/LoginPopup'

// function App() {

//   const [ShowLogin, setShowLogin] = useState(false)
//   return (
//     <>
//     {ShowLogin? <LoginPopup setShowLogin={setShowLogin} />:<></>}
//     <div className='app'>
//       <Navbar setShowLogin={setShowLogin}/>
//       <Routes>
//         <Route path='/' element={<Home />} />
//       </Routes>
//     </div>
//     <Footer />
//     </>
//   )
// }

// export default App


// Filename - App.js

import React, { useState, useRef, useEffect } from "react";

const App = () => {
	// We need ref in this, because we are dealing
	// with JS setInterval to keep track of it and
	// stop it when needed
	const Ref = useRef(null);

	// The state for our timer
	const [timer, setTimer] = useState("00:00:00");

	const getTimeRemaining = (e) => {
		const total =
			Date.parse(e) - Date.parse(new Date());
		const seconds = Math.floor((total / 1000) % 60);
		const minutes = Math.floor(
			(total / 1000 / 60) % 60
		);
		const hours = Math.floor(
			(total / 1000 / 60 / 60) % 24
		);
		return {
			total,
			hours,
			minutes,
			seconds,
		};
	};

	const startTimer = (e) => {
		let { total, hours, minutes, seconds } =
			getTimeRemaining(e);
		if (total >= 0) {
			// update the timer
			// check if less than 10 then we need to
			// add '0' at the beginning of the variable
			setTimer(
				(hours > 9 ? hours : "0" + hours) +
				":" +
				(minutes > 9
					? minutes
					: "0" + minutes) +
				":" +
				(seconds > 9 ? seconds : "0" + seconds)
			);
		}
	};

	const clearTimer = (e) => {
		// If you adjust it you should also need to
		// adjust the Endtime formula we are about
		// to code next
		setTimer("00:00:50");

		// If you try to remove this line the
		// updating of timer Variable will be
		// after 1000ms or 1sec
		if (Ref.current) clearInterval(Ref.current);
		const id = setInterval(() => {
			startTimer(e);
		}, 1000);
		Ref.current = id;
	};

	const getDeadTime = () => {
		let deadline = new Date();

		// This is where you need to adjust if
		// you entend to add more time
		deadline.setSeconds(deadline.getSeconds() + 10);
		return deadline;
	};

	// We can use useEffect so that when the component
	// mount the timer will start as soon as possible

	// We put empty array to act as componentDid
	// mount only
	useEffect(() => {
		clearTimer(getDeadTime());
	}, []);

	// Another way to call the clearTimer() to start
	// the countdown is via action event from the
	// button first we create function to be called
	// by the button
	const onClickReset = () => {
		clearTimer(getDeadTime());
	};

	return (
		<div
			style={{ textAlign: "center", margin: "auto" }}>
			<h1 style={{ color: "green" }}>
				GeeksforGeeks
			</h1>
			<h3>Countdown Timer Using React JS</h3>
			<h2>{timer}</h2>
			<button onClick={onClickReset}>Reset</button>
		</div>
	);
};

export default App;
