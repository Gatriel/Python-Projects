def arranger(problems, ans):
    #initialization of lists 
    arranged_problems = ""
    upperline = [] #list that stores the line with the numbers on top of the operation
    lowerline = [] #same as above, but with the numbers that will be on the bottom
    operands = [] #stores the operands of each problem
    dashes = [] #stores how many dashes will be used
    results = [] #stores the result of each problem
    
    for i in range(0, len(problems)): ##removes any whitespaces, so that 33 + 44 becomes 33+44, to evitate cases of 44+    33, as this would break the formatting
        problems[i] = problems[i].replace(" ", "")

    for problem in problems:
      
        if '+' in problem: #determine the operator
            pos = problem.find('+')
            operands.append('+')
        elif '-' in problem:
            pos = problem.find('-')
            operands.append('-')
        elif '*' in problem:
            pos = problem.find('*')
            operands.append('*')
        elif '/' in problem:
            pos = problem.find('/')
            operands.append('/')

        operand1 = problem[:pos] #separate the first number
        operand2 = problem[pos + 1:len(problem)] #separate the second number
        #try catch to deal with things like a + 2
        try:
            test1 = int(operand1) 
            test2 = int(operand2)
        except:
            return "Error: Numbers must only contain digits."
        #if the numbers are too big, it will still work, but the result will be out of the dashes
        if len(operand1) > 4 and len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        #stores the numbers
        upperline.append(operand1) 
        lowerline.append(operand2)
    
    ##########################################################
    #if you want the results, this will calculate and store it
    if ans:
        for i in range(0, len(upperline)):
            if operands[i] == '+':
                answers = int(upperline[i]) + int(lowerline[i])
                results.append(answers)
            elif operands[i] == '-':
                answers = int(upperline[i]) - int(lowerline[i])
                results.append(answers)
            elif operands[i] == '*':
                answers = int(upperline[i]) * int(lowerline[i])
                results.append(answers)
            elif operands[i] == '/':
                answers = int(upperline[i]) / int(lowerline[i])
                results.append(answers)


    # defines how many spaces and how many dashes will be needed 
    for i in range(0,len(upperline)):
        if len(upperline[i]) > len(lowerline[i]):
            sizedif = 1 + len(upperline[i]) - len(lowerline[i])
            upperline[i] = (2 * ' ') + upperline[i]
            lowerline[i] = operands[i] + (sizedif * ' ') + lowerline[i]
            dashes.append((len(upperline[i]))*'-')

        elif len(upperline[i]) < len(lowerline[i]):
            sizedif = len(lowerline[i]) - len(upperline[i]) + 2
            upperline[i] = (sizedif * ' ') + upperline[i]
            lowerline[i] = operands[i] + ' ' + lowerline[i]
            dashes.append((len(lowerline[i])) * '-')

        elif len(upperline[i]) == len(lowerline[i]):
            sc = 2
            upperline[i] = (sc * ' ') + upperline[i]
            lowerline[i] = operands[i] + ((sc - 1) * ' ') + lowerline[i]
            dashes.append((len(upperline[i])) * '-')


    #stores the lists into a string
    for number in upperline:
        arranged_problems = arranged_problems + number + '    '
    arranged_problems = arranged_problems + "\n"
    for number in lowerline:
        arranged_problems = arranged_problems + number + '    '
    arranged_problems = arranged_problems + "\n"
    for dash in dashes:
        arranged_problems = arranged_problems + dash + '    '
    arranged_problems = arranged_problems + "\n"

    if ans:
        for i in range(0, len(results)):
            results[i] = str(results[i])
            sizedif = len(dashes[i]) - len(results[i])
            results[i] = (sizedif*' ') + results[i]
            arranged_problems = arranged_problems + results[i] + '    '

    return arranged_problems
