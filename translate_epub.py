import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from ai_api import send_to_ai

def translate(text):
    source = 'Japanese'
    target = 'English'
    translated_text = send_to_ai(text,source,target)
    return translated_text

def translate_file(input_file, output_file):
    book = epub.read_epub(input_file)
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        html_content = item.get_content().decode('utf-8')
        html_content = html_content.replace('\\n','\n')

        soup = BeautifulSoup(html_content, 'html.parser')

        for tag in soup.find_all(string=True):
            if tag.parent.name not in ['title','p','div','strong','span','i','em','li','a','h']:
                    origin_text = str(tag.string.strip())
                    tag.string.replace_with(origin_text)
            elif tag.string.strip() not in ['','\n','\\s*']:
                print(tag.string.strip())
                translated_text = translate(tag.string.strip())
                tag.string.replace_with(translated_text.replace('\n', '<br />'))
                

        translated_html = soup.prettify(formatter=None)
        
        # Ugly implementation of deleting duplicated "xml version='1.0' encoding='utf-8'?" and "html"
        lines = translated_html.splitlines()
        remaining_lines = lines[2:]
        translated_html = '\n'.join(remaining_lines)

        item.set_content(translated_html)

    epub.write_epub(output_file, book)

translate_file("input.epub", "output.epub")
