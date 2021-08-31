def perceptron(threshold, adjustment, weights, examples, totalPasses):
    print("Starting weights:", weights)
    print("Threshold:",threshold, "Adjustment:",adjustment)

    for currPass in range(totalPasses): 
        print("\nPass", currPass + 1)
        for example in examples:
            answer = example[0] # answer
            input = example[1] # input list
            print(f"inputs:{input}")
            prediction = None
            print(f"prediction:{prediction} answer:{answer}")
            