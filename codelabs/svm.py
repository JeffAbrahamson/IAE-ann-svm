########################
# Simple classification

from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf_1 = svm.SVC(gamma='scale')
clf_1.fit(X, y)
clf_1.predict([[2., 2.]])

# get support vectors
clf_1.support_vectors_

# get indices of support vectors
clf_1.support_

# get number of support vectors for each class
clf_1.n_support_

##############################
# Multi-class classification

X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf_2 = svm.SVC(gamma='scale', decision_function_shape='ovo')
clf_2.fit(X, Y) 

dec = clf_2.decision_function([[1]])
dec.shape[1]                    # 4 classes: 4*3/2 = 6

clf_2.decision_function_shape = "ovr"
dec = clf_2.decision_function([[1]])
dec.shape[1]                    # 4 classes

clf_2_ovr = svm.SVC(gamma='scale', decision_function_shape='ovr')
clf_2_ovr.fit()
for i in range(4): 
    print(clf_2_ovr.decision_function([[i]]))
