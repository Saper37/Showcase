
from erjps import *
from itertools import permutations
from itertools import combinations
from myfunctions import *
from statistics import mean, median, mode, variance, stdev

# Previous results from rows [ x + 1 :: ] set.
pres = [[74, 9, 1, 0, 0], [67, 3, 0, 0, 0], [74, 4, 1, 0, 0], [73, 6, 1, 0, 0], [75, 4, 1, 0, 0], [74, 5, 0, 0, 0], [70, 5, 0, 0, 0], [70, 4, 0, 0, 0], [69, 8, 0, 0, 0], [66, 2, 0, 0, 0], [68, 7, 0, 0, 0], [69, 5, 0, 0, 0], [63, 4, 1, 0, 0], [66, 7, 0, 0, 0], [70, 6, 0, 0, 0], [73, 7, 2, 0, 0], [69, 2, 0, 0, 0], [67, 4, 0, 0, 0], [61, 7, 1, 0, 0], [67, 6, 1, 0, 0], [60, 3, 0, 0, 0], [66, 8, 0, 0, 0], [68, 1, 0, 0, 0], [72, 8, 1, 0, 0], [62, 6, 0, 0, 0], [59, 5, 0, 0, 0], [64, 6, 0, 0, 0], [61, 5, 0, 0, 0], [73, 9, 2, 0, 0], [66, 9, 0, 0, 0], [58, 6, 0, 0, 0], [70, 4, 0, 0, 0], [70, 5, 0, 0, 0], [70, 6, 0, 0, 0], [60, 3, 0, 0, 0], [72, 5, 1, 0, 0], [57, 3, 0, 0, 0], [69, 4, 1, 0, 0], [64, 4, 2, 1, 0], [69, 7, 1, 0, 0], [66, 5, 0, 0, 0], [63, 5, 1, 0, 0], [65, 5, 0, 0, 0], [56, 3, 0, 0, 0], [67, 2, 0, 0, 0], [66, 7, 1, 0, 0], [65, 4, 0, 0, 0], [59, 7, 0, 0, 0], [62, 3, 0, 0, 0], [71, 13, 1, 0, 0], [67, 4, 0, 0, 0], [65, 5, 0, 0, 0], [61, 7, 1, 0, 0], [62, 7, 0, 0, 0], [61, 6, 1, 0, 0], [67, 7, 0, 0, 0], [70, 2, 0, 0, 0], [60, 3, 1, 0, 0], [66, 6, 0, 0, 0], [64, 6, 1, 0, 0], [61, 3, 0, 0, 0], [70, 7, 0, 0, 0], [69, 10, 0, 0, 0], [61, 3, 0, 0, 0], [59, 2, 0, 0, 0], [66, 6, 3, 0, 0], [68, 6, 0, 0, 0], [60, 2, 0, 0, 0], [63, 10, 0, 0, 0], [67, 7, 0, 0, 0], [62, 3, 0, 0, 0], [60, 9, 1, 0, 0], [57, 8, 0, 0, 0], [61, 6, 0, 0, 0]],[[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [0, 0, 0, 0, 0], [2, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [3, 0, 0, 0, 0], [2, 1, 0, 0, 0], [2, 0, 0, 0, 0], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[1, 90, 263, -1, -1], [10, 196, -1, -1, -1], [11, 63, 387, -1, -1], [18, 87, 91, -1, -1], [10, 10, 405, -1, -1], [21, 156, -1, -1, -1], [16, 42, -1, -1, -1], [4, 89, -1, -1, -1], [0, 0, -1, -1, -1], [5, 122, -1, -1, -1], [5, 17, -1, -1, -1], [6, 334, -1, -1, -1], [10, 94, 94, -1, -1], [3, 39, -1, -1, -1], [5, 25, -1, -1, -1], [8, 10, 25, -1, -1], [4, 412, -1, -1, -1], [10, 174, -1, -1, -1], [0, 100, 100, -1, -1], [19, 289, 289, -1, -1], [3, 21, -1, -1, -1], [0, 30, -1, -1, -1], [20, 22, -1, -1, -1], [24, 36, 69, -1, -1], [1, 132, -1, -1, -1], [3, 96, -1, -1, -1], [7, 416, -1, -1, -1], [5, 287, -1, -1, -1], [5, 107, 228, -1, -1], [3, 225, -1, -1, -1], [4, 270, -1, -1, -1], [6, 67, -1, -1, -1], [3, 3, -1, -1, -1], [3, 163, -1, -1, -1], [0, 177, -1, -1, -1], [4, 193, 566, -1, -1], [5, 186, -1, -1, -1], [3, 79, 321, -1, -1], [1, 17, 17, 634, -1], [1, 8, 174, -1, -1], [0, 0, -1, -1, -1], [3, 102, 319, -1, -1], [2, 8, -1, -1, -1], [0, 143, -1, -1, -1], [0, 170, -1, -1, -1], [12, 26, 276, -1, -1], [11, 22, -1, -1, -1], [4, 94, -1, -1, -1], [10, 107, -1, -1, -1], [10, 30, 573, -1, -1], [14, 104, -1, -1, -1], [3, 14, -1, -1, -1], [13, 42, 402, -1, -1], [6, 17, -1, -1, -1], [1, 125, 448, -1, -1], [1, 1, -1, -1, -1], [18, 41, -1, -1, -1], [5, 256, 615, -1, -1], [3, 77, -1, -1, -1], [7, 19, 484, -1, -1], [12, 57, -1, -1, -1], [3, 31, -1, -1, -1], [2, 28, -1, -1, -1], [27, 27, -1, -1, -1], [4, 4, -1, -1, -1], [11, 12, 28, -1, -1], [1, 73, -1, -1, -1], [9, 469, -1, -1, -1], [0, 0, -1, -1, -1], [2, 48, -1, -1, -1], [1, 290, -1, -1, -1], [18, 342, 395, -1, -1], [30, 163, -1, -1, -1], [1, 56, -1, -1, -1]], [ [1, -1, -1, -1, -1], [10, -1, -1, -1, -1], [11, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [10, 10, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [4, -1, -1, -1, -1], [0, 0, -1, -1, -1], [5, -1, -1, -1, -1], [5, -1, -1, -1, -1], [6, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [3, -1, -1, -1, -1], [5, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [0, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
# fiquout results based on numming printpros result on first level
fres = [[597, 68], [603, 62], [586, 78, 1], [581, 83, 1], [584, 81], [574, 88, 3], [572, 92, 1], [537, 118, 10], [556, 104, 5], [555, 102, 8], [546, 109, 10], [520, 127, 18], [526, 127, 12], [489, 163, 12, 1], [523, 124, 18], [520, 136, 8, 1], [544, 114, 6, 1], [542, 117, 6], [534, 126, 5], [514, 140, 11], [505, 142, 7], [497, 123, 13, 1], [471, 101, 1], [449, 92, 1], [410, 81, 4], [367, 84, 1], [345, 70, 1], [307, 58, 1], [261, 36], [159, 27], [82, 7], [22, 5]]
# fiquout and contn results based on numming printpros result on first level
fcnres = [[407, 227, 30, 1], [410, 219, 35, 1], [439, 191, 31, 4], [436, 196, 32, 1], [436, 204, 22, 3], [437, 200, 26, 2], [441, 200, 23, 1], [400, 225, 38, 2], [411, 224, 29, 1], [391, 230, 42, 2], [390, 234, 41], [352, 130, 23], [123, 36, 5], [2, 1]]


def tester( r1, r2 ):
	res = [ num in r2 for num in r1 ]
	return sum( res )

def simtester( r1, r2 ):
	if len( r1 ) < len( r2 ):
		res = [ r1[ x ] == r2[ x ] for x in range( len( r1 ) ) ]
	else:
		res = [ r1[ x ] == r2[ x ] for x in range( len( r2 ) ) ]
	return sum( res )


# function perms
# param rows list of list of numbers
# param maara integer, default = 51
# return list of list
def perms( rows ):
	col = {}
	for row in rows:
		for perm in list( combinations( row, 5 ) ):
			n1, n2, n3, n4, n5 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ], perm[ 4 ]
			key = "{} {} {} {} {}".format( n1, n2, n3, n4, n5 )
			if col.get( key ) == None:
				col[ key ] = 1
			else:
				col[ key ] += 1
		for perm in list( combinations( row, 4 ) ):
			n1, n2, n3, n4 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ]
			key = "{} {} {} {}".format( n1, n2, n3, n4 )
			if col.get( key ) == None:
				col[ key ] = 1
			else:
				col[ key ] += 1
		for perm in list( combinations( row, 3 ) ):
			n1, n2, n3 = perm[ 0 ], perm[ 1 ], perm[ 2 ]
			key = "{} {} {}".format( n1, n2, n3 )
			if col.get( key ) == None:
				col[ key ] = 1
			else:
				col[ key ] += 1
		for perm in list( combinations( row, 2 ) ):
			n1, n2 = perm[ 0 ], perm[ 1 ]
			key = "{} {}".format( n1, n2 )
			if col.get( key ) == None:
				col[ key ] = 1
			else:
				col[ key ] += 1
		for perm in list( combinations( row, 1 ) ):
			n1 = perm[ 0 ]
			key = "{}".format( n1 )
			if col.get( key ) == None:
				col[ key ] = 1
			else:
				col[ key ] += 1

	return col

# function fperms
# param rows
# param maara default 51

def fperms( rows, maara=51, order=False ):
	col = { }
	for index, row in enumerate( rows ):
		for perm in list( combinations( row, 1 ) ):
			n1 = perm[ 0 ]
			key = "{}".format( n1 )
			item = col.get( key )
			if item == None:
				col[ key ] = [ index ]
			else:
				col[ key ].append( index )
		for perm in list( combinations( row, 2 ) ):
			n1, n2 = perm[ 0 ], perm[ 1 ]
			key = "{} {}".format( n1, n2 )
			item = col.get( key )
			if item == None:
				col[ key ] = [ index ]
			else:
				col[ key ].append( index )
		for perm in list( combinations( row, 3 ) ):
			n1, n2, n3= perm[ 0 ], perm[ 1 ], perm[ 2 ]
			key = "{} {} {}".format( n1, n2, n3 )
			item = col.get( key )
			if item == None:
				col[ key ] = [ index ]
			else:
				col[ key ].append( index )
		for perm in list( combinations( row, 4 ) ):
			n1, n2, n3, n4 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ]
			key = "{} {} {} {}".format( n1, n2, n3, n4 )
			item = col.get( key )
			if item == None:
				col[ key ] = [ index ]
			else:
				col[ key ].append( index )
		for perm in list( combinations( row, 5 ) ):
			n1, n2, n3, n4, n5 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ], perm[ 4 ]
			key = "{} {} {} {} {}".format( n1, n2, n3, n4, n5 )
			item = col.get( key )
			if item == None:
				col[ key ] = [ index ]
			else:
				col[ key ].append( index )
	return col


# function printpro
# param p, a list containing several layer of lists, represents matrix
# return Each layer, with the exception the last one, contains numerical and list element representing the frequency of selected and other values respectively.

def printpro( p ):
	return [ row[ 0 ] if type( row ) == list else row if type( row ) == int and row > 0 else 0 for row in p ]


def scorepoints( oik, pro ):
	riv = [ ]
	n1, n2, n3, n4, n5 = oik[ 0 ], oik[ 1 ], oik[ 2 ], oik[ 3 ], oik[ 4 ]
	riv.append( pro[ n1 ][ 0 ] )
	riv.append( pro[ n1 ][ n2 ][ 0 ] )
	riv.append( pro[ n1 ][ n2 ][ n3 ][ 0 ] )
	riv.append( pro[ n1 ][ n2 ][ n3 ][ n4 ][ 0 ] )
	riv.append( pro[ n1 ][ n2 ][ n3 ][ n4 ][ n5 ] )
	return riv

def probfix( pro1 ):
	for x in range( 1, len( pro1 ) ):
		pro1[ x ][ 0 ] = int( pro1[ x ][ 0 ] / 24 )
		for x1 in range( 1, len( pro1[ x ] ) ):
			pro1[ x ][ x1 ][ 0 ] = int( pro1[ x ][ x1 ][ 0 ] / 6 )
			for x2 in range( 1, len( pro1[ x ][ x1 ] ) ):
				pro1[ x ][ x1 ][ x2 ][ 0 ] = int( pro1[ x ][ x1 ][ x2 ][ 0 ] / 2 )
def retprobfix( pro1 ):
	for x in range( 1, len( pro1 ) ):
		pro1[ x ][ 0 ] = int( pro1[ x ][ 0 ] * 24 )
		for x1 in range( 1, len( pro1[ x ] ) ):
			pro1[ x ][ x1 ][ 0 ] = int( pro1[ x ][ x1 ][ 0 ] * 6 )
			for x2 in range( 1, len( pro1[ x ][ x1 ] ) ):
				pro1[ x ][ x1 ][ x2 ][ 0 ] = int( pro1[ x ][ x1 ][ x2 ][ 0 ] * 2 )
def probadd( pro1 ):
	for x in range( 1, len( pro1 ) ):
		pro1[ x ][ 0 ] = int( pro1[ x ][ 0 ] * 24 )
		for x1 in range( 1, len( pro1[ x ] ) ):
			pro1[ x ][ x1 ][ 0 ] = int( pro1[ x ][ x1 ][ 0 ] * 6 )
			for x2 in range( 1, len( pro1[ x ][ x1 ] ) ):
				pro1[ x ][ x1 ][ x2 ][ 0 ] = int( pro1[ x ][ x1 ][ x2 ][ 0 ] * 2 )

def removeroute( p, nums ):
	if len( num ) == 1:
		num = nums[ 0 ]
		for x in range( len( p[ num ] ) ):
			for x1 in range( len( p[ num ][ x ] ) ):
				for x2 in range( len( p[ num ][ x ][ x1 ] ) ):
					for x3 in range( len( p[ num ][ x ][ x1 ][ x2 ] ) ):
						for x4 in range( len( p[ num ][ x ][ x1 ][ x2 ][ x3 ] ) ):
							p[ num ][ x ][ x1 ][ x2 ][ x3 ][ x4 ] = 0
						p[ num ][ x ][ x1 ][ x2 ][ x3 ][ 0 ] = 0
					p[ num ][ x ][ x1 ][ x2 ][ 0 ] = 0
				p[ num ][ x ][ x1 ][ 0 ] = 0
			p[ num ][ x ][ 0 ] = 0
		p[ num ][ 0 ] = 0
		
def extender( n ):
	col = [ ]
	for row in n:
		col.extend( row )
	return col

def findpairlajs( rows, r ):
	col = {}
	for row in rows:
		for pair in list( permutations( row, r ) ):
			ok = col.get( pair )
			if ok == None:
				col[ pair ] = 1
			else:
				col[ pair ] += 1
	return col

def pickcomb( row, p, r ):
	riv = [ ]
	if r == 2:
		for pair in list( combinations( row, r ) ):
			n1, n2 = pair[ 0 ], pair[ 1 ]
			riv.append( p[ n1 ][ n2 ][ 0 ] )
	elif r == 3:
		for pair in list( combinations( row, r ) ):
			n1, n2, n3 = pair[ 0 ], pair[ 1 ], pair[ 2 ]
			riv.append( p[ n1 ][ n2 ][ n3 ][ 0 ] )
	elif r == 4:
		for pair in list( combinations( row, r ) ):
			n1, n2, n3, n4 = pair[ 0 ], pair[ 1 ], pair[ 2 ], pair[ 3 ]
			riv.append( p[ n1 ][ n2 ][ n3 ][ n4 ][ 0 ] )
	else:
			raise MyException( " ParameterError: Virheelinen r. Arvot 2 <= r <= 3 " )
	return riv

def q0lambdadel( q0, Q, p, r, ls ):
	qpros, qchange, qmaara = 0, .1, len( q0 )
	qmaara = len( q0 )
	qlimit = round( qpros * qmaara, 3 )
	index, counter = 0, 0
	t0 = datetime.today( )
	print( t0, len( q0 ) )
	while index < len( q0 ):
		qrow = Q[ int( q0[ index ], 2 ) ]
		riv = pickcomb( qrow, p, r )
		for oklambda in ls:
			ok = oklambda( riv )
			if not ok:
				break
		if ok:
			index += 1
		else:
			del q0[ index ]
		counter += 1
		if counter > qlimit:
			t1 = datetime.today( )
			print( t1, t1 - t0, len( q0 ) )
			qpros = round( qpros + qchange, 3 )
			qlimit = round( qpros * qmaara, 3 )

def findpairflajs( rows, r ):
	col = {}
	for x in range( len( rows ) ):
		row = rows[ x ]
		for pair in list( permutations( row, r ) ):
			ok = col.get( pair )
			if ok == None:
				col[ pair ] = x
	return col

def q0scoredel( q0, Q, lams, ps ):
		qpros, qchange, qmaara = 0, .1, len( Q )
		qlimit = 0
		index = 0
		counter = 0
		t0 = datetime.today( )
		print( t0 )
		while index < len( q0 ):
			qrow = Q[ int( q0[ index ], 2 ) ]
			s = scorepoints( qrow, ps[ 0 ] )
			s[ 0 ] = int( s[ 0 ] / 24 )
			s[ 1 ] = int( s[ 1 ] / 6 )
			s[ 2 ] = int( s[ 2 ] / 2 )
			ok = lams[ 0 ]( s )
			if ok:
				s = scorepoints( qrow, ps[ 1 ] )
				s[ 0 ] = int( s[ 0 ] / 24 )
				s[ 1 ] = int( s[ 1 ] / 6 )
				s[ 2 ] = int( s[ 2 ] / 2 )
				ok = lams[ 1 ]( s )
				if ok:
					s = scorepoints( qrow, ps[ 2 ] )
					ok = lams[ 2 ]( s )
					if ok:
						s = scorepoints( qrow, ps[ 3 ] )
						ok = lams[ 3 ]( s )
			if ok:
				index += 1
			else:
				del q0[ index ]
			counter += 1
			if counter > qlimit:
				t1 = datetime.today( )
				print( t1, t1 - t0, counter, len( q0 ) )
				qpros = round( qpros + qchange, 3 )
				qlimit = round( qpros * qmaara, 3 )

def returnlambdas(  rajat, funcs=None ):
		lambdas = [ ]
		for x in range( len( rajat ) ):
			raja = rajat[ x ]
			func = funcs[ x ]
			lambdas.append( lambda s: raja[ 0 ] <= func( s ) <= raja[ 1 ] if funcs != None else lambda s: raja[ 0 ] <= s <= raja[ 1 ] )
		return lambdas

def lambdatest( rajat, funcs, ls, oik, p, r ):
	ls = returnlambdas( rajat, funcs )
	riv = pickcomb( oik, p, r )
	res = [ ]
	for x in range( len( funcs ) ):
		res.append( [ funcs[ x ]( riv ), ls[ x ]( riv ) ] )
	return res


def calculateres( rows, r, funcs, const, vali, full=True):
	colres = [ ]
	col = [ ]
	for x in range( len( rows ) - vali ):
		if full:
			c = funcs( rows[ x + 1 :: ], r )
		else:
			c = funcs( rows[ x + 1 : x + vali ], r )
		riv = [ ]
		for pair in list( combinations( rows[ x ], r ) ):
			if pair[ 0 ] != pair[ 1 ]:
				ok = c.get( pair )
				if ok == None:
					riv.append( const )
				else:
					riv.append( c[ pair ] )
		col.append( riv )
	if full:
		res = [ sum( row ) for row in col ]
		pres = min( res[ 0 : 30 ] ), max( res[ 0 : 30 ] ), mean( res[ 0 : 30 ] ), mode( res[ 0 : 30 ] ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ mean( row ) for row in col ]
		pres = min( res[ 0 : 30 ] ), max( res[ 0 : 30 ] ), mean( res[ 0 : 30 ] ), mode( res[ 0 : 30 ] ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ median( row ) for row in col ]
		pres = min( res[ 0 : 30 ] ), max( res[ 0 : 30 ] ), mean( res[ 0 : 30 ] ), mode( res[ 0 : 30 ] ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ mode( row ) for row in col ]
		pres = min( res[ 0 : 30 ] ), max( res[ 0 : 30 ] ), mean( res[ 0 : 30 ] ), mode( res[ 0 : 30 ] ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ round( variance( row ), 3 ) for row in col ]
		pres = min( res[ 0 : 30 ] ), max( res[ 0 : 30 ] ), mean( res[ 0 : 30 ] ), mode( res[ 0 : 30 ] ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [  round( stdev( row ), 3 ) for row in col ]
		pres = min( res[ 0 : 30 ] ), max( res[ 0 : 30 ] ), mean( res[ 0 : 30 ] ), mode( res[ 0 : 30 ] ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )
	else:
		res = [ sum( row ) for row in col ]
		pres = min( res ), max( res ), mean( res ), mode( res ), variance( res[ 0 : 30 ] ), stdev( res[ 0 : 30 ] )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ mean( row ) for row in col ]
		pres = min( res ), max( res ), mean( res ), mode( res ), variance( res ), stdev( res )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ median( row ) for row in col ]
		pres = min( res ), max( res ), mean( res ), mode( res ), variance( res ), stdev( res )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ mode( row ) for row in col ]
		pres = min( res ), max( res ), mean( res ), mode( res ), variance( res ), stdev( res )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [ round( variance( row ), 3 ) for row in col ]
		pres = min( res ), max( res ), mean( res ), mode( res ), variance( res ), stdev( res )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )

		res = [  round( stdev( row ), 3 ) for row in col ]
		pres = min( res ), max( res ), mean( res ), mode( res ), variance( res ), stdev( res )
		pres = [ round( value, 3 ) for value in pres ]
		colres.append( pres )
	return colres
# function serq0lambdabdel
# param oik, list of integers
# param q0, list of strings
# param Q, list of list of integers
# param ps, 
# param rajat, list of list of integer, border values
# param funcs
# param nums
# param testrun
def serq0lamdabdel( oik, q0, Q, ps, rajat, funcs, nums, testrun ):
		rajaindex = 0
		for p in ps:
			for r in nums:
				raja = rajat[ rajaindex ]
				ls = returnlambdas( raja, funcs )
				if not testrun:
					ro = rsoik0( q0, Q, 6, oik )
					print( ro, sum( ro ) )
					q0lambdadel( q0, Q, p, r, ls )
					ro = rsoik0( q0, Q, 6, oik )
					print( ro, sum( ro ) )
				else:
					print( "p {} {}".format( r, lambdatest( raja, funcs, ls, oik, p, r ) ) )

				rajaindex += 1


def pselect( p, size ):
	selected = [ ]
	pp = printpro( p )
	pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
	pp.sort( )
	selected.extend( [ [ pair[ 1 ] ] for pair in pp[ -size:: ] ] )
	while len( selected[ 0 ] ) < 5:
		n = selected.pop( 0 )
		if len( n ) == 1:
			n1 = n[ 0 ]
			pp = printpro( p[ n1 ] )
			pp[ 0 ] = 0
			pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
			pp.sort( )
			selected.extend( [ [ n1, pair[ 1 ] ] for pair in pp[ -size:: ] ] )
		elif len( n ) == 2:
			n1, n2 = n[ 0 ], n[ 1 ]
			pp = printpro( p[ n1 ][ n2 ] )
			pp[ 0 ] = 0
			pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
			pp.sort( )
			selected.extend( [ [ n1, n2, pair[ 1 ] ] for pair in pp[ -size:: ] ] )
		elif len( n ) == 3:
			n1, n2, n3 = n[ 0 ], n[ 1 ], n[ 2 ]
			pp = printpro( p[ n1 ][ n2 ][ n3 ] )
			pp[ 0 ] = 0
			pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
			pp.sort( )
			selected.extend( [ [ n1, n2, n3, pair[ 1 ] ] for pair in pp[ -size:: ] ] )
		elif len( n ) == 4:
			n1, n2, n3, n4 = n[ 0 ], n[ 1 ], n[ 2 ], n[ 3 ]
			pp = printpro( p[ n1 ][ n2 ][ n3 ][ n4 ] )
			pp[ 0 ] = 0
			pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
			pp.sort( )
			selected.extend( [ [ n1, n2, n3, n4, pair[ 1 ] ] for pair in pp[ -size:: ] ] )
	selected.sort( )
	for x in range( len( selected ) ):
		selected[ x ].sort( )
	index = 0
	while index < len( selected ) - 1:
		if selected[ index ] == selected[ index + 1 ]:
			del selected[ index + 1 ]
		else:
			index += 1
	return selected


def permprodel( q0, Q, r, p, lambd ):
	qmaara, qpros, qchange = len( q0 ), 0, .1
	qlimit = round( qmaara * qpros, 3 )
	counter = 0
	index = 0
	t0 = datetime.today( )
	print( t0 )
	while index < len( q0 ):
		qrow = Q[ int( q0[ index ], 2 ) ]
		for perm in combinations( qrow, r ):
			ok = lambd( perm, p )
			if not ok:
				break
		if ok:
			index += 1
		else:
			del q0[ index ]
		counter += 1
		if counter > qlimit:
			t1 = datetime.today( )
			print( t1, t1 - t0, len( q0 ), counter )
			qpros = round( qpros + qchange, 3 )
			qlimit = round( qmaara * qpros, 3 )


def proroad( p, size, rules):
	col = [ ]
	while len( col ) < size:
		pp = printpro( p )
		pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
		pp.sort( )

		riv = [ pp[ -1 ][ 1 ] ]
		while len( riv ) < 5:
			if len( riv ) == 1:
				n1 = riv[ 0 ]
				pp = printpro( p[ n1 ] )
			elif len( riv ) == 2:
				n1, n2 = riv[ 0 ], riv[ 1 ]
				pp = printpro( p[ n1 ][ n2 ] )
			elif len( riv ) == 3:
				n1, n2, n3 = riv[ 0 ], riv[ 1 ], riv[ 2 ]
				pp = printpro( p[ n1 ][ n2 ][ n3 ] )
			elif len( riv ) == 4:
				n1, n2, n3, n4 = riv[ 0 ], riv[ 1 ], riv[ 2 ], riv[ 3 ]
				pp = printpro( p[ n1 ][ n2 ][ n3 ][ n4 ] )
			else:
				raise MyException( "Indefined behaviour ")
			pp[ 0 ] = 0
			pp = [ [ pp[ x ], x ] for x in range( len( pp ) ) ]
			pp.sort( )
			riv.append( pp[ -1 ][ 1 ] )


		n1, n2, n3, n4, n5 = riv[ 0 ], riv[ 1 ], riv[ 2 ], riv[ 3 ], riv[ 4 ]
		values = rules[ "4" ]
		cutoff, frequencies = values[ 0 ], values[ 1 ]
		frequency = frequencies.get( n5 )
		if frequency != None:
			if cutoff < frequency:
				p[ n1 ][ n2 ][ n3 ][ n4 ][ n5 ] = 0
			else:
				frequencies[ n5 ] += 1
		else:
			frequencies[ n5 ] = 0

		values = rules[ "3" ]
		cutoff, frequencies = values[ 0 ], values[ 1 ]
		frequency = frequencies.get( n4 )
		if frequency != None:
			if cutoff < frequency:
				p[ n1 ][ n2 ][ n3 ][ n4 ][ 0 ] = 0
			else:
				frequencies[ n4 ] += 1
		else:
			frequencies[ n4 ] = 0


		values = rules[ "2" ]
		cutoff, frequencies = values[ 0 ], values[ 1 ]
		frequency = frequencies.get( n3 )
		if frequency != None:
			if cutoff < frequency:
				p[ n1 ][ n2 ][ n3 ][ 0 ] = 0
			else:
				frequencies[ n3 ] += 1
		else:
			frequencies[ n3 ] = 0


		values = rules[ "1" ]
		cutoff, frequencies = values[ 0 ], values[ 1 ]
		frequency = frequencies.get( n2 )
		if frequency != None:
			if cutoff < frequency:
				p[ n1 ][ n2 ][ 0 ] = 0
			else:
				frequencies[ n2 ] += 1
		else:
			frequencies[ n2 ] = 0

		values = rules[ "0" ]
		cutoff, frequencies = values[ 0 ], values[ 1 ]
		frequency = frequencies.get( n1 )
		if frequency != None:
			if cutoff < frequency:
				p[ n1 ][ 0 ] = 0
			else:
				frequencies[ n1 ] += 1
		else:
			frequencies[ n1 ] = 0
		#print( printpro( p )[ 0 : 10 ], list( frequencies.keys( ) ), list( frequencies.values( ) ), frequency, cutoff, cutoff < frequency if frequency != None else None  )

		col.append( riv )
	return col

def remrows( rows ):
	for x in range( len( rows ) ):
		rows[ x ].sort( )
	rows.sort( )
	index = 0
	while index < len( rows ) - 1:
		if rows[ index ] == rows[ index + 1 ]:
			del rows[ index + 1 ]
		else:
			index += 1

def filterrows( pairs, index ):
	sel = {}
	for row in pairs:
		pair = row[ -1 ]
		ok = sel.get( row[ index ] )
		if ok == None:
			sel[ row[ index ] ] = [ ]
			sel[ row[ index ] ].append( pair )
		else:
			sel[ row[ index ] ].append( pair )

	return sel

def freqs( Q, p, isDict=True ):
	col = [ ]
	if isDict:
		for row in Q:
			riv = {}
			for perm in list( combinations( row, 2 ) ):
				n1, n2 = perm[ 0 ], perm[ 1 ]
				riv[ perm ] = p[ n1 ][ n2 ][ 0 ]
			for perm in list( combinations( row, 3 ) ):
				n1, n2, n3 = perm[ 0 ], perm[ 1 ], perm[ 2 ]
				riv[ perm ] =  p[ n1 ][ n2 ][ n3 ][ 0 ]
			for perm in list( combinations( row, 4 ) ):
				n1, n2, n3, n4 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ]
				riv[ perm ] =  p[ n1 ][ n2 ][ n3 ][ n4 ][ 0 ]
			col.append( riv )
	else:
		for row in Q:
			riv = [ ]
			riv2 = [ ]
			riv3 = [ ]
			riv4 = [ ]
			for perm in list( combinations( row, 2 ) ):
				n1, n2 = perm[ 0 ], perm[ 1 ]
				riv2.append( p[ n1 ][ n2 ][ 0 ] )
			for perm in list( combinations( row, 3 ) ):
				n1, n2, n3 = perm[ 0 ], perm[ 1 ], perm[ 2 ]
				riv3.append( p[ n1 ][ n2 ][ n3 ][ 0 ] )
			for perm in list( combinations( row, 4 ) ):
				n1, n2, n3, n4 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ]
				riv4.append( p[ n1 ][ n2 ][ n3 ][ n4 ][ 0 ] )
			riv.append( riv2 )
			riv.append( riv3 )
			riv.append( riv4 )
			col.append( riv )
	return col

