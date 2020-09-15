import sys


def sqrt(x):
    """Computing the square roots using the method
     heron of Alexandra

     Args:
         x:The number for which the square root
         has to be computed

    Returns:
        the square root of x
     """
    if x < 0:
        raise ValueError(
            "ERROR - Cannot Compute the square root of the negative number"
            f"{x}"
        )
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)

    print('Continuing on as normal here.')


if __name__ == '__main__':
    main()
