import { client_handler, middle_handler, server_handler, handler_func } from "./handler_funcs"
import { MyInterpreter } from "./myinterpreter"
const network = require( "net")



export class MyHandler{
    handler: handler_func
    serverconnection = ""

    constructor( type: String, handler: handler_func ){
        switch( type ){
            case "client":
                this.handler = client_handler
                break;
            case "server":
                this.handler = server_handler
                break;
            case "middle":
                this.handler = middle_handler
                break;
            default:
                break;
        }
    }
    
    server_func( server, info, interpreter ){
        var selport = info[ 0 ]
        var selip = info[ 1 ]
        
        const node_server = network.createServer( function( serverconnection ) {
            serverconnection.on( "end", function ( ){
                server.close( )
            })
            serverconnection.on( "data", function( data ){
                var message = "stop"
                if( !isNaN( data ) ){
                    
                    data = interpreter.decode( data )
                    message = this.handler( data )
                    message = interpreter.encode( message )
                    serverconnection.write( message ) 
                }
                else if( data == "stop" ){
                    message = "stop"
                    serverconnection.write( message )
                    serverconnection.close( )
                }
            } )
            serverconnection.pipe( serverconnection )
            server.listen( { port: selport, host: selip})
        })
        
    }
    middle_func( server, info, interpreter: MyInterpreter ){
        // server definition
        var selport = info[ 0 ]
        var selip = info[ 1 ]
        const node_server = network.createServer( function( serverconnection ) {
            serverconnection.on( "end", function ( ){
                server.close( )
            })
            serverconnection.on( "data", function( data ){
                var message = "stop"
                if( !isNaN( data ) ){
                    data = interpreter.decode( data )
                    message = this.handler( data )
                    message = interpreter.encode( message )
                    serverconnection.write( message ) 
                }
                else if( data == "stop" )
                    serverconnection.write( message )
            } )
            serverconnection.pipe( serverconnection )
            server.listen( { port: selport, host: selip})
        })
        
        
        // Client definition
        const client = network.connect( {port:selport}, {host:selip }, function( ){
            client.on( "data", function( response ) {
                var message = response
                message = interpreter.encode( message )
                message = this.handler( message )
                message = interpreter.decode( message )
                if( message == "stop" )
                    client.end( )
                else{
                    client.write( message )
                }
            })
            client.on( "end", function( ){
                console.log( "disconnected")
            })
        } )

    }
    client_func( info, interpreter ){
        var selport = info[ 0 ]
        var selip = info[ 1 ]
        const client = network.connect( {port: selport}, {host:selip }, function( ){
            client.on( "data", function( response ) {
                var message = response
                message = interpreter.encode( message )
                message = this.handler( message )
                message = interpreter.decode( message )
                if( message == "stop" )
                    client.end( )
                else{
                    client.write( message )
                }
            })
            client.on( "end", function( ){
                console.log( "disconnected")
            })
        } )
    }
    
}
