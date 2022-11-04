# 2.	Write a Python Program to Display the multiplication Table?
import logging

logging.basicConfig(filename="../programming_Assignment_4.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
table=1
while True:
    try:
        num = int(input("Enter number for which find the Multiplication Table: "))
        logging.info("entered number successfully: %s",num)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue
try:
    if num < 0:
        print("Sorry, negative numbers",num)

    elif num == 0:
        print ("Sorry, number is 0")

    else:
        for i in range(1,11):

            table = num * i
            print("table of {} * {} is : {}".format(num,i,table))
            logging.info("table of {} * {} : {}".format(num,i,table))

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)




