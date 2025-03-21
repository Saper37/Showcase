import sys
import base64
import nacl.utils
from nacl.public import Box
from nacl.public import PrivateKey, PublicKey
from nacl.encoding import Base64Encoder
from cryptography.fernet import Fernet

class MyException( Exception ):
    def __init__( self, message ):
        self.message = message


class MyInterpreter:
    def __init__( self, sk ):
        self.__sk = sk
        self.__targetpk = None
        self.boxes = {}

    def encode( self, text, strformat, targetkey ):
        print( "myinterpreter encode  text is {} type is {} strformat is {}".format( text, type( text ), strformat ) )
        if self.__targetpk == None:
            raise MyException( "Encode failure targetpk is undefined " )
        if isinstance( text, int ):
            text = text.to_bytes( )
        message =  self.boxes[ targetkey ].encrypt( text )
        print( "myinterpreter encode  message is {}".format( message ) )
        return message

    def decode( self, text, strformat, targetkey ):

        print( "Decode text {} is decrypted type is {}".format( text, type( text ) ) )
        #print( "Decode targetpk is {}".format( self.__targetpk ) )
        if isinstance( text, bytes ):
            message = self.boxes[ targetkey ].decrypt( text )
        elif isinstance( text, list ):
            if len( text ) == 1:
                message = self.boxes[ targetkey ].decrypt( text )
            else:
                found, same = None, False
                for message in text:
                    message = message.rsplit( "<RETRY>" )
                    if found == None:
                        found = message
                    elif message == found:
                        same = True
                    else:
                        same = False
                if same:
                    message = self.boxes[ targetkey ].decrypt( found )
        else:
            raise MyException( "Decode Error text wasn't byte" )
        print( "myinterpreter decode message is {}".format( message ) )
        return message
    
    def getPk( self ):
        pk = self.__sk.public_key.encode( Base64Encoder )
        print( "getPk length of pk is {} pk is {}".format( len( pk ), pk ) )
        return pk
    
    def setTargetPk( self, targetpk, targetkey ):
        print( "setTargetPk targetpk {} targetkey {}".format( targetpk, targetkey ) )
        if isinstance( targetpk, list ):
            for x in range( len( targetpk ) ):
                targetpk[ x ] = Base64Encoder.decode( targetpk[ x ] )
        found, same = None, False if len( targetpk ) > 1 else True
        for x in range( len( targetpk ) ):
            if found == None:
                found = targetpk[ x ]
            elif found == targetpk[ x ]:
                same = True
            else:
                same = False
        if same:
            targetpk = targetpk[ 0 ]
        self.__targetpk = PublicKey( targetpk )
        self.boxes[ targetkey ] = Box( self.__sk, self.__targetpk )
        return True
        
