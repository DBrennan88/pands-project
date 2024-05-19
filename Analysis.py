#pands project
#Programme - Analysis of Iris data set. 
#Author Darragh Brennan

import pandas as pd # needed to read in csv data
import matplotlib.pyplot as plt # needed to created and plot data on charts. 

iris_data = pd.read_csv("https://github.com/DBrennan88/pands-project/raw/main/iris.csv") # Load the Iris data from the GitHub link

 # print(iris_data.head()) # Display the first 5 rows~ confirmed data is being pulled into programme
"""""
# 1. Outputs a summary of each variable to a single text file, 
with open("iris_data_summary.txt", 'w') as file: # opens file in write mode
   file.write(iris_data.describe().to_string())


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

 # define variable as a list to include relevant data a from csv as a list
sepal_length = (iris_data["sepal_length"])
sepal_width = (iris_data["sepal_width"])
petal_length = (iris_data["petal_length"])
petal_width = (iris_data["petal_width"])

species = iris_data["species"]
colors = {"iris-setosa": "purple", "Iris-versicolor": "yellow", "Iris-virginica": "red"} # my dictionary creating paired values

#create scatter plots for each variable

# Sepal Length vs Sepal Width

plt.figure(figsize=(10, 8))
plt.scatter(sepal_length, sepal_width, c ="blue", #set variable(will call data from list) and color
            linewidths = 2, # size of edge of marker
            marker ="s", #square marker
            edgecolor ="green", # edge of marker color
            s = 25) # size of indicator
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width") 


# Petal Length vs Petal Width
plt.figure(figsize=(10, 8))
plt.scatter(petal_length, petal_width, c ="orange", 
            linewidths = 2, 
            marker ="D", # marker
            edgecolor ="black", 
            s = 50)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Length vs Petal Width") 


# Sepal Length vs Petal Length
plt.figure(figsize=(10, 8))
plt.scatter(sepal_length, petal_length, c ="black", 
            linewidths = 2, # size of edge of marker
            marker ="8", # marker
            edgecolor ="green", # edge of marker color
            s = 25) # size of indicator
plt.xlabel("Septal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length") 


# Sepal Width vs Petal Width
plt.figure(figsize=(10, 8))
plt.scatter(sepal_width, petal_width, c ="pink", 
            linewidths = 2, # size of edge of marker
            marker ="4", # marker
            edgecolor ="red", # edge of marker color
            s = 25) # size of indicator
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.title("Sepal Width vs Petal Width") 

plt.show()



# 4. Performs any other analysis you think is appropriate.