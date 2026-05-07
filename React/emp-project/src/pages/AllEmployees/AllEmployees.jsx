import "./AllEmployees.css"
import Card from "./Card";
function AllEmployees() {
    const employees = [
    {
        id:1,
        name: "Arjun Nair",
        age: 25,
        designation: "Frontend Developer",
        skills: ["HTML", "CSS", "JavaScript", "React"]
    },
    {
        id:2,
        name: "Meera Iyer",
        age: 28,
        designation: "Backend Developer",
        skills: ["Node.js", "Express", "MongoDB", "API Development"]
    },
    {
        id:3,
        name: "Rahul Menon",
        age: 30,
        designation: "Full Stack Developer",
        skills: ["JavaScript", "React", "Node.js", "SQL"]
    },
    {
        id:4,
        name: "Anjali Pillai",
        age: 26,
        designation: "UI/UX Designer",
        skills: ["Figma", "Adobe XD", "Wireframing", "Prototyping"]
    },
    {
        id:5,
        name: "Vivek Kumar",
        age: 32,
        designation: "DevOps Engineer",
        skills: ["Docker", "Kubernetes", "AWS", "CI/CD"]
    }
    ];
  return (
    <div className="all-emp">
            {
                employees.map((emp)=>(
                   <Card key={emp.id} name={emp.name} age={emp.age} designation={emp.designation} skills={emp.skills}/>
                    
                    
                ))
            }

    </div>

  )
}

export default AllEmployees