// import {
// 	Flex,
// 	Spacer,
// 	Box,
// 	ButtonGroup,
// 	Button,
// 	Heading,
// 	Container,
// } from "@chakra-ui/react";

// function App() {
// 	return (
// 		<Container maxW="container.lg" bg="gray.50">
// 			<Box my="2">
// 				<Flex minWidth="max-content" alignItems="center" gap="2">
// 					<Box p="2" className="logo">
// 						{/* <a href="#">Zen it!</a> */}
// 						<Heading size="md" color="pink.500">
// 							Zen it!
// 						</Heading>
// 					</Box>
// 					<Spacer />
// 					<ButtonGroup gap="2">
// 						{/* <ul>
// 							<li>
// 								<a href="#">Settings</a>
// 							</li>
// 							<li>
// 								<a href="#">Log Out</a>
// 							</li>
// 						</ul> */}
// 						<Button colorScheme="teal">Settings</Button>
// 						<Button colorScheme="teal">Log Out</Button>
// 					</ButtonGroup>
// 				</Flex>
// 			</Box>
// 			<div className="timer-container">
// 				<div className="timer">
// 					<span id="timer-display">00:00:00</span>
// 					<button id="start-button">START</button>
// 				</div>
// 				<div className="break-buttons">
// 					<button>Short Break</button>
// 					<button>Long Break</button>
// 				</div>
// 			</div>

// 			<div className="task-list">
// 				<table>
// 					<thead>
// 						<tr>
// 							<th>Task Title</th>
// 							<th>Duration</th>
// 						</tr>
// 					</thead>
// 					<tbody>
// 						<tr>
// 							<td>Pomodoro</td>
// 							<td id="pomodoro-duration">00:00:00</td>
// 						</tr>
// 						<tr>
// 							<td>Mindfulness</td>
// 							<td id="mindfulness-duration">00:00:00</td>
// 						</tr>
// 						<tr>
// 							<td>Meditation</td>
// 							<td id="meditation-duration">00:00:00</td>
// 						</tr>
// 					</tbody>
// 				</table>
// 			</div>

// 			<div className="controls">
// 				<button id="play-button">
// 					<i className="fa fa-play"></i>
// 				</button>
// 				<button id="pause-button">
// 					<i className="fa fa-pause"></i>
// 				</button>
// 				<button id="reset-button">
// 					<i className="fa fa-undo"></i>
// 				</button>
// 				<div className="sound-control">
// 					<i className="fa fa-volume-up"></i>
// 					<input type="range" min="0" max="100" />
// 				</div>
// 			</div>

// 			<footer>
// 				<p>
// 					Motivational Quote - The finishing is more important than the
// 					beginning
// 				</p>
// 			</footer>
// 		</Container>
// 	);
// }

// export default App;

import React, {useState} from 'react'
import Navbar from './Components/Navbar/Navbar'
import { Route, Routes } from 'react-router-dom'
import Home from './Home/Home'
import Footer from './Components/Footer/Footer'
import LoginPopup from './Components/LoginPopup/LoginPopup'

function App() {

  const [ShowLogin, setShowLogin] = useState(false)
  return (
    <>
    {ShowLogin? <LoginPopup setShowLogin={setShowLogin} />:<></>}
    <div className='app'>
      <Navbar setShowLogin={setShowLogin}/>
      <Routes>
        <Route path='/' element={<Home />} />
      </Routes>
    </div>
    <Footer />
    </>
  )
}

export default App

