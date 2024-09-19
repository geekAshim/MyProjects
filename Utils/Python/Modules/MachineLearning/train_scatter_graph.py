# ref : https://www.w3schools.com/python/python_ml_train_test.asp

import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# train model
myline = numpy.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# test model ,
# a score of .8 means we are confident that the model is traained properly and can be used for prediction
r2 = r2_score(test_y, mymodel(test_x))

print(r2)

#prediction
print(mymodel(5))