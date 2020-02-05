# 에라토스테네스의 채

prime_list = [True]*1000000
k = int(1000000**0.5)

for i in range(2,k+1):
    if prime_list[i] == True:
        for j in range(2*i, 1000000, i):
            prime_list[j] = False

prime = [num for num in range(2,len(prime_list)) if prime_list[num] == True]    
print(*prime)