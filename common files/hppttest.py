import requests as req

r = req.get( "https://www.tutorialpoint.com/python/" )
print( r.text [ 0 : 300 ] ) 