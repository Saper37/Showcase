
import ssl
import time
import threading
import socket

from myexceptions import *
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from myinterpreter import *
#from urrlib.parse import parse_qsl, urlparse
from dataclasses import dataclass



# Class for flexbile node for communicating between different services
# Each node consist of a service or group of services.
# servercontexts for HTTPS functionality
# dictionaries for clients and servers for easy access
# program is responsible socket functioanlities such as binding and listen,  node simply provides basic functionalities such as thread and socket handling
#
# function __init__
# function param infos
# function param initializer
# function defines class variables, specifically infos, initializer
#
# function init
# Responsible initializing node, initializer 
#
# function start
# starts the thereads in clients and servers dictionaries. 
#
# function end
# stops the node and deletes clients and servers
#
# overloads del 

class NetNode:
    def __init__( self, infos, interpreter, handler ):
        self.infos = infos
        self.interpreter = interpreter
        self.handler = handler

        self.clients = {}
        self.servers = {}

    def init( self ):
        timeout = 30
        clientinfo, serverinfo = self.infos[ "clientinfo"], self.infos[ "serverinfo" ]
        targetinfo = self.infos[ "target" ]
        addressfamily, connectiontype = self.infos[ "addressfamily" ], self.infos[ "connectiontype" ]
        if serverinfo[ 0 ] != "" and clientinfo[ 0 ] != "":
            
            serversocket = socket.socket( addressfamily, connectiontype )
            #serversocket.settimeout( timeout )
            #serversocket.setblocking( False )
            serversocket.bind( ( serverinfo[ 0 ], int( serverinfo[ 1 ] ) ) )
            serversocket.listen( 5 )

            #clientsocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM  )
            clientsocket = socket.socket( addressfamily, connectiontype  )
            #clientsocket.settimeout( timeout )
            clientsocket.bind( ( clientinfo[ 0 ], int( clientinfo[ 1 ] ) ) )
            #clientsocket.setblocking( True )
            try:
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            except ( OSError, ConnectionRefusedError ):
                time.sleep( 5 )
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            
            client_thread = threading.Thread( target=self.handler.middle_func, args=( clientsocket, serversocket, self.interpreter ) )
            self.clients[ len( self.clients ) ] = client_thread
            print( "middle thread is created " )

        elif serverinfo[ 0 ] != "":
            # server
            #serversocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM  )
            serversocket = socket.socket( addressfamily, connectiontype )
            #serversocket.settimeout( timeout )
            serversocket.bind( ( serverinfo[ 0 ], int( serverinfo[ 1 ] ) ) )
            serversocket.listen( 5 )
            server_thread = threading.Thread( target=self.handler.server_func, args=( serversocket, self.interpreter ) )
            self.servers[ len( self.servers ) ] = server_thread

        elif clientinfo[ 0 ] != "":
            #clientsocket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM  )
            clientsocket = socket.socket( addressfamily, connectiontype  )
            #clientsocket.settimeout( timeout )
            clientsocket.bind( ( clientinfo[ 0 ], int( clientinfo[ 1 ] ) ) )

            try:
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            except ( OSError, ConnectionRefusedError ):
                time.sleep( 5 )
                clientsocket.connect( ( targetinfo[ 0 ], int( targetinfo[ 1 ] ) ) )
            client_thread = threading.Thread( target=self.handler.client_func, args=( clientsocket, self.interpreter ) )
            self.clients[ len( self.clients ) ] = client_thread
    
    def start( self ):
        if len( self.servers ) > 0:
            for key, thread in self.servers.items( ):
                thread.start( )
            
        if len( self.clients ) > 0:
            for key, thread in self.clients.items( ):
                thread.start( )
                
    
    def status( self ):
        return self.statehandler.getStatus( )
        
    def end( self ):
        del self.clients
        del self.servers
        del self.infos
        del self.initalizer
        del self.handler

    def __delete__( self ):
        self.end( )
        