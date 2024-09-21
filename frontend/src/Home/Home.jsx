import React, { useState } from 'react'
import Header from '../Components/Header/Header'
import AppDownload from '../Components/AppDownload/AppDownload'
import Footer from '../Components/Footer/Footer'
function Home() {

  const [category, setCategory] = useState('All')


  return (
    <div>
      <Header />
      <ExploreMenu category={category} setCategory={setCategory} />
      <AppDownload />
      <Footer />
    </div>
  )
}

export default Home
