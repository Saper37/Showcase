
from nacl.exceptions import ValueError as naclValueError
from nacl.exceptions import CryptoError
from nacl.public import PrivateKey, PublicKey
from nacl.encoding import Base64Encoder
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
    #if isinstance( num, bytes ):
    #    num = Base64Encoder.decode( num )
    
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
    except ( ValueError ):
        value = endvalue
        print( "server_handler error message " )

    print( "server_handle value is {}".format( value ) )
    return value #Base64Encoder.encode( value )

    

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
    #if isinstance( num, bytes ):
    #    num = Base64Encoder.decode( num )
    try:
        
        if interpreter == None:
            
            num = int( num ) if not num is None else None
            if num == None:
                value = startvalue

            elif num < LIMIT_PROC:
                value = num * 3
            else:
                value = endvalue  
            print( "middle handle interpreter is None. value is {}".format( value ) )  
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
                print( "middle handle interpreter is None. value is {}".format( value ) )
            value = interpreter.encode( value, strformat, targetkey )
    except(AttributeError ):
        value = endvalue
        print( "middle_handler error message " )
    print( "middle_handler value is {}".format( value ) )
    return value #Base64Encoder.encode( value )

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
    #if isinstance( num, bytes ):
    #    num = Base64Encoder.decode( num )
    
    try:
        if interpreter == None:
            value = int( num ) if not num is None else None
        else:
            print( "client handler num is {} num is None {}".format( num, num == None ))
            if num == None:
                value = startvalue.to_bytes( )
                print( "client handler if statement")
                #value = bytes( repr( startvalue ), encoding=strformat )

            elif num == endvalue:
                print( "client handler elif statement")
                value = endvalue
            else:
                print( "client handler else statement")
                value = interpreter.decode( num, strformat, targetkey )
                value = value.from_byte( value, "big", signed=True)
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
    return value #Base64Encoder.encode( value )

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
    for x in range( 0, len( rec_message ) ):
        m = rec_message[ x ].split( b"<END>")
        for x1 in range( len( m ) ):
            if m[ x1 ] == b"<END>":
                rec_message.append( m[ x1 ] )
    if rec_message[ -1 ] == byte_endvalue or rec_message[ -1 ] == b'':
        return byte_endvalue
    print( "read_message rec_message is {} rec_message type is {}".format( rec_message, type( rec_message ) ) )
    #comparison, message = rec_message[ message_index :: ], rec_message[ 0 : message_index ]
    return rec_message

def serverhandshake( server, interpreter ):

        server_accepted = False
        pk = None
        endvalue = b"<END>"
        ackvalue = b"<ACK>"
        targetkey = "client"
        connected = False
        message = None
        print( "serverhandshake started" )
        pk = interpreter.getPk( )
        client, addr = server.accept( )
        message = read_message( client )
        print( "serverhandshake read_message is {}".format( message ) )
        interpreter.setTargetPk( message, targetkey )
        send_message( client, pk )
        print( "serverhandshake ended" )
        return client, message

def clienthandshake( client, interpreter ):
        pk = None
        message = ""
        connected = False
        targetkey = "server"
        time.sleep( 3 )
        print( "clienthandshake started" )
        pk = interpreter.getPk(  )
        send_message( client, pk )
        message = read_message( client )
        print( "clienthandshake message from server is {}".format( message ) )
        interpreter.setTargetPk( message, targetkey )
        print( "clienthandshake ended" )
        return client, message

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
        print( "{} message is {} handled message is {}".format( "server_func", message, handled_message ) )
        send_message( client, handled_message )
        while handled_message != endvalue:
            try:
                #message = client.recvfrom( 1024 ) UPD
                message = read_message( client )
                print( "server received message {}".format( message ) )
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
                print( "server_func: No connection to client")
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
        otherclient, message = serverhandshake( server, interpreter )
        
        if message == endvalue:
            send_message( otherclient, message )
        myclient, message = clienthandshake( client, interpreter )
        receiving="server"
        handled_message = self.handler( message, receiving, interpreter=interpreter, strformat=self.strformat  )
        print( "{} message is {} handled message is {}".format( "middle_func server ", message, handled_message ) )
        send_message( otherclient, handled_message )
        receiving="client"
        handled_message = self.handler( message, receiving, interpreter=interpreter, strformat=self.strformat  )
        print( "{} message is {} handled message is {}".format( "middle_func client ", message, handled_message ) )
        send_message( myclient, handled_message )
        while handled_message != endvalue:
            receiving = "client"
            try:
                
                message = read_message( myclient )
                print( "middle client received message {}".format( message ) )
                self.messages[ "client" ].append(  message )
                handled_message = self.handler( message, receiving, interpreter=interpreter, strformat=self.strformat  )
                send_message( myclient, handled_message )
                if handled_message == endvalue or client.fileno( ) == -1:
                    time.sleep( 2 )
                    myclient.close( )
                    return True
                
                counter[ 0 ] = 0
            except ( BrokenPipeError, ConnectionResetError ):
                counter[ 0 ] += 1
                time.sleep( 2 )
                if counter[ 0 ] > counterlimit:
                    myclient.close( )
                    otherclient.close( )
                    return True

            
            receiving = "server"
            try:
                message = read_message( otherclient )
                print( "middle server received message {}".format( message ) )
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
        myclient.close( )
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
        print( "{} message is {}".format( "client_func", message ) )
        self.messages[ "client" ].append( message )
        while message != endvalue:
            try:
                message = read_message( client )
                self.messages[ "server" ].append( [ message ] )
                print( "client received message {}".format( message ) )
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
    
    
    