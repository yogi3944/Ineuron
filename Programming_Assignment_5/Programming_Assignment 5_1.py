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
    def Calculate_LCM(x,y):

        if x > y:
            greater = x

        else:
            greater = y

        while True:
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater = greater + 1
        return lcm

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)

try:
    LCM = Calculate_LCM(num1, num2)
    print("LCM of {} and {} is : {}".format(num1, num2, LCM))
    logging.info("LCM of %s and %s is %s",num1,num2,LCM)

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)


