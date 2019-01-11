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
в начале файла {'source':'', 'GUID':'...'} - источник текста, берется из имени файла +

#### взять фотогербарий Ширшова
* сделать правильные имена +
* конвертнуть  bmp->jpg +
* построить по нему индекс рестений+

#### взять тексты кособурова+
Лекарственное сырье тибетской медицины современный взгляд - 2006.txt
Технологическая обработка лекарственного сырья тибетской медицины - 2005-животное.txt
Технологическая обработка лекарственного сырья тибетской медицины - 2005-минеральное.txt

#####  изучить новую книгу 
* utf-Кособуров А. - Лекарственное сырье тибетской медицины современный взгляд - 2006.doc

#### база картинок  РТ +
* исправить имена файлов - на название cvt_rt.py 
* построить по нему индекс рестений

#### конвертировать исходники Кособуров
убрать "" и [вокруг текста]

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

#### составить исходник название - аналог по РТ+
rt-rast.json

### обработка json

#### разложить синонимы в массив
#### вырезать из кособурова латинские название в массив из {'rusname':'',"latname":"", "comment":""}
русское название: / / латинское - лат.буквы 

#### вырезать из кособурова латинкие название и найти картинки в google, yandex с указанием источника

#### сделать идентификацию и инструмент сличения между словарями. 
сделать коэффициент подобия/доверия указать куда и откуда есть доверие %

