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
    print(f"Output Coloumn :class")
    print(border)

    #step4 :Splict the dataset for Training and testing
    print(border)
    print("step4 :Splict the dataset for Training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Details of training and testing data")
    print(f"Shape of X_train :{X_train.shape}")
    print(f"Shape of X_test :{X_test.shape}")

    print(f"Shape of Y_train :{Y_train.shape}")
    print(f"Shape of Y_test :{Y_test.shape}")
    print(border)

    #step 5 : feature scaling
    print(border)
    print("step4 :Splict the dataset for Training and testing")
    print(border)

    scaler = StandardScaler()
    X_train_scaler = scaler.fit_transform(X_train)
    X_test_scaler = scaler.fit_transform(X_test)

    print("Feature Scaling Done ")

    #step 6 : HyperParameter Tunining 
    accuracy_score = []

    K_values = range(1,21)

    for k in K_values:
        model =  KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaler , Y_train)
        Y_pred = model.predict(X_train_scaler)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_score.append(accuracy)

    print("Accuracy report :")
    for no in accuracy_score:
        print(no)

    print(border)

    

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()