# 5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
import logging

logging.basicConfig(filename="../programming_Assignment_5.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        num1 = int(input("Enter first number: "))
        logging.info("Entered first number successfully: %s",num1)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please enter number only", e)
        continue
while True:
    try:
        num2 = int(input("Enter second number: "))
        logging.info("Entered second number successfully: %s",num2)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please enter number only", e)
        continue

try:
    def add(x,y):
        addition = x + y
        return addition

    def subtraction(x,y):
        subtraction = x - y
        return subtraction

    def multiplication(x,y):
        multiplication = x * y
        return multiplication

    def division(x,y):
        division = x / y
        return division

except Exception as e:
    logging.error("Error has happened")
    print(e)

while True:
    try:
        operation = int(
        input("Enter 1 for addition, Enter 2 for subtraction, Enter 3 for multiplication, Enter 4 for division: "))
        logging.info("Entered operation successfully: %s", operation)

        if operation == 1:
            Addition = add(num1,num2)
            print("Addition of {} and {} is {}".format(num1,num2,Addition))
            logging.info("Addition of %s and %s is %s",num1,num2,Addition)

        elif  operation == 2:
            Subtraction = subtraction(num1,num2)
            print("Subtraction of {} and {} is {}".format(num1,num2,Subtraction))
            logging.info("Subtraction of %s and %s is %s",num1,num2,Subtraction)

        elif  operation == 3:
                Multiplication = multiplication(num1,num2)
                print("Multiplication of {} and {} is {}".format(num1,num2,Multiplication))
                logging.info("Multiplication of %s and %s is %s",num1,num2,Multiplication)

        elif  operation == 4:
                Division = division(num1,num2)
                print("Division of {} and {} is {}".format(num1,num2,Division))
                logging.info("Division of %s and %s is %s",num1,num2,Division)

        else:
            print("Operation is not selected between 1,2,3 and 4")
            logging.info("Operation is not selected between 1,2,3 and 4")
            continue


    except Exception as e:
        logging.error("Error has happened")
        print(e)




