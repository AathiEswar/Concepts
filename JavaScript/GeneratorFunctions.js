function* looper(){
    let count = 0 ;

    for(let i = 0 ; i < 5;i++){
        count++
        yield i;
    }

    //return count;

}

// save instance 
const iterator = looper();

// only gets the yiel when the next is
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());
console.log(iterator.next());