def getpcol( p ):
	pcol = { }
	for num1 in range( 1, 51 ):
		for num2 in range( 1, 51 ):
			if num1 < num2:
				key = "{} {}".format( num1, num2 )
				pcol[ key ] = p[ num1 ][ num2 ][ 0 ]
				for num3 in range( 1, 51 ):
					if num2 < num3:
						key = "{} {} {}".format( num1, num2, num3 )
						pcol[ key ] = p[ num1 ][ num2 ][ num3 ][ 0 ]
						for num4 in range( 1, 51 ):
							if num3 < num4:
								key = "{} {} {} {}".format( num1, num2, num3, num4 )
								pcol[ key ] = p[ num1 ][ num2 ][ num3 ][ num4 ][  0 ]
	return pcol

def findpvalues( pcol, row ):
	col = [ ]
	riv = [ ]
	for perm in combinations( row, 2 ):
		key = "{} {}".format( perm[ 0 ], perm[ 1 ] )
		riv.append( pcol[ key ] )
	col.append( riv )
	riv = [ ]
	for perm in combinations( row, 3 ):
		key = "{} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ] )
		riv.append( pcol[ key ] )
	col.append( riv )
	riv = [ ]
	for perm in combinations( row, 4 ):
		key = "{} {} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ] )
		riv.append( pcol[ key ] )
	col.append( riv )
	return col

