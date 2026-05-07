import { Link } from "react-router-dom"
function Navbar() {
  return (
    <div>
        <header>
            <nav>
                <div className="logo">  
                    <span>OneTeam</span>
                </div>
                <div>
                    <ul className="nav-links">
                         <li><Link to="/">Home</Link></li>
                         <li><Link to="/login">Login</Link></li>
                         <li><Link to="/contactus">Contact Us</Link></li>
                         <li><Link to="/register">Register</Link></li>
                         <li><Link to="/profile">Profile</Link></li>
                         <li><Link to="/allemployees">All Employees</Link></li>
                    </ul>
                </div>
            </nav>
        </header>
    </div>
  )
}

export default Navbar 