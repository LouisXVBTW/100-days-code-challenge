function findNemo(string) {
    index = string.indexOf("Nemo");
    if (index != -1) {
        console.log(`I found Nemo at ${index}`)
    }else{
        console.log("I can't find Nemo")
    }
}

findNemo("I am finding Nemo !");