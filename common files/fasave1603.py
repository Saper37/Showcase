Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running13", 12.3, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ],["walking64", 5, 1 * 40 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 5 * 60 ],["walking6.4", 5, 1 * 60 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.7
	fatless_weight = 63.4
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist


({30: 2876.313, 35: 3193.313, 38: 3383.513, 40: 3510.313, 43: 3700.513, 45: 3827.313}, 23.883, 974.3130000000001)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running13", 12.3, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 5 * 60 ],["walking6.4", 5, 1 * 60 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.7
	fatless_weight = 63.4
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2575.801, 35: 2892.801, 38: 3083.0009999999997, 40: 3209.801, 43: 3400.0009999999997, 45: 3526.801}, 24.0, 673.8009999999999)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running13", 12.3, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 5 * 60 ],["walking6.4", 5, 1 * 60 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2602.62, 35: 2923.62, 38: 3116.22, 40: 3244.62, 43: 3437.22, 45: 3565.62}, 24.0, 676.6199999999999)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running13", 12.3, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ],["walking64", 5, 1 * 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2637.018, 35: 2958.018, 38: 3150.618, 40: 3279.018, 43: 3471.618, 45: 3600.018}, 24.0, 711.018)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running13", 12.3, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ],["walking64", 5, 1 * 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 4191.669, 35: 4512.669, 38: 4705.269, 40: 4833.669, 43: 5026.269, 45: 5154.669}, 25.117, 2265.669)
>>> 3.5 * 1.6
5.6000000000000005
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running13", 12.3, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ],["walking56", 4.3, 1 * 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 4138.749, 35: 4459.749, 38: 4652.349, 40: 4780.749, 43: 4973.349, 45: 5101.749}, 25.117, 2212.749)
>>> 12.8 * 1.6
20.480000000000004
>>> 8 * 1.6
12.8
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 25 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 34 ],[ "stretching", 2.3, 38 ],["walking56", 4.3, 1 * 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 4079.529, 35: 4400.529, 38: 4593.129, 40: 4721.529, 43: 4914.129, 45: 5042.529}, 25.117, 2153.529)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 7 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3977.683, 35: 4298.683, 38: 4491.282999999999, 40: 4619.683, 43: 4812.282999999999, 45: 4940.683}, 24.9, 2051.683)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3857.479, 35: 4178.478999999999, 38: 4371.079, 40: 4499.478999999999, 43: 4692.079, 45: 4820.478999999999}, 23.9, 1931.4789999999998)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2652.39, 35: 2973.39, 38: 3165.99, 40: 3294.39, 43: 3486.99, 45: 3615.39}, 23.217, 726.3899999999999)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 72
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2637.018, 35: 2958.018, 38: 3150.618, 40: 3279.018, 43: 3471.618, 45: 3600.018}, 24.0, 711.018)
>>> mepscore( 5, weight, 1 )
6.3
>>> mepscore( 5, weight, 60 ) / 60
6.3
>>> mepscore( 5, weight, 2 )
12.6
>>> mepscore( 5, weight, 120 ) / 60
12.6
>>> mepscore( 11, weight, 5 * 60 + 7 ) / 60
70.91699999999999
>>> def pacekmtomile( time, km ):
	return time / round( km / 1.609, 3 )

>>> pacekmtomile( 120, 2 )
96.54062751407884
>>> 96.54062751407884 / 60
1.6090104585679805
>>> def pacekmtomile( time, km ):
	return round( ( time / km) / 1.609, 3 )

>>> pacekmtomile( 120, 2 )
37.29
>>> pacekmtomile( 5 * 60 + 2, 5.9 )
31.813
>>> 31.813 / 60
0.5302166666666667
>>> def pacekmtomile( time, km ):
	return round( ( time / km ), 3 )

