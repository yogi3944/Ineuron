# 6.	Write a Python Program to Find the Sum of Natural Numbers?
import logging

logging.basicConfig(filename="../programming_Assignment_4.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        num = int(input("Enter a number till find the sum of natural number: "))
        logging.info("entered number successfully: %s",num)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue
try:
    sum = 0
    sum=((num)*(num+1))/2
    print("sum of {} natual number is : {}".format(num,sum))
    logging.info("sum of %s natual number is %s",num,sum)

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)