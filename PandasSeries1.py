import pandas as pd

def main():
    Data=[11,21,51,101]

    print(Data)

    sobj=pd.Series(Data)

    """
    इथे Pandas तुमच्या Python list ला Pandas Series object मध्ये convert करते.

    Series म्हणजे essentially:

    एक-dimensional labelled array

    म्हणजे data सोबत त्याचा index देखील असतो.
    """

    print(sobj)


if __name__=="__main__":
    main()