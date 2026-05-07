/*
function primeNumber(num){
    let is_prime=true
    if(num>2){
        for(let i=2;i<num;i++){
            if(num%i==0){
                console.log(`${num} is not a prime number`)
                is_prime=false
                break
            }
        }
        if(is_prime){
            console.log(`${num} is a prime number`)
        }
    }
    else{
        console.log(`${num} is not a prime number`)
    } 

}
primeNumber(23)
*/

const greet=(std_name)=>{
    console.log(`Hello ${std_name}`)
}

greet("Ebin") 