import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#---------------------------------------------------------------------------------------------------
#       
#       Function Name:      LoadData
#       Description:        Load the Data from csv
#       Input:              Name of csv File
#       Output:             Data Frame
#       Author:             Parth Nilesh Kabade
#       Date:               16/08/2026
#
#---------------------------------------------------------------------------------------------------

def LoadData(filename):
    df=pd.read_csv(filename)

    print("Dataset Loaded Successfully\n")
    print(df.head())

def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__=="__main__":
    main()
    