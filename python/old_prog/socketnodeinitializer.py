from nodeinitializer import *

# class SocketNodeInitilizaer extends Base class NodeInitializer
# param program. parameter that is executed in the node
# variable clients 
# variable servers
# variable program see program param. 
#
# function socket_init
# Uses socket, threading
# function param socketinfo. Provides information such as IP, host and target IP and host
# Initializes socket for the node using information provided outside the function and class
# Client node only provides target information, server own information and middle node both.
# The function uses threads for executubg the program.


class SocketNodeInitializer( NodeInitializer ):
    def __init__( self, program, connectiontype ):
        self.clients = {}
        self.servers = {}
        self.program = program
        self.addressfamily = addressfamily
        self.connectiontype = connectiontype 
    
    def socket_init( self, socketinfo ):
        clientinfo, serverinfo = socketinfo[ "clientinfo"], socketinfo[ "serverinfo" ]
        targetinfo = socketinfo[ "target" ]
        print( "Node. socket init. clientinfo is {}\nserverinfo is {}\ntargetinfo is {}".format( clientinfo, serverinfo, targetinfo))

        if serverinfo[ 0 ] != "" and clientinfo[ 0 ] != "":
            
            serversocket = socket.socket( addressfamily, connectiontype )
            serversocket.bind( ( serverinfo[ 0 ], int( serverinfo[ 1 ] ) ) )
            serversocket.listen( 5 )

            #clientsocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM  )
            clientsocket = socket.socket( addressfamily, connectiontype  )
            clientsocket.bind( ( clientinfo[ 0 ], int( clientinfo[ 1 ] ) ) )
            try:
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            except OSError:
                time.sleep( 5 )
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )

            client_thread = threading.Thread( target=self.program.middle_func, args=( clientsocket, serversocket, ) )
            self.clients[ len( self.clients ) ] = client_thread

        elif serverinfo[ 0 ] != "":
            # server
            #serversocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM  )
            serversocket = socket.socket( addressfamily, connectiontype )
            serversocket.bind( ( serverinfo[ 0 ], int( serverinfo[ 1 ] ) ) )
            serversocket.listen( 5 )
            server_thread = threading.Thread( target=self.program.server_func, args=( serversocket, ) )
            self.servers[ len( self.servers ) ] = server_thread
            #print( "server defined. serverinfo {}".format( serverinfo ) )
            print( "server thread is defined " )

        elif clientinfo[ 0 ] != "":
            #clientsocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM  )
            clientsocket = socket.socket( addressfamily, connectiontype  )
            clientsocket.bind( ( clientinfo[ 0 ], int( clientinfo[ 1 ] ) ) )

            try:
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            except OSError:
                time.sleep( 5 )
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            print( "client thread is defined " )
            client_thread = threading.Thread( target=self.program.client_func, args=( clientsocket, ) )
            self.clients[ len( self.clients ) ] = client_thread
            
        return self.clients, self.servers