import pandas as pd

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