import random
words = ["artificial", "intelligence", "machine", "robot", "security"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []
print("Welcome to Hangman!")
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(" Wrong!")
        attempts -= 1

if "_" not in guessed_word:
    print("\n You won!")
    print("The word was:", word)
else:
    print("\n Game over!")
    print("The word was:", word)