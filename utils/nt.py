import math

def is_prime(n: int) -> bool:
    """
    Returns True if n is prime, else False. Note that every prime > 3 is congruent to
    +1 or -1 mod 6. Since group orders tend to not be overly large, a non-probabilistic
    method suffices.
    Arguments:
        - n: positive integer
    Outputs:
        - True if n is prime, else False
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer.')
    if n <= 3:
        return (n > 1)
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
