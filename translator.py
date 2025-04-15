import openai
import os
import time
import tkinter as tk
from tkinter import simpledialog

def robust_translate_text_segment(segment, target_lang="한국어", model="gpt-3.5-turbo", max_retries=5):
    prompt = f"다음 텍스트를 {target_lang}로 이전 번역을 고려해서 번역해줘:\n\n{segment}"
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "너는 일류 번역가이자 다개국어, 정치학학 전문가야."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=1024
            )
            return response['choices'][0]['message']['content'].strip()
        except openai.error.RateLimitError:
            wait_time = 2 ** (attempt + 1)  # 2, 4, 8, ... 초
            print(f"RateLimit 에러 발생. {wait_time}초 후 재시도합니다... (시도 {attempt+1}/{max_retries})")
            time.sleep(wait_time)
    raise Exception("최대 재시도 횟수 초과. 잠시 후 다시 시도해주세요.")

def translate_full_text(full_text, target_lang="한국어", model="gpt-3.5-turbo"):
    """
    전체 텍스트를 "\n\n" 단위로 분할하여 각 구간을 번역 후 합쳐서 반환.
    각 구간 번역 시 robust로 오류 발생 시 재시도.
    """
    segments = full_text.split("\n\n")
    translated_segments = []
    
    for idx, segment in enumerate(segments, 1):
        segment = segment.strip()
        if segment:
            print(f"번역 중: 섹션 {idx}")
            translation = robust_translate_text_segment(segment, target_lang=target_lang, model=model)
            translated_segments.append(translation)
    
    return "\n\n".join(translated_segments)

def set_api_key(master = None):
    root = tk.Tk()
    root.withdraw()
    api_key = simpledialog.askstring("API Key 입력", "OpenAI API Key를 입력하세요:", parent=master)
    root.destroy()
    openai.api_key = api_key