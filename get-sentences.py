import sys
import nltk

from deepmultilingualpunctuation import PunctuationModel

nltk.download('punkt')

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
    output_path = args[1]

    get_sentences(input_path, output_path)

if __name__ == "__main__":
    main(sys.argv[1:])