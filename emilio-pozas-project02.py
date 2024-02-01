
mydata = [('Emily', 19, 'Biomedical Engineering'), ('Brandon', 20, 'Accounting'), ('Jackson', 20, 'Biology'), ('Sophia', 21, 'Finance'), ('Liam', 22, 'Nursing')]
import pandas as pd
studentDF = pd.DataFrame(mydata)
print(studentDF.iloc[2])
studentDF

myDF = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")
myDF.head()
myDF.tail()

myDF.shape
myDF.info()

len(myDF[myDF['price'] > 6000])
myDF['state'].unique()
myDF[myDF['state'] == 'in'].size
myDF[myDF['state'] == 'tx'].size
myDF['region'].unique()
len(myDF['region'].unique())

subDF = myDF[myDF['price'] < 6000]
vehicleByStateDF = subDF.groupby('state').size()
import matplotlib.pyplot as plt
vehicleByStateDF.plot (kind = 'bar' , figsize =(20,9))
plt.title("Number of Vehicles in Each State")
plt.xlabel("States")
plt.ylabel("# of vehicles")
plt.show()