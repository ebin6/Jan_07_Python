function Login(){
    return(
        <div>
            <form>
                <h2>Login</h2>
                <label>Username</label>
                <input type="text" name="username"/>
                <label>Password</label>
                <input type="password" name="password"/>
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default Login