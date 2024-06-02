from GM import mutation
import random
random.seed(10)


def test_mutation():
    # Test Case 1: Basic test with known values
    individual1 = "hello world"
    mutated_individual1 = mutation(individual1)
    assert mutated_individual1 != individual1, f"Test Case 1 failed: {mutated_individual1}"

    # Test Case 2: Ensure the length remains the same after mutation
    individual2 = "genetic algorithm"
    mutated_individual2 = mutation(individual2)
    assert len(mutated_individual2) == len(individual2), "Test Case 2 failed"

    # Test Case 3: Ensure that the returned individual is correct
    inst_mutation = "pineapple"
    individual3 = "pineapple"
    mutated_individual3 = mutation(individual3)
    print()
    assert mutated_individual3 == inst_mutation, f"Test Case 3 failed: {mutated_individual3}"

    # Test Case 4: Ensure that the returned individual is correct
    inst_mutation = "hejlo wsrly"
    individual4 = "hello world"
    mutated_individual4 = mutation(individual4)
    assert mutated_individual4 == inst_mutation, f"Test Case 3 failed: {mutated_individual4}"

    print("All test cases passed!")


# Run the test cases
test_mutation()


