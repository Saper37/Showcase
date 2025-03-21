function displaymessage( ){
    let name = document.getElementById( "inputname" ).innerHTML
    let header = document.getElementById( "headerOne").innerHTML
    if( name != null ){
        name = "hello ${name}"
        header += " " + name        
    }
    return name
}

document.getElementById( "inputname" ).addEventListener( "click", displaymessage )