import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

Border="-"*30

"""
code मध्ये Step 1 = Dataset Load आणि Step 2 = EDA (Exploratory Data Analysis) आहे.

EDA म्हणजे:
Dataset ला model train करण्यापूर्वी त्याला समजून घेणे आणि त्यात काही problem आहे का ते तपासणे.
"""
#######################################################################################################
#step1:Load the data set
#######################################################################################################

print(Border)
print("step 1: Load the Database")
print(Border)

DataPath="iris.csv"

df=pd.read_csv(DataPath)


"""
df=pd.read_csv(DataPath)    इथे df हा एक DataFrame object आहे.
                            DataFrame म्हणजे basically Python मधील table

                            Python process च्या memory मध्ये DataFrame object तयार होतो.
                            आणि df हा variable त्या object कडे reference ठेवतो.
"""

print("DataBase Loaded Succesfully")

print("Inital entries from dataset are :")

print(df.head())

"""
head() default ने पहिल्या 5 rows दाखवतो.

Full DataFrame
      ↓
पहिल्या 5 rows select
      ↓
नवीन छोटा DataFrame representation
      ↓
print()
      ↓
Screen
"""
#######################################################################################################
#step2:Data Analysis (EDA)
#######################################################################################################


"""
Dataset मध्ये काय आहे? किती data आहे? कोणते columns आहेत? Missing data आहे का?
Classes किती आहेत? Data ची statistics काय आहे
"""


print(Border)
print("step 2:Data Analysis (EDA)")
print(Border)

print("\n\nShape of Dataset:",df.shape)# df.shape हा function नाही.

print("\n\nColum names:",list(df.columns))# df.columns dataset मधील सर्व column names देतो.
#df.columns हा function नाही.

"""
आपण तपासत आहोत:
कोणत्या column मध्ये किती values missing आहेत?
"""

print("\n\nMissing Values per Column :")
print(df.isnull().sum())


print("\n\nClass Distribution (species count) :")
print(df["species"].value_counts())

print("\n\nClass Report of dataset :")
print(df.describe())#हा command dataset ची statistical summary देतो.

#######################################################################################################
#step3:Decide Independent and dependent variable
#######################################################################################################


print(Border)
print("step 3: Decide Independent and dependent variable")
print(Border)

#X:Independent Variable /Features
#y:Dependent Variable/ Labels

feture_cols =[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
             ]

X=df[feture_cols]
Y=df["species"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

#######################################################################################################
#step 4:Visualisation of Dataset
#######################################################################################################


print(Border)
print("step 4:Visualisation of Dataset")
print(Border)

#Scatter plot
plt.figure(figsize=(7,5))#इथे नवीन graph/figure तयार केली जाते.

for sp in df["species"].unique():#म्हणजे duplicate values काढून फक्त unique values.
    temp=df[df["species"]==sp]   #सध्या आपण ज्या species वर काम करत आहोत, त्या species च्या सर्व rows वेगळ्या काढ.
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp)#ही line actual points graph वर plot करते.

plt.title("Marvellous Iris Case Study")#Graph ला title देतो.

plt.xlabel("petal length (cm)")#X-axis चं नाव:
plt.ylabel("petal width (cm)")#Y-axis चं नाव:

plt.legend()#Legend म्हणजे graph वर कोणते points कोणत्या species चे आहेत ते दाखवणारा box.
plt.grid()#Graph वर grid lines दाखवतो.
plt.show()#तयार झालेला graph user ला दाखवतो.

#######################################################################################################
#step 5:spilt the dataset for traning and testing
#######################################################################################################

print(Border)
print("step 5:spilt the dataset for traning and testing")
print(Border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset spliting activity done")

print("X:",X.shape)     #(150,4)
print("Y:",Y.shape)     #(150,)

print("X_train:",X_train.shape)     #(75,4)
print("X_test:",X_test.shape)     #(75,4)

print("Y_train:",Y_train.shape)     #(75,)
print("Y_test:",Y_test.shape)     #(75,)