# function permpoints
# param row
# param p
# param r

def permpoints( row, p, r, null=0 ):
	col = [ ]
	for perm in list( combinations( row, r ) ):
		if r == 5:
			n1, n2, n3, n4, n5 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ], perm[ 4 ]
			key = "{} {} {} {} {}".format( n1, n2, n3, n4, n5 )
			if p.get( key ) == None:
				col.append( null )
			else:
				col.append( p[ key ] )
		elif r == 4:
			n1, n2, n3, n4 = perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ]
			key = "{} {} {} {}".format( n1, n2, n3, n4 )
			if p.get( key ) == None:
				col.append( null )
			else:
				col.append( p[ key ] )
		elif r == 3:
			n1, n2, n3 = perm[ 0 ], perm[ 1 ], perm[ 2 ]
			key = "{} {} {}".format( n1, n2, n3 )
			if p.get( key ) == None:
				col.append( null )
			else:
				col.append( p[ key ] )
		elif r == 2:
			n1, n2 = perm[ 0 ], perm[ 1 ]
			key = "{} {}".format( n1, n2 )
			if p.get( key ) == None:
				col.append( null )
			else:
				col.append( p[ key ] )
		elif r == 1:
			n1 = perm[ 0 ]
			key = "{}".format( n1 )
			if p.get( key ) == None:
				col.append( 0 )
			else:
				col.append( p[ key ] )
	return col

