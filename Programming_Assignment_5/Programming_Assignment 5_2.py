# 2.	Write a Python Program to Find HCF?
#1.	Write a Python Program to Find LCM?


import logging

logging.basicConfig(filename="../programming_Assignment_5.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        num1 = int(input("Enter first number to check LCM: "))
        logging.info("entered first number successfully: %s",num1)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue
while True:
    try:
        num2 = int(input("Enter second number to check LCM: "))
        logging.info("entered second number successfully: %s",num2)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue

try:
    def Calculate_HCF(x,y):

        if x > y:
            smaller = y

        else:
            smaller = x

        for i in range(1,smaller+1):

            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)

try:
    HCF = Calculate_HCF(num1, num2)
    print("HCF of {} and {} is : {}".format(num1, num2, HCF))
    logging.info("HCF of %s and %s is %s",num1,num2,HCF)

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)


