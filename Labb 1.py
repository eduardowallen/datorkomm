import sys
### EXERCISE 1 ###

def int2binary(num):
    # Using the format function we can convert any number given to its corresponding
    # binary form. The function int2binary takes a integer and returns the binary form.
    return '{:b}'.format(num)

def binary2int(binary):
    # I wanted to see how it worked the other way around, so I made a binary to int function as well, using
    # the int() and str() functions. The int is converted to 
    return int(str(binary), 2)

print("### EXERCISE 1 ###")
print(int2binary(0))
print(int2binary(10))

### EXERCISE 2 ###
def parseMessage(inputString):
    #Your code for parsing the HTTP message goes here
    # First, I'm splitting the string into lines. This makes it easier to handle the resources
    lines = inputString.splitlines()
    # I then create some strings and copy the values of the strings that can be found in the line.
    # I know that the requested_resource is at the second index of the split (which in python is 1), so I copy it to my string variable.
    requested_resource = lines[0].split()[1]
    # I do the same for the rest of the variables that were asked for in the exercise.
    client_browser = lines[2].split()[1]
    http_version = lines[0].split()[2]
    language = lines[4].split()[1]
    # Last, I create a list with the strings copied
    use_me = [requested_resource, client_browser, http_version, language]
    # Return the list
    return use_me

        
def main():
    string1='GET /index.html HTTP/1.1\r\nHost: www-net.cs.umass.edu\r\nUser-Agent: Firefox\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-us\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n'
    
    function_output=parseMessage(string1)
    #Here you will print:
    #print(function_output)
    #the requested_resource,
    #the client’s_browser
    #the HTTP version
    #the language
    print(function_output)

print("\n")
print("### EXERCISE 2 ###")
main()

print("\n")
print("### EXERCISE 3 ###")

def changeChar(string, index, char):
    # This function takes three parameters. The parameters are pretty straightforward (string, index, char)
    # I set a new string based on the incoming string, but while creating the new string I modify it as strings
    # in python are immutable and cannot be changed when already set.
    string = string[:index] + char + string[index+1:]
    print(string)

# Running the examples
changeChar("This is a string",0,"X")
changeChar("This is a string",5,"X")
changeChar("This is a string",10,"X")
