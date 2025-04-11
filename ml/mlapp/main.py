import sys
import os
from mlnode import *
from mlhandler import *
from mlinterpreter import *


# Main function for the node program.
# reads environmeental information for defining infos dictionary that is used in the 
# defines handlers that MyProgram and Handler classes use, these define the basic functionaltiies of the program
# initalizer initalizers the sockets and threads  
# node implementes the node functionlity. 

# The program reads environmental values for serverip, serverport, targetip, targetport and whatever HTTP is used.
# These are defined in the docker compose file.  They are used to define a handler that is used as a parameter for instanting NewHandler instances
# Handler is responsible for sockets functionalities, they decides how the node reacts based handler functions
# TODO change the handler class name since it overlaps with the function name too much. 

if __name__ == "__main__":
    
    infos = { }
    infos[ "serverinfo" ] = [ os.environ[ "serverip" ], os.environ[ "serverport" ] ]
    infos[ "clientinfo" ] = [ os.environ[ "clientip" ], os.environ[ "clientport" ] ]
    infos[ "target" ] = [ os.environ[ "targetip" ], os.environ[ "targetport" ] ]
    infos[ "http" ] = os.environ[ "ishttp" ]
    infos[ "addressfamily" ] = os.environ[ "addressfamily" ]
    infos[ "connectiontype" ] = os.environ[ "connectiontype" ]
    if( infos[ "connectiontype" ] ) == "":
        connectiontype = socket.SOCK_STREAM
    if( infos[ "addressfamily" ] ) == "":
        addressfamily = socket.AF_INET
    
    if infos[ "serverinfo" ][ 0 ] != "" and infos[ "clientinfo" ][ 0 ] != "":
        handler = MyHandler( middle_handler )
    elif infos[ "serverinfo" ][ 0 ] == "" and infos[ "clientinfo" ][ 0 ] != "":
        handler = MyHandler( client_handler )
    elif infos[ "serverinfo" ][ 0 ] != "" and infos[ "clientinfo" ][ 0 ] == "":
        handler = MyHandler( server_handler )

    interpreter = MLInterpreter( )
    model = MLModel( )
    node = NetNode( infos, handler, interpreter, model )
    node.init( )
    node.start( )

    

    