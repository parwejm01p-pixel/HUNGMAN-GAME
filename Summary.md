# PROJECT SUMMARY
## HANGMAN GAME

### 1. Introduction
Hangman is a word guessing game developed using Python 3. The computer selects a secret word, and the player guesses the letters one by one.

The player gets six wrong guesses. The game finishes when the player guesses the complete word or makes six wrong guesses.

### 2. Objectives
- To understand Python programming.
- To practise strings and lists.
- To learn loops and conditional statements.
- To implement input validation.
- To develop logical thinking.

### 3. Working of the Project
1. The computer selects a secret word.
2. The program displays underscores for hidden letters.
3. The player enters a letter.
4. If the letter is correct, it appears in the word.
5. If the letter is incorrect, the wrong guess counter increases.
6. The game ends after winning or six wrong guesses.

### 4. Concepts Used
- Strings
- Lists
- For Loop
- While Loop
- If-Else Statements
- Random Module

### 5. Difficulties Faced

**Difficulty 1: Displaying hidden letters**

It was difficult to display guessed letters and hide the remaining letters. I solved this using a for loop and if-else conditions.

**Difficulty 2: Invalid Input**

I used input validation to prevent numbers and multiple characters from being accepted.

**Difficulty 3: Repeated Guesses**

I used a list to store previously guessed letters and prevent repeated attempts.

**Difficulty 4: Game Ending**

I used a wrong guess counter and while loop to stop the game after six wrong guesses.

### 6. Test Cases

**Test Case 1: Normal Input**

Input: p, y, t, h, o, n

Expected Result: You won!

Wrong Guesses: 0/6

**Test Case 2: Six Wrong Guesses**

Input: a, b, c, d, e, f

Expected Result: Game Over!

Wrong Guesses: 6/6

**Test Case 3: Invalid Input**

Input: 1, ab, p, p again

Expected Result: Invalid input messages and repeated guess warning.

**Test Case 4: Different Valid Scenario**

Input: p, z, y, x, t, h, o, n

Expected Result: You won!

Wrong Guesses: 2/6

### 7. Conclusion

Through this project, I learned how to use Python strings, lists, loops, conditions and random module.

I also improved my programming logic and problem-solving skills.
