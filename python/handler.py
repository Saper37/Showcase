import time
from cryptography.fernet import Fernet



# Abstract class for defining handlers for the node classes

class Handler:
    def __init__( self, strformat="utf-8" ):
        pass

    def http_server_func( self, server ):
        pass

    def http_client_func( self, client ):
        pass
        
    def server_handle( self, message ):
        pass
    
    def middle_handle( self ):
        pass

    def client_handle( self, message ):
        pass

    def server_func( self, server ):
        pass
            
    def middle_func( self ):
        pass
                
    def client_func( self, client ):
        pass