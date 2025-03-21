from nacl.public import PrivateKey, Box


if __name__ == "__main__":
    sk = PrivateKey.generate( )
    pk = sk.public_key

    
    
    print( sk, type( sk ) )
    print( pk, type( pk ) )