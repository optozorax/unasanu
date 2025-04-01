import os
import xml.etree.ElementTree as ET
import json
import re

def extract_text_from_svg(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    texts = []
    for elem in root.iter():
        if elem.text and elem.text.strip():
            text = elem.text.strip()
            if not text.startswith("@font-face") and re.search(r'[a-zA-Zа-яА-Я]', text):
                texts.append(text)
    return texts

def prepare_prompt():
    ru_folder = 'ru'
    en_folder = 'en'
    target_languages = ['es', 'cn', 'hi']
    
    all_texts = {}
    
    for filename in os.listdir(en_folder):
        if filename.endswith('.svg'):
            file_base = os.path.splitext(filename)[0]
            
            en_file = os.path.join(en_folder, filename)
            ru_file = os.path.join(ru_folder, filename)
            
            en_text = extract_text_from_svg(en_file)
            ru_text = extract_text_from_svg(ru_file)
            
            all_texts[file_base] = {
                'en': en_text,
                'ru': ru_text
            }
    
    prompt = f"""I need you to translate the following texts from English and Russian to Spanish (es), Chinese (cn), and Hindi (hi). 
The texts are from SVG files, and each file may contain multiple text elements.
Please provide the translations in a JSON format where the keys are the file names (without extension) and the values are objects containing the translations for each language.

Here are the texts to translate:

{json.dumps(all_texts, indent=2, ensure_ascii=False)}

Please provide the translations in the following JSON format:

{{
  "file_name": {{
    "es": ["Spanish translation 1", "Spanish translation 2", ...],
    "cn": ["Chinese translation 1", "Chinese translation 2", ...],
    "hi": ["Hindi translation 1", "Hindi translation 2", ...]
  }},
  ...
}}

Ensure that the order of translations matches the order of the original texts in English and Russian.
If a text is empty or the same as another, please include it in the translation as is.
"""
    
    with open('translation_prompt.txt', 'w', encoding='utf-8') as f:
        f.write(prompt)


prepare_prompt()
