from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Supported languages
languages = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-CN": "Simplified Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi",
    "bn": "Bengali",
    "pa": "Punjabi",
    "ur": "Urdu",
    "id": "Indonesian",
    "ms": "Malay",
    "sw": "Swahili",
    "vi": "Vietnamese",
    "tr": "Turkish",
    "fa": "Persian",
    "th": "Thai",
    "gu": "Gujarati",
    "mr": "Marathi",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "pl": "Polish",
    "uk": "Ukrainian",
    "nl": "Dutch",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "no": "Norwegian",
    "hu": "Hungarian",
    "cs": "Czech",
    "sk": "Slovak",
    "el": "Greek",
    "ro": "Romanian",
    "bg": "Bulgarian",
    "sr": "Serbian",
    "hr": "Croatian",
    "sl": "Slovenian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "et": "Estonian",
    "ca": "Catalan",
    "eu": "Basque",
    "gl": "Galician",
    "sq": "Albanian",
    "mk": "Macedonian",
    "af": "Afrikaans",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bs": "Bosnian",
    "ka": "Georgian",
    "ky": "Kyrgyz",
    "mn": "Mongolian",
    "ne": "Nepali",
    "uz": "Uzbek",
    "am": "Amharic",
    "ha": "Hausa",
    "ig": "Igbo",
    "yo": "Yoruba",
    "zu": "Zulu"
}

def translateText(text, source, target):
    translator = GoogleTranslator(source=source, target=target)
    text = translator.translate(text)
    return text

def translateToMap(arr, source, target):
    translator = GoogleTranslator(source=source, target=target)
    translated_map = {}
    for word in arr:
        translated_word = translator.translate(word)
        translated_map[word] = translated_word
    return translated_map


@app.route("/", methods=["GET","POST"])
def translate():
    input_text = None
    translated_text = None
    translated_words = None
    source_language = None
    target_language = None

    if request.method == "POST":
        input_text = request.form.get("text")
        source_language = request.form.get("source_language")
        target_language = request.form.get("target_language")

        if input_text:
            translated_text = translateText(input_text,source_language,target_language)
            input_words = input_text.split()
            translated_words = translateToMap(input_words, source_language, target_language)
    
    return render_template(
                            "index.html",
                            translated_text=translated_text,
                            input_text=input_text,
                            source_language=source_language,
                            target_language=target_language,
                            translated_words=translated_words,
                            languages=languages
                        )

if __name__ == "__main__":
    app.run(debug=False)