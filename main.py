import json
import sys

def read_from_file(book_name="sorted_bg.json"):
    BG = None
    with open(book_name, 'r') as bg_file:
        BG = json.load(bg_file)
    return BG

def main():
    chapter_number = int(sys.argv[1])
    text_number = int(sys.argv[2])

    BG = read_from_file()
    
    chapters = [chapter for chapter in BG.keys()]

    requested_text = BG[chapters[chapter_number]][text_number]
    for content in requested_text.values():
        print(content, end='\n\n')
    

if __name__ == '__main__':
    main()
