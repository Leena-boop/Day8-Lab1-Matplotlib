


import matplotlib.pyplot as plt 
import numpy as np
import pandas as pnd
#Q1: Create two charts using list and dataframe

plt.plot([1,2,3]); 
#plt.plot(DataFrame = (1,2,3))
plt.figure(figsize= ( 20 ,10))
plt.subplot(1,3,1)
#Q2: Create pie chart with equal explode values
pie_chart = np.arange(0,4)
plt.pie(pie_chart , labels= ['Summer' , 'Winter' , 'Spring' , 'Autumn' ] , explode= [0 , 0 , 0 , 0]) ; 

#Q3: Create a scatter chart with circle marker, alpha = 0.4, and size = 50.
plt.subplot(1,3,2)
Y_axis_Scatter = np.random.randn(20)
X_axis_Sactter = np.random.randn(20)
plt.scatter(Y_axis_Scatter,X_axis_Sactter ,marker = 'o' ,alpha= 0.4 , s=50) 

#Q4: Add the following to your chart:
#title placed in the left and has a red color
#x and y label with font size = 16
plt.title('Sales' , fontsize = 16 , loc = 'left' , color = 'r')
plt.xlabel('sales')
plt.ylabel('months')

#Q5: Create three line charts with Legends at left and colors
plt.subplot(1,3,3)
plt.plot([1,2,3] , color = 'm') #color for deciding the color  of the line 
plt.plot([4,5,6] , color = "b")
plt.plot([7,8,9] , color = "g" )
plt.legend(['2009' , '2008'])

#Q6: Create subplots with three charts and figsize=20,10
# i did it with the three above 