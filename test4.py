def find_permutations(x):
    # Initialize the list of valid permutations to empty
    permutations = {}
    def generate_permutations(current_permutation, remaining_sum):
        if remaining_sum == 0:
            if x in permutations:
                permutations[x].append(current_permutation)
            else:
                permutations[x] = [current_permutation]
        elif remaining_sum > 0:
            generate_permutations(current_permutation + [3], remaining_sum - 3)
            generate_permutations(current_permutation + [4], remaining_sum - 4)

    generate_permutations([], x)

    test = permutations[next(iter(permutations))]
    return test[-1]
result = find_permutations(15)

if result:
    print(f"Permutations for : {result}")
    test = result[next(iter(result))]
    print("probeer",  test[-1])
else:
    # Otherwise, print a message indicating that no permutations were found
    print("No permutations found.")
