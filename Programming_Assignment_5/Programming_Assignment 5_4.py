# 4.	Write a Python Program To Find ASCII value of a character?

import logging

logging.basicConfig(filename="../programming_Assignment_5.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        char = raw_input("Enter character to convert to ASCII value: ")
        if(len(char)<2):
            logging.info("Entered character to convert to ASCII value successfully: %s",char)
            break
    except Exception as e:
        logging.error("Error has happened")
        print(e)
        continue

try:
    def Char_to_ASCII(x):
        ascii = ord(x)
        return ascii

except Exception as e:
    logging.error("Error has happened")
    print(e)

try:
    Ascii = Char_to_ASCII(char)
    print("Character {} to ASCII is : {}".format(char,Ascii))
    logging.info("Character %s to ASCII is : %s",char,Ascii)

except Exception as e:
    logging.error("Error has happened")
    print(e)