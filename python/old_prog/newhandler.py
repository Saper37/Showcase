from handler import *

LIMIT_PROC = 1000000

# Consists of NewHandler class and handler functions.


def server_handler( num, receiving=None, interpreter=None ):
    endvalue = "stop"
    print( "server handle num is {}".format( num ) )
    try:
        print( "server_handle num is {}".format( num ) )
        num = int( num ) if not num is None else None
    except ValueError:
        num = endvalue
        return num
    print( "server handle num is {}".format( num ) )
    if num < LIMIT_PROC:
        return num + 1
    else:
        return endvalue
    
def middle_handler( num, receiving, interpreter=None ):
    endvalue = "stop"
    if receiving == "client":
        print( "middle handle message from the client num is {} receiving is {}".format( num, receiving ) )
        try:
            
            num = int( num )
            if num < LIMIT_PROC:
                return num * 3
        except ValueError:
            num = endvalue
            return num
        num = endvalue
        print( "middle handle says stop. num is {}".format( num ) )
        return num

    elif receiving == "server":
        print( "middle handle message from the server num is {} receiving is {}".format( num, receiving ) )
        try:
            
            num = int( num )
            if num < LIMIT_PROC:
                return num * 3
        except ValueError:
            print( "middle handle ", num )
            num = endvalue
            return num
        print( "middle handle ", num )
        num = endvalue
        print( "middle handle says stop. num is {}".format( num ) )
        return num
    else:
        raise MyExpection(" hello this happend in middle node")

def client_handler( num=None, receiving=None, interpreter=None):
    endvalue = "stop"
    if num == None:
        return 1
    print( "client handle num is {}".format( num ) )
    try:
        print( "client_handle num is {}".format( num ) )
        num = int( num ) if not num is None else None
    except ValueError:
        num = endvalue
        print( "client handle valueError ", num )
        return num
    print( "client handle ", num )
        
    if num < LIMIT_PROC:
        return num * 3
    print( "client handle says stop. num is {}".format( num ) )
    return "stop"


