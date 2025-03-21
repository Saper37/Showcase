
function hello(s: string ){
    console.log( s )
}

let message: string = "So this does something";

function greeting( fn: ( a: string ) => void ){
    fn( message )
}

const examplefunc = ( par1, par2, par3  ) => {
    
    return "Example's id is  " + par1 + " Example's name is " + par2 + " Example's type is " + par3 
}

interface Example{
    id: number,
    name: string
}
type typeexample = 'no example' | 'example';

function getExample( id, name ) : Example{
    return {
        id: id,
        name: name
    }
}

const app = document.getElementById( "app" )
const app1 = document.getElementById( "app1")
const p = document.getElementById( "p" )

let heading = document.createElement( "h1" )
heading.textContent = message

let heading2 = document.createElement( "h2" )
heading2.textContent = message 

let heading3 = document.createElement( "h3" )


let nameinput = document.createElement( "input" )
nameinput.addEventListener( "change", function( ) {
    let text: string = nameinput.value

    if ( text === "heheh" && heading3 !== null ){
        heading3.textContent = "mikä on niin hauskaa?"
    }
})

var example = getExample( 3, "example" )

heading3.textContent = examplefunc( example.id,example.name, typeof( example ))

app?.appendChild( heading2 )
app1?.appendChild( heading )
app?.appendChild( heading3 )
app1?.appendChild( nameinput ) 
