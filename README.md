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


## How to use
Download the repository, navigate to the directory containing "translator.py" on the command line, and run

on Mac or Linux:

```
  python3 translator.py <your language> <language you want to translate to, or "all" for all languages> <word to translate>
```
on Windows:
```
  python translator.py <your language> <language you want to translate to, or "all" for all languages> <word to translate>
```

### Example
To translate "hi" from english to french:

![french translation of hi](https://github.com/v-richards/multilingual-online-translator/blob/master/screenshots/english%20french%20hi.png)

To translate "hi" into all available languages:
![hi translated to all available languages](https://github.com/v-richards/multilingual-online-translator/blob/master/screenshots/english%20all%20hi.png)

## Requirements
This program uses the requests and Beautiful Soup modules. You can install all necessary modules by running

on Mac or Linux:

```
pip3 install -r requirements.txt
```
on Windows:
```
pip install -r requirements.txt
```


## License
The source code is released under the MIT License.
