#Rough->1
#smooth->0

#Tennis->1
#Cricket->2
def main():
    print("Ball Classification Case Study")

    #Encoding

    Features=[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[96,0]]

    Labels=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    print(Features)
    print(Labels)
    
if __name__=="__main__":
    main()