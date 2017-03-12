from random import randint
optioninput = 'text'
option = []
temp = 0
while optioninput != 'result':
    optioninput = raw_input('Please type the name of an option or type "result", to finalize the vote => ')
    if optioninput != 'result':
        chance =  input('How many chances does this option have ? => ')
        for i in range (0 , chance):
            option.append(optioninput)
            i = i + 1
    temp = temp + chance
resultcounter = randint(0 , temp)
print(option[resultcounter])
