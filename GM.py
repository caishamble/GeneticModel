###############################################################################
# Genetic Model for Sentence Guessing
# Pseudo Code for Main Algorithm
#   Prompt the user to input the sentence they would like the program to guess.
#   Initialize the population with random strings.
#   Repeat for a number of generations:
#       Selection: Perform tournament selection to choose individuals for
#           breeding.
#       Crossover: Apply single-point crossover to generate offspring.
#       Mutation: Randomly mutate the offspring with a given probability.
#       Fitness Evaluation: Assess how close each individual is to the target
#           sentence.
#       If the target sentence is found or the maximum number of generations
#           is reached, terminate the loop.
#   Output the best guess at the target sentence, and prompt the user to
#       continue.
###############################################################################
import random

random.seed(10)

# Constants for the genetic algorithm
NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

# Banner for the program
BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer!
This program will attempt to guess a sentence that you input.
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""

# Input prompt for the user
INPUT = "\nWould you like to continue? (y/n) "

def make_population(target):
    """
    Generates the initial population by creating a long string of random
    characters, with a length equal to the population size multiplied by
    the target sentence length.
    :param target: a string representing the target phrase input by user
    :return: the population string created
    """

    population = ''    # Initialize the population string
    len_population = NUM_POPULATION * len(target)
    for i in range(len_population):
        population += random.choice(ALPHABET)  # Adds random char to the pop string
    return population


def fitness(target, individual):
    """
    Calculates the fitness of an individual by comparing it to the target
    sentence. Fitness is the ratio of characters in the individual that exactly
    match the target at their respective positions.
    :param target: a string representing the target phrase input by user
    :param individual: a string representing a sliced string from population
    :return: the fitness score of the individual
    """
    num_of_sim_char = 0  # Initialize the number of similar characters
    fitness_score = 0      # Initialize the fitness score
    for i in range(len(target)):
        if individual[i] == target[i]:
            num_of_sim_char += 1
        fitness_score = num_of_sim_char / len(target)
    return fitness_score

def mutation(individual):
    """
    Mutates an individual by randomly changing some of its characters based on
    the mutation probability.
    :param individual: a string representing a sliced string from population
    :return: mutated (possibly) individual
    """
    for i in range(len(individual)):
        chosen_number = random.random()
        if chosen_number <= PROBABILITY_MUTATION:  # Check if mutation probability met
            if i == 0:
                individual = random.choice(ALPHABET) + individual[1:]
            else:
                individual = individual[:i] + random.choice(ALPHABET) + individual[i+1:]
        else:
            continue
    return individual

def single_point_crossover(individual1, individual2):
    """
    Performs a single-point crossover between two individuals. A point on the
    parent strings is chosen at random, and the substrings before and after
    this point are swapped to create two new individuals.
    :param individual1: 1st selected in the five_tournament_selection
    :param individual2: 2nd selected in the five_tournament_selection
    :return: the crossover result of the two individuals
    """
    judge_number = random.random()   # Randomly generate num to decide for crossover
    if judge_number <= PROBABILITY_CROSSOVER:

        # Randomly choose a crossover point
        point_to_cross = random.randint(1, len(individual1))

        new_individual1 = (individual1[:point_to_cross] + individual2[point_to_cross:])
        new_individual2 = (individual2[:point_to_cross] + individual1[point_to_cross:])
        return new_individual1, new_individual2
    else:
        return individual1, individual2



def five_tournament_selection(population, target):
    """
    Selects the best individual out of five randomly chosen from the population,
    based on fitness. This process is repeated to select individuals for breed.
    :param population: the string representing the population
    :param target: the target user input
    :return: the best individual selected
    """

    individual_fitness = -1 # Initialize the fitness of the individual
    individual = ''         # Initialize the individual
    best_individual = ''    # Initialize the best individual
    indi_count = 0          # Initialize the count of individuals selected
    while indi_count < 5:
        # Randomly choose a number within the population size
        rand_pop_num = random.randint(0, NUM_POPULATION - 1)

        if rand_pop_num == NUM_POPULATION - 1:
            individual = population[rand_pop_num * len(target):]
        elif rand_pop_num < NUM_POPULATION - 1:
            beginning_index = rand_pop_num * len(target)
            end_index = beginning_index + len(target)
            individual = population[beginning_index:end_index]

        if fitness(target, individual) > individual_fitness:
            individual_fitness = fitness(target, individual)
            best_individual = individual

        indi_count += 1
    return best_individual

def find_best_individual(population, target):
    """
    Searches the entire population to find the individual that has the highest
    fitness score, indicating it is the closest guess to the target sentence.
    :param population: the string representing the population
    :param target: the target user input
    :return: the best individual found
    """
    individual = ''              # Initialize the individual
    individual_fitness = -1      # Initialize the fitness of the individual
    best_individual = ''         # Initialize the best individual
    pop_loop_count = 0
    while pop_loop_count <= NUM_POPULATION - 1:
        if pop_loop_count <= NUM_POPULATION - 2:
            beginning_index = pop_loop_count * len(target)
            end_index = beginning_index + len(target)
            individual = population[beginning_index:end_index]
        elif pop_loop_count == NUM_POPULATION - 1:
            individual = population[pop_loop_count * len(target):]
        if fitness(target, individual) > individual_fitness:
            individual_fitness = fitness(target, individual)
            best_individual = individual
        pop_loop_count += 1
    return best_individual
def main():
    """
    Main function to run the GeneticGuess Sentencer program.
    """
    print(BANNER)
    while True:
        user_input = input(INPUT)
        # Prompt user to input the sentence they would like program to guess
        if user_input == 'y' or user_input == 'Y':

            # Prompt user to input the target and judge if the input is valid
            while True:
                target_input = input("\nPlease input the sentence you would like "
                                     "the program to guess: ").lower()
                if all(char in ALPHABET for char in target_input):
                    target = target_input
                    break
                else:
                    print("\nIncorrect input. Please try again.\n")

            # Generate the initial population
            population = make_population(target)

            print("\n\nGeneticGuess results:")

            # Set a flag to check if the sentence is found
            sentence_found = False

            for i in range(NUM_GENERATIONS):
                print("Generation: ", i)
                new_population = ''      # Initialize the new population
                for j in range(NUM_POPULATION):

                    # Perform tournament selection to choose individuals for breeding
                    new_individual1 = five_tournament_selection(population, target)
                    new_individual2 = five_tournament_selection(population, target)

                    # Apply mutation on each individual
                    new_individual1 = mutation(new_individual1)
                    new_individual2 = mutation(new_individual2)

                    # Apply single-point crossover to generate offspring
                    more_new_individual1, more_new_individual2 = (
                        single_point_crossover(new_individual1,new_individual2))

                    # calculate the fitness of the more_new_individuals
                    fitness1 = fitness(target, more_new_individual1)
                    fitness2 = fitness(target, more_new_individual2)

                    if fitness1 > fitness2:
                        most_new_individual = more_new_individual1
                    else:
                        most_new_individual = more_new_individual2

                    # Add the most_new_individual to the new_population
                    new_population += most_new_individual

                    if sentence_found == False:
                        if fitness1 == 1 or fitness2 == 1:      # Check if the sentence is found
                            print("I found the sentence early!")
                            print("\nBest Individual: ", most_new_individual)
                            sentence_found = True         # Set the flag to True if the sentence is found

                # Update the population
                population = new_population

                if sentence_found:
                    break
            if not sentence_found:
                print("\nBest Individual: ", find_best_individual(population, target))
        else:
            print("\n\nThank you for using GeneticGuess Sentencer!")
            break
if __name__ == '__main__':
    main()