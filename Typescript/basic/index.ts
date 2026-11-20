//  ****** EXPLICIT TYPE CONVERSION *****

// for function parameters 
function add(a :number , b : number){
    return a+b;
}

// for primitive types 
var username : string = "hello";
var age : number = 21;
var isStudent : boolean = true ;

// for arrays 
var hobbies : string[] = ["Drawing" , "Guitar" , "Workout"];
var classAge : number[] = [18 , 20 , 21 , 50];
var isStudents : boolean[] = [true , false , true ];

// for objects 
// define the entire structure 
var person : {
    name : string , 
    age : number
} ; 

person = {
    name : "Aathi",
    age : 21,
}

// array of objects with structure 
var persons : {
    name : string , 
    age : number 
}[];

persons = [{name : "Aathi" , age : 21} , {name : "Eswar" , age : 5}]

// type inference 
// its where the type of the var is identified by TS using the value assigned to it 
// IMPLICIT Type conversion By TS
var className = "CSE";
// className = 123; gives an error coz TS sets classNmae : string by itself 

// UNION types 
// allow multiple types to be integrated 

var coursename : string | number ;

coursename = "CSE";
coursename = 12;

// no error coz both types are accepted!


// TYPE ALIAS 
// declaring a userDefined type and alias it to some other variable 
type CAR = {
    name : string ,
    carId : number 
}
// using the userdefined type 
var car : CAR;
car = {
    name : "Ferrari",
    carId : 1
}

// function types : 
function printVar( a : any ){
    console.log(a);
    
}

// no return so type is void 
// any - any type ( completely negates TS )


// Generics

// function insetAtEnd(array : any[] , value : any){
//     return [...array , value];
// }

// // number array 
// const array = [1 , 2, 3, 4,5]
// // the return is of any type too 
// const newArray = insetAtEnd(array , 6);
// // the newArray of numbers is still considered as any data type array 
// console.log(newArray);


function inserAtEnd<T>(array:T[]  , value : T){
    return [...array , value];
}
// since the type is generic the value that is used will be integrated to the array hence it is a number[] now 
const array = [1,2,3,4,5];
const newArray = inserAtEnd(array , 6);





