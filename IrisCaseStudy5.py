from sklearn.datasets import load_iris
def main():
    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    Dataset=load_iris()

    print(Dataset.feature_names)
    for i in range(len(Dataset.target)):
        print(f"ID {i},Features {Dataset.data[i]},Label {Dataset.target[i]}")
    #print(Dataset.data[0])
    #print(Dataset.target[103])


if __name__=="__main__":
    main()