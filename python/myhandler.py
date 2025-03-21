
from nacl.exceptions import ValueError as naclValueError
from nacl.exceptions import CryptoError
from nacl.public import PrivateKey, PublicKey
from handler import *
from myexceptions import *
import struct

LIMIT_PROC = 1000000

# Consists of NewHandler class and handler functions.

# functions server_handler, middle_handler, client_handler

# function server_handler
# param num, input value 
# param receiving, default None, not really used 
# param interpreter, default None, responsible for providing data handling 
# 
def server_handler( num, receiving=None, interpreter=None, strformat=None ):
    endvalue = b"<END>"
    targetkey = receiving
    print( "server_handler num is {} ".format( num ) )
    try: 
        if interpreter is None:
            num = int( num ) if not num is None else None
            if num < LIMIT_PROC:
                num += 1
            value = num
        else:

            if num == endvalue or num == b'':
                    value = endvalue
                    
            else:
                value = interpreter.decode( num, strformat, targetkey )
                value = int( value )
                if value < LIMIT_PROC:
                    value += 1
                elif value >= LIMIT_PROC:
                    value = endvalue
            value = interpreter.encode( value, strformat, targetkey)
    except ( ValueError, naclValueError, CryptoError, AttributeError ):
        value = endvalue
        print( "server_handler error message " )

    print( "server_handle value is {}".format( value ) )
    return value

    

# function middle_handler
# param num, input value 
# param receiving, default None, establishes whatever handler is server or client
# param interpreter, default None, responsible for providing data handling 
# 
def middle_handler( num=None, receiving=None, interpreter=None, strformat=None ):
    if strformat != None and interpreter == strformat:
        raise MyException( "Interpreter and strformat need to be defined " )

    endvalue = b"<END>"
    targetkey = receiving
    startvalue = 1
    print( "middle handle message from the client num is {} receiving is {}".format( num, receiving ) )
    try:
        if interpreter == None:
            num = int( num ) if not num is None else None
            if num == None:
                value = startvalue

            elif num < LIMIT_PROC:
                value = num * 3
            else:
                value = endvalue    
        else:
                
            if num == None:
                value = startvalue
            elif num == endvalue:
                value = endvalue
            else:
                value = interpreter.decode( num, strformat, targetkey )
                value = int( value )
                if value:
                    value = endvalue
                elif value < LIMIT_PROC:
                    value = value * 3
                else:
                    value = endvalue
            value = interpreter.encode( value, strformat, targetkey )
    except( ValueError, naclValueError, CryptoError, AttributeError ):
        value = endvalue
        print( "middle_handler error message " )
    print( "middle_handler value is {}".format( value ) )
    return value

# function client_handler
# param num, input value 
# param receiving, default None, not in use in this function
# param interpreter, default None, responsible for providing data handling 
# 
def client_handler( num=None, receiving=None, interpreter=None, strformat=None):
    endvalue = b"<END>"
    startvalue = 1
    targetkey = receiving
    print( "client_handler num is {} ".format( num ) )
    try:
        print( "client_handle num is {}".format( num ) )
        if interpreter == None:
            value = int( num ) if not num is None else None
        else:
            print( "client handler num is {} num is None {}".format( num, num == None ))
            if num == None:
                value = startvalue
                print( "client handler if statement")
                #value = bytes( repr( startvalue ), encoding=strformat )

            elif num == endvalue:
                print( "client handler elif statement")
                value = endvalue
            else:
                if num == None:
                    print( "client handler second if statement")
                    value = startvalue
                else:
                    print( "client handler else statement")
                    value = interpreter.decode( num, strformat, targetkey )
                    if value < LIMIT_PROC:
                        value *= 3
                    else:
                        value = endvalue
            value = interpreter.encode( value, strformat, targetkey )
    except ( ValueError ):
        print( "client_handler error message " )
        value = endvalue
        #value = bytes( endvalue, encoding=strformat )
        
    print( "client_handler value is {}".format( value ) )
    return value

def send_message( socket, message ):  
    
    print( "send message is {} type of message is {}".format( message, type( message  ) ) )
    res = socket.sendall( message )

