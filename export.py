import argparse
import html
import json
import os
import re
import zipfile


def wrap_math_expressions(content):
    # Wrap LaTeX math expressions with $$
    return re.sub(r'\\\[([\s\S]+?)\\\]', r'$$\1$$', content)


def clean_content(content, user=False):
    if isinstance(content, str):
        # Replace only H1 headings (lines starting with #)
        content = content.replace('---', '\n').replace('--', '<br>').replace('==', 'equal equal')
        if user:
            content = content.replace('```', '').replace('<', '').replace('>', '').replace('\n', '\n<br>')
            # lines = content.split('\n')
            # wrapped_lines = [f"<p><font color='blue'>{line}</font></p>" for line in lines]
            # content = "\n".join(wrapped_lines)
        else:
            content = html.unescape(content)
        content = re.sub(r'^# ', 'H1 # ', content, flags=re.MULTILINE)
        content = wrap_math_expressions(content)
    return content


def format_conversation_to_md(conversation):
    messages = []
    current_node = conversation["current_node"]

    while current_node is not None:
        node = conversation["mapping"][current_node]
        message = node["message"]
        if message is not None:
            author = message["author"]["role"]
            if 'parts' in message["content"]:
                content = message["content"]["parts"][0]
            else:
                content = json.dumps(message["content"], ensure_ascii=False)

            if author == "user":
                content = clean_content(content, user=True)
                messages.append(f"**Author**: User\n\n<font color='blue'>{content}</font>")
            else:
                content = clean_content(content, user=False)
                messages.append(f"**Author**: {author.upper()}\n\n{content}")
        current_node = node["parent"]

    messages.reverse()
    return "\n\n---\n\n".join(messages)


def save_conversation_as_md(conversation, index, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    title = conversation["title"].replace('/', '_').replace('#',
                                                            '')  # Replace '/' and '#' in titles to avoid path issues
    filename = f"{index}. {title}.md"
    md_content = format_conversation_to_md(conversation)

    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
        file.write(md_content)


def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Check if it is a file and not a hidden file
        if os.path.isfile(file_path) and not filename.startswith('.'):
            os.remove(file_path)


def unzip_conversations(zip_path, extract_to_folder):
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)  # Extract to the specified folder or to current directory if folder empty


parser = argparse.ArgumentParser(description="Extract and process ChatGPT conversations from a zip file.")
parser.add_argument("zip_file", default='2024-01-27 JSON.zip', help="Name of the zip file containing the conversations.")
args = parser.parse_args()
zip_path = args.zip_file
extracted_folder = 'extracted'
save_folder = "conversations_md"
unzip_conversations(zip_path, extracted_folder)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
delete_files_in_folder(save_folder)

conversations_json_path = os.path.join(extracted_folder, "conversations.json")
with open(conversations_json_path, "r", encoding='utf-8') as file:
    conversations = json.load(file)
for i, conversation in enumerate(conversations):
    save_conversation_as_md(conversation, i, save_folder)
