def calculate_expression(
    first_number,
    second_number,
    third_number
):
    """
    Calculates the result of:
    first_number + (second_number * third_number)
    """

    return (
        first_number
        + second_number * third_number
    )


result = calculate_expression(
    4,
    5,
    2
)

print(result)
