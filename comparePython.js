//double slash to make comments

//set a variable
var y="bananas";
var num=6;
var arr =["John","Callie",y];
var mybool = true;

//output to the console
console.log(y); //output will be "bananas"

//output some strings
console.log("My name is Amanda.")
console.log("Hi Vinh")

var x = 10
function myFunction(){
    x=5;
    return;
}
myFunction();
console.log(x)

var myvar=10;
if(myvar<5){
    console.log("greater than 5");
}
else{
    console.log("less than 5");
}

function sayHello(name){
    var hellostr = "Hello, "+name;
    return hellostr;
}
console.log(sayHello("Mike"));

var x =sayHello("Vinh");
console.log(x)

sayHello();
console.log("You")

function myLoop(){
    for(var i=0; i<=10;i++){
        console.log(i);
    }
    return;
}
myLoop();

var bestArray=["Dog",1,2,3,"Vinh"];

function Loopy(arr){
    var newArray=[];
    for(var i= arr.length-1; i>=0; i--){
        newArray.push(arr[i]);
    }
    return newArray;
}
console.log(Loopy(bestArray));

arr.push("I love coding");