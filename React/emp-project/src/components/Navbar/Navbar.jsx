import { Link } from "react-router-dom"
function Navbar() {
  return (
    <div>
        <header>
            <nav>
                <div class="logo">  
                    <span>OneTeam</span>
                </div>
                <div>
                    <ul class="nav-links">
                         <li><Link to="/">Home</Link></li>
                         <li><Link to="/login">Login</Link></li>
                         <li><Link to="/login">Contact Us</Link></li>
                            <li><Link to="/login">Register</Link></li>
                       
                    </ul>
                </div>
            </nav>
        </header>
    </div>
  )
}

export default Navbar