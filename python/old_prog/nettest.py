import sys
import os
from netnode import *
from newhandler import *
from socketnodeinitializer import *
from python.myprogram import *

# Main function for the node program.
# reads environmeental information for defining infos dictionary that is used in the 
# defines handlers that MyProgram and Handler classes use, these define the basic functionaltiies of the program
# initalizer initalizers the sockets and threads  
# node implementes the node functionlity. 

# The program reads environmental values for serverip, serverport, targetip, targetport and whatever HTTP is used.
# These are defined in the docker compose file.  They are used to define a handler that is used as a parameter for instanting NewHandler instances
# Handler is responsible for sockets functionalities, they decides how the node reacts based handler functions
# TODO change the handler class name since it overlaps with the function name too much. 
# 
# SocketNodeInitalizer uses myprogram
#
# initalizer and info are used for defining NetNode
#
# NetNode then initializes and starts the node. 

if __name__ == "__main__":
    
    infos = { }
    infos[ "serverinfo" ] = [ os.environ[ "serverip" ], os.environ[ "serverport" ] ]
    infos[ "clientinfo" ] = [ os.environ[ "clientip" ], os.environ[ "clientport" ] ]
    infos[ "target" ] = [ os.environ[ "targetip" ], os.environ[ "targetport" ] ]
    infos[ "http" ] = os.environ[ "ishttp" ]
    print( "info is {}".format( infos ) )
    if infos[ "serverinfo" ][ 0 ] == "middle" or infos[ "serverinfo" ][ 0 ] == "middle_last":
        handler = middle_handler
    elif infos[ "serverinfo"][ 0 ] == "server":
        handler = server_handler
    elif infos[ "serverinfo" ][ 0 ] == "":
        handler = client_handler
    print( "handler is {}".format( handler ) )
    myprogram = MyProgram( NewHandler( "utf-8", handler ) )
    initializer = SocketNodeInitializer( myprogram )
    node = NetNode( infos, initializer )
    node.init( ) 
    node.start( )
    
        
    