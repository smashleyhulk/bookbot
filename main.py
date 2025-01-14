
def main():

    book_path = "books/frankenstein.txt"

    print(f"--- Begin report of {book_path} ---")
    
    with open(book_path) as f:
        content = f.read()

    word_count = wordCount(content)
    print(f"{word_count} words found in the document\n")

    character_count = countCharacters(content)


    alphabet = [chr(i) for i in range(97,123)]
    for letter in alphabet:
        print(f"The '{letter}' character was found {character_count[letter]} times")

def wordCount(content):

    count = 0
    words = content.split()
    for word in words:
        count += 1
    return count

def countCharacters(content):

    characters = {}
    alphabet = [chr(i) for i in range(97,123)]
    for letter in alphabet:
        characters[letter] = 0


    alphabet_content = ''.join(filter(str.isalpha, content))
    lowered_content = alphabet_content.lower()

    for char in lowered_content:
        characters[char] += 1

    return characters
    
    
    








main()