import json
import nacl.utils
from nacl.public import PrivateKey, Box

clientsk = PrivateKey.generate( )
middlesk = PrivateKey.generate( )
serversk = PrivateKey.generate( )

clientpk = clientsk.public_key
middlepk = middlesk.public_key
serverpk = serversk.public_key

open( "./clientfile", 'w').close( )
open( "./middlefile", 'w').close( )
open( "./serverfile", 'w').close( )
open( "./nodesecret", 'w').close( )

with open( "./clientfile", 'w' ) as clientfile:
    
    clientfile.write( repr( clientsk ) )

with open( "./middlefile", 'w' ) as middlefile:
    middlefile.write( repr( middlesk ) )

with open( "./serverfile", 'w' ) as serverfile:
    serverfile.write( repr( serversk ) )

with open( "./nodesecret", "a" ) as nodefile:
    nodefile.write( "client:{}".format( repr( clientpk ) ) )
    nodefile.write( "\n" )
    nodefile.write( "middle:{}".format( repr( middlepk ) ) )
    nodefile.write( "\n" )
    nodefile.write( "server:{}".format( repr( serverpk ) ) )
