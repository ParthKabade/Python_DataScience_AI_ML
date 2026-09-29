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

    return df

#---------------------------------------------------------------------------------------------------
#       
#       Function Name:      PreprocessData
#       Description:        it performs data analysics
#       Input:              DataFrame
#       Output:             Updated DataFrame
#       Author:             Parth Nilesh Kabade
#       Date:               16/08/2026
#
#---------------------------------------------------------------------------------------------------

def PreprocessData(df):
    df=df.drop([
            "Passengerid",
            "zero",
            "name"
        ],
        errors="ignore")

    #Handel Missing Values
    df["Age"]=df["Age"].fillna(df["Age"].median())
    df["Fare"]=df["Fare"].fillna(df["Fare"].median())
    df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert categorical to numeric Data
    df=pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )


    print(df.head())

    print("Data Preprocessing Completed")

    return df

#---------------------------------------------------------------------------------------------------
#       
#       Function Name:      main
#       Description:        entry point function
#       Input:              Function calls
#       Output:             None
#       Author:             Parth Nilesh Kabade
#       Date:               16/08/2026
#
#---------------------------------------------------------------------------------------------------

def main():
    #STEP 1:Load Data
    df=LoadData("MarvellousTitanicDataset.csv")

    #STEP 2:PreProcess Data
    df=PreprocessData(df)

if __name__=="__main__":
    main()
    