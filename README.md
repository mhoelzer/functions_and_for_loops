<p align="center">
  <img src=logo.jpg/>
</p>

# Kenzie Academy: Python 2.7 Katas - Functions and For Loops

In this assessment, we had to create functions without using built-in operators and functions.

## Add

Write a function named "add" that takes two arguments and returns their sum.

You may use built-in operators to finish the definition.

Display the result of calling add(2, 4), which should be 6.

## Multiply

Write a function named "multiply" that takes two arguments and returns their product.

You may not use built-in arithmetic operators or functions. Instead, you'll need a for loop which calls the "add" function you wrote earlier.

Display the result of calling multiply(6, 8), which should be 48.

## Power

Write a function named "power" that takes two arguments (x and n) and returns the the result of raising x to the nth power.

You may not use built-in arithmetic operators or functions. Instead, use functions you wrote in earlier katas to write this function.

Display the result of calling power(2, 8), which should be 256.

Another word for this is "exponentiation". In the above example, we arrive at 256 by multiplying 2 by itself 8 times:

    2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 256

If we had called power(3, 4), we'd want to multiply 3 by itself 4 times:

    3 * 3 * 3 * 3 = 81

See [this](https://simple.wikipedia.org/wiki/Exponentiation) Wikipedia article for more details on exponentiation.

## Factorial

Write a function named "factorial" that takes a single argument and returns the factorial of that argument.

You may not use built-in arithmetic operators or functions. Instead, use functions you wrote in earlier katas to write this function.

Display their result of calling factorial(4), which should be 24

(4 \* 3 \* 2 \* 1)

## Fibonacci

Write a function named "fibonacci" that takes an argument n and returns the nth, [Fibonacci number](https://simple.wikipedia.org/wiki/Fibonacci_number) (click me!).

You may not use built-in arithmetic operators or functions. Instead, use functions you wrote in earlier katas to write this function.

Display the result of calling fibonacci(8), which should be 13:

0 1 1 2 3 5 8 [13] 21

The number in brackets is the 8th fibonacci number

## Hints:

1. The answer to most of these will look similar. They will typically involve:

   - declaring a variable to keep track of a final result
   - writing a for loop to consistently modify the result
   - returning the result

2. Try writing a separate function that takes an argument and creates a div displaying that argument. Doing so will allow you to write pure functions (Links to an external site.)Links to an external site. that only deal with the problem at hand (e.g. adding two numbers, calculating the factorial of a number, etc), and pass their results to the function whose only responsibility is to display stuff on a page.

3. If you struggle for more than 5 minutes, ask for help! This is an exercise in critical thinking, not torture.

# How to Make the Magic Happen:

1. Enter `python main.py` in the terminal.
2. Celebrate! :)
