import sys
import os
import nltk

from deepmultilingualpunctuation import PunctuationModel

nltk.download('punkt')

def get_filename(file_path):
  file_name, _ = os.path.basename(file_path).split('.')
  return file_name

def get_sentences(input_path, output_path):
    with open(input_path, 'r') as file:
        text = file.read()

    model = PunctuationModel()
    punctuated_text = model.restore_punctuation(text)
        
    sentences = nltk.sent_tokenize(punctuated_text)
    
    with open(output_path, 'w') as output_file:
        for sentence in sentences:
            capitalized_sentence = sentence.capitalize()
            output_file.write(f"- {capitalized_sentence}\n")

def main(args):
    input_path = args[0] 
    output_dir = args[1]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = get_filename(input_path)
    output_path = f"{output_dir}/{file_name}.md"

    get_sentences(input_path, output_path)

if __name__ == "__main__":
    main(sys.argv[1:])