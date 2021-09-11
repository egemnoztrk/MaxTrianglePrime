numbers=[215,193,124,117,237,442,218,935,347,235,320,804,522,417,345,229,601,723,835,133,124,248,202,277,433,207,263,257,359,464,504,528,516,716,871,182,461,441,426,656,863,560,380,171,923,381,348,573,533,447,632,387,176,975,449,223,711,445,645,245,543,931,532,937,541,444,330,131,333,928,377,733,17,778,839,168,197,197,131,171,522,137,217,224,291,413,528,520,227,229,928,223,626,34,683,839,53,627,310,713,999,629,817,410,121,924,622,911,233,325,139,721,218,253,223,107,233,230,124,233]

def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True

#prime olan sayıları -1000liyorum ki maximum countu bulurken o yolu kullanmasın 
counter=0
for num in numbers:
    if isPrime(num):numbers[counter]=-1000
    counter+=1


rows=[]
x=y=0
plus=2
while True:
    try:
        rows.append([])
        for z in range(y,x+1):
            rows[plus-2].append(numbers[z])
        y=x+1
        x+=plus
        plus+=1
    except Exception as e:break    
rows.pop(-1)

# Python3 program for Dynamic
# Programming implementation of
# Min Sum Path in a Triangle
 
# Util function to find
# minimum sum for a path
def maxSumPath(A):
     
    # For storing the result in
    # a 1-D array, and simultaneously
    # updating the result.
    memo = [None] * len(A)
    n = len(A) - 1
     
    # For the bottom row
    for i in range(len(A[n])):
        memo[i] = A[n][i]
 
    # Calculation of the
    # remaining rows,
    # in bottom up manner.
    for i in range(len(A) - 2, -1,-1):
        for j in range( len(A[i])):
            memo[j] = A[i][j] + max(memo[j],memo[j + 1])
    
    # return the top element
    return memo[0]

print(maxSumPath(rows))
 