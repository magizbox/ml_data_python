# Data IO

This post shows how to import data to Python from numerous resources [^1] [^2] [^3]

## CSV

Read a csv file from local or from a server

```python
import numpy as np
import pandas as pd
# read data
df = pd.read_csv("data.csv", header = 0)
# write data
df.to_csv("data.csv", header=1, index=False)
```

## Excel

```python
import pandas as pd
# read data
df = pd.read_excel("data.xls")
# write data
df = pd.to_excel("data.xls", index=False)
```

## Sqlite

```python
import sqlite3

DB_NAME = "db.sqlite3"
SELECT_QUERY = "SELECT page_id, type FROM service_page"
# connect to sqlite3
db_connector = sqlite3.connect(DB_NAME)
# excute query
cursor = db_connector.execute(SELECT_QUERY)
# return dataset
data_set = cursor.fetchall()
```

[^1]: [pandas.read_excel](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html)
[^2]: [pandas.read_sqlite](http://www.datacarpentry.org/python-ecology/08-working-with-sql)
[^3]: [sqlite3.read_sqlite](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