# Class NewHandler extends Handler
#  Handler responsible for receiving and handling  network data, uses handler function for decision making
#  TODO changes the class name, confusing with handler functions
#
# function __init__
#  param strformat. Format for encoding and decoding byte data
#  param handlr. handler function for handling received or to be send data.
# 
# function server_func
#  param server. The server socket defined in NodeInitalizer, started in Netnode
#  param interpreter responsible for decoding received messages and encoding the send messages.
#  the function accepts the connection of the server, initiazed variables that are used for handling the interaction
#  variable message refer to encoded messages, message1 refer to decoded message. 
#  endvalue defined here for defining the value that stops the node.
#  TODO change this to be defined on docker side.
#
# function middle_func
#  param middle. The middle socket defined in NodeInitalizer, started in Netnode
#  implements client and server functionality, decision which to use based on the handler type
#
# function client_func
#  param client. The client socket defined in NodeInitalizer, started in Netnode
#
class NewHandler( Handler ):
    def __init__( self, strformat="utf-8", handler=None ):
        self.parent = None
        #print( "newhandler strformat: {}\nhandler: {}".format( strformat, handler ))
        self.strformat = strformat
        self.counter = [ 0, 0 ]
        self.messages = { }
        self.handler = handler
            
    def server_func( self, server, interpreter=None ):
        client, addr = server.accept( )
        message = ""
        counter = 0
        endvalue = "stop"
        self.messages[ "server" ] = [ ]
        print( "server_func started " )
        #print( "server: client is {}. addr is {}".format( client, addr ) )

        while message != endvalue:
            try:
                #message = client.recvfrom( 1024 ) UPD
                message = client.recv( 1024 )
                print( "server func message is {}".format( message ) )
                message1 = message.decode( self.strformat )
                
                self.messages[ "server" ].append(  message1 )
                message1 = self.handler( message1, interpreter=interpreter )
                message1 = message1 if type( message1 ) == repr else repr( message1 )

                message = bytes( message1, encoding=self.strformat )
                client.sendall( message )
                self.messages[ "server" ].append( message )

                if message1 == endvalue:
                    time.sleep( 1 )
                    print( "server ended " )
                    client.close( )
                    return True

            except ConnectionError:
                print( "Server: No connection to client")
                time.sleep( 1 )
                counter += 1
                if counter > 5:
                    return True

    
    def middle_func( self, client, server, interpreter=None ):

        my_client, addr = server.accept( )
        self.messages[ "client" ] = [ ]
        self.messages[ "server"] = [ ]
        endvalue = "'stop'"
        counter = [ 0, 0 ]
        counterlimit = 5
        endvalue = "'stop'"
        message = ""
        print( "middle_func started " )
        while message != "stop":
            self.receiving = "client"
            try:
                #message = my_client.recvfrom( 1024 ) UPD
                message = my_client.recv( 1024 )
                print( "middle client func message is {}".format( message ) )
                message = message.decode( encoding=self.strformat )
                
                message1 = message
                self.messages[ "client" ].append(  message1 )
                if message == endvalue:
                    time.sleep( 2 )
                    print( "middle  ended " )
                    client.close( )

                    return True
                message = self.handler( message1, self.receiving, interpreter=interpreter  )
                message = message if type( message ) == repr else repr( message ) 
                message1 = bytes( message, encoding=self.strformat )
                client.sendall( message1 )
                counter[ 0 ] = 0
            except ( BrokenPipeError, ConnectionResetError ):
                counter[ 0 ] += 1
                time.sleep( 2 )
                if counter[ 0 ] > counterlimit:
                    client.close( )
                    my_client.close( )
                    print( "middle ended " )
                    return True

            
            self.receiving = "server"
            try:
                message = client.recvfrom( 1024 )
                print( "middle server func message is {}".format( message ) )
                message = message[ 0 ].decode( encoding=self.strformat )
                
                message1 = message
                if message1 == endvalue:
                    time.sleep( 2 )
                    print( "middle  ended " )
                    client.close( )

                    return True
                self.messages[ "server" ].append( message1 )
                message = self.handler( message1, self.receiving, interpreter=interpreter )
                message = message if type( message ) == repr else repr( message )
                print( "middle server func message is {}".format( message ) )
                if message == endvalue:
                    time.sleep( 2 )
                    print( "middle  ended " )
                    client.close( )

                    return True
                message1 = bytes( message, encoding=self.strformat )
                my_client.sendall( message1 ) 
                counter[ 1 ] = 0
            except ( ConnectionResetError, BrokenPipeError ):
                counter[ 1 ] += 1
                time.sleep( 2 )
                if counter[ 1 ] > counterlimit:
                    client.close( )
                    my_client.close( )
                    print( "middle ended " )
                    return True
                
    def client_func( self, client, interpreter=None ):
        self.messages[ "client" ] = [ ]
        self.messages[ "server" ] = [ ]
        endvalue = "stop"
        counter = 0
        message = self.handler(  )
        message1 = bytes( repr( message ), encoding=self.strformat )
        client.sendall( message1 )
        self.messages[ "client" ].append( message1 )
        print( "client_func started " )
        while message != "stop":
            try:
                #message = client.recvfrom( 1024 ) UPD
                message = client.recv( 1024 )
                print( "client_func message is {}".format( message ) )
                self.messages[ "server" ].append( [ message1 ] )
                message = self.handler( message, interpreter=interpreter )
                message1 = bytes( message if type( message ) == repr else repr( message ), encoding=self.strformat )
                client.sendall( message1 )
                self.messages[ "client" ].append( message1 )
                if message == endvalue:
                    time.sleep( 1 )
                    print( "client  ended " )
                    client.close( )

                    return True
            except ConnectionError:
                print( "Client: No connection to server")
                time.sleep( 1 )
                counter += 1
                if counter > 5:
                    return True
            #print( "client_func is {}".format( self.messages[ "client" ][ -1 ] ) )