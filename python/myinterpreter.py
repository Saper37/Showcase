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
    
    # encode function
    # param text: the text to be encoded, expected to be bytes or int
    # param strformat: Deprecated
    # param targetkey: key value for boxes dictionary containing Box entity from nacl
    # return: the encoded message
    # raise MyException in case of targetpk is undefined
    def encode( self, text, strformat, targetkey ):
        print( "myinterpreter encode  text is {} type is {} strformat is {}".format( text, type( text ), strformat ) )
        if self.__targetpk is None:
            raise MyException( "Encode failure targetpk is undefined " )
        if isinstance( text, int ):
            text = text.to_bytes(length=(text.bit_length() + 7) // 8, byteorder='big')
        message =  self.boxes[ targetkey ].encrypt( text )
        print( "myinterpreter encode  message is {}".format( message ) )
        return message

    def decode( self, text, strformat, targetkey ):

        #print( "Decode text {} is decrypted type is {} pk is {}".format( text, type( text ), self.__sk.public_key ) )
        #print( "Decode targetpk is {}".format( self.__targetpk ) )
        if isinstance( text, bytes ):
            message = self.boxes[ targetkey ].decrypt( text )
        elif isinstance( text, list ):
            if len( text ) == 1:
                text = text[ 0 ]
                print( "Decode text is {}".format( text ) )
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
                    message = [ self.boxes[ targetkey ].decrypt( message ) for message in found if message != '' ]
                    if len( message ) == 1:
                        message = message[ 0 ]
        else:
            raise MyException( "Decode Error text wasn't byte" )
        print( "myinterpreter decode message is {}".format( message ) )
        return message
    
    def getPk( self ):
        pk = self.__sk.public_key.encode( Base64Encoder )
        #pk = Base64Encoder.encode( self.__sk.public_key )
        #print( "getPk length of pk is {} pk is {}".format( len( pk ), pk ) )
        return pk
    
    def setTargetPk( self, targetpk, targetkey ):
        #print( "setTargetPk targetpk {} targetkey {}".format( targetpk, targetkey ) )
        #if isinstance( targetpk, list ):
        #    for x in range( len( targetpk ) ):
        #        targetpk[ x ] = Base64Encoder.decode( targetpk[ x ] )
        found, same = None, False if len( targetpk ) > 1 else True
        if not same:
            for x in range( len( targetpk ) ):
                if found == None:
                    found = targetpk[ x ]
                elif found == targetpk[ x ]:
                    same = True
                else:
                    same = False
        if same:
            targetpk = targetpk[ 0 ]
        else:
            targetpk = targetpk[ -1 ]
        #print( "myinterpreter targetpk is {} ".format( targetpk ) ) 
        targetpk = Base64Encoder.decode( targetpk )
        #print( "myinterpreter targetpk is {} ".format( targetpk ) ) 
        print( "myinterpreter targetpk is {} ".format( targetpk ) ) 
        #pk = self.__sk.public_key.decode( Base64Encoder )
        self.__targetpk = PublicKey( targetpk )
        self.boxes[ targetkey ] = Box( self.__sk, self.__targetpk )
        return True
        
