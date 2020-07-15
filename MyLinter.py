"""
 _              _                            _ ____                            _
| |   (_)_ __  | |   ____ _ ___             | `__  |_ ___ _____  (_)____ _____| |
| |   | | `_  \| |_ | ___| `___|     ___    | |__| | `___|  _  | | | ___| ____| |_
| |___| | | | ||  _|| ___| |        |___|   |  ____| |   | |_| | | | ___| |___|  _|_
|_____|_|_| |_||____|____|_|                |_|    |_|   |_____|_| |____|_____|_____|
                                                              |____|
Author - Rostislav Konkov
Bibliography:
https://ideafix.name/wp-content/uploads/2012/05/Python-6.pdf
https://ozzmaker.com/add-colour-to-text-in-python/

"""
import os

startWords= ['def','for','import','with', 'return','pass','if','elif','else','startswith']  # __________________________|
savedWords= ['in','as','and','not']                                                         #                           |
commands =  ['open','print','range','globals','system']                                     #                           |
varibles =  ['True','False','None','or','global','f']                                       #   lists of control words  |
functions = ['chr','str','int','tuple','list','append','strip']                             #                           |
normalWords=['os']                                                                          #                           |
                                                                                            #___________________________|
bigLetters = [chr(x) for x in range(65,91)]                                                 #                           |
smallLetters = [chr(x) for x in range(97,123)]                                              #                           |
numbers = [ str(x) for x in range(10000+1) ]                                                #    lists of characters    |
controlChars = [chr(x) for x in range(0,31)]                                                #                           |
controlChars.append(chr(127))                                                               # __________________________|
specialChars = [chr(x) for x in range(32,47)]+[chr(x) for x in range(58,64)]+[chr(x) for x in range(91,96)]+[chr(x) for x in range(123,126)]

ownErrors = list()                              # __________________________________|
ownVaribles = list()                            #                                   |
ownFunctions = list()                           #       lists of users values       |
ownLocalVaribles = list()                       #                                   |
                                                #___________________________________|
toggleText1 = False                             #                                   |
toggleText2 = False                             #                                   |
esc =False                                      #  varibles for checkWord function  |
commentMode = False                             #                                   |
                                                #___________________________________|____________
firstWord = True                                #                                               |
grubNewFunc = False                             #  varibles for checkForNewFunctions function   |
                                                #                                               |
previousWord = ''                               #_______________________________________________|
eqMode = False                                  #                                               |
eqMode2 = False                                 #  varibles for checkForNewVaribles function    |
defMode = False                                 #                                               |
                                                #_______________________________________________|
