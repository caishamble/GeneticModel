from GM import single_point_crossover
import random
random.seed(10)


def test_single_point_crossover():
    # Test Case 1: Basic test
    individual1 = "hello world"
    individual2 = "genetic alg"
    inst_cross1 = "hello w alg"
    inst_cross2 = "geneticorld"
    crossover_result1, crossover_result2 = single_point_crossover(individual1, individual2)
    assert len(crossover_result1) == len(individual1) and len(crossover_result2) == len(individual2), "Test Case 1 failed"

    # Test Case 2: Ensure crossover point is valid
    assert crossover_result1 == inst_cross1 and crossover_result2 == inst_cross2, "Test Case 2 failed"

    # Test Case 3: Basic test
    individual3 = "afloo wowlz"
    individual4 = "haklwe frld"
    inst_cross3 = "aaklwe frld"
    inst_cross4 = "hfloo wowlz"
    crossover_result3, crossover_result4 = single_point_crossover(individual3, individual4)
    assert crossover_result3 == inst_cross3 and crossover_result4 == inst_cross4, "Test Case 3 failed"

    print("All test cases passed!")


# Run the test cases
test_single_point_crossover()

