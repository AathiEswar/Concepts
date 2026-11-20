const user = false;
const watchCat = false;
function handle (){
    return new Promise((resolve , reject) => {
    if(user){
        reject("User left T-T")
    }
    else if(watchCat){
        reject("User wasting time")
    }
    else{
        resolve("Yay !!")
    }
})
}

handle().then((msg) => {
    console.log("Success" + msg);
})
.catch((err) => {
    console.log("Fail " + err);
})