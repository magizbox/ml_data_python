# Transformation

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. [^1]

## Create data frame

Create new data frame from lists

```python
import pandas as pd
students = pd.DataFrame({
  'name' : ["Kate", "John", "Tom", "Mark"],
  'age' : [20, 21, 19, 18]
})
#       age  name
#    0   20  Kate
#    1   21  John
#    2   19   Tom
#    3   18  Mark
```

## Load dataframe

Load dataframe from datasets
```python
import pandas as pd
from sklearn import datasets
iris_data = datasets.load_iris()
iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris
```

## Selection

Select by column index

```python
students.iloc[1:3, :]
#       age  name
#    1   21  John
#    2   19   Tom
```

## Filter

```python
students = pd.DataFrame({
  'math' : [90, 80, 95, 50],
  'physic' : [20, 50, 95, 60]
})
#    math  physic
# 0    90      20
# 1    80      50
# 2    95      95
# 3    50      60
```

```python
students[students['math'] > 85]
#    math  physic
# 0    90      20
# 2    95      95

students[students['math'] == students['physic']]
#    math  physic
# 2    95      95
```


## Create new column

```python
students = pd.DataFrame({
  'name' : ["Kate", "John", "Tom", "Mark"],
  'age' : [20, 21, 19, 18]
})
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
students = pd.DataFrame({
  'name' : ["Kate", "John", "Tom", "Mark"],
  'age' : [20, 21, 19, 18]
})
students = students.drop('age', 1)
```

* Wes McKinney, 10-minute tour of pandas: [video](https://vimeo.com/59324550), [notebook](nbviewer.ipython.org/urls/gist.github.com/wesm/4757075/raw/a72d3450ad4924d0e74fb57c9f62d1d895ea4574/PandasTour.ipynb)

[^1]: [DataFrame, Intro to Data Structures](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)