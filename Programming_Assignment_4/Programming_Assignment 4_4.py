# 4.	Write a Python Program to Check Armstrong Number?
# 0, 1, 153, 370, 371, 407 are armstrong number

import logging

logging.basicConfig(filename="../programming_Assignment_4.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        num = int(input("Enter a number to check Armstrong number or not: "))
        logging.info("entered number successfully: %s",num)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue
try:
    sum = 0
    org = num
    str_org = str(org)
    c=len(str_org)

    while num > 0:
        a = num % 10
        b = pow(a, c)
        sum = (sum + b)
        num = int(num / 10)
    print("num is {} and sum is {}".format(org,sum))

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)

try:
    if org==sum:
        print("{} is armstrong number".format(sum))
        logging.info("%s is a armstrong number",sum)

    else:
        print("{} is not a armstrong number".format(org))
        logging.info("%s is not a armstrong number",org)

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)



