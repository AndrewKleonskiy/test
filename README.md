# Parser

В коде описана функция парсинга текстового файла (parse_file), которая в качестве единственного аргумента принимает путь к файлу и возвращает набор словарей, содержащих данные. 

Файл представляет собой набор данных типа ключ-значение, ключ от значения отделен двоеточием. Из значений должны быть удалены лишние пробелы, многострочные значения должны быть объеденены в одну строку с сохранением переносов (но не отступов). Данные с повторяющимися ключами считаются многострочными.

Каждый документ в файле разделен как минимум одной пустой строкой, строки, начинающиеся с символа # означают комментарии и должны игнорироваться.

Пример исходных данных находится в файле example.txt.
