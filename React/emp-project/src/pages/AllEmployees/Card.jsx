
function Card(props) {
  return (
    <div className="emp-card">
        <h4>{props.name}</h4>
        <p>Age : {props.age}</p>
        <p>Designation : {props.designation}</p>
        <p>Skills : {props.skills}</p>
    </div>
  )
}

export default Card