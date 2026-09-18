import matplotlib.pyplot as plt

def main():
    language=["C","c++","java","python"]
    students=[30,40,35,55]

    plt.bar(
        language,       #values of x axis
        students,       #values of y axis
        width=0.6,      #width of bar
        edgecolor=['black'], #border color of bars
        linewidth=1,     #width of bar border
        alpha=0.8,      #transperance 0.0 to 1.0
        label="students" # legend text
    )

    plt.title("Marvellous title plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.grid(False)

    plt.legend()

    plt.show()

if __name__=="__main__":
    main()