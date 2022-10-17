# -*- coding: utf-8 -*-
"""Copy of Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Mt_mQfbFwLu617xuVSvQrcCMvY11ne4

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

s = "Hi ther Sam!"
a = s.split()
print(a)

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers".format(planet,diameter))

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d = {'k1':[1,2,3,{'tricky':['óh','man','inception',{'target':[1,2,3,'hello']}]}]}
  print(d['k1'][3]['tricky'][3]['target'][3])

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)



"""## 5. Create an array of all the even integers from 20 to 35"""

import numpy as np
array=np.arange(20,36,2)
print("Array of all even integers from 20 to 35:")
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

import numpy as np
x = np.arange(0,9).reshape(3,3)
print(x)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
np.concatenate((a,b))

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

import pandas as pd
data = [10,20,30]
df=pd.DataFrame(data,columns=['Numbers'])
df

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

import pandas as pd
per1=pd.date_range(start='1-1-2023',end = '10-2-2023',freq='24H')
for val in per1:
  print(val)

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

import pandas as pd
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df = pd.DataFrame(lists,columns=['s.no','name','val'])
print(df)