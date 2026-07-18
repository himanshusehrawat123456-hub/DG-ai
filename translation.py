# DG AI Translation System


def translate(text, language):

    translations = {

        "Hindi": text,

        "English": text,

        "Spanish": text,

        "French": text

    }


    if language in translations:

        return translations[language]


    else:

        return "Language not supported"



def show_translation(text, language):

    result = translate(text, language)

    print("Translation:", result)
