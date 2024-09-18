import React, { useState, useContext } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { assets } from '../../assets/assets'
import {StoreContext} from '../../Context/StoreContext'


function Navbar({setShowLogin}) {
    const [menu, setMenu] = useState("home");

    const {getTotalCartAmount} = useContext(StoreContext);

    const location = useLocation();
    const isHome = location.pathname === '/';

  return (
    <div className='navbar' id='navbar'>
      {isHome && (<div class="top">
        <a href="#navbar">Back To Top</a>
      </div>)}
      
      <Link to='/'><img src={assets.} alt="" className='logo' /></Link>
      <ul className="navbar-menu">
        <Link to='/' onClick={()=>setMenu("home")} className={menu==="home"?"active":""}>home</Link>
        <a href='#explore-menu' onClick={()=>setMenu("menu")} className={menu==="menu"?"active":""}>menu</a>
        <a href='#app-download' onClick={()=>setMenu("mobile-app")} className={menu==="mobile-app"?"active":""}>mobile-app</a>
        <a href='#footer' onClick={()=>setMenu("contact-us")} className={menu==="contact-us"?"active":""}>contact us</a>
      </ul>
      <div className="navbar-right">
        <img src={assets.} alt="" />
        <div className='navbar-search-icon'>
            <Link to={'/cart'}><img src={assets.} alt="" /></Link>
            <div className={getTotalCartAmount()===0?"":"dot"}></div>
        </div>
        <button onClick={()=>setShowLogin(true)}>sign in</button>
      </div>
    </div>
  )
}

export default Navbar
