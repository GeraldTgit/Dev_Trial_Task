from bs4 import BeautifulSoup
from mtranslate import translate
import os

def translate_text(text, dest='hi'):
    try:
        return translate(text, 'hi')
    except Exception as e:
        print(f"Error translating text: {text}. Error message: {e}")
        return text

def translate_file(file_path):
    # Open the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the contents of the file
        contents = file.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(contents, 'html.parser')

    print(f"Starting translations for {file_path}...")

    # Translate all paragraph elements to Hindi
    print("Translating paragraphs...")
    for p in soup.find_all('p'):
        p.string = translate_text(p.get_text())

    # Translate all title elements to Hindi
    print("Translating titles...")
    for title in soup.find_all('title'):
        title.string = translate_text(title.get_text())

    # Translate all heading elements to Hindi
    print("Translating headings...")
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        heading.string = translate_text(heading.get_text())

    # Translate text from label of anchor elements to Hindi
    print("Translating anchors...")
    for a in soup.find_all('a'):
        label = a.get('label') or a.string
        if label:
            a.string = translate_text(label)

    # Translate text before the </a> element to Hindi
    print("Translating text before </a> elements...")
    for a in soup.find_all('a'):
        a.string = translate_text(a.get_text())

    # Translate text before the </span> element to Hindi
    print("Translating text before </span> elements...")
    for span in soup.find_all('span'):
        span.string = translate_text(span.get_text())

    # Translate text before the </strong> element to Hindi
    print("Translating text before </strong> elements...")
    for strong in soup.find_all('strong'):
        strong.string = translate_text(strong.get_text())

    # Translate text before the </button> element to Hindi
    print("Translating text before </button> elements...")
    for button in soup.find_all('button'):
        button.string = translate_text(button.get_text())

    # Translate text in the aria-placeholder attribute to Hindi
    print("Translating placeholder attributes...")
    for input_tag in soup.find_all('input'):
        if input_tag.has_attr('placeholder'):
            input_tag['placeholder'] = translate_text(input_tag['placeholder'])

    # Save the translated HTML file
    output_dir = os.path.join(os.path.dirname(file_path), 'Hindi')
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, os.path.basename(file_path))
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
        print(f"Translation for {file_path} complete. Saved to {output_file_path}.")

    # Check if there were any errors during translation
    if soup.find_all(text='Error translating text:'):
        print(f"Some translation errors occurred while translating {file_path}.")

