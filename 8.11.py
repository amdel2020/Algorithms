import timeit


def currency(target):
    coin_sizes = [1, 5, 10, 25]
    ways = [0] * (target + 1)
    ways[0] = 1

    for i in range(len(coin_sizes)):
        for j in range(coin_sizes[i], target + 1):
            ways[j] += ways[j - coin_sizes[i]]


def check_speed():
    test_code = '''
def currency():
    target = 10000000
    coin_sizes = [1, 5, 10, 25]
    ways = [0] * (target + 1)
    ways[0] = 1

    for i in range(len(coin_sizes)):
        for j in range(coin_sizes[i], target + 1):
            ways[j] += ways[j - coin_sizes[i]]

currency()'''

    print(timeit.timeit(stmt=test_code, number=1))


check_speed()
