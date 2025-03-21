import http 

class TestHTTP:
    def __init__( self ):
        self.connection = None
    def server( self ):
        pass
    def client( self, address, port, timeout ):
        self.connection = http.client.HTTPConnection( address, port, timeout )
