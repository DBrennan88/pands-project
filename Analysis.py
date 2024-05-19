#pands project
#Programme - Analysis of Iris data set. 
#Author Darragh Brennan

import pip

import pandas as pd #  function needed to read in data from csv file
iris_data = pd.read_csv("https://github.com/DBrennan88/pands-project/blob/main/iris.csv") # Load the Iris data from my git hub link
for row in data[:5]: # Display initial rows
     print (row)
