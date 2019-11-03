import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

# This line takes a few seconds (or more, depending on your internet
# connection).
mnist = fetch_openml('mnist_784', version=1)

# Let's save it so we needn't re-fetch it.
with open('mnist_784', 'wb') as fp:
    pickle.dump(mnist, fp)

# Later we can re-load it:
with open('mnist_784', 'rb') as fp:
    mnist_2 = pickle.load(fp)

# It comes with a description.
print(mnist.DESCR)

# Normalise data from [0, 255] to [0, 1].
normalised_data = mnist.data / 255.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(normalised_data, mnist.target, test_size=0.3)

mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=20, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=500, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)
mlp.fit(X_train, y_train)
print('Training set score: {s:.2f}'.format(s=mlp.score(X_train, y_train)))
print('Test set score: {s:.2f}'.format(s=mlp.score(X_test, y_test)))

fig, axes = plt.subplots(4, 4)
# use global min / max to ensure all weights are shown on the same scale
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin,
               vmax=.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()

