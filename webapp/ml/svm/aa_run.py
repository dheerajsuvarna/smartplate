print("Hello world")

#import tensorflow as tf
#x = tf.placeholder(tf.float32, [None, 2]) # We will have 2 neurons input variables x1 and x2. None, because we dont know the lenght of each input.
#y = tf.placeholder(tf.float32, [None, 1]) # We will have only one neuron output.

import numpy as np
from sklearn import svm

#Two classes and two
#X = [[0, 0], [1, 1]]
#y = [0, 1]

#Setup the model parameters. In this case default.
#clf = svm.SVC()

#Train the model
#clf.fit(X, y)

#Now test and predict the class
#print(clf.predict([[2., 2.]]))

########
#Two classes and two
X = [[1,2,3,4,5,4,3,2,1,0], [1,4,9,16,25,36,49,64,81,10]]
y = [0, 1]

#Setup the model parameters. In this case default.
clf = svm.SVC()

#Train the model
clf.fit(X, y)

#Now test and predict the class
print(clf.predict([[4,2,3,4,20,4,30,40,30,10]]))

'''
One vs All
'''
#Two classes and two
X = [[1,2,3,4,5,4,3,2,1,0], [1,4,9,16,25,36,49,64,81,100], [1,1,1,1,1,1,1,1,1,1]]
y = [0, 1, 2]

#Setup the model parameters. In this case default.
clf = svm.SVC()

#Train the model
clf.fit(X, y)

#Now test and predict the class
print(clf.predict([[4,2,3,4,20,4,30,40,30,10]]))
print(clf.predict([[1,1,2,1,1,10,1,70,90,100]]))



####Example with amplitude+frequency shifted

#Two classes and two
X = [[1,2,3,4,5,1,2,3,4,5], [1,4,9,16,25,1,2,3,4,5], [1,2,3,4,5,3,4,5,6,7]]
y = [0, 1, 2]

#Setup the model parameters. In this case default.
clf = svm.SVC()

#Train the model
clf.fit(X, y)

#Now test and predict the class
print('amplitude freq',clf.predict([[1,1,2,5,5,3,4,5,6,7]]))#Yes it identifies the shifted class easily
print('amplitude freq',clf.predict([[1,4,9,16,25,3,4,5,6,7]]))



'''
dict = {
    "apple": {
        "cals":100,
        "proteins": 30,
        "fats":10,
        "carbohydrates":10
        "healthy": true
    }
}

apple
100gr


proteins:dict["apple"]["proteins"]*weight
cals:
json =

'''


