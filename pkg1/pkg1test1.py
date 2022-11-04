
def prime_number(number):
    flag = False
    for i in range(2,number):
        if(number % i == 0):
            flag = True
            break

    return flag

prime_list=[]
num_list=range(2,10000)
for i in num_list:
    a= prime_number(i)
    if a:
        pass
    else:
        prime_list.append(i)
print ("Prime number from 1 to 10000 are: ",prime_list)



