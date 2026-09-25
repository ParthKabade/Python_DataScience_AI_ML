import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(Datapath):
#Step 1=Load the data
    df=pd.read_csv(Datapath)

    print(df.head())

def main():
    Border="*"*100
    print(Border)
    MarvellousRegression("Advertising.csv")
    print(Border)

if __name__=="__main__":
    main()