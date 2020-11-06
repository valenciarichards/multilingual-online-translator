# Multilingual Online Translator.

# Import the requests, sys and BeautifulSoup modules.
import requests
import sys
from bs4 import BeautifulSoup

languages = [
    "arabic",
    "german",
    "english",
    "spanish",
    "french",
    "hebrew",
    "japanese",
    "dutch",
    "polish",
    "portuguese",
    "romanian",
    "russian",
    "turkish",
    ]


def get_translations(original_language, translated_language, text):
    """Get translations and example sentences from "context.reverso.net".

    Accept an original language, translated language, and a text string as parameters, query the
    "context.reverso.net" server using the "requests" module and return all translations and paired example sentences.
    """

    # Define the url and send the GET request to the server.
    # If no "User-Agent" is defined, the server responds with a 403 error.
    url = f"https://context.reverso.net/translation/{original_language}-{translated_language}/{text}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    # Parse the HTML if the response status code starts with 2(request accepted) or 3(redirection).
    if response:
        # Extract the translations.
        soup = BeautifulSoup(response.text, "html.parser")
        div_tag = soup.find_all("div", {"id": "translations-content"})[0]
        a_tags = div_tag.find_all("a")
        translations = [a_tag.text.strip() for a_tag in a_tags]
        # Extract the paired example sentences.
        span_tags = soup.find_all("span", {"class": "text"})
        example_sentences = strip_formatting([tag.text.strip() for tag in span_tags][34:-3])
        original_language_sentences = example_sentences[::2]
        translated_language_sentences = example_sentences[1::2]
        paired_sentences = list(zip(original_language_sentences, translated_language_sentences))
        return translations, paired_sentences


def print_all_translations(original_language, text):
    """Print translations in all languages and save to a file.

    Accept an original language and a string of text as parameters, translate the text into all available languages,
    print the first translation and example sentence, and save it to a .txt file named after the text being translated.
    """

    # Create a .txt file
    file = open(f"{text}.txt", "w", encoding="utf-8")

    # Translate the text into each language, print the first result and save to the file.
    for language in languages:
        if language != original_language:
            translations, paired_sentences = get_translations(original_language, language, text)
            print(f"{language.capitalize()} Translations:\n{translations[0][0]}\n{translations[0][1]}\n")
            file.write(f"{language.capitalize()} Translations:\n{translations[0][0]}\n{translations[0][1]}\n\n")
            print(f"{language.capitalize()} Example:\n{paired_sentences[0][0]}\n{paired_sentences[0][1]}\n")
            file.write(f"{language.capitalize()} Example:\n{paired_sentences[0][0]}\n{paired_sentences[0][1]}\n\n")

    file.close()


def strip_formatting(original_list: list) -> list:
    """Accept a list of strings as a parameter, remove certain punctuation characters, and return the edited list."""

    punctuation = ["[", "]", "'", '"', ","]
    stripped_list = original_list
    for text in stripped_list:
        for char in punctuation:
            text.replace(char, "")
    return stripped_list


def main():
    # Accept arguments from the command line and assign them to original_language, translated_language and text
    args = sys.argv
    original_language, translated_language, text = [arg.lower() for arg in args[1:]]

    # If all languages are selected, print the first translation and example sentence and save the output to a file.
    if translated_language == "all":
        print_all_translations(original_language, text)
    # Otherwise, print the first 5 translations and example sentences in the selected language.
    elif translated_language in languages:
        translations, paired_sentences = get_translations(original_language, translated_language, text)
        print("\nContext examples:\n")
        print(f"{translated_language.capitalize()} Translations:\n" + "\n".join(translations[:5]))
        print(f"\n{translated_language.capitalize()} Examples:")
        for original_language_sentence, translated_language_sentence in paired_sentences[:5]:
            print(f"{original_language_sentence}:\n{translated_language_sentence}\n")


if __name__ == "__main__":
    main()
