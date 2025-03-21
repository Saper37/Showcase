import { MyHandler } from "./myhandler";
import { MyInterpreter } from "./myinterpreter";



export class Node{

    myhandler: MyHandler
    interpreter: MyInterpreter
    infos = [ ]

    constructor( infos: any, handler: MyHandler, interpreter: MyInterpreter  ){
        this.myhandler = handler
        this.interpreter = interpreter
        this.infos = infos
    }

    start( ){ 

        if( this.infos[ 0 ][ 0 ] != "" && this.infos[ 1 ][ 0 ] != "")
            this.myhandler.middle_func( )
        else if( this.infos[ 0 ][ 0 ] == "" && this.infos[ 1 ][ 0 ] != "")
            this.myhandler.client_func( )
        else if( this.infos[ 0 ][ 0 ] != "" && this.infos[ 1 ][ 0 ] == "")
            this.myhandler.server_func( )

    }

    stop( ){
        this.myhandler.stop( )
    }

}


