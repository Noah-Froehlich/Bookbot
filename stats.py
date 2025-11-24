

def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def get_num_words(book):
    text = book.split()
    words_count = len(text)
    return words_count

def get_character_count(text):
    stats = {}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character in stats:
            stats[character] += 1
        else:
            stats[character] = 1
    return stats

def sort_on(item):
    return item["num"]

def sort_dic(dic):
    counts = []
    for i in dic:
        temp = {}
        temp["char"] = i
        temp["num"] = dic[i]
        counts.append(temp)
    counts.sort(reverse=True,key=sort_on)
    return counts
