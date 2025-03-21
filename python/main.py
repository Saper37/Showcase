import sys
import os
import socket
import time
from myexceptions import *
from nacl.public import PrivateKey, Box
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from netnode import *
from myhandler import *
from myinterpreter import *



# Main function for the network node program.
# reads environmeental information for defining infos dictionary that is used in the 
# defines handlers that MyProgram and Handler classes use, these define the basic functionaltiies of the program
# initalizer initalizers the sockets and threads  
# node implementes the node functionlity. 

# The program reads environmental values for serverip, serverport, targetip, targetport and whatever HTTP is used.
# These are defined in the docker compose file.  They are used to define a handler that is used as a parameter for instanting NewHandler instances
# Handler is responsible for sockets functionalities, they decides how the node reacts based handler functions


if __name__ == "__main__":
    
    infos = { }
    infos[ "serverinfo" ] = [ os.environ[ "serverip" ], os.environ[ "serverport" ] ]
    infos[ "clientinfo" ] = [ os.environ[ "clientip" ], os.environ[ "clientport" ] ]
    infos[ "target" ] = [ os.environ[ "targetip" ], os.environ[ "targetport" ] ]
    infos[ "http" ] = os.environ[ "ishttp" ]
    infos[ "addressfamily" ] = os.environ[ "addressfamily" ]
    infos[ "connectiontype" ] = os.environ[ "connectiontype" ]
    if( infos[ "connectiontype" ] ) == "SOCK_STREAM":
        infos[ "connectiontype" ] = socket.SOCK_STREAM
    if( infos[ "addressfamily" ] ) == "AF_INET":
        infos[ "addressfamily" ] = socket.AF_INET
    #print( "main py ", infos[ "serverinfo" ],infos[ "serverinfo" ][ 0 ] != '', infos[ "clientinfo" ][ 0 ] )
    #print( "main py ", infos[ "clientinfo" ] )
    if infos[ "serverinfo" ][ 0 ] != '' and infos[ "clientinfo" ][ 0 ] != '':
        handler_func = middle_handler
        print( "main py middle defined ", handler_func)
        time.sleep( 4 )
        
    elif infos[ "serverinfo" ][ 0 ] != '' and infos[ "clientinfo" ][ 0 ] == '':
        handler_func = server_handler
        time.sleep( 6 )

    elif infos[ "serverinfo" ][ 0 ] == '' and infos[ "clientinfo" ][ 0 ] != '':
        handler_func = client_handler
        time.sleep( 2 )
        
    else:
        raise MyException( "Env Info not configured correctly. Serverinfo or clientinfo are invalid")
 
    # Dummy conditional for now TODO add conditional logic for multiple interpreters if needed
    # for now hard coded to MyInterpreter, NOT safe 

    # Crypto module
    #salt_length = 16
    #blength = 128
    #salt = os.urandom( salt_length )
    #key = AESGCM.generate_key( bit_length= blength )
    #f = AESGCM( key )
    
    sk = PrivateKey.generate(  )

    interpreter =  MyInterpreter( sk )
    handler = MyHandler( handler_func )
    #print( "main py handler is defined as {}".format( handler_func ))
    node = NetNode( infos, interpreter, handler )
    node.init( )
    node.start( )

    

    