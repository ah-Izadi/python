import googletrans
from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display

# print(googletrans.LANGUAGES)

translator = Translator()
result = translator.translate('',src='persian',dest='english')
reshape = arabic_reshaper.reshape(result.text)
print(get_display(reshape))