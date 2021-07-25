# Multilingual Online Translator

This app translates words into one or all of the following languages:
- Arabic
- German
- English
- Spanish
- French
- Hebrew
- Japanese
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Turkish

If a specific language is selected, the program prints the first 5 translations of the word as well as 5 sentences including the word. 
If "all" is selected, the program prints one translation and sentence from each of the other languages and saves the output to a file.

This program was built as a JetBrains Academy project.


## Installation

Clone the repository
```
git clone git@github.com:valenciarichards/multilingual-online-translator.git
```

This program uses the requests and Beautiful Soup modules. You can install all necessary modules by running

```
pip install -r requirements.txt
```

## Usage

Navigate to the directory containing "translator.py" on the command line, and run

```
  python translator.py <your language> <language you want to translate to, or "all" for all languages> <word to translate>
```

### Example
To translate "hi" from english to french:

![french translation of hi](https://github.com/v-richards/multilingual-online-translator/blob/master/screenshots/english%20french%20hi.png)

To translate "hi" into all available languages:
![hi translated to all available languages](https://github.com/v-richards/multilingual-online-translator/blob/master/screenshots/english%20all%20hi.png)


## License
The source code is released under the MIT License.

## Acknowledgements
Translations obtained from [context.reverso.net/translation](https://context.reverso.net/translation/)
