import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

df=pd.read_csv("customer_churn.csv")

print("Customer Dataset :")
print(df)
print(df.shape)
print("-"*40)

X=df[["Age","Tenure","MonthlyCharges","SupportCalls"]]
Y=df[["Churn"]]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.2,random_state=42)

model=LogisticRegression(max_iter=1000)

model.fit(X_train,Y_train)

Y_pred=model.predict(X_test)

accuracy=accuracy_score(Y_test,Y_pred)

print("Accuracy is :",accuracy*100)

print("Confusion Matrix")
print((confusion_matrix(Y_test,Y_pred)))