def read_message( client ):

    buffersize = 1024
    byte_endvalue = b"<END>"
    endvalue = "<END>"
    #print( "read_message client fileno {}".format( client.fileno( ) ) )
    
    rec_message = client.recv( buffersize )
    foundEnd = rec_message.find( byte_endvalue )
    rec_message = rec_message.split( b"<RETRY>" )
    if rec_message[ 0 ] == byte_endvalue or rec_message[ 0 ] == b'':
        return byte_endvalue
    print( "read_message rec_message is {} rec_message type is {}".format( rec_message, type( rec_message ) ) )
    #comparison, message = rec_message[ message_index :: ], rec_message[ 0 : message_index ]
    return rec_message

def serverhandshake( server, interpreter ):

        server_accepted = False
        pk = None
        endvalue = b"<END>"
        targetkey = "client"
        connected = False
        message = None
        print( "serverhandshake " )
        while message != endvalue:
            if not server_accepted:
                client, addr = server.accept( )
                print( "server_func client is accepted " )
            try:
                client.settimeout( 4 )
                message = read_message( client )
                print( "serverhandshake is {} endvalue equals {}".format( message, message == endvalue ) )
                if message != b'' and message != endvalue:
                    interpreter.setTargetPk( message, targetkey)
                    connected = True
                elif message == endvalue:
                    break
            except TimeoutError:
                print( "serverhandshake TimeoutError")
            client.settimeout( None )
            
            
            if pk == None:
                print( "server_func getPk " )
                pk = interpreter.getPk( )
            if connected and message != endvalue:
                send_message( client, pk )
                message = read_message( client )
                break
            
        return client, message

def middlehandshake( client, server, interpreter ):
        print( "middlehandshake " )
        server_accepted = False
        otherclient = None
        pk = None
        message = ""
        endvalue = b"<END>"
        targetkey = "client"
        contacted = False
        while message != endvalue:
            if not server_accepted:
                otherclient, addr = server.accept( )
                server_accepted = True
                print( "middle_func otherclient accepted " )
            try:
                otherclient.settimeout( 3 )
                message = read_message( otherclient )
                if message != b'' and message[ 0 ] != endvalue:
                    interpreter.setTargetPk( message, targetkey )
                    contacted = True
                    print( "middle_func message {} read".format( message ) )
                elif message == endvalue:
                    break
            except TimeoutError:
                print( "middlehandshake TimeoutError")
            otherclient.settimeout( None )
            
            if pk == None:
                print( "middle_func getPk " )
                pk = interpreter.getPk(  )
            if contacted and message != endvalue:
                send_message( otherclient, pk )
                message = read_message( otherclient )
            elif message == endvalue:
                break
        if message == endvalue:
            print( "middle handshake failed ")
            return otherclient, message
        message = ""
        targetkey = "server"
        print( "client shaked" )
        while message != endvalue:
            send_message( client, pk )
            try:
                client.settimeout( 3 )
                message = read_message( client )
            except TimeoutError:
                print( "middlehandshake middleclient timeouterror " )
            client.settimeout( None )
            
            if message != b'<RETRY>':
                break
            
        return otherclient, message

def clienthandshake( client, interpreter ):
        pk = None
        message = ""
        endvalue = b"<END>"
        connected = False
        targetkey = "server"
        print( "clienthandshake " )
        while message != endvalue:
            print( "client_func started pk get" )
            if pk == None:
                pk = interpreter.getPk(  )
            send_message( client, pk )
            print( "client_func messaged send {}".format( pk ) )
            try:
                client.settimeout( 2 )
                message = read_message( client )
                print( "message from middle {} ".format( message ))
                connected = True
            except TimeoutError:
                print( "clienthandshake TimeoutError")
            client.settimeout( None )
            
            if connected and message != endvalue:
                print( "client_func message read " )
                interpreter.setTargetPk( message, targetkey )
                break
            elif message == endvalue:
                break
            else:
                message = b'<RETRY>'
                send_message( client, message )
                
        return message

# Class MyHandler extends Handler class
# function __init__
# function server_func
    # function provides basic receive - response functionality for the server 
    # function uses handler function to handle invidiual messaging
    # func param server, socket that the function accepts
    # func param interpreter, interpreter class responsible for handling message encyrption and decryption, used in handler function 
    
# function middle_func
    # function uses handler function to handle messaging
    # func param server, socket that the function accepts
    # func param interpreter, interpreter class responsible for handling message encyrption and decryption, used in handler function 
    
