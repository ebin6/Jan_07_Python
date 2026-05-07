
function Profile() {
  const user={
    name:"Ebin",
    designation:"Python Django Developer",
    skills:"Python,Django,HTML,CSS,JavaScript"
  }
  return (
    <div>
        <h1>{user.name}</h1>
        <p>Designation : {user.designation}</p>
        <p>Skills : {user.skills}</p>
    </div>
  )
}

export default Profile