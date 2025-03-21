from nacl.public import Box
from nacl.public import PrivateKey, PublicKey
from nacl.encoding import Base64Encoder


sk1 = PrivateKey.generate( )
pk1 = sk1.public_key

sk2 = PrivateKey.generate( )
pk2 = sk2.public_key

box1 = Box( sk1, pk2 )

box2 = Box( sk2, pk1 )

message1 = b"hello you" 
message2 = b"hello world"

encrypted1 = box1.encrypted( message1 )
encrypted2 = box2.encrypted( message2 )

print( encrypted1 )
print( encrypted2 )