# Author : Sean Bennett
# Contact for questions: sebennett@ursinus.edu
################################################################################
#                                   Introduction
#   This program takes informations from the config File feeds Solar that info,
#   then Solar generates the code for the submission File, compilation File,
#   and shell File automatically. It also creates the log File and generates the code
#   for that file as well. All of this is done automatically off the run and requires
#   no intervention besides changing the params in the config File that you want.
#   There are further comments through out that document how this is all done.
#
#
# Importing packages for use
# os for directroy paths
# math for math functions
# numpy for float(s) and array management
# sys for pathing directories
# datetime for loging the date of run
# ascii_lowercase for managing alphabet looping later on
import os
import math
import numpy
import sys
from datetime import datetime
from string import ascii_lowercase
# creating some global character variables  for clarity, that will be used throughout
indent = "\t"
newLine = "\n"
# array that holds all non comment lines from configFile
lineArray = []
# array for holding for loops
forLoopHolder = []
# array that holds the os.system call paramaters for the submissionFile
osParamHolder = []
# array that holds the os.system call paramaters for the shellFile
shellParamHolder = []
# Generic number variables that make the code easier to read and less likely
# to type in a wrong number
_ZERO = 0
_ONE = 1
_TWO = 2
_THREE = 3
_FOUR = 4
_FIVE = 5
_SIX = 6
_SEVEN = 7
_EIGHT = 8
_NINE = 9
_TEN = 10
_ELEVEN = 11
_TWELVE = 12
_THIRTEEN = 13
_FOURTEEN = 14
_FIFTEEN = 15
# Opening the configFile in read mode --- 'r'
# sys.path[0] equates to the directory you are in already(the solar folder)
configFile = open(os.path.join(sys.path[_ZERO], "configFile.txt"), "r")
# Same process as configFile but in write mode "w" for the rest of the files
submissionFile = open(os.path.join(sys.path[_ZERO], "submissionFile.py"), "w")
compilationFile = open(os.path.join(
    sys.path[_ZERO], "compilationFile.py"), "w")
logFile = open(os.path.join(sys.path[_ZERO], "logFile.txt"), 'w')
shellFile = open(os.path.join(sys.path[_ZERO], "Solar.sh"), "w")
# This is where the datetime package comes into play where I am using it to
# get the date and time of the run and naming it 'now'.
now = datetime.now()
# This line writes to the logFile without having to do it manually everytime
# At run the logFile will have this line written to it : Time of run = 'The Time'
logFile.write("Time of run: " + str(now))
# importing package numpy in the submission file to handle float looping with numpy.arange
submissionFile.write("import numpy")
# New line print, will be used a lot for file management
submissionFile.write(newLine)
# imports for the submissionFile
submissionFile.write("import os")
submissionFile.write(newLine)
submissionFile.write("import math")
submissionFile.write(newLine)
submissionFile.write("import sys")
submissionFile.write(newLine)
# imports for compilation File
compilationFile.write("import os")
compilationFile.write(newLine)
compilationFile.write("import numpy")
compilationFile.write(newLine)
compilationFile.write("import sys")
compilationFile.write(newLine)


def readTheFile():
    """
    Main function that reads in each line of the file and calls forLooper
    Appends non comment lines to lineArray

    Returns - NONE
    -------
    type - ----

    """
    # loop line counter
    loopCounter = _ZERO
    with configFile as configFileObject:
        for line in configFileObject:
            line = line.strip()
            # skips to next line if the line in the param file is
            # a comment line
            if line[_ZERO] == '#':
                continue
            # if the line isn't a comment line, its a param and we want it in the
            # logFile
            logFile.write(newLine)
            logFile.write(line)
            # adding line if non comment to lineArray
            lineArray.append(line)
            # counter for counting commas in line
            commaCounter = _ZERO
            for x in line:
                if x == ',':
                    commaCounter += _ONE
            # The logic behind this is that if there is ever another variable
            # you want to loop over such as 1,2,3 it will automatically
            # make a new nested loop for it
            # In other words, there are 3 seperated things - so loop it
            if commaCounter == _TWO:
                # strips end of line off string
                line = line.rstrip()
                # increments loopCounter since a loop was found
                loopCounter += _ONE
                # the line gets appended to the forLoopHolder array
                # for later use
                forLoopHolder.append(line)
    # this method call only happens once and takes in the number of loops
    # counted in the file as its param
    forLooper(loopCounter)


