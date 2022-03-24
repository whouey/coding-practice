import sys, json

prob_num = int(sys.argv[1])
test_case = int(sys.argv[2])

print(f"python runner {prob_num + test_case}")

with open(f'../test_cases/{problem_name}.json') as f:
    test_cases = json.load(f)


def test(func, test_case):
    res = func(**test_case['input'])
    assert res == test_case['output']

def test_all(func, test_cases):
    for test_case in test_cases:
        test(func, test_case)




test_all(twoSum, test_cases)