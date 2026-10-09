import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error,r2_score


#------------------------------------
#Step 1:-Load the Data
#------------------------------------

df=pd.read_csv("california_housing.csv")

print("Shape of Dataset :",df.shape)
print("First 5 Records",df.head())

#------------------------------------
#Step 2:-Separate Features and Lables
#------------------------------------

X=df.drop("target",axis=1)
Y=df["target"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

#----------------------------------------------
#Step 3:-Split Dataset For Training and Testing
#----------------------------------------------

X_train,X_test,Y_train,Y_test=train_test_split(
                                X,
                                Y,
                                test_size=0.2,
                                random_state=42
                                )

#------------------------------------
#Step 4:-Create the models
#------------------------------------

model=DecisionTreeRegressor(random_state=42)

#------------------------------------
#Step 5:-Train the model
#------------------------------------

model.fit(X_train,Y_train)

#------------------------------------
#Step 6:-Test the model
#------------------------------------

Y_pred=model.predict(X_test)

#----------------------------------------------
#Step 7:-Evaluate the Model
#----------------------------------------------

print("MSE :",mean_squared_error(Y_test,Y_pred))
print("R2 :",r2_score(Y_test,Y_pred))

#------------------------------------
#Step :-
#------------------------------------