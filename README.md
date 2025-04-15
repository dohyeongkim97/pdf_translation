# pdf_translation

pdf파일에서 텍스트를 추출 해 openai api를 통해 번역하는 코드.

요청에 의해 제작된 것이므로 api 키 파일의 env파일로의 저장 및 활용은 고려되지 않았음.

Tkinter 패키지를 통한 GUI 기반 제작.

기본적으로 영->한 번역(해당 루트만 요청받음)과 정치외교학 번역 기반. 다른 언어(ex 불->영 등)나 다른 주제(경제학, 공학 등)이 필요하면 prompt와 translator.py 내의 파일 일부를 수정하여 얻을 수 있음.

April 2025 기준 최신 패키지들로 구성(ex tkinter 0.9.0). 


api 키 입력 -> 요금 산정 -> pdf 파일에서 주석을 제거하고 본문만 추출(주석 번역은 설정하지 않았음) -> 모델 설정(gpt 3.5 turbo | gpt 4) -> 번역 후 txt로 저장.

env파일 사용으로 변형하고 싶다면 translator.py set_api_key에서 설정.

detect words 세팅:
extractor.py의 extractor 함수 중, detect words는 사용한 테스트파일의 첫장 주석에 가장 먼저 등장하는 학자. 첫장은 주석과 본문 분리가 잘 되지 않았음. 

detect word를 추가하는 창에 넣어야 할 것: 첫장 주석에 처음 등장하는 학자, 학술지 이름(e.g. Foreign Affairs 등), 논문 혹은 기고문의 부제




차후 계산복잡도를 줄이고 더 정교한 전처리를 위해 상세 부분 변경 예정.

패키지: tkinter, threading, tiktoken, re, openai, fitz(pymupdf)

## pyinstaller 사용으로 exe 파일 변환 시, tiktoken파일을 함께 hidden import 해 주어야 에러가 생기지 않음.

-------------------

Code that extracts text from a pdf file and translates it through the openai api.

Since it was created upon request, saving and utilizing of API key codes as an env file was not considered.

GUI-based creation using the Tkinter package.

Basically, English->Korean translation (only the corresponding route is requested) and political diplomacy translation. If you need other languages ​​(e.g. French->English, etc.) or other topics (economy, engineering, etc.), you can obtain them by modifying some of the files in the prompt and translator.py.

Composed of the latest packages as of April 2025 (e.g. tkinter 0.9.0).



Enter api key -> Calculate fee -> Remove comments from pdf file and extract only text (not set to translate comments) -> Set model (gpt 3.5 turbo | gpt 4) -> Save as txt after translation.

If you want to transform using env file, set in translator.py set_api_key.

Among the extractor functions in extractor.py, detect words is the scholar who first appears in the first page comment of the test file used. The first page does not have a good separation between the comment and the main text. When using it, if a window for adding detect words appears, enter the scholar who first appears in the first page comment.

## When converting exe file using pyinstaller, you need to import tkinter file together with hidden import to avoid error.

pkg: tkinter, threading, tiktoken, re, openai, fitz(pymupdf)
