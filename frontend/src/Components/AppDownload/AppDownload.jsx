import React from 'react'
import './AppDownload.css'
import { assets } from '../../assets/assets'
import { Image } from '@chakra-ui/react'

function AppDownload() {
  return (
    <div>
        <div className="app-download" id="app-download">
            <p>For Better Experience Download <br /> ZenTask App</p>
            <div className="app-download-platform">
                <Image src={assets.play_store} alt="" />
                <Image src={assets.app_store} alt="" />
            </div>
        </div>
    </div>
  )
}

export default AppDownload