# function makeys
# param row
# param r
def makeys( row, r ):
	col = [ ]
	for perm in list( combinations( row, r ) ):
		line = ''
		for x in range( len( perm ) ):
			if x == len( perm ) - 1:
				line += repr( perm[ x ] )
			else:
				line += repr( perm[ x ] )
				line += ' '
		col.append( line )
	return col

def pickresults( res ):
	col = [ ]
	for sample in res:
		riv = [ [ ] for x in range( 3 ) ]
		for x in range( len( sample ) ):
			item0, item1, item2 = sample[ x ][ 0 ], sample[ x ][ 1 ], sample[ x ][ 2 ]
			if type( item0[ 0 ] ) == int:
				riv[ 0 ].append( [ sum( item0 ), min( item0 ), mean( item0 ), median( item0 ), max( item0 ) ] )
				riv[ 1 ].append( [ sum( item1 ), min( item1 ), mean( item1 ), median( item1 ), max( item1 ) ] )
				riv[ 2 ].append( [ sum( item2 ), min( item2 ), mean( item2 ), median( item2 ), max( item2 ) ] )
			else:
				item0 = [ row[ 0 ] for row in sample[ x ][ 0 ] ]
				item1 = [ row[ 0 ] for row in sample[ x ][ 1 ] ]
				item2 = [ row[ 0 ] for row in sample[ x ][ 2 ] ]
				riv[ 0 ].append( [ sum( item0 ), min( item0 ), mean( item0 ), median( item0 ), max( item0 ) ] )
				riv[ 1 ].append( [ sum( item1 ), min( item1 ), mean( item1 ), median( item1 ), max( item1 ) ] )
				riv[ 2 ].append( [ sum( item2 ), min( item2 ), mean( item2 ), median( item2 ), max( item2 ) ] )

		col.append( riv )
	return col

