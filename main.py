import sys
from stats import count_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(path):
	with open(path) as f:
		return f.read()


def main():
	if len (sys.argv) != 2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else: 
		book_path = sys.argv[1]
		text = get_book_text(book_path)
		print ("============ BOOKBOT ============")
		print ("Analyzing book found at books/frankenstein.txt...")
		print ("----------- Word Count ----------")
		num_words = count_words(text)
		print (f"Found {num_words} total words")
		print ("--------- Character Count -------")
		chars = get_chars_dict(text)
		sorted_chars = chars_dict_to_sorted_list(chars)

	for char_dict in sorted_chars:
		if char_dict["char"].isalpha():
			print(f"{char_dict['char']}: {char_dict['num']}")

	print ("============= END ===============")

main()
