# https://scikit-learn.org/stable/tutorial/basic/tutorial.html

# %%
from sklearn import datasets, svm

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.0)

clf.fit(digits.data[:-1], digits.target[:-1]) # Train with the data except the last one

print(clf.predict(digits.data[-1:]))

#%% 
import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype="float32")
print(X.dtype)

#%% 
from sklearn import datasets, svm

iris = datasets.load_iris()
clf = svm.SVC()
clf.fit(iris.data, iris.target)

print(list(clf.predict(iris.data[:3])))

print(clf.fit(iris.data, iris.target_names[iris.target]))

print(list(clf.predict(iris.data[:3])))

# %%
import numpy as np
from sklearn import datasets, svm

X, y = datasets.load_iris(return_X_y=True)

clf = svm.SVC()

clf.set_params(kernel="linear").fit(X, y)
print(clf.predict(X[:5]))

clf.set_params(kernel="rbf").fit(X, y)
print(clf.predict(X[:5]))

# %%
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
print(classif.fit(X, y).predict(X))

# %%
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]
y = LabelBinarizer().fit_transform(y)

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
print(classif.fit(X, y).predict(X))

# %%
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
print(classif.fit(X, y).predict(X))
# %%
