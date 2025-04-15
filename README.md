# pdf_translation

pdf파일에서 텍스트를 추출 해 openai api를 통해 번역하는 코드.

요청에 의해 제작된 것이므로 env파일로의 저장 및 활용은 고려되지 않았음.

Tkinter 패키지를 통한 GUI 기반 제작.

기본적으로 영->한 번역(해당 루트만 요청받음)과 정치외교학 번역 기반. 다른 언어(ex 불->영 등)나 다른 주제(경제학, 공학 등)이 필요하면 prompt와 translator.py 내의 파일 일부를 수정하여 얻을 수 있음.

April 2025 기준 최신 패키지들로 구성(ex tkinter 0.9.0). 

-------------------

Code that extracts text from a pdf file and translates it through the openai api.

Since it was created upon request, saving and utilizing it as an env file was not considered.

GUI-based creation using the Tkinter package.

Basically, English->Korean translation (only the corresponding route is requested) and political diplomacy translation. If you need other languages ​​(e.g. French->English, etc.) or other topics (economy, engineering, etc.), you can obtain them by modifying some of the files in the prompt and translator.py.

Composed of the latest packages as of April 2025 (e.g. tkinter 0.9.0).



