'''

Interesting Integers
Google Kickstart 2022 Round - D

456 is interesting if (4*5*6) % (4+5+6) is 0

'''

def interesting_integer_brute(A, B):
    count = 0
    for i in range(A,B+1):
        p, s = get_product_and_sum(i)
        # print ("i="+str(i)+ ", p=" + str(p) + ", s=" + str(s))
        if (p % s == 0):
            count+=1
            # print ("i="+str(i)+ ", p=" + str(p) + ", s=" + str(s))
    return count

def get_product_and_sum(n):
    p = 1
    s = 0
    while (n != 0):
        p = p * (n%10)
        s = s + (n%10)
        n = n//10
    return (p,s)


num_cases = int(input())
for case in range(1, num_cases + 1):
    A, B = [int(s) for s in input().split(" ")]
    ans = interesting_integer_brute(A,B)
    print('Case #{}: {}'.format(case, str(ans)))
    
# from Measure import measure
# measure(interesting_integer_brute,1,1000000000000)