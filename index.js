console.log("I am js file")
let data = {}
let handleChange = (event)=>{
    let {name, value} = event.target;
    data = {...data, [name]: value};
    console.log(data)
};