# function client_func

class MyHandler( Handler ):
    
    # function __init__
    # param handler, function responsible for handling messages
    # param strformat, 
    def __init__(self, handler, strformat="utf-8"):
        self.messages = {}
        self.handler = handler
        self.strformat = strformat
    
    def server_func(self, server, interpreter):

        counter = 0
        endvalue = b"<END>"
        self.messages[ "server" ] = [ ]
        
        client, message = serverhandshake( server, interpreter )
        handled_message = self.handler( message, receiving="client", interpreter=interpreter, strformat=self.strformat )
        send_message( client, handled_message )
        while handled_message != endvalue:
            try:
                #message = client.recvfrom( 1024 ) UPD
                message = read_message( client )
                self.messages[ "server" ].append(  message )
                #decoded_message = message.decode( encoding=self.strformat )
                handled_message = self.handler( message, receiving="client", interpreter=interpreter, strformat=self.strformat )
                send_message( client, handled_message )
                self.messages[ "server" ].append( handled_message )

                if handled_message == endvalue:
                    time.sleep( 1 )
                    client.close( )
                    return True

            except ConnectionError:
                print( "Server: No connection to client")
                time.sleep( 1 )
                counter += 1
                if counter > 5:
                    return True
        client.close( )
        return True
    
    def middle_func(self, client, server, interpreter):

        self.messages[ "client" ] = [ ]
        self.messages[ "server"] = [ ]
        endvalue = b"<END>"
        counter = [ 0, 0 ]
        counterlimit = 5
        message = ""
        receiving = "client"
        otherclient, message = middlehandshake( client, server, interpreter )
        if message == endvalue:
            send_message( client, message )
            send_message( otherclient, message )
        handled_message = self.handler( message, receiving, interpreter=interpreter, strformat=self.strformat  )
        send_message( client, handled_message )
        while handled_message != endvalue:
            receiving = "client"
            try:
                
                message = read_message( client )
                self.messages[ "client" ].append(  message )
                handled_message = self.handler( message, receiving, interpreter=interpreter, strformat=self.strformat  )
                send_message( client, handled_message )
                if handled_message == endvalue or client.fileno( ) == -1:
                    time.sleep( 2 )
                    client.close( )
                    return True
                
                counter[ 0 ] = 0
            except ( BrokenPipeError, ConnectionResetError ):
                counter[ 0 ] += 1
                time.sleep( 2 )
                if counter[ 0 ] > counterlimit:
                    client.close( )
                    otherclient.close( )
                    return True

            
            receiving = "server"
            try:
                message = read_message( otherclient )
                self.messages[ "server" ].append( message )
                handled_message = self.handler( message, receiving, interpreter=interpreter, strformat=self.strformat )
                send_message( otherclient, handled_message )
                if handled_message == endvalue:
                    time.sleep( 2 )
                    otherclient.close( )
                    client.close( )
                    return True
                counter[ 1 ] = 0
            except ( ConnectionResetError, BrokenPipeError ):
                counter[ 1 ] += 1
                time.sleep( 2 )
                if counter[ 1 ] > counterlimit:
                    client.close( )
                    otherclient.close( )
                    return True
        otherclient.close( )
        client.close( )
        return True

    def client_func(self, client, interpreter):
        
        self.messages[ "client" ] = [ ]
        self.messages[ "server" ] = [ ]
        endvalue = b"<END>"
        counter = 0
        clienthandshake( client, interpreter )
        print( "middle shaked " )
        message = client_handler(  receiving="server",interpreter=interpreter, strformat=self.strformat )
        send_message( client, message )
        self.messages[ "client" ].append( message )
        while message != endvalue:
            try:
                message = read_message( client )
                self.messages[ "server" ].append( [ message ] )
                handled_message = self.handler( message, receiving="server", interpreter=interpreter, strformat=self.strformat )
                send_message( client, handled_message )
                self.messages[ "client" ].append( handled_message )
                if handled_message == endvalue or client.fileno( ) == -1:
                    time.sleep( 1 )
                    client.close( )
                    return True
            except ConnectionError:
                time.sleep( 1 )
                counter += 1
                if counter > 5:
                    return True
        client.close( )
        return True
    
    
    