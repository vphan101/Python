// double slash to make a comment

// set a variable
var y = "bananas";
var num = 5;
var arr = ["Vinh", "Callie", y];
var mybool = true;

//output to the console
console.log(y);

//output some strings
console.log("My name is Vinh")

//conditionals
if(num > 10){
    console.log("big");
}
else if(num == 10){
    console.log("equal")
}
else{
    console.log("small")
}

//loops
for(var  i=1; i<11; i++){
    console.log(i);
}

for(var x=0; x<arr.length; x++){
    console.log(arr[x]);
}

//add and remove and array
arr.push("i love coding");
console.log(arr)

arr.pop() //last index

console.log(arr.length)