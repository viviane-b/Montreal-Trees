print("data")
import numpy as np 
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s[0])
print(s)

dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df.head)

arbres = pd.read_csv("C:\\_Code\\projects\\arbres\\arbres-publics.csv")
print(arbres.head)
print(arbres.loc[[0,1]])
print(arbres.info())

options = ["Côte-des-Neiges - Notre-Dame-de-Grâce"]
autour = arbres.loc[(arbres["Longitude"]>= -73.622) & (arbres["Longitude"]<= -73.621)  
                    & (arbres["Latitude"]>= 45.476) & (arbres["Latitude"]<= 45.477) ]

# print(arbres.loc[arbres["Rue"].str.contains("Girouard", na=False)])
pd.set_option('display.max_columns', None)
print(autour)




# to open/create a new html file in the write mode 
f = open('GFG.html', 'w') 
  
# the html code which will go in the file GFG.html 
html_template = """<html> 
<head> 
<title>Title</title> 
</head> 
<body> 
<h2>Welcome </h2> 
  
<iframe width="425" height="350" src="https://www.openstreetmap.org/export/embed.html?bbox=-73.62839698791505%2C45.47437416248056%2C-73.61459970474245%2C45.47927918127812&amp;layer=mapnik&amp;marker=45.47683421598429%2C-73.62149834632874" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/?mlat=45.47683&amp;mlon=-73.62150#map=17/45.47683/-73.62150">View Larger Map</a></small>

  
</body> 
</html> 
"""
# <p>Default code has been loaded into the Editor.""" + str(autour) + """</p> 
  
# writing the code into the file 
f.write(html_template) 
  
# close the file 
f.close() 