def getresults( rows, pfunc, targetfunc, resfunc, vali=None, fre=False ):
	res = [ ]
	index = 0
	rvali = 0 if vali == None else vali + 1
	for x in range( len( rows ) - rvali ):
		if vali == None:
			target = pfunc( rows[  x + 1 :: ] )
		else:
			target = pfunc( rows[  x + 1 : x + rvali ] )
		m2 = makerow( rows[ x ], 2, target )
		m3 = makerow( rows[ x ], 3, target )
		m4 = makerow( rows[ x ], 4, target )
		if fre:
			m2 = [ row[ 0 ] if type( row ) == list else row for row in m2 ]
			m3 = [ row[ 0 ] if type( row ) == list else row for row in m3 ]
			m4 = [ row[ 0 ] if type( row ) == list else row for row in m4 ]
		res.append( [ targetfunc( m2 ), targetfunc( m3 ), targetfunc( m4 ) ] )
	return resfunc( [ row[ 0 ] for row in res ] ), resfunc( [ row[ 1 ] for row in res ] ), resfunc( [ row[ 2 ] for row in res ] )

def makerow( row, r, p ):
	m = makeys( row, r )
	riv = [ ]
	for key in m:
		item = p.get( key )
		if item == None:
			riv.append( 0 )
		else:
			riv.append( item )
	return riv

