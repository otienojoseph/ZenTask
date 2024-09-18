import React from 'react'
import { assets } from '../../assets/assets'

function AppDownload() {
  return (
    <div>
        <div className="app-download" id="app-download">
            <p>For Better Experience Download <br /> ZenTask App</p>
            <div className="app-download-platform">
                <img src={assets.play_store} alt="" />
                <img src={assets.app_store} alt="" />
            </div>
        </div>
    </div>
  )
}

export default AppDownload
