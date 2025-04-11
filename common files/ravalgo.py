from myfunctions import MyException

# function mypros
# creates a list of floats, 
# param row list of numbers
# param pros float, significant for round function
# 

def mypros( row, pros ):
	riv = [ ]
	koko = sum( row )
	for num in row:
		riv.append( round( num / koko, pros ) )
	return riv

# function planprofile
# takes 
# param meals
# param amounts
# param mydict
# var values list of float values 
# var summary list of 0. This gets iterated based on values from values var.
# var riv immediate value for calculating values from amounts and values.
# var list of lists of floats, collection of values gained from 

def planprofile( meals, amounts, mydict ):
	values = list( mydict.values( ) )
	amount_values = 8
	summary = [ 0 for x in range( amount_values )]
	md = [ ]
	for x in range( len( meals ) ):
		meal = meals[ x ]
		amount = amounts[ x ]

		if len( meal ) != len ( amount ):
                        # in case where meal and amount aren't equal
			raise MyException( "Ongelma meal koko {} ja amount koko {}. \n meal is {} \namount is {}".format( len( meal ), len( amount ), meal, amount ) )
		
		riv = [ 0 for x in range( amount_values ) ]
		for x1 in range( len( meal ) ):
			smeal = meal[ x1 ]
			samount = float( amount[x1] )
			value = values[ smeal ]
			#debugging
			#print( summary, value )
			for x2 in range( len( value ) ):
				try:
					riv[ x2 ] += ( value[ x2 ] * samount )
					summary[ x2 ] += ( value[ x2 ] * samount )
				except IndexError:
					raise MyException( "summary len is {} value len is {} amount len is {} x1 is {}".format( len( summary ), len( value ), len( amount ), x1 ) )
		md.append( riv )
	return md, summary

# function makedict
# reads file content into dictionary and returns it
# param filename
# retunr mydict
def makedict( filename ):
	file = open( filename, 'r' )
	mydict = {}
	line = file.readline( )
	while line != '':
		riv = [ ]
		line = line.rsplit( " " )
		for token in line[1::]:
			try:
				riv.append( float( token ) )
			except ValueError:
				raise MyException( "Line is {}".format( line ) )
		mydict[ line[0] ] = riv
		line = file.readline( )
	file.close( )
	return mydict


# function pickkeys
# param keys list of strings. 
# param meals list of list of strings
# param smealamounts list of list of floats. Value received from file meals.py
# raises error if smeals and smealamount aren't equal length.
# creates list variables meals and amounts, and appends them with key indexces and float values. 
def pickkeys( keys, smeals, smealamounts ):
	meals = [ ]
	amounts = smealamounts.rsplit( " " )
	if len( amounts ) != len( smeals ):
		raise MyException( " Error with length\n amounts len is {} smeals len is {}\n amounts is {}\n smeals is {} ".format( len( amounts ), len( smeals ), amounts, smeals ) )
	for x in range( len( smeals ) ):
		meals.append( keys.index( smeals[ x ] ) )
	return meals, amounts

# function rounding
# param s list of numbers
# param maara significant value for num
# rounds values gained from s with significance maara and returns values.
def rounding( s, maara ):
	col = [ ]
	for num in s:
		col.append( round( num, maara ) )
	return col


def countCosts( meals, prices ):
	col = [ ]
	for x in range( len( meals ) ):
		amounts = meals[ x ][1].rsplit( " " )
		riv = [ ]
		for x1 in range( len( meals[ x ][ 0 ] ) ):
			smeal = meals[ x ][ 0 ][ x1 ]
			amount = amounts[ x1 ]
			price = prices[ smeal ]
			riv.append( round( price[0] * ( float( amount ) / price[ 1 ] ) , 3 ) )
		col.append( riv )
	return col

def rounding( s, maara ):
		col = [ ]
		for num in s:
			col.append( round( num, maara ) )
		return col

