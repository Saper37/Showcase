

const net = require( "net" )
import { client_handler } from './handler_funcs'
import { STOP_NUM } from './myconstant'

var selip = process.env.TARGETIP
var selport = Number( process.env.TARGETPORT )


selip = "localhost"
selport = 8080

//var selport = 100
var client = net.connect( { port: selport}, {host: selip}, function( ){
    console.log( "connected to the server, on port " + selport )
    var message = client_handler( "" )
    client.write( message )
    console.log( "client send message " )
}
)
client.on( 'data', function( response ) {
    let data = response
    data = data.toString( )
    console.log( "client on data. data is " + data + " is it NaN " + isNaN( data ) )
    if( !isNaN( data ) ){
        data = client_handler( data )
        console.log( "client handler on data. data is " + data )
        if ( data == "stop" ){
            client.end( )
        }
        else{
            client.write( data )
    }
}
})

client.on( "end", function( ) {
    console.log( "disconneect from server" )
})