def opt(show = False):
    """
        Shows all possible coloring variants in console
        The only function I copied
    """
    if(show):
        return None
    else:
        print()
        print("\033[0;37;40m Normal text\n")
        print("\033[2;37;40m Underlined text\033[0;37;40m \n")
        print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
        print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
        print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
        
        print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground       TextColour GreyBackground           WhiteText ColouredBackground\033[0;37;40m\n")
        print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
        print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
        print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
        print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
        print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
        print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
        print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
        print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

def colorize(word,color = 'normal'):
    """
        Function colorize takes word and color it in color 
        defined by second argument :
            'error'             | red with underline
            'start' or 'saved'  | purpple
            'command'           | yellow
            'text'              | green with no closing coloring next words
            'endtext'           | green with closing coloring next words
            'comment'           | grey with black background
            'myFunction'        | grey
            'myVarible'         | cyan with underline
            'normal'            | with no color applied
    """
    if color == 'error' or color == 'e':
        return f'\033[4;31;48m{word}\033[0m'
    elif color == 'start' :
        return f'\033[0;35;48m{word}\033[0m'    
    elif color == 'saved':
        return f'\033[0;35;48m{word}\033[0m'
    elif color == 'varible':
        return f'\033[1;36;48m{word}\033[0m'
    elif color == 'command':
        return f'\033[0;33;48m{word}\033[0m'
    elif color == 'comment':
        return f'\033[1;30;40m{word}\033[0m'
    elif color == 'endtext' or color == 'function':
        return f'\033[0;37;92m{word}\033[0m'
    elif color == 'text':
        return f'\033[0;37;92m{word}'
    elif color == 'myFunction':
        return f'\033[0;37;2m{word}\033[0m'
    elif color == 'myVarible':
        return f'\033[4;36;48m{word}'    
    elif color == 'myLocalVarible':
        return f'\033[4;36;48m{word}' 
    elif color == 'normal':
        return f'\033[0m{word}'
    else:
        return f'\033[0m{word}'

def checkWord(word):
    """
        This function takes word ( it also can be (,[,{,'\'','\"',),],}... or any kind of symbol )
        and checks if it is in some of lists with pre-saved values
        
        First condition is checks if end line is now 
        Then it turn a coment mode on if it took \# as a parameter
        Then it can toggle text mode depends on '\'', '\"' , '\\' - chars
        Then it searches in lists with values and if it finds something that fits
        it call "colorize" function with needed parameter of color 
        and returning colored word 
    """
    global toggleText1,toggleText2,esc,commentMode


    if word == 'END_LINE':                      #exit comment mode on the end of line
        commentMode = False                     
        return colorize(word,'normal')
    elif commentMode:                           #if in comment mode
        return(colorize(word,'comment'))        #color word in comment color
    elif word == '#' and not toggleText1 and not toggleText2:   # if not in text mode 1 or 2 and 
                                                #found '#' - symbol enter text mode
        commentMode = True
        return(colorize(word,'comment'))

    elif word == '\'' and not esc:              #if word is  - ' and it is not escape mode
        toggleText1 = not toggleText1           #toggle text mode_1
        if toggleText1:                         #if text mode_1 is on
            return(colorize('\'','text'))       #rerurn ' without closing text colorizing
        else:                                   #else
            return(colorize('\'','endtext'))    #return '  with closing

    if word == '\"' and not esc:                #if word is  - " and it is not escape mode
        toggleText2 = not toggleText2           #toggle text mode_2
        if toggleText2:                         #if text mode_2 is on
            return(colorize('\"','text'))       #rerurn " without closing text colorizing
        else:                                   #else
            return(colorize('\"','endtext'))    #return "  with closing

    elif toggleText1:                           #if in text mode_1
        if word == '\\' and not esc:            #if word is  - \ and it is not escape mode
            esc = True                          #enter escape mode 
            return colorize(word,'command')     #return \ colored in other color
        elif esc:                               #if already in escape mode
            esc = False                         #exit escape mode
            return(colorize(word,'command'))    #return symbol colored in other color
        else:                                   #else
            return colorize(word,'text')        #continue returning text colored words

    elif toggleText2:                           #if in text mode_2
        if word == '\\':                        #if word is  - \ and it is not escape mode
            esc = True                          #enter escape mode
            return colorize(word,'command')     #return \ colored in other color
        elif esc:                               #if already in escape mode
            esc = False                         #exit escape mode
            return(colorize(word,'command'))    #return symbol colored in other color
        else:                                   #else
            return colorize(word,'text')        #continue returning text colored words
                                                #IF WORD IN SOME OF SAVED LISTS COLOR IT RESPECTIVELY
    elif word in startWords:                    
        return colorize(word,'start')
    elif word in savedWords:
        return colorize(word,'saved')
    elif word.startswith(tuple(x for x in commands)):
        return colorize(word,'command')
    elif word in varibles:
        return colorize(word,'varible')
    elif word.startswith('#'):
        return colorize(word,'comment')
    elif word in ownFunctions:  
        return colorize(word,'myFunction')
    elif word in ownVaribles:  
        return colorize(word,'myVarible')
    elif word in ownLocalVaribles:  
        return colorize(word,'myLocalVarible')
    elif word in functions:  
        return colorize(word,'function')        
    elif word in specialChars or word.strip() == '' or word in normalWords or word in numbers:  
        return colorize(word,'normal')
    else:
        return colorize(word,'error')

def formatedCode(filePath):
    """
        This function opens file from args, opens it and split it by characters
        Then it defines where is words and where symbols or spaces
        And returns list of separated words symbols and spaces
    """
    charCode = list()                               #list for all chars in file
    with open(filePath) as myFile:                       #this loop takes each individual symbol in file
        newLine = list()                            #and adding it to 'charCode' list
        for line in myFile:
            for ch in line:
                newLine.append(ch)
            charCode.append(newLine)
            newLine = list()
    
    separatedCode = list()                          #list of all separated words 
    
    for line in charCode:                           #each line
        newLine = list()                            #set newLine to blank list
        word = ''                                   #set word to ''
        spaces = 0                                  #and spaces to 0
        for char in line:                           #each char
            if char == ' ':                         #if it space
                if word != '':                      #and tere is word saved before
                    newLine.append(word)            #add word to newLine
                    word=''                         #add 1 space
                spaces+=1                          
            elif char == '\n':                      #if it 'new line' 
                if word != '':                      #and there is word saved before
                    newLine.append(word)            #add word to newLine
                    word=''
                newLine.append(str(spaces*' '))     #add spaces if needed
                spaces = 0                           
            elif char in specialChars:              #if it spesial caracter
                if word != '':                      #and tere is word saved before
                    newLine.append(word)            #add word to newLine
                    word=''                
                newLine.append(str(spaces*' '))     #add spaces if needed     
                spaces = 0
                newLine.append(char)                #add spesial character to newLine
            elif char in smallLetters or char in bigLetters or char in numbers:
                newLine.append(str(spaces*' '))     #finally if it simple letter or number
                spaces = 0                          #add spaces if needed
                word+=char                          #and add character to word
                                                    
        separatedCode.append(newLine)               #add newLine to separatedCode
    return separatedCode                            #and return separatedCode

def checkForNewFunctions(nCode):
    """
        This function takes list of formated code and finding user defined functions
        than adds them to ownFunctions list
        or to ownErrors list if found wrong spelling
    """
    global firstWord, grubNewFunc
    for line in nCode:                                      #each line
        for word in line:                                   #each word
            if word.strip() != '':                          #if 'word' is not spaces
                if firstWord and word == 'def':             #if word is first in line and it is 'def'
                    firstWord = False                       #
                    grubNewFunc  = True                     #set grubing next word true
                elif grubNewFunc:                           #if grubing next word is true
                    isRightWord = True                      #chek if it has wrong symbols
                    for ch in word:                         #
                        if ch in smallLetters or ch in bigLetters or ch in numbers or ch == '_':
                            pass                            #if hasn't 
                        else:                               #else set it to wrong word
                            ownErrors.append(word)
                            isRightWord = False 
                    if isRightWord:                         #if it rigtht word
                        ownFunctions.append(word)           #add it to functions list

                    grubNewFunc = False                     #set grubing next word to false

        firstWord = True                                    #set next word as first

def checkForNewVaribles(nCode):
    """
     This function takes list of formated code and finding user defined varibles
        than adds them to ownVaribles of ownLocalVaribles lists respectively
        or to ownErrors list if found wrong spelling

    """
    global previousWord, eqMode, eqMode2, defMode
    for line in nCode:                                      #each line
        for word in line:                                   #each word
            if word.strip() != '':                          #if 'word' is not spaces
                                                            #FOR NEW VARIBLES
                if word == '=':                             
                    if eqMode:                              #if there was ==
                        eqMode2 = True
                    else:                                   #if there just =
                        eqMode = True
                elif eqMode and not eqMode2 and previousWord != '': #if it is '=' and there is a word
                    if previousWord not in ownVaribles and previousWord not in specialChars:
                        ownVaribles.append(previousWord)    #add to ownVaribles if still not there
                    previousWord = ''                       #reset previous 
                    eqMode = False  
                elif eqMode2 and eqMode:                    #set modes to False
                    eqMode = eqMode2 =False                                     
                                                                                #FOR 'for' OR 'as' VARIBLES
                elif previousWord == 'for' or previousWord == 'as':             #if previos word was 'for' or 'as'
                    correct = True                                              #
                    for i in word:                                              #
                        if i in smallLetters or i in bigLetters or i == '_':    #check if it wrote correctly
                            pass                                                #
                        else:                                                   #
                            ownErrors.append(word)                              #if wrong add it to ownError list
                            correct = False                                     #
                    if correct:                                                 #if wrote correct 
                        ownVaribles.append(word)                                #add to ownVaribles list
                        previousWord =''                                        #

                                                                                #FOR ARGUMENTS
                elif previousWord == 'def' and word not in specialChars:        #if in the title of function
                    defMode = True                                              #turn defMode on
                    previousWord = ''                                           #
                elif defMode:                                                   #if defMode is on
                    if word == '(' or word == ',' or word =='*':                #ignore ( , or * symbols
                        pass                                                    #
                    elif word == ')':                                           #if catch ) turn off defMode
                        defMode = False                                         #
                    else:
                       ownLocalVaribles.append(word)                            #add word to ownLocalVaribles
                else:
                    previousWord = word                                         #change previousWord if was no operations

        defMode = False                                                         #defMode off after line ends

def printCode(code):
    """
        Just print formated code with colors
    """
    lineNum = 0
    os.system('cls||clear')
    for line in code: ##### <-------     YOUR FILE HERE (in same dir as this file)
        print(colorize(f'{lineNum}\t|','myFunction'),end='')
        for word in line:
            if word == '':
                pass
            else:
                print(checkWord(word),end='')
        checkWord('END_LINE')
        print()
        lineNum += 1

def main():
    path=globals()['__file__']
    fCode = formatedCode(path)

    checkForNewFunctions(fCode)
    checkForNewVaribles(fCode)
    printCode(fCode)
    
main()