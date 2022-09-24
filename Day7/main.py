import random
from turtle import position
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

# choosing a random word from the list
chosen_word = random.choice(word_list)
# print(f"hint: {chosen_word}")
# Length of the randomly chosen word
len_word = len(chosen_word)
# Displaying _ for letters
display = []

for letter in range(len_word):
    display += "_"
print(display)

lives = 6
end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already guessed this letter.")

    for position in range(len_word):
        # print(position)
        letter = chosen_word[position]

        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(
            f"You guessed {guess},  it is not in the word, You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True

            print(f"You loose, the word is: {chosen_word}")
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You win")
        end_of_game == True

    print(stages[lives])
