log_file = open("um-server-01.txt") # opens the file called um-server-01.txt


def sales_reports(log_file): # defines a function called sales report which takes in an argument called log_file, which is a file
    for line in log_file: # starts a for loop which iterates for every line in a file
        line = line.rstrip() # strips the white space from each line
        day = line[0:3] # defines the variable day as the first 2 letters(?) of the line
        if day == "Mon": # if statement that prints the line if the day is Tuesday
            print(line)


sales_reports(log_file) # runs the sales report function on the log_file
