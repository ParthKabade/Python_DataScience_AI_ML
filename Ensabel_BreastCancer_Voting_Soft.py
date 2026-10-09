import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

#-------------------------
#Step 1:-Load the Dataset
#-------------------------
df=pd.read_csv("breast_cancer.csv")

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

#----------------------------------------------
#Step 4:-Scale the Features
#----------------------------------------------

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_test=scaler.fit_transform(X_test)

#----------------------------------------------
#Step 5.1:-Create Individual models
#----------------------------------------------

model_log=LogisticRegression(max_iter=1000)

model_det=DecisionTreeClassifier(random_state=42)

model_knn=KNeighborsClassifier(n_neighbors=5)

#----------------------------------------------
#Step 5.2:-Create Voiting models
#----------------------------------------------

model=VotingClassifier(estimators=[('logistic',model_log),('decision_tree',model_det),('knn',model_knn)],voting="soft")

#----------------------------------------------
#Step 6:-Train the model
#----------------------------------------------

model=model.fit(X_train,Y_train)

#----------------------------------------------
#Step 7:-Test the Model
#----------------------------------------------

Y_pred=model.predict(X_test)

#----------------------------------------------
#Step 8:-Evaluate the Model
#----------------------------------------------

print("Accuracy :",accuracy_score(Y_pred,Y_test)*100)

print("Confusion Matrix :\n",confusion_matrix(Y_pred,Y_test))



