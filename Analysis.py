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

colors = {"setosa": "purple", "versicolor": "yellow", "virginica": "red"} # my dictionary creating paired values # labelling difference here caused me errors. 

 # define variable as a list to include relevant data a from csv as a list
sepal_length = (iris_data["sepal_length"])
sepal_width = (iris_data["sepal_width"])
petal_length = (iris_data["petal_length"])
petal_width = (iris_data["petal_width"])
species = iris_data["species"]

#create scatter plots for each variable

# Sepal Length vs Sepal Width
"""""
plt.figure(figsize=(10, 8))
plt.scatter(sepal_length, sepal_width, c ="blue", #set variable(will call data from list) and color
            linewidths = 2, # size of edge of marker
            marker ="s", #square marker
            edgecolor ="green", # edge of marker color
            s = 25) # size of indicator
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width") 
plt.savefig("Sepal Length vs Sepal Width scatter.png") # saves as image to directory/git repo

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
plt.savefig("Petal Length vs Petal Width scatter.png") 

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
plt.savefig("Sepal Length vs Petal Length scatter.png")

# Sepal Width vs Petal Width

plt.figure(figsize=(10, 8))
plt.scatter(sepal_width, petal_width, c ="red", 
            linewidths = 2, # size of edge of marker
            marker ="4", # marker
            edgecolor ="pink", # edge of marker color
            s = 30) # size of indicator
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.title("Sepal Width vs Petal Width") 
plt.savefig("Sepal Width vs Petal Width scatter.png")
plt.show()

"""""

# 4. Performs any other analysis you think is appropriate. 
# Add code that details species type to compare each variable across the 3 classes of Iris -  need to group by species 


# Sepal Length vs Sepal Width

plt.figure(figsize=(8, 6))
for species_name, color in colors.items(): # boolean runs to create new variables (species_name, color) by pullinh the the 2 "items" in my color dictionary
    species_data = iris_data[iris_data["species"] == species_name] # as the loop runs the programme filters the iris data "species" column using to create 3 subsets of data.  Is True (==) expression runs to categorise the species under the "species name" umbrella fi the value is the same  -  thats long winded apologies. 
    plt.scatter(species_data["sepal_length"], species_data["sepal_width"], label=species_name, c=color)  #tuple used to store the 2 list virables, label and color identifier
    linewidths = 2, # size of edge of marker
    marker ="s", #square marker
    s = 25 # size of indicator

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width") 
plt.legend(colors)
plt.show()

# Petal Length vs Petal Width

plt.figure(figsize=(8, 6))
for species_name, color in colors.items(): # boolean runs to create new variables (species_name, color) by pullinh the the 2 "items" in my color dictionary
    species_data = iris_data[iris_data["species"] == species_name] 
    plt.scatter(species_data["petal_length"], species_data["petal_width"], label=species_name, c=color)  
    linewidths = 2, # size of edge of marker
    marker ="s", #square marker
    s = 25 # size of indicator

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Length vs Petal Width") 
plt.legend(colors)
plt.show()


# Sepal Length vs Petal Length

plt.figure(figsize=(8, 6))
for species_name, color in colors.items(): # boolean runs to create new variables (species_name, color) by pullinh the the 2 "items" in my color dictionary
    species_data = iris_data[iris_data["species"] == species_name] 
    plt.scatter(species_data["sepal_length"], species_data["petal_length"], label=species_name, c=color)  
    linewidths = 2, # size of edge of marker
    marker ="s", #square marker
    s = 25 # size of indicator

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length") 
plt.legend(colors)
plt.show()

# Sepal Width vs Petal Width

plt.figure(figsize=(8, 6))
for species_name, color in colors.items(): # boolean runs to create new variables (species_name, color) by pullinh the the 2 "items" in my color dictionary
    species_data = iris_data[iris_data["species"] == species_name] 
    plt.scatter(species_data["sepal_width"], species_data["petal_width"], label=species_name, c=color)  
    linewidths = 2, # size of edge of marker
    marker ="s", #square marker
    s = 25 # size of indicator

plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.title("Sepal Width vs Petal Width") 
plt.legend(colors)
plt.show()
