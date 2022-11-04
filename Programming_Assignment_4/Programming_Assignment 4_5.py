# 5.	Write a Python Program to Find Armstrong Number in an Interval?



import logging

logging.basicConfig(filename="../programming_Assignment_4.log", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
while True:
    try:
        lower_limit = int(input("Enter a number to check Armstrong number of lower limit: "))
        logging.info("entered number successfully: %s",lower_limit)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue

while True:
    try:
        upper_limit = int(input("Enter a number to check Armstrong number of upper limit: "))
        logging.info("entered number successfully: %s",upper_limit)
        break
    except Exception as e:
        logging.error("Error has happened")
        print("Please input number only", e)
        continue
try:
    for num in range(lower_limit,upper_limit+1):
        order = len(str(num))
        sum = 0
        org = num
        while num > 0:
            a = num % 10
            b = pow(a, order)
            sum = (sum + b)
            num = int(num / 10)
        #print("num is {} and sum is {}".format(org,sum))
        if org == sum:
            print("{} is armstrong number".format(sum))
            logging.info("%s is a armstrong number",sum)

except Exception as e:
    logging.error("Error has happened")
    print("error found", e)