def findkeys( p, key ):
	col = { }
	for perm in list( p.keys( ) ):
		for pkey in perm.split( " " ):
			if key == pkey:
				col[ perm ] = p[ perm ]
				break
	return col

def findrow( row, p ):
	fk = findkeys( p, repr( row[ 0 ] ) )
	for num in row[ 1 :: ]:
		fk = findkeys( fk, repr( num ) )
	return fk

def turnnumber( col ):
	keys = list( col.keys( ) )
	nums = {}
	for key in keys:
		for num in key.rsplit( " " ):
			ok = nums.get( num )
			if ok == None:
				nums[ num ] = 1
			else:
				nums[ num ] += 1
	return nums

def findrelnumber( npk ):
	nums = {}
	keys, values = list( npk.keys( ) ), list( npk.values( ) )
	for x in range( len( keys ) ):
		row = keys[ x ].rsplit( " " )
		for num in row:
			ok = nums.get( num )
			if ok == None:
				nums[ num ] = len( values[ x ] )
	return nums

def calculatedist( col ):
	res = [ ]
	for x in range( len( col ) - 1 ):
		res.append( abs( col[ x ] - col[ x + 1 ] ) )
	return res

def q0rowdel( q0, Q, delfunc ):
	index = 0
	qmaara, qpros, qchange = len( q0 ), .1, .1
	qlimit = round( qmaara * qpros, 3 )
	t0 = datetime.today( )
	print( t0 )
	while index < len( q0 ):
		qrow = Q[ int( q0[ index ], 2 ) ]
		if delfunc( qrow ):
			index += 1
		else:
			del q0[ index ]
		counter += 1
		if counter > qlimit:
			t1 = datetime.today( )
			print( t1, t1 - t0, counter, len( q0 ) )
			qpros += qchange
			qlimit = round( qmaara * qpros, 3 )

