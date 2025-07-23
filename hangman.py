import random
from colorama import init, Fore, Style

# ✅ Initialize colorama
init(autoreset=True)

# 🌟 Word list with hints
word_bank = {
    'apple': 'A crunchy fruit often associated with teachers 🍏',
    'banana': 'A yellow fruit loved by monkeys 🍌',
    'grapes': 'Tiny purple or green fruits often found in bunches 🍇',
    'orange': 'Citrusy fruit and also a color 🍊',
    'mango': 'King of fruits, juicy and tropical 🥭'
}

# 🎯 Choose a secret word and its hint
secret_word, hint = random.choice(list(word_bank.items()))
display_word = ['_' for _ in secret_word]
guessed_letters = set()
max_attempts = 6
incorrect_guesses = 0
score = 0  # 🧮 Start with zero score

# 🎮 Game start
print(Fore.CYAN + Style.BRIGHT + "🌟 Welcome to Hangman Deluxe!")
print("Your mission: Guess the word one letter at a time.\n")
print(Fore.YELLOW + f"💡 Hint: {hint}\n")

# 🔁 Main game loop
while incorrect_guesses < max_attempts and '_' in display_word:
    print("Word:", Fore.GREEN + ' '.join(display_word))
    print(Fore.RED + f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    print(Fore.MAGENTA + f"Score: {score}")
    
    guess = input(Fore.BLUE + "🔠 Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(Fore.RED + "⚠️ Please enter a single alphabetical character.\n")
        continue

    if guess in guessed_letters:
        print(Fore.YELLOW + "🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print(Fore.GREEN + "✅ Correct!\n")
        score += 10
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        print(Fore.RED + "❌ Incorrect guess.\n")
        incorrect_guesses += 1
        score -= 5

# 🏁 Game outcome
if '_' not in display_word:
    print(Fore.GREEN + f"\n🎉 You won! The word was '{secret_word}'.")
    print(Fore.CYAN + f"🏆 Final Score: {score}")
else:
    print(Fore.RED + f"\n💀 Game over. The word was '{secret_word}'.")
    print(Fore.CYAN + f"🏆 Final Score: {score}")
