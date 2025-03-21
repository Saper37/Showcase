import sys
import base64
from cryptography.fernet import Fernet

if __name__ == "__main__":
    filename = sys.argv[ 1 ]
    mode = sys.argv[ 2 ]
    key = sys.argv[ 3 ]
    while len( key ) < 32:
        key += '|'
    key = bytes( key, encoding="utf-8" )
    key = base64.urlsafe_b64encode( key )
    if mode == "d":
        f = Fernet( key  )
        with open( filename, 'r' ) as file:
            content = file.read( )
            content = f.decrypt( content[ 1:: ] )
        with open( filename, 'w' ) as file:
            r = file.write( str( content ) )

    elif mode == 'e':
        f = Fernet( key )
        with open( filename, 'r' ) as file:
            content = file.read( )
            content = f.encrypt( bytes( content, encoding="utf-8" ) )
        filename = filename.rsplit( "." )
        filename[ 0 ] += '1.'
        filename[ 0 ] += filename[ 1 ]
        filename = filename[ 0 ]
        with open( "{}".format( filename ), 'w' ) as file:
            res = file.write( str( content ) )