def getNumProcessors():
    """
     This function only does writing to the submissionFile where an
     algorithm generates the number of processors to use that goes in the slurm
     command based off the number of atoms that is specified in the config.txt

    Returns - NONE
    -------
    type - ---

    """
    submissionFile.write(newLine)
    submissionFile.write("def getNumProcs(numAtoms):")
    submissionFile.write(newLine)
    submissionFile.write(indent + "n = int(numAtoms)")
    submissionFile.write(newLine)
    submissionFile.write(indent + "N = 0")
    submissionFile.write(newLine)
    submissionFile.write(indent + "m = 0")
    submissionFile.write(newLine)
    submissionFile.write(indent + "for m in range(0, m < n, 2):")
    submissionFile.write(newLine)
    submissionFile.write(
        indent + indent + "N = N + (2**(n - m)) * math.factorial(n) / (math.factorial(m) * math.factorial(n - m)) * math.factorial(m) / (math.factorial(m / 2) * math.factorial(m / 2))")
    submissionFile.write(newLine)
    submissionFile.write(indent + "if(N < 8100):")
    submissionFile.write(newLine)
    submissionFile.write(indent + indent + "return 1")
    submissionFile.write(newLine)
    submissionFile.write(indent + "elif(N >= 8100 and N <= 16000):")
    submissionFile.write(newLine)
    submissionFile.write(indent + indent + "return 4")
    submissionFile.write(newLine)
    submissionFile.write(indent + "elif(N > 16000 and N <= 30000):")
    submissionFile.write(newLine)
    submissionFile.write(indent + indent + "return 6")
    submissionFile.write(newLine)
    submissionFile.write(indent + "elif (N > 30000 and N <= 70000):")
    submissionFile.write(newLine)
    submissionFile.write(indent + indent + "return 12")
    submissionFile.write(newLine)
    submissionFile.write(indent + "elif (N > 70000 and N <= 100000):")
    submissionFile.write(newLine)
    submissionFile.write(indent + indent + "return 24")
    submissionFile.write(newLine)
    submissionFile.write(indent + "elif(N > 100000):")
    submissionFile.write(newLine)
    submissionFile.write(indent + indent + "return 48")
    submissionFile.write(newLine)


