import Navbar from "./components/Navbar/Navbar.jsx"
import Home from "./pages/Home/Home.jsx"
import Login from "./pages/Login/Login.jsx"

import { Routes,Route } from "react-router-dom"

function App(){
  return(
    <>
      
   
          <Navbar/>
          <Routes>
              <Route path="/" element={<Home/>}/>
              <Route path="/login" element={<Login/>}/>
          </Routes>
      
     


    </>
  )
}
export default App