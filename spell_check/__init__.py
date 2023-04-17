"""
https://twitter.com/RealBenjizo/status/1646857541664555008

Day 39: Password Generator

Create a function called generate_password that generates any
length of password for the user. The password should have a random
mix of uppercase letters, lowercase letters, numbers, and
punctuation symbols. The function should ask the user how strong
they want the password to be. The user should pick from weak,
strong, or very strong. If the user picks "weak," the function
should generate a 5-character long password. If the user picks
"strong," generate an 8-character password, and if they pick "very
strong," generate a 12-character password.
"""
import nltk

SPELLCHECK_TRESHOLD = 0.5
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
