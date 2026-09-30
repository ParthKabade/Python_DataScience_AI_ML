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
#       Function Name:      SplitData
#       Description:        It performs Splitting activity
#       Input:              DataFrame
#       Output:             4 Subsets for Training and testing
#       Author:             Parth Nilesh Kabade
#       Date:               16/08/2026
#
#---------------------------------------------------------------------------------------------------

def SplitData(df):
    X=df.drop("Survived",axis=1)

    Y=df["Survived"]

    X_train,X_test,Y_train,Y_test=train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset Splitting completed Succesfully")

    return X_train, X_test, Y_train, Y_test

# Step 4 : Train the model

#---------------------------------------------------------------------------------------------------#   Function Name : TrainModel
#   Description :   It performs model training
#   Input :         Training fetures and labels
#   Output :        Trained model
#   Author :        Parth Nilesh Kabade
#   Date :          16/08/2026
#---------------------------------------------------------------------------------------------------

def TrainModel(X_train, Y_train):
    model=LogisticRegression(max_iter=1000)

    model=model.fit(X_train,Y_train)

    print("Model Trained Succesfully")

    return model

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

    #Step 3:Splits the Data
    X_train, X_test, Y_train, Y_test =SplitData(df)

    #Step 4:Train The Model
    model = TrainModel(X_train, Y_train)


if __name__=="__main__":
    main()
    