# function countCosts
# param meals
# param prices
# var col list of list of floats
# 
def countCosts( meals, prices ):
	col = [ ]
	
	for x in range( len( meals ) ):
		amounts = meals[ x ][1].rsplit( " " )
		riv = [ ]
		
		for x1 in range( len( meals[ x ][ 0 ] ) ):
                        
			smeal = meals[ x ][ 0 ][ x1 ]
			amount = amounts[ x1 ]
			amount = float( amount )
			price = prices[ smeal ]
			
			total_price = price[ 0 ]
			product_size = price[ 1 ]
			change_amount = int( price[ 2 ] )
			# Changes between discrete = 1 and continous amounts = 0
			if change_amount == 0:
				amount1 = ( amount * 100.0 ) / product_size
			elif change_amount == 1:
				amount1 = ( amount / product_size )
				
			total_Cost = round( total_price * amount1 , 5 )
			#print( '{} prodcut_size {} amount {} amount1 {} total_price {} totalCost {}'.format( smeal, product_size, amount, amount1, total_price, total_Cost ) )
			riv.append( total_Cost )
		col.append( riv )
	return col

#function readContent
# Reads the costs file 
# param textile
# 
# return costs
def readContent( textfile ):
	with open( textfile, 'r' ) as file:
		content = file.read( )
	content = content.rsplit( "\n" )
	costs = {}
	for x in range( len( content ) ):
		if content[ x ] != '':
			content[ x ] = content[ x ].rsplit( " " )
			content[ x ][ 1 ] = float( content[ x ][ 1 ] )
			costs[ content[ x ][ 0 ]  ] = content[ x ][ 1 ], float( content[ x ][ 2 ] ), content[ x ][ 3 ]
	return costs

# function printmeal
# param smeals
# param keys
# param costs
# param mydict
# uses function pickkeys
# uses function planpfogile
# uses function countCosts
# uses function rounding
def printmeal( smeals, keys, costs, mydict ):
	meals = [ ]
	for x in range( len( smeals ) ):
		try:
			meals.append( pickkeys( keys, smeals[x][0], smeals[x][1] ) )
		except IndexError:
			raise MyException( " Error in index \n smeals length {} smeals[ 0 ] length {} smeals[ 1 ] {}\n smeals[ 0 ] is {} \n smeals[ 1 ] is {} ".format( len( smeals ), len( smeals[ 0 ] ), len( smeals[ 1 ] ), smeals[ 0 ], smeals[1 ] ) )
	n = [ 0 for x in range( 8 ) ]
	wc = [ .0 for x in range( 8 ) ]
	amounts = [ meal[1] for meal in meals ]
	meals = [ meal[0] for meal in meals ]
	nm, summary = planprofile( meals, amounts, mydict )
	scosts = countCosts( smeals, costs )
	sumCost = 0
	print( "------------------------------------------------------------ ")
	for x in range( len( nm ) ):
		n = nm[ x ]
		s = scosts[ x ]
		sumCost += sum( s )
		print("      {}  {}  {}".format( rounding( n, 2 ), sum( s ), s ) )
	print( "Whole {} Cost {}\nPrecentage    {}\nWater consumption {} {}".format( rounding( summary, 3 ), sumCost, mypros( summary[1::], 3 ), wc, round( sum( wc ), 3 ) ) )

mydict = makedict( 'ravinto.txt' )

