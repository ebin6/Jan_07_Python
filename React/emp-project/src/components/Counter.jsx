import { useState } from "react"

function Counter() {
  const [count,SetCount]=useState(0);

  function Increment(){
    SetCount(count+1)
    console.log(count)
  }

  function Decrement(){
    SetCount(count-1)
    console.log(count)
  }

  return (
    <div>
        <h3>{count}</h3>
        <button onClick={Increment}>+ Increment</button>
        <button onClick={Decrement}>- Decrement</button>
    </div>
  )
}

export default Counter