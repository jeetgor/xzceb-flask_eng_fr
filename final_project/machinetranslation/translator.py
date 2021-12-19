import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def translator_service(user_text,translation_lang):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
    language_translator.set_service_url(url)
    translation = language_translator.translate(
    text=user_text,
    model_id=translation_lang).get_result()
    return translation

def english_to_french(english_text):
    if english_text:
        french_text = translator_service(english_text,'en-fr')
        return french_text.get('translations')[0].get('translation')

def french_to_english(french_text):
    if french_text:
        english_text = translator_service(french_text,'fr-en')
        return english_text.get('translations')[0].get('translation')
