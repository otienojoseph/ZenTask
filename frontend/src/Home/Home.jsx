import { useState } from 'react'
import Header from '../Components/Header/Header'
import AppDownload from '../Components/AppDownload/AppDownload'
function Home() {

//  const [category, setCategory] = useState('All')


  return (
    <div className='home' id='home'>
      <Header />
      <AppDownload />
    </div>
  )
}

export default Home
