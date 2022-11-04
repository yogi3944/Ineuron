# 3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
import logging

logging.basicConfig(filename="../programming_Assignment_5.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        dec = int(input("Enter number to convert Decimal to Binary, Octal and Hexadecimal: "))
        logging.info("entered number to convert Decimal to Binary, Octal and Hexadecimal successfully: %s",dec)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue

try:
    def Dec_to_BIN(x):
        binary = bin(x)
        return binary

    def Dec_to_Octal(x):
        octal = oct(x)
        return octal

    def Dec_to_Hex(x):
        hexadecimal = hex(x)
        return hexadecimal

except Exception as e:
    logging.error("Error has happened")
    print("Please input number only", e)

try:
    Binary = Dec_to_BIN(dec)
    Octal = Dec_to_Octal(dec)
    Hexadecimal = Dec_to_Hex(dec)
    print("Decimal {} to Binary is : {}, Octal is : {} and Hexadecimal is : {}".format(dec,Binary,Octal,Hexadecimal))
    logging.info("Decimal %s to Binary is : %s, Octal is : %s and Hexadecimal is : %s",dec,Binary,Octal,Hexadecimal)

except Exception as e:
    logging.error("Error has happened")
    print("Please input number only", e)


