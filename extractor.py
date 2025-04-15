import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, simpledialog
import os
import re

def reposition_page_markers(text: str) -> str:

    parts = re.split(r"(\n\n\[page \d+\])", text)
    if len(parts) <= 1:
        return text

    new_parts = [parts[0]]
    for i in range(1, len(parts), 2):
        marker = parts[i]  
        content = parts[i+1] if (i+1) < len(parts) else ""
        content = content.lstrip()  

        prev_text = new_parts[-1]
        dot_index = prev_text.rfind(".")
        if dot_index != -1:
            prev_text = prev_text[:dot_index+1] + marker + " " + prev_text[dot_index+1:]
            new_parts[-1] = prev_text
        else:
            new_parts[-1] = new_parts[-1].rstrip() + marker
        new_parts.append(content)
    return "".join(new_parts)

def extractor(doc, name, detect_words):
    new_txt = ''
    tags = ''
    default_detect_words = ['International Security ', 'Foreign Affairs', 'Henry E. Hale is', 
                            'Michael McFaul is', 'Victor D. Cha is', 'Eric Heginbotham is ']
    if detect_words:
        detect_words = default_detect_words + detect_words
    else:
        detect_words = default_detect_words

    for text_num in range(len(doc)):
        appearance = 0
        new_txt += f'[page {text_num+1}]'
        tags += f'[page {text_num+1}]'
        temp_txt = ''
        temp_tags = ''
        for phrase in doc[text_num].get_text().split('\n'):
            phrase_detect = re.sub(r'[^\w\s]', '', phrase)
            if (text_num == 0) and ('1. ' in phrase):
                appearance = 1
                temp_tags += phrase + ' \n'
            elif ((text_num % 2 == 0) and (phrase_detect == name)) or any(sub in phrase for sub in detect_words):
                appearance = 1
                temp_tags += phrase + ' \n'
            elif appearance == 1:
                temp_tags += phrase + ' \n'
            else:
                temp_txt += phrase + ' \n'

        temp_txt = re.sub(r'\.(\d+)', '.', temp_txt)
        temp_txt = temp_txt.replace('- \n', '').replace('.\n', '마침표') \
                           .replace('. \n', '마침표').replace('\n\n', '|space|').replace('\n', '')
        temp_txt = temp_txt.replace('마침표', '.\n').replace('|space|', '\n\n')
        temp_tags = temp_tags.replace('- \n', '').replace('.\n', '마침표') \
                             .replace('. \n', '마침표').replace('\n\n', '|space|').replace('\n', '')
        temp_tags = temp_tags.replace('마침표', '.\n').replace('|space|', '\n\n')
        new_txt += temp_txt + '\n\n'
        tags += temp_tags + '\n\n'
    new_txt = reposition_page_markers(new_txt)
    return new_txt, tags

def select_pdf_file(master = None):
    """
    PDF 파일 선택 후 파일 경로 반환.
    """
    if master is None:
        root = tk.Tk()
        root.withdraw()
    else:
        root = master
    file_path = filedialog.askopenfilename(
        title="PDF 파일 선택",
        filetypes=[("PDF Files", "*.pdf")],
        parent=root
    )
    return file_path

def get_scholar_keywords(master = None):
    if master is None:
        root = tk.Tk()
        root.withdraw()
    else:
        root = master
    scholar_input = simpledialog.askstring(
        "학자 키워드 입력",
        "PDF 첫 페이지의 학자 검출을 위해\n원하는 학자 키워드를 쉼표(,)로 구분하여 입력하세요.\n(입력하지 않으면 건너뜁니다.)",
        parent=root
    )
    if scholar_input:
        detect_words = [word.strip() for word in scholar_input.split(',') if word.strip()]
    else:
        detect_words = []
    return detect_words

def extract_text_from_pdf(file_path, detect_words, master=None):
    """
    PDF 파일을 열고 파일 이름(확장자 제외)을 기준으로 extractor를 실행하여
    텍스트와 태그 데이터 반환.
    """
    if not file_path:
        print("파일 선택되지 않음음.")
        return None, None, None

    filename_wo_ext = os.path.splitext(os.path.basename(file_path))[0]
    doc = fitz.open(file_path)
    new_txt, tags = extractor(doc, filename_wo_ext, detect_words)
    doc.close()
    return new_txt, tags, filename_wo_ext

if __name__ == "__main__":
    file_path = select_pdf_file()

    detect_words = get_scholar_keywords()
    if detect_words:
        print("입력된 학자 키워드:", detect_words)
    else:
        print("학자 키워드가 입력되지 않았습니다. 해당 검출 기능을 건너뜁니다.")

    new_txt, tags, fname = extract_text_from_pdf(file_path, detect_words)
    if new_txt is not None:
        with open(f"{fname}_text.txt", "w", encoding="utf-8") as f:
            f.write(new_txt)
        with open(f"{fname}_tags.txt", "w", encoding="utf-8") as f:
            f.write(tags)
        print("저장 완료:", fname + "_text.txt", fname + "_tags.txt")