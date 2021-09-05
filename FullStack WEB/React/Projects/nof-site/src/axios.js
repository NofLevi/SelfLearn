function getApi(){
    axios.get("https://jsonplaceholder.typicode.com/users")
    .then(response=> {
        return response.data
        
    }).then(data=> {
        for(let key of data){
            console.log(key.name)
        }
    });
}
getApi()