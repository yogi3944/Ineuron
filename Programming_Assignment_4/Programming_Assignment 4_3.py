# 3.	Write a Python Program to Print the Fibonacci sequence?

import logging

logging.basicConfig(filename="../programming_Assignment_4.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        num = int(input("Enter count for which Fibonacci sequence required: "))
        logging.info("entered number successfully: %s",num)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue

try:
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)

    for i in range(2, num + 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)