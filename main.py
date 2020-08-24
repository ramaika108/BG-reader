import json
import sys

def read_from_file(book_name="sorted_bg.json"):
    BG = None
    with open(book_name, 'r') as bg_file:
        BG = json.load(bg_file)
    return BG

def main():
    chapter_number = int(sys.argv[1])-1
    text_number = int(sys.argv[2])-1

    BG = read_from_file()
    
    chapters = [chapter for chapter in BG.keys()]

    requested_text = BG[chapters[chapter_number]][text_number]
    print(chapters[chapter_number], end='\n\n')
    for content in requested_text.values():
        print(content, end='\n\n')
    

if __name__ == '__main__':
    main()
