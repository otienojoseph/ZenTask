import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
    <div class="logo">
      <a href="#">Zen it!</a>
    </div>
    <nav>
      <ul>
        <li><a href="#">Settings</a></li>
        <li><a href="#">Log Out</a></li>
      </ul>
    </nav>
  </header>
    <div class="timer-container">
      <div class="timer">
        <span id="timer-display">00:00:00</span>
        <button id="start-button">START</button>
      </div>
      <div class="break-buttons">
        <button>Short Break</button>
        <button>Long Break</button>
      </div>
    </div>

    <div class="task-list">
      <table>
        <thead>
          <tr>
            <th>Task Title</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Pomodoro</td>
            <td id="pomodoro-duration">00:00:00</td>
          </tr>
          <tr>
            <td>Mindfulness</td>
            <td id="mindfulness-duration">00:00:00</td>
          </tr>
          <tr>
            <td>Meditation</td>
            <td id="meditation-duration">00:00:00</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="controls">
      <button id="play-button"><i class="fa fa-play"></i></button>
      <button id="pause-button"><i class="fa fa-pause"></i></button>
      <button id="reset-button"><i class="fa fa-undo"></i></button>
      <div class="sound-control">
        <i class="fa fa-volume-up"></i>
        <input type="range" min="0" max="100" value="50">
      </div>
    </div>
  </main>

  <footer>
    <p>Motivational Quote - The finishing is more important than the beginning</p>
  </footer>
    </div>
  )
}

export default App
