import openai
import json
import os

openai.api_key = os.getenv('OPENAI_API')

# Custom prompt for proofreading
prompt = (
    "Выступи в роле корректора текста. Корректор исправляет: орфографические, пунктуационные ошибки,"
    " нарушений правил набора и неестественный порядок слов. Всегда используй букву Ë там где она присутствует."
    " Отредактируй только русский текст, не вмешивайся в оригинальную разметку, которая состоит из markdown и jinja шаблонов."
)

# Read the content of the input file
input_file_path = 'index.md'
output_file_path = 'proofread_output.md'

# Clear the output file if it exists
if os.path.exists(output_file_path):
    os.remove(output_file_path)

with open(input_file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Split text into parts of 3K symbols by paragraphs or words if needed
def split_text(text, max_length):
    parts = []
    current_part = ""
    for paragraph in text.split('\n\n'):
        if len(current_part) + len(paragraph) <= max_length:
            current_part += paragraph + '\n\n'
        else:
            parts.append(current_part.strip())
            current_part = paragraph + '\n\n'
    if current_part:
        parts.append(current_part.strip())
    return parts

# Proofread each part using OpenAI API
def proofread_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты полезный ассистент."},
            {"role": "user", "content": prompt + "\n\n```" + text + "```"},
        ],
    )
    return response

# Split the text and proofread each part
parts = split_text(text, max_length=2000)
proofread_parts = []

for idx, part in enumerate(parts):
    print(f"Proofreading part {idx+1}/{len(parts)}")
    response = proofread_text(part)
    proofread_part = response.choices[0].message.content
    proofread_parts.append(proofread_part)
    
    # Log the response information
    response_info = {
        "usage": response.usage
    }
    print("Response Info:", json.dumps(response_info))

    # Write the proofread part into the output file
    with open(output_file_path, 'a', encoding='utf-8') as f:
        f.write('\n\n' + proofread_part)

print("Proofreading completed. Result saved in", output_file_path)
