import sys, json, os, re

# problem_num = int(sys.argv[1])
# test_case = int(sys.argv[2]) if len(sys.argv) > 2 else None
problem_num = 1

for filename in os.listdir(sys.path[0]):
    match = re.match(rf"^{problem_num}\.([a-zA-Z-]+)\..+", filename)
    if match:
        problem_name = match.group(1)

print(f"python runner on problem {problem_num}. {problem_name}")

with open(f'{sys.path[0]}/../test_cases/{problem_num}.{problem_name}.json') as f:
    test_cases = json.load(f)


# def test(func, test_case):
#     res = func(**test_case['input'])
#     assert res == test_case['output']

# def test_all(func, test_cases):
#     for test_case in test_cases:
#         test(func, test_case)




# test_all(twoSum, test_cases)