import timeit


def check_speed():
    test_code = '''
string = 'amitsharma'*14000
print(len(string))
suffix_array = []
for i in range(len(string)):
    suffix_array.append(string[:i])
suffix_array.sort()
'''
    print(timeit.timeit(stmt=test_code, number=1))


check_speed()