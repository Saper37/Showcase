import threading
from nacl.public import PrivateKey
from nacl.encoding import Base64Encoder

#t1 = threading.thread( )
#t2 = threading.thread( )

message = "hello<RETRY>hello"
en_message = Base64Encoder.encode( message )
print( en_message )
str_message = str( message )
str_message = str_message.rsplit( "<RETRY>" )
str_message = str_message[ -1 ]
en_message = Base64Encoder.encode( str_message )
print( en_message )