import pandas as pd

def main():
    sobj=pd.Series([27000,32000,35000],index=["Amit","Sagar","Sagar"])

    print(sobj)

    print(sobj["Amit"])


if __name__=="__main__":
    main()