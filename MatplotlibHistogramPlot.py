
import matplotlib.pyplot as plt

def main():
    marks=[45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]

    plt.hist(
        marks,       #values of y axis
        bins=5,     #number of groups
        edgecolor='black',      #border colour 
        alpha=1.0,          #transperncy
        rwidth=0.9      #relative width of bars
    )

    plt.title("Marvellous Histogram plot")
    plt.xlabel("Student Hours")
    plt.ylabel("Marks")

    plt.grid(False)

    plt.legend()

    plt.show()

if __name__=="__main__":
    main()