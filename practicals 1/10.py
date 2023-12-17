from matplotlib import pyplot as pl
import numpy as np 

Population = ["Indians", "Australians", "Japanese", "Russian","Wagandians","Niggas","Bengalis"]
Rate = [5454,885,545,2459,5324,352,3548]

graph = pl.figure(figsize = (20,10))
pl.bar(Population,Rate,color = "#cc0000",width = 0.5)

pl.xlabel("Countries")
pl.ylabel("Rate")
pl.title("Rate of Population")

pl.show()