def forLooper(loopCounter):
    """
    This method is an infinite nested for looper for as many lines as
    given from the config.txt that get passed in as loopCounter

    Parameters
    ----------
    loopCounter : int
        The amount of loop lines found in the configFile.txt

    Returns - NONE
    -------
    type - ---

    """
    counter = _ONE
    # this little block of code seperates the tMax and tStep into seperate variables
    # for easier manipulation
    lineFromArray = lineArray[_EIGHT]
    splitLineArray = lineFromArray.split(',', _TWO)
    tMax = splitLineArray[_ZERO]
    tStep = splitLineArray[_ONE]
    # end of tMax/tStep block
    # the name of the loop variables is best if they are arbitrary so I
    # loop through the alphabet to ensure an easy to assign and easy to manage the system
    name = ''
    alphabet = []
    for x in ascii_lowercase:
        alphabet += x
    alphabetCounter = _ZERO

    # this is where the loop building happens
    # we begin with having a while loop encase the entire process so that
    # it will keep occuring as long as needed - counter <=loopCounter
    while counter <= loopCounter:
        # here we take out each string one by one from forLoopHolder and
        # turn it into a nested for loop
        for string in forLoopHolder:
            # every loop needs a name, a min value, max and increment value
            name = alphabet[alphabetCounter]
            splitLine = string.split(',', _THREE)
            min = splitLine[_ZERO]
            max = splitLine[_ONE]
            add = splitLine[_TWO]
            forLoop = ''
            # pythons range function does not work with floats so I specify a
            # numpy call for those occasions for which a float is found
            floatFound = _ZERO
            addStr = str(add)
            # a secondary support counter that is used for reference for how many
            # indents should be used to properly nest the next loop
            counter2 = _ZERO
            # string that holds the indents for nesting
            indentLine = ''
            # this is where I check for a float value so I can use
            # numpy.arrange instead of range
            for char in addStr:
                if char == '.':
                    floatFound = _ONE
                    addedToFRange = float(max) + float(add)
                    forLoop = indent + 'for ' + name + ' in numpy.arange(' + min + \
                        ',' + str(addedToFRange) + ',' + add + '):'
            # since addedTo is only used for range, we need to set it to something
            # even when its not in use
            if floatFound == _ONE:
                addedTo = ''
            else:
                # this is the whole integer loop builder that gets printed if a
                # float is not found
                addedTo = int(max) + int(add)
                forLoop = indent + 'for ' + name + ' in range(' + min + ',' + \
                    str(addedTo) + ',' + add + '):'
            # We have to begin the nested printing with the first loop
            # which doesnt have any special indenting
            if counter == _ONE:
                submissionFile.write(forLoop)
                submissionFile.write(newLine)
            # this is where counter2 comes in and counts the number of indents
            # we need to generate
            while(counter2 < counter - _ONE):
                indentLine += indent
                counter2 = counter2 + _ONE
            # this if statement prints the indents and for loop accordingly
            # for the rest of the loops after the first excluding the second to last
            # and last loop
            if counter2 >= _ONE:
                forLoop = indentLine + forLoop
                submissionFile.write(forLoop)
                submissionFile.write(newLine)
            # this write out to the sub file must come at the second to last loop
            # which this if statement takes care of for us
            if counter == loopCounter - _ONE:
                # the number of processes is generated here from the getNumProcessors
                # method that was written to the submissionFile earlier
                submissionFile.write(
                    indentLine + indent + indent + "numP = getNumProcs(" + lineArray[_SEVEN] + ")")
                submissionFile.write(newLine)
                submissionFile.write(indentLine + indent + indent + "try:")
                submissionFile.write(newLine)
                # here we begin to make the data directories that store our raw data
                # and print the data to them
                submissionFile.write(indentLine + indent + indent + indent + "os.makedirs('" +
                                     lineArray[_SIX] + "/" + lineArray[_ELEVEN] + "/'+str(counter))")
                submissionFile.write(newLine)
                submissionFile.write(indentLine + indent + indent + indent + "paramFilePath = '" +
                                     lineArray[_SIX] + "/" + lineArray[_ELEVEN] + "/'+str(counter)+'/'")
                submissionFile.write(newLine)
                submissionFile.write(indentLine + indent + indent + indent +
                                     "pFile = os.path.join(paramFilePath, 'params.txt')")
                submissionFile.write(newLine)
                submissionFile.write(
                    indentLine + indent + indent + indent + "paramFile = open(pFile, 'w')")
                submissionFile.write(newLine)
                stringOfParams = paramLooper()
                stringOfParams = stringOfParams[:-_TWO]
                submissionFile.write(indentLine + indent + indent + indent + "paramFile.write('Electric Field at run -> " +
                                     "'" + "+" + "str(a)" + "+" + "'" + ", " + stringOfParams + "')")
                submissionFile.write(newLine)
                submissionFile.write(
                    indentLine + indent + indent + indent + "paramFile.close()")
                submissionFile.write(newLine)
                submissionFile.write(
                    indentLine + indent + indent + "except OSError:")
                submissionFile.write(newLine)
                submissionFile.write(
                    indentLine + indent + indent + indent + "pass")
                submissionFile.write(newLine)

            # this write out to the sub file always has to come after the last loop
            # which this if statement takes care of for us
            if counter == loopCounter:
                # there are a few variables that are spaced out between information
                # in the config file that we do not need so this loop
                # gets the necessary info while excluding the unnecessasry
                stringFromLineArray = lineArray[_TEN] + " "
                for i in range(_FIFTEEN, len(lineArray), _ONE):
                    stringFromLineArray += str(lineArray[i]) + " "
                stringFromLineArray = stringFromLineArray.replace(',', ' ')
                stringFromLineArray = stringFromLineArray[:-_ONE]

                # this is the os.system call in string form so that I can manipulate it later
                # a useful little tip is that for the .sh file  the params are
                # everthing after lineArray[_THREE]

                osString = "os.system(" + '"' + "sbatch -N 1 -n " + '"' + "+" + "str(numP)" + "+" + '"' + " -p " + lineArray[_ZERO] + " -o " + lineArray[_TWO] + "/" + lineArray[_ELEVEN] + "-%j.out --nice=0 -J " + lineArray[_TWELVE] + " " + lineArray[_THREE] + " " + '"' + "+" + "str(numP)" + "+" + '"' + " " + lineArray[_FIVE] + " " + lineArray[
                    _SIX] + "/" + lineArray[_ELEVEN] + "/" + '"' + "+" + "str(counter)" + "+" + '"' + " " + '"' + "+" + "str(" + name + ")" + "+" + '"' + " " + "40 /share/states/spps/spps_N_4.nc " + lineArray[_SEVEN] + " " + tMax + " " + tStep + " " + '"' + "+" + "str(a)" + "+" + '"' + " " + stringFromLineArray + '"' + ")"

                # this is where i do some string manipulation to store the .sh
                # params that I will use later on in shellFileWriting
                osStringSplit = osString.split(' ')
                for k in osStringSplit:
                    osParamHolder.append(k)
                # I reverse the array of params here because the ones we want
                # are at the end of the array. This made it easier for me to
                # accomplis this task.
                breakString = False
                while(breakString == False):
                    for param in reversed(osParamHolder):
                    # here we break if Solar.sh is found
                    # this is the string right after the last param we want
                    # so if we hit Solar.sh we want to leave the loop
                        if param == 'Solar.sh':
                            breakString = True
                        else:
                            shellParamHolder.append(param)
                # here I print the osString in its original state
                submissionFile.write(indentLine + indent + indent + osString)
                submissionFile.write(newLine)
                submissionFile.write(indentLine + indent + "counter += 1")
            # increment counter and goes back to the top
            counter += _ONE
            alphabetCounter += _ONE


