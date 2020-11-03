# Multilingual Online Translator.

# Import the requests and BeautifulSoup modules.
import requests
from bs4 import BeautifulSoup


def get_translations(original_language, translated_language, text):
    """This function takes an original language, translated language, and a text string as parameters,
    and prints the first 5 translations and example sentences."""

    # Define the url and send the GET request to the server.
    # If no "User-Agent" is defined, the server responds with a 403 error.
    url = f"https://context.reverso.net/translation/{original_language}-{translated_language}/{text}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    print(response.status_code)

    # Parse the HTML if the response status code starts with 2(request accepted) or 3(redirection).
    if response:
        # Extract and print the first 5 translations.
        soup = BeautifulSoup(response.text, "html.parser")
        div_tag = soup.find_all("div", {"id": "translations-content"})[0]
        a_tags = div_tag.find_all("a")
        translations = [a_tag.text.strip() for a_tag in a_tags]
        first_5_translations = translations[:5]
        print("\nContext examples:\n")
        print(f"{translated_language.capitalize()} Translations:")
        print("\n".join(first_5_translations))
        # Extract and print the first 5 example sentences.
        span_tags = soup.find_all("span", {"class": "text"})
        example_sentences = strip_formatting([tag.text.strip() for tag in span_tags][34:-3])
        original_language_sentences = example_sentences[::2]
        translated_language_sentences = example_sentences[1::2]
        first_5_sentences = list(zip(original_language_sentences, translated_language_sentences))[:5]
        print(f"\n{translated_language.capitalize()} Examples:")
        for original_language_sentence, translated_language_sentence in first_5_sentences:
            print(f"{original_language_sentence}:\n{translated_language_sentence}\n")


def strip_formatting(original_list: list) -> list:
    """This function takes a list of strings as parameters, strips its punctuation,
    and returns a list of stripped strings."""
    punctuation = ["[", "]", "'", '"', ","]
    stripped_list = original_list
    for text in stripped_list:
        for char in punctuation:
            text.replace(char, "")
    return stripped_list


def main():
    language = input('Type "en" if you want to translate from French into English, or "fr" if you want to '
                     'translate from English into French:\n').lower()
    text = input("Type the word you want to translate:\n").lower()
    print(f'You chose "{language}" as the to_language to translate "{text}" to.')
    if language == "en":
        to_language = "english"
        from_language = "french"
    else:
        to_language = "french"
        from_language = "english"
    get_translations(from_language, to_language, text)


if __name__ == "__main__":
    main()