# class MealManager
# variables meals, the list of list of names and list of amounts of food
# variables mealindex, the index for nextmeal function
# variables mealdict, dictionary build previously containing food names and nutritional values
# function init
# function setmeal setter function for meals
# function iterate, iterates the value of mealindex
# function nextmeal, return next meal with the format of the food name, the amount, nutrional value per the amount 
class MealManager:
	def __init__( self, mydict, meals=None, costs=None):

		self.meals = meals
		self.mealindex = 0
		self.mealdict = mydict
		self.costs = costs
		self.keys = list( self.mealdict.keys( ) )
		self.values = list( self.mealdict.values( ) )
		self.num_of_values = len( self.values[ 0 ] )

	def setmeals( self, meals ):
		self.meals = meals

	def setcosts( self, costs ):
		self.meals = costs

	def iterate( self ):
		self.mealindex = self.mealindex + 1 if self.mealindex < len( self.meals ) else 0

	def countCosts( self, amounts ):
		col = [ ]
		for x in range( len( self.meals ) ):
			riv = [ ]
			meals = self.meals[ x ]
			for x1 in range( len( meals[ 0 ] ) ):
				meal = meals[ 0 ][ x1 ]
				amount = float( amounts[ x1 ] )
				price = self.costs[ meal ]
				total_price = price[ 0 ]
				product_size = price[ 1 ]
				change_amount = int( price[ 2 ] )
				# Changes between discrete = 1 and continous amounts = 0
				if change_amount == 0:
					amount1 = ( amount * 100.0 ) / product_size
				elif change_amount == 1:
					amount1 = ( amount / product_size )
				total_Cost = round( total_price * amount1 , 5 )
				#print( '{} prodcut_size {} amount {} amount1 {} total_price {} totalCost {}'.format( smeal, product_size, amount, amount1, total_price, total_Cost ) )
				riv.append( total_Cost )
			col.append( riv )
		return col

	def printmeal( self ):
		meals = [ ]
		keys = list( self.mealdict.keys( ) )
		for x in range( len( self.meals ) ):
			try:
				meals.append( pickkeys( keys, self.meals[ x ][ 0 ], self.meals[ x ][ 1 ] ) )
			except IndexError:
				raise MyException( " Error in index \n smeals length {} smeals[ 0 ] length {} smeals[ 1 ] {}\n smeals[ 0 ] is {} \n smeals[ 1 ] is {} ".format( len( smeals ), len( smeals[ 0 ] ), len( smeals[ 1 ] ), smeals[ 0 ], smeals[1 ] ) )
		amounts = [ meal[ 1 ] for meal in meals ]
		meals = [ meal[ 0 ] for meal in meals ]
		nm, summary = self.planprofile( meals, amounts )
		scosts = self.countCosts( self.costs )
		sumCost = 0
		print( "---------------------------------- ")
		for x in range( len( nm ) ):
			n = nm[ x ]
			s = scosts[ x ]
			sumCost += sum( s )
			print("      {}  {}  {}".format( rounding( n, 2 ), sum( s ), s ) )
		print( "Whole {} Cost {}\nPrecentage    {}\nWater consumption {} {}".format( rounding( summary, 3 ), sumCost, mypros( summary[1::], 3 ), wc, round( sum( wc ), 3 ) ) )

	def planprofile( self, meals, amounts ):
		summary = [ 0 for x in range( self.num_of_values ) ]
		md = [ ]
		for x in range( len( meals ) ):
			meal = meals[ x ]
			amount = amounts[ x ]
			if len( meal ) != len ( amount ):
				# in case where meal and amount aren't equal
				print( meal, len( meal ) )
				print( amount, len( amount ) )
				raise MyException( "Ongelma meal koko {} ja amount koko {}. \n meal is {} \namount is {}".format( len( meal ), len( amount ), meal, amount ) )
			riv = [ 0 for x in range( self.num_of_values ) ]
			for x1 in range( len( meal ) ):
				food = meal[ x1 ]
				foodamount = float( amount[ x1 ] )
				value = self.values[ food ]
				for x2 in range( len( value ) ):
					try:
                                                rivvalue = ( value[ x2 ] * foodamount )
                                                riv[ x2 ] += rivvalue
                                                summary[ x2 ] += ( value[ x2 ] * foodamount )
					except IndexError:
						raise MyException( "summary len is {} value len is {} amount len is {} x1 is {} values is {}, foodamount is {}".format( len( summary ), len( value ), len( amount ), x1, value[ x2 ], foodamount ) )
			md.append( riv )
		return md, summary


	def nextmeal( self ):
		col = [ ]
		m0, m1 = self.meals[ self.mealindex ][ 0 ], self.meals[ self.mealindex ][ 1 ]
		m1 = m1.rsplit( " " )
		for x in range( len( m0 ) ):
			foodvalues = self.mealdict[ m0[ x ] ]
			sm0 = m0[ x ]
			amount = float( m1[ x ] )
			price = self.costs[ sm0 ]
			total_price = price[ 0 ]
			product_size = price[ 1 ]
			change_amount = int( price[ 2 ] )
			# Changes between discrete = 1 and continous amounts = 0
			if change_amount == 0:
				amount1 = ( amount * 100.0 ) / product_size
			elif change_amount == 1:
				amount1 = ( amount / product_size )
			total_cost = round( total_price * amount1 , 5 )

			while len( sm0 ) < 28:
				sm0 += ' '
			amount = float( m1[ x ] )
			values = [ round( nutrion * amount, 4 ) for nutrion in foodvalues ]
			try:
				col.append( "{}{}| {} | {}  {}  {}  {}  {}  {} {} {}".format( sm0, amount, total_cost, values[ 0 ], values[ 1 ], values[ 2 ], values[ 3 ], values[ 4 ], values[ 5 ], values[ 6 ], values[ 7 ] ) )
			except IndexError:
				raise MyException( m0[ x ] )

		return col
