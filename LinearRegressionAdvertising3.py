import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(Datapath):

    Border="-"*100

#Step 1=Load the data

    print("\nStep 1=Load the data\n")
    df=pd.read_csv(Datapath)

    print(df.head())

    print(Border)

#Step 2=Remove unwanted coloums

    print(Border)

    print("\nStep 2=Remove unwanted coloums\n")

    if "Unnamed: 0" in df.columns:
        df=df.drop(columns="Unnamed: 0")

        print(df.head())

    print(Border)

#Step 3=Check Missing Values

    print(Border)

    print("\nStep 3=Check Missing Values\n")

    print("Total Missing Values :")
    print(df.isnull().sum())

    print(Border)

#step 4=Stastical Summary

    print(Border)
    
    print("\nstep 4=Stastical Summary\n")

    print(df.describe())

    print(Border)



def main():
    Border="-"*100
    print(Border)
    MarvellousRegression("Advertising.csv")
    print(Border)

if __name__=="__main__":
    main()