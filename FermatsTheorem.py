from random import randint


def parse(line):
    """
        creates a tuple of the number and percentage of confidence

        Parameters:

            :param str line : string containing number and confidence percentage

        Returns:

            :rtype  : tuple
            :return : Returns a tuple of number and confidence as strings

        """

    package = tuple(line.split(" "))

    return package


def fermats_test(number, probability, num_trials):
    """
        Completes the Fermat primality test to determine the likelihood of a
        number being prime

        Parameters:

            :param int number  : The number to test for primality
            :param int probability : Given likelihood of the number being prime
            :param int num_trials : The amount of trials for testing of
            primality

        Returns:

            :rtype  : int
            :return : The amount of times fermets test succeeded

        I complete a given number of trials with different random numbers
        that are less than the value we are testing for primality. If
        Fermat's theorem: (a**p) % p = a is True, we add it to the success
        count variable as it has passed the test. When all trails are
        complete we return the amount of trials that passed.
    """
    success_count = 0

    for count in range(1, num_trials):

        rand_num = randint(1, number-1)

        # Fermat's theorem (a**p) % p = a
        if pow(rand_num, number, number) == rand_num:

            success_count += 1

    return success_count


if __name__ == "__main__":

    string = "29497513910652490397 0.9"
    trials = 1000000

    num, prob = parse(string)

    successes = fermats_test(int(num), float(prob), trials)

    # Print the probability that the given number is a prime number
    print(successes/trials)








