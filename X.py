
def angryProfessor(k, a):
    # Write your code here
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    if count >= k:
        return "NO"
    else:
        return "YES"




t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = angryProfessor(k, a)

    print(result)