>>> pacekmtomile( 5 * 60 + 2, 5.9 )
51.186
>>> 5 * 60 + 2
302
>>> 302 / 5.9
51.1864406779661
>>> 51.1864406779661 / 60
0.8531073446327683
>>> 51.1864406779661 / 60 * 60
51.1864406779661
>>> pacekmtomile( 5 * 60 + 2, .5 )
604.0
>>> 604.0 / 60
10.066666666666666
>>> 0.5( 5 * 60 + 2 )
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    0.5( 5 * 60 + 2 )
TypeError: 'float' object is not callable
>>> 0.5 / ( 5 * 60 + 2 )
0.0016556291390728477
>>> 0.0016556291390728477 / 60
2.759381898454746e-05
>>> 0.5 / ( 5 )
0.1
>>> ( 5 * 60 + 2 ) / .5
604.0
>>> 604.0 / 60
10.066666666666666
>>> .5 / ( 5 * 60 + 2 )
0.0016556291390728477
>>> 0.0016556291390728477 / 60
2.759381898454746e-05
>>> 60 / 0.0016556291390728477
36240.0
>>> 0.0016556291390728477 * 60
0.09933774834437085
>>> .5 / ( 5 * 60 + 2 )
0.0016556291390728477
>>> 500 / ( 5 * 60 + 2 )
1.6556291390728477
>>> 5.9 * 1.6
9.440000000000001
>>> 5.9 / 1.6
3.6875
>>> def kmtomile( km ):
	return km / 1.6

>>> kmtomile( 5.9 )
3.6875
>>> kmtomile( 6.7 )
4.1875
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking64", 5, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2630.105, 35: 2951.105, 38: 3143.705, 40: 3272.105, 43: 3464.705, 45: 3593.105}, 24.0, 704.105)
>>> kmtomile( 7.5 )
4.6875
>>> kmtomile( 7.6 )
4.749999999999999
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking75", 7, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2630.105, 35: 2951.105, 38: 3143.705, 40: 3272.105, 43: 3464.705, 45: 3593.105}, 24.0, 704.105)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking75", 7, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2795.058, 35: 3116.058, 38: 3308.658, 40: 3437.058, 43: 3629.658, 45: 3758.058}, 23.217, 869.058)
>>> 
========================================================================================================= RESTART: Shell ========================================================================================================
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking75", 7, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2795.058, 35: 3116.058, 38: 3308.658, 40: 3437.058, 43: 3629.658, 45: 3758.058}, 23.217, 869.058)
>>> mepscore( mepclass( "walking", kmtomile( 5.9 ) ), weight, 5 )
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    mepscore( mepclass( "walking", kmtomile( 5.9 ) ), weight, 5 )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 126, in mepclass
    raise MyException( "Undefined milesPerHour ")
NameError: name 'MyException' is not defined
>>> kmtomile( 5.9 )
3.667
>>> 
========================================================================================================= RESTART: Shell ========================================================================================================
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ],["walking75", 7, 1 * 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2795.058, 35: 3116.058, 38: 3308.658, 40: 3437.058, 43: 3629.658, 45: 3758.058}, 23.217, 869.058)
>>> mepscore( mepclass( "walking", kmtomile( 5.9 ) ), weight, 5 )
26.826624999999996
>>> mepscore( mepclass( "walking", kmtomile( 6.7 ) ), weight, 5 )
31.193749999999998
>>> mepscore( mepclass( "running", kmtomile( 11.6 ) ), weight, 5 )
68.62625
>>> 60 * 5 + 2
302
>>> 302 / 60
5.033333333333333
>>> def convertime( seconds ):
	return seconds / 60

