## Dataset

Sample datasets to learn and practice data analytics.

### anscombe

```
import seaborn as sns

anscombe = sns.load_dataset('anscombe')

anscombe.shape
# (44, 3)

anscombe.head()
#   dataset     x     y
# 0       I  10.0  8.04
# 1       I   8.0  6.95
# 2       I  13.0  7.58
# 3       I   9.0  8.81
# 4       I  11.0  8.33
```

### attention

```
import seaborn as sns

attention = sns.load_dataset('attention')

attention.shape
# (60, 5)

attention.head()
#    Unnamed: 0  subject attention  solutions  score
# 0           0        1   divided          1    2.0
# 1           1        2   divided          1    3.0
# 2           2        3   divided          1    3.0
# 3           3        4   divided          1    5.0
# 4           4        5   divided          1    4.0
```

### brain network

```
import seaborn as sns

brain = sns.load_dataset('brain_networks')

brain.shape
# (923, 63)

brain.head()
#   network                  1                1.1                   2  \
# 0    node                  1                  1                   1
# 1    hemi                 lh                 rh                  lh
# 2     NaN                NaN                NaN                 NaN
# 3       0  56.05574417114258  92.03103637695312   3.391575574874878
# 4       1   55.5472526550293   43.6900749206543  -65.49598693847656
# 
#                    2.1                   3                 3.1  \
# 0                    1                   1                   1
# 1                   rh                  lh                  rh
# 2                  NaN                 NaN                 NaN
# 3    38.65968322753906  26.203819274902344  -49.71556854248047
# 4  -13.974522590637207  -28.27496337890625  -39.05012893676758
# 
#                      4                  4.1                    5  \
# 0                    1                    1                    1
# 1                   lh                   rh                   lh
# 2                  NaN                  NaN                  NaN
# 3     47.4610366821289   26.746612548828125  -35.898860931396484
# 4  -1.2106596231460571  -19.012897491455078   19.568010330200195
# 
#           ...                         16.5                16.6  \
# 0         ...                            3                   4
# 1         ...                           rh                  lh
# 2         ...                          NaN                 NaN
# 3         ...           0.6079040169715881  -70.27054595947266
# 4         ...            57.49507141113281  -76.39321899414062
# 
#                  16.7                   17                17.1  \
# 0                   4                    1                   1
# 1                  rh                   lh                  rh
# 2                 NaN                  NaN                 NaN
# 3   77.36577606201172   -21.73455047607422  1.0282527208328247
# 4  127.26136016845705  -13.035799026489258    46.3818244934082
# 
#                   17.2               17.3                 17.4  \
# 0                    2                  2                    3
# 1                   lh                 rh                   lh
# 2                  NaN                NaN                  NaN
# 3   7.7917842864990225  68.90372467041016  -10.520872116088867
# 4  -15.752449989318848  31.00033187866211  -39.607521057128906
# 
#                  17.5                 17.6
# 0                   3                    4
# 1                  rh                   lh
# 2                 NaN                  NaN
# 3  120.49046325683594  -39.686431884765625
# 4   24.76401138305664    -36.7710075378418
#
# [5 rows x 63 columns]
```

### car crashes

```
import seaborn as sns

car = sns.load_dataset('car_crashes')

car.shape
# (51, 8)

car.head()
#    total  speeding  alcohol  not_distracted  no_previous  ins_premium  \
# 0   18.8     7.332    5.640          18.048       15.040       784.55
# 1   18.1     7.421    4.525          16.290       17.014      1053.48
# 2   18.6     6.510    5.208          15.624       17.856       899.47
# 3   22.4     4.032    5.824          21.056       21.280       827.34
# 4   12.0     4.200    3.360          10.920       10.680       878.41
# 
#    ins_losses abbrev
# 0      145.08     AL
# 1      133.93     AK
# 2      110.35     AZ
# 3      142.39     AR
# 4      165.63     CA
```

### exercise

```
import seaborn as sns

exercise = sns.load_dataset('exercise')

exercise.shape
# (90, 6)

exercise.head()
#    Unnamed: 0  id     diet  pulse    time  kind
# 0           0   1  low fat     85   1 min  rest
# 1           1   1  low fat     85  15 min  rest
# 2           2   1  low fat     88  30 min  rest
# 3           3   2  low fat     90   1 min  rest
# 4           4   2  low fat     92  15 min  rest
```

### flights

```
import seaborn as sns

flights = sns.load_dataset('flights')

flights.shape
# (144, 3)

flights.head()
#    year     month  passengers
# 0  1949   January         112
# 1  1949  February         118
# 2  1949     March         132
# 3  1949     April         129
# 4  1949       May         121
```

### gammas

```
import seaborn as sns

gammas = sns.load_dataset('gammas')

gammas.shape
# (6000, 4)

gammas.head()
#    timepoint  ROI  subject  BOLD signal
# 0        0.0  IPS        0     0.513433
# 1        0.0  IPS        1    -0.414368
# 2        0.0  IPS        2     0.214695
# 3        0.0  IPS        3     0.814809
# 4        0.0  IPS        4    -0.894992
```

### iris

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".

```
import seaborn as sns

iris = sns.load_dataset('iris')

iris.shape
# (150, 5)

iris.head()
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa
```

### plannets

Gives information on planets that astronomers have discovered around other stars (known as extrasolar planets or exoplanets for short)


```
import seaborn as sns

plannets = sns.load_dataset('planets')

plannets.shape
# (1035, 6)

plannets.head()
#             method  number  orbital_period   mass  distance  year
# 0  Radial Velocity       1         269.300   7.10     77.40  2006
# 1  Radial Velocity       1         874.774   2.21     56.95  2008
# 2  Radial Velocity       1         763.000   2.60     19.84  2011
# 3  Radial Velocity       1         326.030  19.40    110.62  2007
# 4  Radial Velocity       1         516.220  10.50    119.47  2009
```

### tips

```
import seaborn as sns

tips = sns.load_dataset('tips')

tips.shape
# (244, 7)

tips.head()
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4
```

### titanic

```
import seaborn as sns

titanic = sns.load_dataset('titanic')

titanic.shape
# (891, 15)

titanic.head()
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class  \
# 0         0       3    male  22.0      1      0   7.2500        S  Third
# 1         1       1  female  38.0      1      0  71.2833        C  First
# 2         1       3  female  26.0      0      0   7.9250        S  Third
# 3         1       1  female  35.0      1      0  53.1000        S  First
# 4         0       3    male  35.0      0      0   8.0500        S  Third
# 
#      who  adult_male deck  embark_town alive  alone
# 0    man        True  NaN  Southampton    no  False
# 1  woman       False    C    Cherbourg   yes  False
# 2  woman       False  NaN  Southampton   yes   True
# 3  woman       False    C  Southampton   yes  False
# 4    man        True  NaN  Southampton    no   True
```

## References

* [Iris flower data set. https://en.wikipedia.org/wiki/Iris_flower_data_set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
* [seaborn-data. https://github.com/mwaskom/seaborn-data](https://github.com/mwaskom/seaborn-data)