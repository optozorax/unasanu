import os
import json
import xml.etree.ElementTree as ET
import re

def update_svg_with_translations(input_file, output_file, translations):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    translation_index = 0
    for elem in root.iter():
        if elem.text and elem.text.strip():
            text = elem.text.strip()
            if not text.startswith("@font-face") and re.search(r'[a-zA-Zа-яА-Я]', text):
                if translation_index < len(translations):
                    elem.text = translations[translation_index]
                    translation_index += 1
    
    tree.write(output_file, encoding='unicode', xml_declaration=True)

def process_translations(claude_response_file):
    with open(claude_response_file, 'r', encoding='utf-8') as f:
        response = f.read()

    # Extract JSON from Claude's response
    json_start = response.find('{')
    json_end = response.rfind('}') + 1
    translations_json = response[json_start:json_end]
    
    translations = json.loads(translations_json)
    
    en_folder = 'en'
    target_languages = ['es', 'cn', 'hi']
    
    for lang in target_languages:
        os.makedirs(lang, exist_ok=True)
    
    for filename in os.listdir(en_folder):
        if filename.endswith('.svg'):
            file_base = os.path.splitext(filename)[0]
            
            if file_base in translations:
                input_file = os.path.join(en_folder, filename)
                
                for lang in target_languages:
                    output_file = os.path.join(lang, filename)
                    update_svg_with_translations(input_file, output_file, translations[file_base][lang])
            else:
                print(f"Warning: No translations found for {filename}")

process_translations('claude_response.txt')