def delfunc( qrow, r, fo, lim ):
	for perm in list( combinations( qrow, r ) ):
		if r == 1:
			nums = "{}".format( perm[ 0 ] )
		elif r == 2:
			nums = "{} {}".format( perm[ 0 ], perm[ 1 ] )
		elif r == 3:
			nums = "{} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ] )
		elif r == 4:
			nums = "{} {} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ] )
		freqs = fo.get( nums )
		if freqs != None and freqs[ 0 ] < lim:
			return False
	return True

def q0rowdel( q0, Q, delfunc ):
	index = 0
	counter = 0
	qmaara, qpros, qchange = len( q0 ), .1, .1
	qlimit = round( qmaara * qpros, 3 )
	t0 = datetime.today( )
	print( t0 )
	while index < len( q0 ):
		qrow = Q[ int( q0[ index ], 2 ) ]
		if delfunc( qrow ):
			index += 1
		else:
			del q0[ index ]
		counter += 1
		if counter > qlimit:
			t1 = datetime.today( )
			print( t1, t1 - t0, counter, len( q0 ) )
			qpros += qchange
			qlimit = round( qmaara * qpros, 3 )

def pickperms( row, r ):
	col = [ ]
	for perm in list( combinations( row, r ) ):
		if r == 1:
			key = "{}".format( perm[ 0 ] )
		elif r == 2:
			key = "{} {}".format( perm[ 0 ], perm[ 1 ] )
		elif r == 3:
			key = "{} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ] )
		elif r == 4:
			key = "{} {} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ] )
		col.append( key )
	return col

