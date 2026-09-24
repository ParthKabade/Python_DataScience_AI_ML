import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Load the Data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of independent variables X :",X)
    print("Values of dependent variables Y :",Y)

    sum_x=0
    sum_y=0

    for i in range(len(X)):
        sum_x=sum_x+X[i]
        sum_y=sum_y+Y[i]

    mean_x=sum_x/len(X)
    mean_y=sum_y/len(Y)

    print("Mean_X is :",mean_x)
    print("Mean_Y is :",mean_y)

    n=len(X)

    numeerator=0
    denomeneter=0

    for i in range(n):
        numeerator=numeerator+((X[i]-mean_x)*(Y[i]-mean_y))
        denomeneter=denomeneter+((X[i]-mean_x)**2)

    m=numeerator/denomeneter

    print("Slope of line is :",m)

    c=mean_y-m*mean_x

    print("Y intercept is C :",c)

    x=np.linspace(1,6,n)
    y=c+m*x

    plt.plot(x,y,color='g',label="Regression line")
    plt.scatter(X,Y,color='r',label="Scatter plot")

    plt.xlabel("X :Independent Variables")
    plt.ylabel("Y :Independent Variables")

    plt.grid(True)

    plt.legend()
    plt.show()

def main():
    MarvellousPredictor()


if __name__=="__main__":
    main()