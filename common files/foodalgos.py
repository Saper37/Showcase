import sys

# rasvaprosentti 10.47 62.67
# mitat 37 77
FATLESS_WEIGHT = 62.67

# function basicfunc
# param factor double value
# param weight double value
# param add inter value
# return numerical value
# The purpose of the function is to calculate the basic energy need for the day.
# Both factor and add are constant values
# The function can be used alone or with caloreintake, in which case
# this function's result is used as parameter for caloreintake function
# It is important to know that the values need to be added for the function
# as it doesn't know them, it merely provides the formula
# Formula checked from vastauspankki - kuinka laskea kalorinkulutus
def basicfunc( factor, weight, add ):
	return ( factor * weight ) + add

# function caloreintake
# param basicf double value
# param factor double value
# return double value
# The purpose of the function is to calculate the caloreintake need for the day.
# It is important to know that the values need to be added for the function
# as it doesn't know them, it merely provides the formula
# Formula checked from vastauspankki - kuinka laskea kalorinkulutus
def caloreintake( basicf, factor ):
	return basicf * factor



# function calculatecaloreintake
# param gender string, currently takes values mies and nainen
# param age integer
# param weight double
# param strain string, currently takes values kevyt, keskitehoinen
# return double value
# Calculates the expected calore need for the day based on gender, age, weight and strain
# Formula checked from vastauspankki - kuinka laskea kalorinkulutus 
def calculatecaloreintake( gender, age, weight, strain ):
	if gender == "mies":
		if 18 <= age <= 30:
			factor = 15.3
			add = 679
		elif 31 <= age <= 60:
			factor = 11.6
			add = 897
		else:
			factor = 13.5
			add = 487
		sfactor = strain
	elif gender == "nainen":
		if 18 <= age <= 30:
			factor = 14.7
			add = 496
		elif 31 <= age <= 60:
			factor = 8.7
			add = 829
		else:
			factor = 10.5
			add = 596
		sfactor = strain
	else:
                raise MyException( "Invalid Parameter Value for Gender. Argument : {}".format( gender )  )
	bf = basicfunc( factor, weight, add )
	return caloreintake( bf, sfactor )

# function optimalEA
# param optkal
# param weigt
# param spentcalore
# return float
# Calculates actual calore loss, calore balance. 
def optimalEA( optkal, weight, spentcalore ):
	return optkal * weight + spentcalore


def printcalore( weight, calore ):
	return "30: {}, 35: {}, 40: {}, 45: {}".format( optimalEA( 30, weight, calore ),optimalEA( 35, weight, calore ), optimalEA( 40, weight, calore ), optimalEA( 45, weight, calore ) )


if __name__ == "__main__":
	args = sys.argv
	if args[ 1 ] == "availability":
		weight = float( args[ 2 ] )if len( args ) > 3 else FATLESS_WEIGHT
		exercise = float( args[ 2 ] ) if len( args ) < 4 else float( args[ 3 ] )
		calore_value = printcalore( weight, exercise )
		print( "{}\n".format( calore_value ) )
	elif args[ 1 ] == "calore":
		gender = args[ 2 ]
		age = int( args[ 3 ] )
		weight = float( args[ 4 ] )
		strain = args[ 5 ]
		print( calculatecaloreintake( gender, age, weight, strain ) )
	else:
		raise MyException( "Invalid second Parameter {}".format( args[ 1 ] ) )
	