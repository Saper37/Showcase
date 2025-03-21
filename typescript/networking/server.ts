
import { Worker, isMainThread, workerData, parentPort} from 'node:worker_threads';


// Node.js networking functionality
const servernet = require( "net" )
import { server_handler } from './handler_funcs';
import { STOP_NUM } from './myconstant'

var selip = process.env.TARGETIP
var selport = Number( process.env.TARGETPORT )
var ownerip = process.env.OWNERIP
var ownerport = process.env.OWNERPORT

function serverfunc( message: string ){
    var message_temp = ""
    while( message != "stop" ){
        message_temp = server_handler( message )
        message = String( message_temp )
    }
}

var serverconnection = ""
const server = servernet.createServer( function( serverconnection ){
    serverconnection.on( "end", function( ){
        console.log( "disconnected" )
        server.close( )
    })

    serverconnection.on( "data", function( data ){
        console.log( " serverconnection data event. data is " + data + " is it NaN " + isNaN( data ) )
        if( !isNaN( data ) ) {
            var message = server_handler( data )
            serverconnection.write( message )
        }
    } )
    //serverconnection.write( "hello" )
    //var message = ""
    serverconnection.pipe( serverconnection )
})



selport = 8080
selip = "localhost"
server.listen(  { port: selport, host: selip }, function( ){
    console.log( "listening")
})