def picksel( row, fo, r ):
	p = pickperms( row, r )
	sel = {}
	for key in p:
		item = fo.get( key )
		if item == None:
			sel[ key ] = [ ]
		else:
			sel[ key ] = item
	return sel


def genlres( freqs ):
		lres = [ [] for x in range( 5 ) ]
		for row in freqs[ 0 ]:
			l = length( row )
			for x in range( len( l ) ):
				while len( lres[ 0 ] ) < len( l ):
					lres[ 0 ].append( [ ] )
				while len( lres[ 0 ][ x ] ) < l[ x ] + 1:
					lres[ 0 ][ x ].append( 0 )
				lres[ 0 ][ x ][ l[ x ] ] += 1
		for row in freqs[ 1 ]:
			l = length( row )
			for x in range( len( l ) ):
				while len( lres[ 1 ] ) < len( l ):
					lres[ 1 ].append( [ ] )
				while len( lres[ 1 ][ x ] ) < l[ x ] + 1:
					lres[ 1 ][ x ].append( 0 )
				lres[ 1 ][ x ][ l[ x ] ] += 1
		for row in freqs[ 2 ]:
			l = length( row )
			for x in range( len( l ) ):
				while len( lres[ 2 ] ) < len( l ):
					lres[ 2 ].append( [ ] )
				while len( lres[ 2 ][ x ] ) < l[ x ] + 1:
					lres[ 2 ][ x ].append( 0 )
				lres[ 2 ][ x ][ l[ x ] ] += 1
		for row in freqs[ 3 ]:
			l = length( row )
			for x in range( len( l ) ):
				while len( lres[ 3 ] ) < len( l ):
					lres[ 3 ].append( [ ] )
				while len( lres[ 3 ][ x ] ) < l[ x ] + 1:
					lres[ 3 ][ x ].append( 0 )
				lres[ 3 ][ x ][ l[ x ] ] += 1
		return lres

def genfreq( row, x, f, r, vali ):
		riv = {}
		for item in combinations( row, r ):
			if r == 1:
				key = "{}".format( item[ 0 ] )
			elif r == 2:
				key = "{} {}".format( item[ 0 ], item[ 1 ] )
			elif r == 3:
				key = "{} {} {}".format( item[ 0 ], item[ 1 ], item[ 2 ] )
			elif r == 4:
				key = "{} {} {} {}".format( item[ 0 ], item[ 1 ], item[ 2 ], item[ 3 ] )
			item = f.get( key )
			if item == None:
                                riv[ key ] = [ ]
			else:
                                riv[ key ] = [ num - x for num in item if num < x + vali and ( num - x ) > 0 ]
		return riv

def genfreqs( rows, f, perms, vali ):
		freqs = [ [ ] for x in range( perms[ -1 ] ) ]

		for x in range( len( rows ) - vali ):
			for r in perms:
				riv = genfreq( rows[ x ], x, f, r, vali )
				freqs[ r - 1 ].append( list( riv.values( ) ) )
		return freqs

def qfreqdel( q0, Q, delfunc ):
	index, counter = 0, 0
	qmaara, qpros, qchange = len( q0 ), 0, .1
	qlimit, t0 = round( qmaara * qpros, 3 ), datetime.today( )
	print( t0 )
	while index < len( q0 ):
		qrow = Q[ int( q0[ index ], 2 ) ]
		if delfunc( qrow ):
			index += 1
		else:
			del q0[ index ]
		counter += 1
		if counter > qlimit:
			t1 = datetime.today( )
			print( t1, t1 - t0, len( q0 ), counter )
			qpros += qchange
			qlimit = round( qmaara * qpros )

def countpoints( row, f, r, x, vali ):
	points = 0
	for perm in list( combinations( row, r ) ):
		if r == 2:
			key = "{} {}".format( perm[ 0 ], perm[ 1 ] )
		if r == 3:
			key = "{} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ] )
		if r == 4:
			key = "{} {} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ] )
		item = f.get( key )
		if item != None:
			riv = [ num - x for num in f[ key ] if num < x + vali and ( num - x ) > 0 ]
			points += len( riv )
	return points

def getfkeys( row, r ):
	return [ "{} {}".format( perm[ 0 ], perm[ 1 ] ) if len( perm ) == 2 else "{} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ] ) if len( perm ) == 3 else "{} {} {} {}".format( perm[ 0 ], perm[ 1 ], perm[ 2 ], perm[ 3 ] ) for perm in list( combinations( row, r ) ) ]


def getfvalues( f, keys ):
	return [ f[ key ] if f.get( key ) != None else [ ] for key in keys ]


def numpairs( row, f1, r, index=None ):
	riv = [ ]
	for perm in list( combinations( row, r ) ):
		key = ''
		stop = len( perm )
		for x in range( stop ):
			if x == stop - 1:
				key += repr( perm[ x ] )
			else:
				key += repr( perm[ x ] )
				key += ' '
		item = f1.get( key )
		if item == None:
			riv.append( [ ] )
		else:
			if index != None:
				item = [ num for num in item if num > index ]
			riv.append( item )
	return riv

def rivscore( riv, max_value ):
	points = [ ]
	for value in riv:
		start_value, end_value = 0, value[ 0 ] if len( value ) > 0 else 1
		if end_value == 0:
			end_value = 1
		points.append( ( ( end_value - start_value ) / end_value  ) * ( ( max_value - len( value ) ) / max_value )  )
	return points


def pickmax( f1, r ):
	max_value = -1
	for key in list( f1.keys( ) ):
		if len( key.rsplit( " " ) ) == r:
			length = len( f1[ key ] )
			max_value = max_value if max_value > length else length
	return max_value

def picksizes( qv ):
	col = [ ]
	for row in qv:
		token = row[ 0 ].rsplit( " ")
		while len( col ) < len( token ) + 1:
			col.append( [ ] )
		col[ len( token ) ].append( row )
	return col
