import { Node } from "./node";
import { MyHandler } from "./myhandler";
import { MyInterpreter } from "./myinterpreter";
import { client_handler, middle_handler, server_handler, handler_func } from "./handler_funcs";
const process = require( "process" )

main: ( ) => {
    
    const serverinfo = [ process.env.serverip as string, process.env.serverport as string ]
    const clientinfo = [ process.env.clientip as string, process.env.clientport as string ]
    const targetinfo = [ process.env.targetip as string, process.env.targetport as string ]
    const ishttp = process.env.ishttp as string
    const addressfamily = process.env.addressfamily as string
    const connectiontype = process.env.connectiontype as string
    const encode = process.env.encode as string
    var handler: handler_func
    var type: String = ""

    if( serverinfo[ 0 ] != "" && clientinfo[ 0 ] != "" ){
        handler = middle_handler
        type = "middle"
    }
    else if( serverinfo[ 0 ] != "" && clientinfo[ 0 ] == "" ){
        handler = server_handler
        type = "server"
    }
    else if( serverinfo[ 0 ] == "" && clientinfo[ 0 ] != "" ){
        handler = client_handler
        type = "client"
    }
    else{
        handler = undefined
    }
        
    const infos = [ serverinfo, clientinfo, targetinfo, ishttp, addressfamily, connectiontype, encode ]
    var myHandler = new MyHandler( type, handler )
    var interpreter = new MyInterpreter( )
    var mynode = new Node( infos, myHandler, interpreter )
    mynode.start( )
}