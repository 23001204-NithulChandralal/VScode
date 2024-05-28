get_avg = (a,b) => {
    return(a + b) / 2;
}

let a = parseInt(prompt("Enter the first integer: ")) ;
let b = parseInt(prompt("Enter the second integer: ")) ;
const result = get_avg(a ,b);

console.log(result);

alert("Average of " + a + " and " + b + " is " + result )