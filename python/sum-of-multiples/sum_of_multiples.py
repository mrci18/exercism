def sum_of_multiples(limit, multiples):
    result = []
    sum_res = 0

    for i in range(limit):
        for x in multiples:
            if i % x == 0 and i !=0 and not i in result:
                result.append(i)
    for i in result:
        sum_res += i

    return sum_res

if __name__ == "__main__":
    x = sum_of_multiples(20,[3, 5])
    print(x)

