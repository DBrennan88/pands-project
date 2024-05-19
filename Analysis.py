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
"""""
plt.figure(figsize=(8, 6)) # scale of graph
plt.hist(iris_data["sepal_length"], bins=30, color="blue", edgecolor="black") # define the variable, how its repesented (number of buckets/bins the data will be contained in) and the format
plt.title("Histogram of sepal_length") # title of chart
plt.xlabel("sepal_length") # ploting all data points for this variabe on my x axis
plt.ylabel("Frequency") # a count or number of data points defined on my y axis
plt.show() # show time
plt.savefig("sepal_length_histogram.png") # saves as image to directory/git repo

plt.figure(figsize=(8, 6))
plt.hist(iris_data["sepal_width"], bins=30, color="orange", edgecolor="black")
plt.title("Histogram of sepal_width")
plt.xlabel("sepal_width")
plt.ylabel("Frequency")
plt.savefig("sepal_width_histogram.png")

plt.figure(figsize=(8, 6))
plt.hist(iris_data["petal_length"], bins=30, color="pink", edgecolor="black")
plt.title("Histogram of petal_length")
plt.xlabel("petal_length")
plt.ylabel("Frequency")
plt.show()
plt.savefig("petal_length_histogram.png")

plt.figure(figsize=(8, 6))
plt.hist(iris_data["petal_width"], bins=30, color="green", edgecolor="black")
plt.title("Histogram of petal_width")
plt.xlabel("petal_width")
plt.ylabel("Frequency")
plt.show()
plt.savefig("petal_width_histogram.png")
"""""
# 3. Outputs a scatter plot of each pair of variables. 

 # define variable to include relevant data as a list
sepal_length = iris_data["sepal_length"]
sepal_width = iris_data["sepal_width"]
petal_length = iris_data["petal_length"]
petal_width = iris_data["petal_width"]

#create scatter plots 
plt.scatter(sepal_length, sepal_width, c ="green",  #
            linewidths = 2, 
            marker ="s", #square marker
            edgecolor ="green", 
            s = 200)
 
plt.scatter(petal_length, petal_width, c ="yellow",
            linewidths = 2,
            marker ="^", #triange marker
            edgecolor ="red", 
            s = 100)
 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# 4. Performs any other analysis you think is appropriate.