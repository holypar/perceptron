#Parminder Singh
#Perceptron

#main driver function, inputs:threshold, adjustment, weights list, examples list, and passes wanted
#returns nothing but prints out statements needed for the homework.
def perceptron(threshold, adjustment, weights, examples, totalPasses):
    print("Starting weights:", weights)
    print("Threshold:",threshold, "Adjustment:",adjustment)

    for currPass in range(totalPasses): 
        print("\nPass", currPass + 1)
        for example in examples:
            answer = example[0] # this is the True or False part of the example
            input = example[1] # this is the list part of the example
            print(f"inputs: {input}")

            prediction = checkExamples(threshold, example, weights)
            print(f"prediction: {prediction} answer: {answer}")

            if (prediction != answer):
                if (answer == True): # if should be true but is false
                    adjustedWeightsUp = adjustUp(adjustment, input, weights)
                    weights = adjustedWeightsUp
                else: # if should be false but is true
                    adjustedWeightsDown = adjustDown(adjustment, input, weights)
                    weights = adjustedWeightsDown
            print(f"adjusted weights: {weights}")
    return

# input: threshold, input list, weight list
# finds the sum and returns true if greater than threshold else returns false
def checkExamples(threshold, example, weights):
    sum = 0
    for i in range(len(weights)):
        
        sum = sum + (example[1][i] * weights[i])
    if (sum > threshold):
        return True
    else: 
        return False   #sum is less than threshold so its false

# input: adjustment factor, input list, weight list
# increases weight  by the given  adjustment factor for every time there is a 1 in the input example
# returns updated weights that are adjusted
def adjustUp(adjustment, example, weights):
    for i in range(len(example)):
        if (example[i] == 1):
            weights[i] += adjustment
    return weights

# input: adjustment factor, input list, weight list
# decreases weight  by the given adjustment factor for every 1 in the input example
# returns updated weights that are adjusted
def adjustDown(adjustment, example, weights):
    for i in range(len(example)):
        if (example[i] == 1):
            weights[i] -= adjustment
    return weights

    #perceptron(0.5,0.1,[-0.5, 0, 0.5, 0, -0.5],[[True,  [1,1,1,1,0]],[False, [1,1,1,1,1]],[False, [0,0,0,0,0]],[False, [0,0,1,1,0]],[False, [1,0,1,0,1]],[False, [1,0,1,0,0]],[False, [0,1,0,1,1]],[False,[0,1,0,1,0]],[False, [0,0,1,0,0]],[False, [0,0,0,1,0]]],4)
