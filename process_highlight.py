# process_highlight.py
import docx, os
from highlight_reader.parse_highlight import parse_highlight
from highlight_reader.write_file import write_file

def file_options():
    dirlist = [i for i in os.listdir() if i.endswith('.docx')]
    for index, value in enumerate(dirlist):
        print(f'{index + 1}. {value}')

    user_input = int(input('What option do you want to choose?'))
    return os.path.splitext(dirlist[user_input - 1])[0] 

def process_highlight():
    filename = file_options()
    doc = docx.Document(filename + '.docx')
    text_list = parse_highlight(doc)
    write_file(text_list, filename + '_procesado.docx')


if __name__ == "__main__":
    # process_highlight()
    process_highlight()