#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing the
                    upper limits for each round.

    Returns:
        str or None: The name of the player who won the most rounds
                    (either 'Maria' or 'Ben').
                     If the winner cannot be determined, returns None.
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0
    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # Filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
