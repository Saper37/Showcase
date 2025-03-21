




#
class StateHandler:
    def __init__( self ):
        self.info = { }
        self.parent = None

    def add_program( self, parent ):
        self.parent = parent 

    def add( self, type, host, target, http ):
        if type in self.info:
            self.info[ type ].append( [ host, target, http ] ) 
        else:
            self.info[ type ] = [ [ host, target, http ] ]

