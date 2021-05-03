#!C:\Program Files\Python37\Python.exe
print("Content-type:text/html \n")


import cgi
import pickle

f = cgi.FieldStorage()

carbrand = f.getvalue("carBrand")
modelno = f.getvalue("modelno")
city = f.getvalue("city")
year = f.getvalue("year")
km = f.getvalue("km")
fuel = f.getvalue("fuel")
transmission = f.getvalue("transmission")
ownertype = f.getvalue("ownertype")
mileage = f.getvalue("mileage")
engine = f.getvalue("engine")
power = f.getvalue("power")
seats = f.getvalue("seats")
 

with open('check.pkl', 'rb') as f:
    x = pickle.load(f)
    

#predict the test set results
y_pred = x.predict([[float(city), float(year), float(km), float(fuel), float(transmission), float(ownertype), float(mileage), float(engine), float(power), float(seats)]])


redirectURL = "http://localhost/CarPricePredictionTemplate/final.py?data={:.2f}".format(abs(y_pred[0]))
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')