# day8/main.py

def sum_of_digits(n):
  """
  Recursively calculates the sum of digits of a number.
  :param n: The number whose digits are to be summed.
  :return: The sum of the digits.
  """
  if n == 0:
    return 0
  return n % 10 + sum_of_digits(n // 10)

# Example usage
if __name__ == "__main__":
  number = 12345
  print(f"The sum of digits of {number} is {sum_of_digits(number)}")