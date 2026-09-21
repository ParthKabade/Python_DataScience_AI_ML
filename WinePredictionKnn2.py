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
    """
    inplace=True म्हणजे:

    Original df DataFrame मध्येच बदल करा.
    """

    print(f"shape of dataset :{df.shape}")
    print(f"Total records :{df.shape[0]}")
    print(f"Total Coloumns :{df.shape[1]}")

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()