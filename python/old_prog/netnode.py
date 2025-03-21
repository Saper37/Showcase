
import ssl
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from statehandler import *
from interpreter import *
#from urrlib.parse import parse_qsl, urlparse
from dataclasses import dataclass

class MyException( Exception ):
    def __init__( self, message ):
        self.message = message

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

#
# function start
# starts the thereads in clients and servers dictionaries. 
#
# function end
# stops the node and deletes clients and servers
# 


class NetNode:
    def __init__( self, infos, initializer ):
        self.infos = infos
        self.initializer = initializer
        self.servercontext = ssl.SSLContext( ssl.PROTOCOL_TLS_SERVER )
        self.clientcontext = ssl.SSLContext( ssl.PROTOCOL_TLS_CLIENT )

        self.clients = {}
        self.servers = {}
        self.serverId = 0
        self.clientId = 0

        self.https = [ ]
        self.types = [ ]
        self.targets = [ ]
        self.host = ""
        
        #self.init( )
        #self.start( )
        #self.deactivate( )
    

    def init( self ):
        
        self.clients, self.servers = self.initializer.socket_init( self.infos )
              

    def start( self ):
        print( "Node servers size is {} clients size is {}".format( len( self.servers ), len( self.clients )))
        if len( self.servers ) > 0:
            for key, thread in self.servers.items( ):
                print( "program start server thread {} activated\thread is {}".format( key, thread ) )
                thread.start( )
            
        if len( self.clients ) > 0:
            for key, thread in self.clients.items( ):
                print( "program start client thread {} activated\thread is {}".format( key, thread ) )
                thread.start( )
        #self.end( )
        
    def end( self ):
        print( "node ends")
        del self.clients
        del self.servers
    def run( self ):
        pass
    def __delete__( self ):
        self.end( )
    def removeInit( self ):
        self.initializer = None