#Created By Dawn
import math
def gain():
    done=False
    while not done:
        try:
            num=int(input('Please provide a even number(>2):\n'))
            if num<3 or num%2!=0:
                print('Please provide a correct number!')
            else:
                done=True
                return num
        except ValueError or TypeError:
            print('Please provide a number!')

def goldbach(n):
    answer=[]
    for i in range(2,n):
        if isprime(i) and isprime(n-i):
            answer.append(i)
            answer.append(n-i)
            return answer

def isprime(n):
    if n==2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
        
def main():
    num=gain()
    ans=goldbach(num)
    print('the two prime numbers are:{} and {}.'.format(ans[0],ans[1]))

if __name__=='__main__':
    main()

