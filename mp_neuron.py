def mp_neuron(inputs:int,weights:int,threshold:int):
    s=0
    for w,x in zip(weights,inputs):
        s += w*x 
    
    if s >= threshold:
        return 1
    else:
        return 0

def main():
    print("enter the choice of logic gate")
    choice=int(input("\n1)AND\n 2)OR\n 3)NOT\n 4)NAND\n 5)NOR\n"))
    print("===============================================================")
    if(choice==3):
        X1=int(input("enter a binary input X =>"))
        inputs=[X1]
        print("=============================================================")
    else:
        print("Enter binary operands X1 and X2\n")
        while(True):
            X1=int(input("enter operand X1 => \n"))
            X2=int(input("enter operand X2 => \n"))
            inputs=[X1,X2]
            print("=================================================================")
            if((X1==1 or X1==0) and (X2==1 or X2==0)):
                break
            else: 
                print("invalid input please enter again")
                continue
    
    match choice:
        case 1:
            weights=[1,1]
            threshold = 1
        case 2:
            threshold = 1
            weights=[1,1]
        case 3:
            thrshold = 0
            weights=[-1]
        case 4:
            threshold = -1
            weights=[-1,-1]
        case 5:
            threshold = 0
            weights=[-1,-1]

    output = mp_neuron(inputs,weights,threshold)
    print(f"output according to mp neuron machine is {output}")
    print("=======================================================")


main()