>>> convertime( 60 * 5 + 2 )
5.033333333333333
>>> mepscore( mepclass( "walking", kmtomile( 5.9 ) ), weight, convertime( 60 * 5 + 2 ) )
27.005469166666664
>>> mepscore( mepclass( "running", kmtomile( 11.6 ) ), weight, convertime( 60 * 2 + 35 ) )
35.456895833333334
>>> for t in range( 1 ):
	meps = [ ]
	types = "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking"
	times = [ 5, 2 ], [ 4, 29 ], [ 2, 35 ], [ 4, 36 ], [ 4, 12 ], [ 2, 20], [ 4, 51 ], [ 4,29 ], [ 2, 15 ], [ 4, 45 ], [ 4, 28 ], [ 2, 16 ], [ 4, 43 ], [ 4, 39 ], [ 2, 9 ], [ 4, 58 ], [ 0, 19 ]
	kms = 5.9, 6.7, 11.6, 6.5, 7.1, 12.9, 6.2, 6.7, 13.3, 6.3, 6.7, 13.2,6.4, 6.4, 14, 6, 6.1
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
>>> meps
[27.005469166666664, 27.97039583333333, 35.456895833333334, 28.698249999999994, 26.202749999999998, 34.35471666666667, 26.021826249999997, 27.97039583333333, 33.1277625, 25.485293749999997, 27.866416666666666, 33.373153333333335, 25.306449583333332, 24.94876125, 32.99674875, 26.647780833333332, 1.699019583333333]
>>> sum( meps )
465.13208583333335
>>> mepscore( 7, weight, 60 )
524.055
>>> mepscore( "customhit", weight, 60 )
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    mepscore( "customhit", weight, 60 )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 91, in mepscore
    return ( ( met * 3.5 * weight ) / 200 ) * minutes
