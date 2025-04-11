def countRPE( minute, experience ):
	if experience > 10:
		raise MyException( "Virheellinen määrittely experience" )
	return minute * experience

def weekRPE( minutes, experiences ):
	number = 0
	for row in zip( minutes, experiences ):
		number += countRPE( row[ 0 ], row[ 1 ] )
	return number
    
for t in range( 1 ):
        #from PREalgo import *
	w0 = list( zip( [ 90, 60, 90, 140, 90, 90, 140 ], [ 8, 2, 3, 8, 3, 3, 8] ) )
	w1 = list( zip( [ 60, 60, 56, 140, 60, 57, 58 ], [ 2, 5, 7, 2, 2, 2, 2] ) )
	w2 = list( zip( [ 104, 140, 57, 144, 120, 0, 129 ], [ 8, 2, 2, 8, 4, 0, 6] ) )
	w3 = list( zip( [ 30, 30, 95, 0, 150, 49, 56 ], [ 2, 2, 7, 0, 4, 8, 2 ] ) )
	w4 = list( zip( [ 51, 142, 63, 53, 148, 86, 55 ], [ 2, 8, 2, 4, 7, 4, 2 ] ) )
	w5 = list( zip( [ 140, 52, 53, 99, 54, 90, 140 ], [ 7, 2, 2, 7, 2, 2, 7] ) )
	weeks = {}
	dates = 1, 52, 51, 50, 49, 48
	ws = w0, w1, w2, w3, w4, w5
	for x in range( len( ws ) ):
		load = {}
		for x1 in range( len( ws[ x ] ) ):
			load[ 7 - x1 ] = [ ws[ x ][ x1 ][ 0 ], ws[ x ][ x1 ][ 1 ] ]
		weeks[ dates[ x ] ] = load
	

	#point = ( sum( list( weeks.values( )[ 1 : 5 ] ) ) ) / 4
	#w0 / point
for t in range( 1 ):
	with open( 'loaddata.json', 'w' ) as jsonfile:
		json.dump( weeks, jsonfile )

		
for t in range( 1 ):
	with open( 'loaddata.json' ) as jsonfile:
		data = json.load( jsonfile )
