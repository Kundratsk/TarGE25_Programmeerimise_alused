def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if len(s) == 0:
        return s

    return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """

    answer = 0
    while n > 0:
        true_answer = answer + (n+1)
    return true_answer


if __name__ == '__main__':
    tervitus = "Hey"
    tulemus = loop_reverse(tervitus)

    print(f"Algne:{tervitus}, Tagurpidi {tulemus}")

    algne = "rekursioon"
    tulem = recursive_reverse(algne)
    print(f"Algne {algne}, Tagurpidi rekursiooniga {tulem}")

    print(loop_sum(4))
    print(loop_sum(5))





