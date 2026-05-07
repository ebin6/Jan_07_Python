import React, { useState } from 'react'

function Register() {
  const [firstName,setfirstName]=useState("")
  const [email,setEmail]=useState("")
  return (
    <div>
        <form>
            <div>
                <label>First name</label>
                <input type='text' value={firstName} onChange={(e)=>setfirstName(e.target.value)}/>
            </div>
            
            <div>
                <label>E-mail</label>
                <input type='text' value={email} onChange={(e)=>setEmail(e.target.value)}/>
            </div>
            <div>
                <button type='submit'>SignUp</button>
            </div>
        </form>
    </div>
  )
}

export default Register