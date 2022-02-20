from random import randrange

'''
probability function
    - creates a possible instance of an array of 3 numbers randomly selected from numbers: 1-5
    - input     // nothing
    - output    // an array of 3 numbers
'''

def prob_function():
    B = []
    for b in range(3):
        can_number = randrange(1,5)
        B.append(can_number)
    return B

if __name__ == "__main__":
    event = 0
    print("The numbers 1-5 are randomly generated and selected into an array of 3 elements."
          "\nWhat is the frequency that all of the elements in the array are different numbers?")
    trials = int(input("Enter number of trials: "))

    #comment outside loop

    for i in range(trials):
        i += 1
        test = prob_function()
        if ((test[0] != test[1]) and (test[0] != test[2]) and (test[1] != test[2])):
            event += 1

    answer = event/trials
    print(answer)
