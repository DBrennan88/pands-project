#pands project
#Programme - Analysis of Iris data set. 
#Author Darragh Brennan

import pandas as pd # needed to read in csv data
import matplotlib.pyplot as plt # needed to created and plot data on charts. 

iris_data = pd.read_csv("https://github.com/DBrennan88/pands-project/raw/main/iris.csv") # Load the Iris data from the GitHub link

 # print(iris_data.head()) # Display the first 5 rows~ confirmed data is being pulled into programme

# 1. Outputs a summary of each variable to a single text file, 
with open("iris_data_summary.txt", 'w') as file: # opens file in write mode
   file.write(iris_data.describe().to_string())

# 2. Saves a histogram of each variable to png files

# 3. Outputs a scatter plot of each pair of variables. 
# 4. Performs any other analysis you think is appropriate.