def paramLooper():
    """
    This is a pretty basic method that loops through lineArray and appends the
    params at every index into a big string which it returns

    Returns:
    stringOfParams
    -------
    type: String
        Returns a string of params that are gathered from the configFile

    """
    # this loop goes through and gathers all the paramaters
    # that were used in the run and prepares them for pritning
    stringOfParams = ''
    for i in range(_EIGHT, len(lineArray), _ONE):
        stringOfParams += lineArray[i] + ", "
    return stringOfParams


def declareMain(nameOfFile):
    """
    Genertic def main() print to any file based off the nameOfFile given

    Parameters
    ----------
    nameOfFile : String
        Name of any file that needs to be written to

    Returns - NONE
    -------
    type - ---

    """
    nameOfFile.write(newLine)
    nameOfFile.write("def main(): ")
    nameOfFile.write(newLine)


def mainIf(nameOfFile):
    """
    Generic if name is main print to any file based off the nameOfFile given


    Parameters
    ----------
    nameOfFile : String
        Name of any file that needs to be written to

    Returns - NONE
    -------
    type - ---

    """
    nameOfFile.write(newLine)
    nameOfFile.write("if __name__ =='__main__': ")
    nameOfFile.write(newLine)
    nameOfFile.write("  main()")

def compilationScript():
    """
    This method handles the write out to the compilation file

    Returns - NONE
    -------
    type - ---

    """
    # counter to keep track of which file to create next
    compilationFile.write(indent + "counter = 0")
    compilationFile.write(newLine)
    compilationFile.write(indent + "try:")
    compilationFile.write(newLine)
    # creating the directory results
    compilationFile.write(
        indent + indent + "os.makedirs('" + lineArray[_THIRTEEN] + "/" + lineArray[_ELEVEN] + "')")
    compilationFile.write(newLine)
    compilationFile.write(indent + "except OSError:")
    compilationFile.write(newLine)
    compilationFile.write(indent + indent + "pass")
    compilationFile.write(newLine)
    # this is slightly reused code from before that re makes the electric field for loop
    elecFieldString = forLoopHolder[_ZERO]
    splitLine = elecFieldString.split(',', _THREE)
    min = splitLine[_ZERO]
    max = splitLine[_ONE]
    add = splitLine[_TWO]
    forLoop = ''
    addStr = str(add)
    addedToFRange = float(max) + float(add)
    forLoop = indent + \
        'for x in numpy.arange(' + min + ',' + \
        str(addedToFRange) + ',' + add + '):'
    compilationFile.write(forLoop)
    compilationFile.write(newLine)
    # os system call that handles the compilation of the data
    compilationFile.write(indent + indent + "os.system(" + '"' + "java -classpath $CLASSPATH:/opt/share/rydberg/jar/mtj.jar:/opt/share/rydberg/jar/StarkMapper.jar:/opt/share/rydberg/jar/netcdfAll-4.0.jar:/data DDSimulator.DDDataReader " +
                          lineArray[_SIX] + "/" + lineArray[_ELEVEN] + "/" + '"' + "+" + "str(counter)" + "+" + '"' + "/data_ 120 " + lineArray[_FOURTEEN] + " " + lineArray[_THIRTEEN] + "/" + lineArray[_ELEVEN] + "/" + lineArray[_ELEVEN] + "_" + '"' + "+" + "str(counter)" + "+" + '"' + ".txt 2" + '")')
    compilationFile.write(newLine)
    # creating each individual file and appending the data to it
    compilationFile.write(indent + indent + "resFilePath = '" +
                          lineArray[_THIRTEEN] + "/" + lineArray[_ELEVEN] + "/'")
    compilationFile.write(newLine)
    compilationFile.write(indent + indent + "joinString = '" +
                          lineArray[_ELEVEN] + "_'+str(counter)+'.txt'")
    compilationFile.write(newLine)
    compilationFile.write(
        indent + indent + "rFile = os.path.join(resFilePath,joinString)")
    compilationFile.write(newLine)
    # results file already has the params printed to them so it needs to be opened
    # in mode 'a' for append.
    # Note: 'w' will overwrtie the data!
    compilationFile.write(indent + indent + "resFile = open(rFile,'a')")
    compilationFile.write(newLine)
    # gathering a fresh original list of params
    stringOfParams = paramLooper()
    stringOfParams = stringOfParams[:-2]
    # pritning the list of params to the end of the file
    compilationFile.write(
        indent + indent + "resFile.write(',{'+str(x)+'" + "," + stringOfParams + "}}')")
    compilationFile.write(newLine)
    compilationFile.write(indent+ indent+"resFile.close()")
    compilationFile.write(newLine)
    # this block of code takes the contents of the results file and adds a
    # { bracket to the very beginning of the file that is used for managing the data
    # in mathematica
    compilationFile.write(indent+indent+"resFile = open(rFile,'r')")
    compilationFile.write(newLine)
    compilationFile.write(indent+indent+"data = resFile.read()")
    compilationFile.write(newLine)
    compilationFile.write(indent+indent+"resFile.close()")
    compilationFile.write(newLine)
    compilationFile.write(indent+indent+"resFile = open (rFile,'w')")
    compilationFile.write(newLine)
    compilationFile.write(indent+indent+"resFile.write('{'+ data)")
    compilationFile.write(newLine)
    compilationFile.write(indent+indent+"resFile.close()")
    compilationFile.write(newLine)

    compilationFile.write(indent + indent + "counter += 1")
    compilationFile.write(newLine)
    # changing directories back to the main results and creating a a compressed
    # version of the results for exporting
    compilationFile.write(indent + "os.chdir('" + lineArray[_THIRTEEN] + "')")
    compilationFile.write(newLine)
    compilationFile.write(indent + "os.system(" + '"' + "tar czf " +
                          lineArray[_ELEVEN] + ".tz.gz " + lineArray[_ELEVEN] + '"' + ")")


