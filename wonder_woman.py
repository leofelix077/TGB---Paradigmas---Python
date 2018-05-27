from numpy import random
import random as rand

def NUMBER_OF_TRIES():
    return 5

def SPACE():
    return ' '

def ADDITIONAL_LETTERS():
    return 1

def SCRAMBLE_WORD():
    return 2

def MSG_INPUT_DECODE():
    return 'Adivinhe a mensagem gerada'

def MSG_WIN():
    return "Você decodificou a mensagem"

def MSG_TRY_AGAIN():
    return "A mensagem não foi decodificada. Tente novamente"

def MSG_GAME_OVER():
    return "O exército alemão acaba de liberar o gás na Bélica"

def CHAR_PAST_Z():
    return '['
words = [
        "GUERRA",
        "ALEMANHA",
        "BELGICA", 
        "NAZI",
        "OCIDENTE",
        "DIANA",
        "ATAQUE",
        "MORTAL",
        "PRIMEIRA",
        "BOMBA"
        ]

word = ''
generated_word = ''

def increment_word(word):
    new_word = ''.join(chr(ord(letter)+1) for letter in word)
    new_word_as_letters = list(new_word)
    for character in range(0, len(new_word)):
        if (new_word[character] is CHAR_PAST_Z()):
            new_word_as_letters[character] = 'A'
    return ''.join(new_word_as_letters)

def add_letters():
    global word
    global add_letters_word
    global generated_word
    generated_word = word
    number_of_increments = random.randint(1,3)
    increments = 0
    while increments < number_of_increments:
        generated_word = increment_word(generated_word)
        increments += 1
    

def get_generated_word():
        add_letters()
        scramble_word()
        
def scramble_word():
    global generated_word
    global word
    generated_word = ''.join(rand.sample(generated_word, len(generated_word)))
            
def get_word():
    global word
    word = words[random.randint(0,NUMBER_OF_TRIES())]
        
def start_decode_game():
    tries = 0
    print(generated_word[:4])
    while tries < NUMBER_OF_TRIES():
        print(MSG_INPUT_DECODE())
        input_word = input()
        if input_word.upper() == word:
            print(MSG_WIN())
            return
        else:
            print(MSG_TRY_AGAIN())
        tries = tries + 1
    print(MSG_GAME_OVER())
        
    
#---------------------------------------------------
get_word()
get_generated_word()
start_decode_game()





