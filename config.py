# DG AI Global Language Configuration


APP_NAME = "DG AI"

VERSION = "1.0"


SUPPORTED_LANGUAGES = {

    "India": [
        "Hindi",
        "English",
        "Bengali",
        "Telugu",
        "Marathi",
        "Tamil",
        "Gujarati",
        "Urdu",
        "Kannada",
        "Malayalam",
        "Punjabi",
        "Odia",
        "Assamese",
        "Sanskrit"
    ],


    "Europe": [
        "Spanish",
        "French",
        "German",
        "Italian",
        "Portuguese",
        "Russian"
    ],


    "Asia": [
        "Chinese",
        "Japanese",
        "Korean",
        "Arabic",
        "Thai",
        "Vietnamese"
    ],


    "Africa": [
        "Swahili",
        "Amharic",
        "Hausa"
    ],


    "Americas": [
        "English",
        "Spanish",
        "Portuguese",
        "French"
    ]

}


CURRENT_LANGUAGE = "Hindi"



def show_languages():

    print("===== DG AI Languages =====")


    for region, languages in SUPPORTED_LANGUAGES.items():

        print("\n", region)

        for language in languages:

            print("-", language)
