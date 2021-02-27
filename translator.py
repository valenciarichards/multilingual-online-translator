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
    "context.reverso.net" server using the "requests" module and return all translations and paired
    example sentences. Return None if there are no translations.
    """

    # Define the url and send the GET request to the server.
    # If no "User-Agent" is defined, the server responds with a 403 error.
    url = f"https://context.reverso.net/translation/{original_language}-{translated_language}/{text}"
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    except ConnectionError:
        print("Something wrong with your internet connection")
        sys.exit()

    # Parse the HTML if the response status code starts with 2(request accepted) or 3(redirection).
    if response:
        # Extract the translations.
        soup = BeautifulSoup(response.text, "html.parser")
        div_tag = soup.find_all("div", {"id": "translations-content"})[0]
        # Return None if there are no translations.
        if not div_tag:
            return None
        a_tags = div_tag.find_all("a")
        translations = [a_tag.text.strip() for a_tag in a_tags]
        # Extract the paired example sentences.
        span_tags = soup.find_all("span", {"class": "text"})
        example_sentences = strip_formatting([tag.text.strip() for tag in span_tags][34:-3])
        original_language_sentences = example_sentences[::2]
        translated_language_sentences = example_sentences[1::2]
        paired_sentences = list(zip(original_language_sentences, translated_language_sentences))
        return translations, paired_sentences


def print_and_save_all_translations(original_language, text) -> bool:
    """Print translations in all languages and save to a file.

    Accept an original language and a string of text as parameters, translate the text into all available languages,
    print the first translation and example sentence, and save it to a .txt file named after the text being translated.
    Return False and print an error message if the get_translations function returns None. Return True if successful.
    """

    # Create a .txt file
    file = open(f"{text}.txt", "w", encoding="utf-8")

    # Translate the text into each language, print the first result and save to the file.
    for language in languages:
        if language != original_language:
            # Return None and print an error message if the get_translation function returns None.
            try:
                translations, paired_sentences = get_translations(original_language, language, text)
            except TypeError:
                return False
            try:
                print(f"{language.capitalize()} Translation:\n{translations[0]}\n")
                file.write(f"{language.capitalize()} Translation:\n{translations[0]}\n")
                print(f"{language.capitalize()} Example:\n{paired_sentences[0][0]}\n{paired_sentences[0][1]}\n")
                file.write(f"{language.capitalize()} Example:\n{paired_sentences[0][0]}\n{paired_sentences[0][1]}\n\n")
            except IndexError:
                pass

    file.close()
    return True


def strip_formatting(original_list: list) -> list:
    """Accept a list of strings as a parameter, remove certain punctuation characters, and return the edited list."""

    punctuation = ["[", "]", "'", '"', ","]
    stripped_list = original_list
    for text in stripped_list:
        for char in punctuation:
            text.replace(char, "")
    return stripped_list


def show_available_languages():
    print("Available languages:")
    for language in languages:
        print(f"- {language.capitalize()}")


def main():
    # Accept arguments from the command line, check that the correct number of arguments are provided, and assign them
    # to original_language, translated_language and text
    args = sys.argv
    if len(args) == 4:
        original_language, translated_language, text = [arg.lower() for arg in args[1:]]
    else:
        if sys.platform.startswith("win32"):
            print("Usage: python translator.py <your language> <language you want to translate to, or \"all\" for "
                  "all languages> <word to translate>")
        else:
            print("Usage: python3 translator.py <your language> <language you want to translate to, or \"all\" for "
                  "all languages> <word to translate>")
        sys.exit()

    # If all languages are selected, print the first translation and example sentence and save the output to a file.
    if translated_language == "all":
        request_fulfilled = print_and_save_all_translations(original_language, text)
        if not request_fulfilled:
            print(f"Sorry, unable to find {text}")
            sys.exit()
    # Otherwise, print the first 5 translations and example sentences in the selected language.
    elif translated_language in languages:
        try:
            translations, paired_sentences = get_translations(original_language, translated_language, text)
        except TypeError:
            print(f"Sorry, unable to find {text}")
            sys.exit()
        print("\nContext examples:\n")
        print(f"{translated_language.capitalize()} Translations:\n" + "\n".join(translations[:5]))
        print(f"\n{translated_language.capitalize()} Examples:")
        for original_language_sentence, translated_language_sentence in paired_sentences[:5]:
            print(f"{original_language_sentence}:\n{translated_language_sentence}\n")
    else:
        print(f"Sorry, the program doesn't support {translated_language}.")
        show_available_languages()


if __name__ == "__main__":
    main()
    sys.exit()
