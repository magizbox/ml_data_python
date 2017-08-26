#  Preperation

## Normalization

Example [^1]

```python
import numpy
from sklearn.preprocessing import normalize
matrix = numpy.arange(0,27,3).reshape(3,3).astype(numpy.float64)

# array([[  0.,   3.,   6.],
#   [  9.,  12.,  15.],
#   [ 18.,  21.,  24.]])

normed_matrix = normalize(matrix, axis=1, norm='l1')

# [[ 0.          0.33333333  0.66666667]
# [ 0.25        0.33333333  0.41666667]
# [ 0.28571429  0.33333333  0.38095238]]
```

## Label Encoder

Encode labels (categorical variables) with value between 0 and n_classes-1. [^2]

```python
import sklearn
le = sklearn.preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
# LabelEncoder()
list(le.classes_)
# ['amsterdam', 'paris', 'tokyo']
le.transform(["tokyo", "tokyo", "paris"])
# array([2, 2, 1]...)
list(le.inverse_transform([2, 2, 1]))
# ['tokyo', 'tokyo', 'paris']
```

[^1]: [How to normalize a 2-dimensional numpy array in python less verbose?](http://stackoverflow.com/questions/8904694/how-to-normalize-a-2-dimensional-numpy-array-in-python-less-verbose)
[^2]: [sklearn.preprocessing.LabelEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
