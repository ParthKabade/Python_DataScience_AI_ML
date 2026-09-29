
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

#step 5= Correlation

    print(Border)

    print("\nstep 5= Correlation\n")

    print(df.corr())

    print(Border)

#step 6=Seprate Independent and dependent variables

    print(Border)

    print("\nstep 6=Seprate Independent and dependent variables\n")

    X=df[[
        "TV",
        "radio",
        "newspaper"
    ]]

    Y=df["sales"]

    print("\nIndependent Variables :\n")
    print(X.head())
    print("\ndependent Variables :\n")
    print(Y.head())

    print(Border)

#step 7=split the dataset

    print(Border)

    print("\nstep 7=split the dataset\n")

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Training Data :\n")
    print(X_train.shape)

    print("\nTesting Data :\n")
    print(X_test.shape)

    print(Border)

#Step 8=Create & train the model
    print(Border)

    print("\nStep 8=Create & train the model\n")

    model=LinearRegression()

    model=model.fit(X_train,Y_train)

    print("Model trained succesfully...")

    print(Border)

#Step 9=Test the Model
    print(Border)

    print("\nStep 9=Test the Model\n")

    Y_pred=model.predict(X_test)

    print("\nExpected Answer :\n")
    print(Y_test[:3])

    print("\nPredicted Answer :\n")
    print(Y_pred[:3])

    print(Border)

#Step 10=Evaluate the Model
    print(Border)

    print("\nStep 10=Evaluate the Model\n")

    MSE=mean_squared_error(Y_test,Y_pred)

    RMSE=np.sqrt(MSE)

    R2=r2_score(Y_test,Y_pred)

    print("\nMSE :",MSE)
    print("\nRMSE :",RMSE)
    print("\nR2 :",R2)

    print(Border)

#Step 11=Display Coefficient
    print(Border)

    print("\nStep 11=Display Coefficient\n")

    print("\nTV Coefficient :",model.coef_[0])
    print("\nRadio Coefficient :",model.coef_[1])
    print("\nNewspaper Coefficient :",model.coef_[2])

    print("\nIntercept :",model.intercept_)

    print(Border)


def main():
    Border="-"*100
    print(Border)
    MarvellousRegression("Advertising.csv")
    print(Border)

if __name__=="__main__":
    main()