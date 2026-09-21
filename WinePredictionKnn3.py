import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border="-"*85

    #Step 1: Load the Dataset from the csv
    print(border)
    print("Step 1: Load the Dataset from the csv")
    print(border)

    df=pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

    #Step 2: Clean the Dataset
    print(border)
    print("Step 2: Clean the Dataset")
    print(border)

    df.dropna(inplace=True)

    print(f"shape of dataset :{df.shape}")
    print(f"Total records :{df.shape[0]}")
    print(f"Total Coloumns :{df.shape[1]}")

    print(border)

    #step3 :seprate dependent and independent variables
    print(border)
    print("step3 :seprate dependent and independent variables")
    print(border)

    X=df.drop(columns=['Class'])
    Y=df['Class']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    print(border)
    print(f"Input coloumns :{X.columns.to_list()}")
    print("Output column : Class")
    print(border)

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()