import numpy as np
from sklearn import svm
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot

speed = [  0, 6.1, 7, 8, 9, 10.2, 11.3, 12.4, 13.5, 14.6, 14.6]
beat = [  52, 120, 135, 141, 146, 156, 160, 172, 177, 183, 187 ]
vo2 = [ 3.5, 23.4, 30.5, 36, 39.2, 42.1, 46.7, 53.8, 59.6, 63.6, 65.5 ]

speed = [ [ float( item ) ] for item in speed ]
beat = [ [ float( item ) ] for item in beat ]
vo2 = [ [ item ] for item in vo2 ]

def extender( cand_lists ):
    col = [ ]
    for clist in cand_lists:
        col.extend( col )
    return col
x_train = extender( [ beat for x in list( range( 0, 10 ) ) ] )
y_train = extender( [ vo2 for x in list( range( 0, 10 ) ) ] )
preds = [ 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185 ]
print( len( speed ), len( beat ), len( vo2 ), len( preds ))
#predict = np.array( preds )
#predict = predict.reshape( 1, -1 )

#svm = svm.SVC( )
#svm.fit( beat, vo2 )
#sv.predict( predict )
#enet = LinearRegression( )
#enet = ElasticNet( random_state=0 )
#enet.fit( beat, vo2 )

svr_poly = SVR( kernel="poly", C=100, gamma="auto", degree=2, epsilon=0.1, coef0=1, max_iter=100000 )
svr_poly.fit( beat, vo2 )

#forestRegressor = RandomForestRegressor( n_estimators=100, criterion="absolute_error" )
#forestRegressor.fit( beat, vo2 )
model = svr_poly
predict = [ ]
reses = [ ]
for num in preds:
    print( num )
    num = np.array( num )
    num = num.reshape( 1, -1 )
    res = model.predict( num )
    reses.append( [ float( res / 3.5 ), int( num ) ]  )
    predict.append( num )
print( reses )

#pyplot.figure( )
#pyplot.plot( speed, vo2, "bo"  )
#pyplot.plot( [ predict ] )
#pyplot.show( )