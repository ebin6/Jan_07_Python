// Array 
let arr=["Kochi",12,3,'JavaScript']
for(let i=0;i<arr.length;i++){
    console.log(arr[i])
}

// Object

let student={std_name:"Ebin",age:25,place:"Kochi"}
delete student.age

console.log(student)

arr.forEach((k)=>{
    console.log(k)
})

arr.unshift("Ebin")
console.log(arr)

arr.splice(1,2,"Tesna")
console.log(arr)