def shellFileWriting():
    """
    Method that handles all the writing to the shellFile
    Each line that is printed out has to follow a specific guideline so to say
    There isn't much here for commenting , it has to be how it is for the
    functions to work


    Returns - NONE
    -------
    type - ---

    """
    # this is the specific format that needs to be followed
    shellFile.write("#!/bin/bash")
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("module purge")
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("module load openmpi-2.0/gcc")
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("mkdir /scratch/" + '"$' + "SLURM_JOB_ID" + '"')
    shellFile.write(newLine)
    shellFile.write(newLine)

    # this loop goes through the ammount of paramaters that will need to be added
    # to the echo and time mpirun lines and makes them into a string
    amountOfParams = len(shellParamHolder)
    stringToPrint = ''
    for s in range(_ONE, amountOfParams - _ONE):
        if s == _THREE:
            stringToPrint += '/scratch/"$SLURM_JOB_ID"/data_' + ' '
        else:
            # this is the specific format that needs to be followed
            stringToPrint += '"' + '${' + str(s) + '}' + '"' + ' '
    # removing the space at the end
    stringToPrint = stringToPrint[:-_ONE]
    # this is the specific format that needs to be followed
    shellFile.write("echo mpirun --mca btl openib,self -np " + stringToPrint)
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("time mpirun --mca btl openib,self -np " + stringToPrint)
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("echo mv /scratch/" + '"' + "$SLURM_JOB_ID" +
                    '"' + "/data_*.nc " + '"' + "${3}" + '"')
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("mv /scratch/" + '"' + "$SLURM_JOB_ID" +
                    '"' + "/data_*.nc " + '"' + "${3}" + '"')
    shellFile.write(newLine)
    shellFile.write(newLine)
    shellFile.write("rm -rf /scratch/" + '"' + "$SLURM_JOB_ID" + '"')


def main():
    """
    The main of the program that calls all of the functions in the correct order
    and closes all the files after the last function call

    Returns - NONE
    -------
    type - ---

    """
    nameOfFileSub = submissionFile
    nameOfFileComp = compilationFile
    getNumProcessors()
    declareMain(nameOfFileSub)
    submissionFile.write(indent + "counter = 0")
    submissionFile.write(newLine)
    readTheFile()
    print("Now run the submissionFile.py ---> python submissionFile.py")
    mainIf(nameOfFileSub)
    declareMain(nameOfFileComp)
    compilationScript()
    mainIf(nameOfFileComp)
    shellFileWriting()

    submissionFile.close()
    compilationFile.close()
    shellFile.close()
    logFile.close()


# this needs to be here for the main to be able to be recognized and function
if __name__ == '__main__':
    main()
