# Transformation

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. [^1]

## Create data frame


```python
import pandas as pd
students = pd.DataFrame({
  'name' : ["Kate", "John", "Tom", "Mark"],
  'age' : [20, 21, 19, 18]})

#       age  name
#    0   20  Kate
#    1   21  John
#    2   19   Tom
#    3   18  Mark
```

## Load dataframe

```python
import pandas as pd
from sklearn import datasets
iris_data = datasets.load_iris()
iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris
```

## Selection

```python
students.iloc[1:3, :]
#       age  name
#    1   21  John
#    2   19   Tom
```

## Create new column

```python
students["birthyear"] = students.apply(lambda row: 2016 - row['age'], axis=1)
students["birthyear"] = 2016 - students["age"]

#       age  name  birthyear
#    0   20  Kate       1996
#    1   21  John       1995
#    2   19   Tom       1997
#    3   18  Mark       1998
```

## Delete column

```
students = students.drop('birthyear', 1)
```

* Wes McKinney, 10-minute tour of pandas: [video](https://vimeo.com/59324550), [notebook](nbviewer.ipython.org/urls/gist.github.com/wesm/4757075/raw/a72d3450ad4924d0e74fb57c9f62d1d895ea4574/PandasTour.ipynb)

[^1]: [DataFrame, Intro to Data Structures](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)