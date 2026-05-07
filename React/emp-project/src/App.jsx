import Navbar from "./components/Navbar/Navbar"
import { Routes,Route } from "react-router-dom"
import Home from "./pages/Home/Home"
import Login from "./pages/Login/Login"
import ContactUs from "./pages/ContactUs/ContactUs"
import Profile from "./pages/Profile/Profile"
import AllEmployees from "./pages/AllEmployees/AllEmployees"
import Register from "./pages/Register/Register"

function App() {
  return (
    <>
    <Navbar/>
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/register" element={<Register/>}/>
      <Route path="/contactus" element={<ContactUs/>}></Route>
      <Route path="/profile" element={<Profile/>}/>
      <Route path="/allemployees" element={<AllEmployees/>} />
    </Routes>
    </>
  )
}

export default App