TypeError: can't multiply sequence by non-int of type 'float'
>>> mepscore( 5, weight, 60 )
374.325
>>> mepscore( 6, weight, 60 )
449.18999999999994
>>> mepscore( 7, weight, 60 )
524.055
>>> mepscore( 6, weight, 60 )
449.18999999999994
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 0 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2271.003, 35: 2592.003, 38: 2784.603, 40: 2913.003, 43: 3105.603, 45: 3234.003}, 22.217, 345.00300000000016)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2742.652, 35: 3063.652, 38: 3256.252, 40: 3384.652, 43: 3577.252, 45: 3705.652}, 23.267, 816.652)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.2
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2630.105, 35: 2951.105, 38: 3143.705, 40: 3272.105, 43: 3464.705, 45: 3593.105}, 24.0, 704.105)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 5 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.24
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2631.305, 35: 2952.5049999999997, 38: 3145.225, 40: 3273.705, 43: 3466.4249999999997, 45: 3594.9049999999997}, 24.0, 704.105)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 64.24
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2775.046, 35: 3096.2459999999996, 38: 3288.966, 40: 3417.446, 43: 3610.1659999999997, 45: 3738.6459999999997}, 23.35, 847.846)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.24
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2631.305, 35: 2952.5049999999997, 38: 3145.225, 40: 3273.705, 43: 3466.4249999999997, 45: 3594.9049999999997}, 24.0, 704.105)
>>> for t in range( 1 ):
	meps = [ ]
	types = "walking", "walking", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking"
	times = [ 5, 15 ], [ 4, 47 ], [ 4, 50 ], [ 4, 42 ], [ 2, 36 ], [ 5, 0], [ 4, 49 ], [ 2,57 ], [ 5, 14 ], [ 4, 52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7, 6.3, 6.2, 6.4, 11.5, 6, 6.2, 6.2, 10.2, 5.7, 6.2, 5.9,6.2, 5.7, 6, 5.9, 6.0
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
Traceback (most recent call last):
  File "<pyshell#121>", line 7, in <module>
    m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 149, in mepclass
    raise MyException( "Undefined milesPerHour ")
NameError: name 'MyException' is not defined
>>> len( types )
17
>>> len( times )
17
>>> len( kms )
17
>>> x
7
>>> types[ x ]
'running'
>>> for t in range( 1 ):
	meps = [ ]
	types = "walking", "walking", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking"
	times = [ 5, 15 ], [ 4, 47 ], [ 4, 50 ], [ 4, 42 ], [ 2, 36 ], [ 5, 0], [ 4, 49 ], [ 2,57 ], [ 5, 14 ], [ 4, 52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7, 6.3, 6.2, 6.4, 11.5, 6, 6.2, 6.2, 10.2, 5.7, 6.2, 5.9,6.2, 5.7, 6, 5.9, 6.0
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
Traceback (most recent call last):
  File "<pyshell#128>", line 7, in <module>
    m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 149, in mepclass
    raise MyException( "Undefined milesPerHour ")
NameError: name 'MyException' is not defined
>>> kms[ x ]
6.2
>>> types[ x ]
'running'
>>> times[ x ]
[2, 57]
>>> for t in range( 1 ):
	meps = [ ]
	types = "walking", "walking", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking"
	times = [ 5, 15 ], [ 4, 47 ], [ 4, 50 ], [ 4, 42 ], [ 2, 36 ], [ 5, 0], [ 4, 49 ], [ 2,57 ], [ 5, 14 ], [ 4, 52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7, 6.3, 6.2, 6.4, 11.5, 6, 6.2, 6.2, 10.2, 5.7, 6.2, 5.9,6.2, 5.7, 6, 5.9, 6.0
	types = "walking","walking" "running"
	times = [ 5, 15 ],
	kms = 5.7
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )
KeyboardInterrupt
>>> for t in range( 1 ):
	meps = [ ]
	types = "walking", "walking", "walking", "walking", "running", "walking", "walking", "running", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking"
	times = [ 5, 15 ], [ 4, 47 ], [ 4, 50 ], [ 4, 42 ], [ 2, 36 ], [ 5, 0], [ 4, 49 ], [ 2,57 ], [ 5, 14 ], [ 4, 52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7, 6.3, 6.2, 6.4, 11.5, 6, 6.2, 6.2, 10.2, 5.7, 6.2, 5.9,6.2, 5.7, 6, 5.9, 6.0
	types = "walking","walking","walking","walking","running","walking","walking","running","walking","walking","walking","walking","walking","walking","walking","walking","walking"
	times = [ 5, 15 ],[4, 47 ], [4,50 ], [ 4,42 ],[2,36 ],[5, 0 ], [4, 49 ], [ 2, 57 ], [ 5, 14 ], [ 4,52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7,6.3, 6.2, 6.4, 11.5, 6, 6.2, 10.2, 5.7, 6.2, 5.9, 6.2, 5.7, 6, 5.9, 5.8, 6
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
Traceback (most recent call last):
  File "<pyshell#133>", line 10, in <module>
    m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 149, in mepclass
    raise MyException( "Undefined milesPerHour ")
NameError: name 'MyException' is not defined
>>> x
7
>>> for t in range( 1 ):
	meps = [ ]
	types = "walking", "walking", "walking", "walking", "running", "walking", "walking", "walking", "running", "walking", "walking", "walking", "walking", "walking", "walking", "walking", "walking"
	times = [ 5, 15 ], [ 4, 47 ], [ 4, 50 ], [ 4, 42 ], [ 2, 36 ], [ 5, 0], [ 4, 49 ], [ 2,57 ], [ 5, 14 ], [ 4, 52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7, 6.3, 6.2, 6.4, 11.5, 6, 6.2, 6.2, 10.2, 5.7, 6.2, 5.9,6.2, 5.7, 6, 5.9, 6.0
	types = "walking","walking","walking","walking","running","walking","walking","running","walking","walking","walking","walking","walking","walking","walking","walking","walking"
	times = [ 5, 15 ],[4, 47 ], [4,50 ], [ 4,42 ],[2,36 ],[5, 0 ], [4, 49 ], [ 2, 57 ], [ 5, 14 ], [ 4,52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7,6.3, 6.2, 6.4, 11.5, 6, 6.2, 10.2, 5.7, 6.2, 5.9, 6.2, 5.7, 6, 5.9, 5.8, 6
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
Traceback (most recent call last):
  File "<pyshell#136>", line 10, in <module>
    m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 149, in mepclass
    raise MyException( "Undefined milesPerHour ")
NameError: name 'MyException' is not defined
>>> x
7
>>> for t in range( 1 ):
	meps = [ ]
	
	types = "walking","walking","walking","walking","running","walking","walking","running","walking","walking","walking","walking","walking","walking","walking","walking","walking"
	times = [ 5, 15 ],[4, 47 ], [4,50 ], [ 4,42 ],[2,36 ],[5, 0 ], [4, 49 ], [ 2, 57 ], [ 5, 14 ], [ 4,52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7,6.3, 6.2, 6.4, 11.5, 6, 6.2, 10.2, 5.7, 6.2, 5.9, 6.2, 5.7, 6, 5.9, 5.8, 6
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
Traceback (most recent call last):
  File "<pyshell#139>", line 8, in <module>
    m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
  File "C:\Users\Samppa\AppData\Local\Programs\Python\Python38\foodalgos.py", line 149, in mepclass
    raise MyException( "Undefined milesPerHour ")
NameError: name 'MyException' is not defined
>>> x
7
>>> types[ x ]
'running'
>>> times[ x ]
[2, 57]
>>> kms[ x ]
10.2
>>> def kmtomile( km ):
	return round( km / 1.609, 3 )

>>> kmtomile( 10.2 )
6.339
>>> 
========================================================================================================= RESTART: Shell ========================================================================================================
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.24
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2631.305, 35: 2952.5049999999997, 38: 3145.225, 40: 3273.705, 43: 3466.4249999999997, 45: 3594.9049999999997}, 24.0, 704.105)
>>> for t in range( 1 ):
	meps = [ ]

	types = "walking","walking","walking","walking","running","walking","walking","running","walking","walking","walking","walking","walking","walking","walking","walking","walking"
	times = [ 5, 15 ],[4, 47 ], [4,50 ], [ 4,42 ],[2,36 ],[5, 0 ], [4, 49 ], [ 2, 57 ], [ 5, 14 ], [ 4,52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7,6.3, 6.2, 6.4, 11.5, 6, 6.2, 10.2, 5.7, 6.2, 5.9, 6.2, 5.7, 6, 5.9, 5.8, 6
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
Traceback (most recent call last):
  File "<pyshell#150>", line 8, in <module>
    m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
NameError: name 'convertime' is not defined
>>> 
========================================================================================================= RESTART: Shell ========================================================================================================
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 64.24
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2631.305, 35: 2952.5049999999997, 38: 3145.225, 40: 3273.705, 43: 3466.4249999999997, 45: 3594.9049999999997}, 24.0, 704.105)
>>> for t in range( 1 ):
	meps = [ ]

	types = "walking","walking","walking","walking","running","walking","walking","running","walking","walking","walking","walking","walking","walking","walking","walking","walking"
	times = [ 5, 15 ],[4, 47 ], [4,50 ], [ 4,42 ],[2,36 ],[5, 0 ], [4, 49 ], [ 2, 57 ], [ 5, 14 ], [ 4,52 ], [ 5, 7 ], [ 4, 48 ], [ 5, 13 ], [ 4, 59 ], [ 5, 7 ], [ 5, 8 ], [ 1, 51 ]
	kms = 5.7,6.3, 6.2, 6.4, 11.5, 6, 6.2, 10.2, 5.7, 6.2, 5.9, 6.2, 5.7, 6, 5.9, 5.8, 6
	for x in range( len( types ) ):
		m = mepscore( mepclass( types[ x ], kmtomile( kms[ x ] ) ), weight, convertime( 60 * times[ x ][ 0 ] + times[ x ][ 1 ] ) )
		meps.append( m )

		
>>> meps
[28.167956249999996, 25.664137916666665, 25.93240416666666, 25.217027499999997, 35.685649999999995, 26.826624999999996, 25.84298208333333, 40.4894875, 28.078534166666664, 26.11124833333333, 27.45257958333333, 25.753559999999997, 27.989112083333332, 26.737202916666664, 27.45257958333333, 27.542001666666668, 9.92585125]
>>> sum( meps )
460.86893999999995
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["walking6.4", 5, 1 * 60 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2617.08, 35: 2935.58, 38: 3126.6800000000003, 40: 3254.08, 43: 3445.1800000000003, 45: 3572.58}, 24.0, 706.0800000000002)
>>> mepscore( 7, weight, 77 )
674.4237499999999
>>> mepscore( 6, weight, 77 )
578.0775
>>> mepscore( 5, weight, 77 )
481.73125
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedule_easywalk
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2723.437, 35: 3041.937, 38: 3233.0370000000003, 40: 3360.437, 43: 3551.5370000000003, 45: 3678.937}, 24.283, 812.4370000000001)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 27 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3829.066, 35: 4147.566, 38: 4338.666, 40: 4466.066, 43: 4657.166, 45: 4784.566}, 23.9, 1918.066)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 30 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 + 30 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ]


	selected = schedulerun
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3873.3599999999997, 35: 4191.86, 38: 4382.96, 40: 4510.36, 43: 4701.46, 45: 4828.86}, 23.95, 1962.36)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 28 ], ["cooking", 2.5, 30 ], [ "running12.8", 11.8, 1 * 60 + 30 ],[ "stretching", 2.3, 38 ],["walking64", 5, 51 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedulerun
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3873.3599999999997, 35: 4191.86, 38: 4382.96, 40: 4510.36, 43: 4701.46, 45: 4828.86}, 23.95, 1962.36)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.3, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedulerun
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3858.3450000000003, 35: 4176.845, 38: 4367.945, 40: 4495.345, 43: 4686.445, 45: 4813.845}, 23.817, 1947.345)
>>> mepscore( 12.3, weight, 1 * 60 + 23 )
1277.401125
>>> mepscore( 12.5, weight, 1 * 60 + 23 )
1298.171875
>>> mepscore( 13, weight, 1 * 60 + 23 )
1350.0987499999999
>>> mepscore( 12.8, weight, 1 * 60 + 23 )
1329.3280000000002
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedulerun
	weight = 71.5
	fatless_weight = 63.7
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3910.272, 35: 4228.772, 38: 4419.872, 40: 4547.272, 43: 4738.372, 45: 4865.772}, 23.817, 1999.2720000000002)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedulerun
	weight = 71.6
	fatless_weight = 64.18
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3927.4680000000003, 35: 4248.368, 38: 4440.908, 40: 4569.268, 43: 4761.808000000001, 45: 4890.168000000001}, 23.817, 2002.0680000000002)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 6 * 60 ], [ "HIT", 6, 63 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_exercise_walk_easy
	weight = 71.6
	fatless_weight = 64.18
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2811.02, 35: 3131.92, 38: 3324.46, 40: 3452.82, 43: 3645.36, 45: 3773.7200000000003}, 23.35, 885.6199999999999)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 30 ], [ "HIT", 6, 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_exercise_walk_easy
	weight = 71.6
	fatless_weight = 64.18
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2815.155, 35: 3136.0550000000003, 38: 3328.5950000000003, 40: 3456.9550000000004, 43: 3649.4950000000003, 45: 3777.8550000000005}, 23.3, 889.7550000000001)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 30 ], [ "HIT", 6, 60 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2803.027, 35: 3122.527, 38: 3314.227, 40: 3442.027, 43: 3633.727, 45: 3761.527}, 23.3, 886.027)
>>> mepscore( 6, weight, 60 )
449.18999999999994
>>> mepscore( 6.5, weight, 60 )
486.62249999999995
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 30 ], [ "HIT", 6.5, 62 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 30 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2856.681, 35: 3176.181, 38: 3367.881, 40: 3495.681, 43: 3687.381, 45: 3815.181}, 23.333, 939.681)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 30 ], [ "HIT", 6.5, 62 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 1 * 60 + 20 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 3000.172, 35: 3319.672, 38: 3511.372, 40: 3639.172, 43: 3830.872, 45: 3958.672}, 24.167, 1083.172)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 20 ], [ "HIT", 6.5, 62 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 1 * 60 + 20 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],["CUSTOM_WALK", 5, 1 * 60 + 17 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_exercise_walk_easy
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2980.333, 35: 3299.833, 38: 3491.533, 40: 3619.333, 43: 3811.033, 45: 3938.833}, 24.0, 1063.333)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 20 ], [ "HIT", 6.5, 62 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 1 * 60 + 20 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 + 30 ],[ "HIT", 6.5, 62 ], ["cooking", 2.5, 30 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2749.6240000000003, 35: 3069.1240000000003, 38: 3260.824, 40: 3388.6240000000003, 43: 3580.324, 45: 3708.1240000000003}, 24.033, 832.6240000000003)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 20 ], [ "HIT", 6.5, 62 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 1 * 60 + 20 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60 ], ["standing", 1.59, 4 * 60 ],[ "HIT", 6.5, 62 ], ["cooking", 2.5, 30 ],[ "stretching13", 2.3, 38 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2799.159, 35: 3118.659, 38: 3310.359, 40: 3438.159, 43: 3629.859, 45: 3757.659}, 24.167, 882.1590000000001)
>>> for t in range( 1 ):
	from foodalgos import *

	exercises = {}
	times = []
	mets = [ ]
	activities = [ ]
	templates = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ],["walking5.8", 5, 2 * 60 ], ["walking_weighted64", 9, 0 ], ["walking6.4", 5, 0 ], ["walking7", 6, 46 ], [ "walking7.2",7,0 ], ["pushups", 3.8, 0 ], ["situp", 2.5, 0 ], [ "cleaning", 2.3, 0 ], [ "cleaning_weighted", 3.5, 0 ], ["walking_weighted30kg58", 6, 60 ], [ "resistance", 3.5, 0 ], [ "resistance_weighted", 6, 0 ], ["standingweighted", 2.1, 0 ], [ "biking", 9.4, 0 ], [ "running12", 11.5, 0 ], [ "running13", 12.3, 0 ],[ "running14", 14.5, 0 ],[ "stretching13", 2.3, 52 ],[ "stretching13", 2.3, 38 ],["walking6.8", 6, 60 ], ["walking7", 7, 67 ], [ "jogging", 7, 0 ], [ "jogwalk", 6, 0 ], ["walking5.2", 3.5, 60 ], [ "liftingweights", 5, 0 ], [ "HIT", 6, 0 ]



	baseactivities = [ "sleeping", 0.9, ( 60 * 8 ) ], [ 'lying', 1, 60 * 16 ]

	schedulerun = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 6 * 60 ], ["standing", 1.59, 6 * 60 + 18 ], ["cooking", 2.5, 30 ], [ "running12.8", 12.8, 1 * 60 + 23 ],[ "stretching", 2.3, 38 ],["walking64", 5, 60 ]

	schedule_exercise_walk =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 10 * 60], ["standing", 1.59, 3 * 60 ], [ "resistance_weighted30kg", 7, 10 ], ["walking_weighted20kg58", 5.1, 60 ],[ "stretching13", 2.3, 38 ], [ "liftingweights", 5, 10 ]
	schedule_exercise_walk_easy =  [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 7 * 60 ], ["standing", 1.59, 5 * 60 + 20 ], [ "HIT", 6.5, 62 ],[ "stretching", 2.3, 38 ], [ "liftingweights", 5, 10 ], ["cooking", 2.5, 30 ], [ "cleaning", 2.3, 1 * 60 + 20 ]


	schedule_easywalk = [ "sleeping", 0.9, ( 60 * 8 ) ],["sitting", 1.2, 9 * 60 + 50 ], ["standing", 1.59, 4 * 60 ],[ "HIT", 6.5, 62 ], ["cooking", 2.5, 30 ],[ "stretching13", 2.3, 38 ]
	schedule_total_rest = [ "sleeping", 0.9, ( 60 * 8 ) ], ["sitting", 1.2, 16 * 60 ], ["standing", 1.59, 0 ], ["cooking", 2.5, 30 ]


	selected = schedule_easywalk
	weight = 71.3
	fatless_weight = 63.9
	optkal = 45
	valuedict = {}
	calculatemep = lambda mep, time: mepscore( mep, weight, time )

	c1 = calculatecalories( selected, calculatemep )
	base_calories = calculatecalories( baseactivities, calculatemep )
	caloredist = abs( c1[ 0 ] - base_calories[ 0 ] )
	optvalue = [ optimalEA( value, fatless_weight, caloredist ) for value in [ 30, 35, 38, 40, 43, 45 ] ]
	for index, value in enumerate( [ 30, 35, 38, 40, 43, 45 ] ):
		valuedict[ value ] = optvalue[ index ]
	valuedict, c1[ 1 ], caloredist

	
({30: 2784.186, 35: 3103.686, 38: 3295.386, 40: 3423.186, 43: 3614.886, 45: 3742.686}, 24.0, 867.1860000000001)
>>> 