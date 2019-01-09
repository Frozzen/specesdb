# specesdb
База данных сырья

* главным является тибетское название - к нему прицеплено несколько европейских - с комментарием
* набор картинок для каждого европейского названия
* несколько источников описаний для каждого
* поля для европейского 
 * название, лат название, картинки, какую часть собирать, время сбора, обработка, место где собирать, действие  
* поля для тибетского
 * действие, название тиб, название вайли, вайли русское, лат аналоги(основной аналог, сила аналогов), 
 специфика основного, тип: минеральное, животное, растительное
* распознавалку по фотографии - предлагать варианты

## конвертеры исходных данных

### взять текст кособурова

#### база картинок  РТ
* исправить имена файлов - на название cvt_rt.py 

#### конвертировать исходники Кособуров
конвертировать в json. читаем в словарь и сохраняем его в json. 

потом дать возможность раскрыть скобки [5]

ཀ་ཀོ་ལ
Транслитерация: ка-ко-ла
Синонимы: ко-ла [5]
Истинное сырье:лишенные кожуры плоды

[
{
"tib_name": "ཀ་ཀོ་ལ",
"Транслитерация": "ка-ко-ла",
"Синонимы": "ко-ла [5]",
"Истинное сырье":"лишенные кожуры плоды" 
}
] 

Транслитерация: цха-ла
Синонимы: 'джу-бйэд, дар-цхур [6], дар-сман [1], зангс-рци [6]
Исходное сырье: бура [6, 7]
Методы обработки
...
Химический анализ
...

