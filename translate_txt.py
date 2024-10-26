from ai_api import send_to_ai

def translate(text):
    source = 'Japanese'
    target = 'English'
    translated_text = send_to_ai(text,source,target)
    return translated_text

def translate_file(input_file, output_file):
    file = open(input_file)
    content = file.read()
    file.close()
    paragraphs = content.split('\n\n')

    for item in paragraphs:
        if item.strip() not in ['','\n','\\s*']:
            translated_item = translate(item.strip())
            output = open(output_file, "a")
            output.write(translated_item + "\n\n")
            output.close()


translate_file("input.txt", "output.txt")
