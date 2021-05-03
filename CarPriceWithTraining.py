#!C:\Program Files\Python37\Python.exe
print("Content-type:text/html \n")


import cgi
import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv('Data_Train1.csv')
x = dataset.iloc[:,1:11].values
y = dataset.iloc[:,-1].values

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
 


from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
x[:,0]=lb.fit_transform(x[:,0])
x[:,3]=lb.fit_transform(x[:,3])
x[:,4]=lb.fit_transform(x[:,4])
x[:,5]=lb.fit_transform(x[:,5])


from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',strategy='mean',axis=0)
imputer = imputer.fit(x[:,])
x[:, ] = imputer.transform(x[:,])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state = 0)
#print(x_test[1])

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


with open('check.pkl', 'wb') as f:
    pickle.dump(regressor, f)




#predict the test set results
y_pred = regressor.predict([[float(city), float(year), float(km), float(fuel), float(transmission), float(ownertype), float(mileage), float(engine), float(power), float(seats)]])


redirectURL = "http://localhost/CarPricePredictionTemplate/final.py?data={:.2f}".format(y_pred[0])
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')