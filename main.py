def welcomeMessage():
    print ("\n" + "..." + "\n")
    return 0

def userInput():
    userChoice = input("Would you like to encode or decode a message? ")
    userChoice = userChoice.upper()

    while True:
        if (userChoice == "ENCODE"):
            userMessage = input("Enter a message to encode: ")
            break

        elif (userChoice == "DECODE"):
            userMessage = input("Enter a message to decode: ")
            break

        else:
            userChoice = input('ERROR: Incorrect input. Please type "Encode" or "Decode": ')
            userChoice = userChoice.upper()

    return userChoice, userMessage

def encodeMessage(userMessage):
    return 0

def decodeMessage(userMessage):
    return 0

try:
    running = True
    welcomeMessage()

    while (running == True):
        userChoice, userMessage = userInput()

        if (userChoice == "ENCODE"):
            encryptedMessage = encodeMessage(userMessage)
            print ("\n" + "Encrypted Message: " + str(encryptedMessage) + "\n")

        elif (userChoice == "DECODE"):
            decryptedMessage = decodeMessage(userMessage)
            print ("\n" + "Decrypted Message: " + str(decryptedMessage) + "\n")

        restartApplication = input("Would you like to restart the application ? ")
        restartApplication = restartApplication.upper()

        while True:
            if (restartApplication == "YES"):
                print ("Restarting the application." + "\n")
                break

            elif (restartApplication == "NO"):
                print ("Exiting the application" + "\n")
                running = False
                break

            else:
                restartApplication = input('ERROR: Incorrect input. Please type "Yes" or "No": ')
                restartApplication = restartApplication.upper()

except KeyboardInterrupt:
    print ("\n" + "KEYBOARD INTERRUPT: Exiting the application.")