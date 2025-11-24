import sys
from stats import get_num_words,get_book_text,get_character_count,sort_dic


def main():
    
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    book = get_book_text(path_to_book)
    
    count = get_num_words(book)
    stats = get_character_count(book)
    sorted_stats = sort_dic(stats)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sorted_stats:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
        else:
            continue
    print("============= END ===============")

main()