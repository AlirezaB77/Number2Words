from constants import ABOVE_100, TENS, UNDER_20

def num_2_word(number):
    """
    Converts a number to its written word form.

    Args:
        number (int): The number to be converted.

    Returns:
        str: The written word form of the input number.
    """
    if number < 20:
        return UNDER_20[number]
    elif number < 100:
        remainder = number % 10
        if remainder == 0:
            return TENS[number//10]
        return TENS[number//10] + ' ' + UNDER_20[remainder]
    pivot = max(i for i in ABOVE_100 if i <= number)
    p1 = num_2_word(number // pivot)
    p2 = ABOVE_100[pivot]
    if number % pivot == 0:
        return f"{p1} {p2} "
    return f"{p1} {p2} {num_2_word(number % pivot)}"

def test_num_2_word():
    assert num_2_word(0) == "Zero"
    assert num_2_word(15) == "Fifteen"
    assert num_2_word(20) == "Twenty"
    assert num_2_word(45) == "Forty five"
    assert num_2_word(100) == "One Hundred "
    assert num_2_word(123) == "One Hundred Twenty three"
    assert num_2_word(1000) == "One Thousand "
    assert num_2_word(1234) == "One Thousand Two Hundred Thirty four"
    assert num_2_word(1000000) == "One Million "
    assert num_2_word(1000000000) == "One Billion "

if __name__ == "__main__":
    test_num_2_word()
    print("All tests passed!")

    number = int(input("Enter a number: "))
    print(num_2_word(number))