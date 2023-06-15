# sololearn-Data-Science
This repository contains projects contributing towards the earning of the Data Science certificate from sololearn.

## Project 1: Average of Rows

In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

**Task**

Given a 2D array, return the rowmeans.

**Input Format**

First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)

Next n lines: values of the row in X

**Output Format**

An numpy 1d array of values rounded to the second decimal.

2 2

1.5 1

2 2.9

**Sample Output**

[1.25 2.45]


## Project 2: Reshape

**Task**

Given a list of numbers and the number of rows (r), reshape the list into a 2-dimensional array. Note that r divides the length of the list evenly.

**Input Format**

First line: an integer (r) indicating the number of rows of the 2-dimensional array

Next line: numbers separated by the space

**Output Format**

An numpy 2d array of values rounded to the second decimal.

**Sample Input**

2

1.2 0 0.5 -1

**Sample Output**

[[ 1.2 0. ]

[ 0.5 -1. ]]

## Project 3: Missing Numbers

Imputing missing values.

In the real world, you will often need to handle missing values. One way to impute (i.e., fill) the numerical column is to replace the null values with its mean.

**Task**

Given a list of numbers including some missing values, turn it into a pandas series, impute the missing values with the mean, and finally return the series.

**Input Format**

A list of numbers including one or more string "nan" to indicate a missing value.

**Output Format**

A list of imputed values where all values are rounded to its first decimal place.

**Sample Input**

3 4 5 3 4 4 nan

**Sample Output**

0 3.0

1 4.0

2 5.0

3 3.0

4 4.0

5 4.0

6 3.8

## Project 4: Ordinary Squares

Ordinary least squares for linear regression.

Ordinary least squares (OLS) is a method to estimate the parameters β in a simple linear regression, Xβ = y, where X is the feature matrix and y is the dependent variable (or target), by minimizing the sum of the squares of the differences between the observed dependent variable in the given dataset and those predicted by the linear function. Mathematically, the solution is given by the formula in the image, where the superscript T means the transpose of a matrix, and the superscript -1 means it is an inverse of a matrix.

![Ordinary Squares.](https://api.sololearn.com/DownloadFile?id=4874)

**Task**

Given a 2D array feature matrix X and a vector y, return the coefficient vector; see the formula above.

**Input Format**

First line: two integers separated by spaces, the first indicates the rows of the feature matrix X (n) and the second indicates the columns of X (p)

Next n lines: values of the row in the feature matrix

Last line: p values of target y

**Output Format**

An numpy 1d array of values rounded to the second decimal.

**Sample Input**

2 2

1 0

0 2

2 3

**Sample Output**

[2. , 1.5]
