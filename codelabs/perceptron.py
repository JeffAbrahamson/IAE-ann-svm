# We start by importing two useful functions.
from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron

# Look at the documentation for load_digits and Perceptron.
# This snippet of code gives you the straight-line path
# to classifying digits, but you should learn what's to
# the side of the path.
#
# What do the arguments do?
# What other arguments are possible?
X, y = load_digits(return_X_y=True)
clf_1 = Perceptron(tol=1e-3)
clf_1.fit(X, y)

# What do these functions do?
clf_1.score(X, y)
clf_1.predict([X[2]])


# This is rubbish.  (Why?)
# Let's do better.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf_2 = Perceptron()
clf_2.fit(X_train, y_train)
clf_2.score(X_test, y_test)

# Question: what did we just do?

# Question: were we lucky (or unlucky)?
import numpy as np
num_tries = 20
scores = np.array(np.zeros(num_tries))
for n in range(num_tries):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    clf_2 = Perceptron()
    clf_2.fit(X_train, y_train)
    scores[n] = clf_2.score(X_test, y_test)
    print('{v:.3f}'.format(v=scores[n]))
print('mean={m:.3f}  std dev={sd:.3f}'.format(
    m=scores.mean(), sd=scores.std()))

# Let's look at the data.
import matplotlib.pyplot as plt
digits = load_digits()
plt.gray()
plt.matshow(digits.images[0])
plt.show()
print('That was a {c}'.format(c=digits.target[0]))

## Exercise: Show more images.

## Exercise:  Construct a training set to learn the logical function AND.
## Exercise:  Construct a training set to learn the logical function XOR.  (What happens?)
