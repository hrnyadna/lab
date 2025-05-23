# 🧬 Лабораторная работа 2: Нахождение мотива в ДНК

# Цель 
Изучить метод поиска мотивов (повторяющихся подстрок) в ДНК-цепочках и применить его для нахождения всех вхождений заданной последовательности в геноме.
## Задачи

1) Ознакомиться с понятием мотива в молекулярной биологии и его ролью в геноме.

2) Разработать алгоритм поиска всех вхождений подстроки в строке ДНК.

3) Реализовать данный алгоритм на языке Python.

4) Обеспечить считывание входных данных из текстовых файлов.

5) Вывести позиции всех вхождений мотива в основной строке.

6) Протестировать программу на нескольких наборах данных (используя 7 .txt файлов).

# Как пользоваться
Тестовые файлы расположены в этой же папке lab2 (IN 1.txt,..,IN 7.txt). В этих файлах как раз и содержится две строки с ДНК организма и искомым мотивом. В одной папке должен располагаться код и тестовые файлы. Чтобы посмотреть другие последовательности, то просто замените "IN_1.txt" на нужное имя файла (например, "IN_2.txt"), и программа прочитает новые данные.

# Что делала
Сначала мы открываем файл с тестовыми данными, он у меня расположен в той же папке, что и мой проект, поэтому путь к нему очень легко прописан. 

Затем мы читаем первую строку(ДНК орагнизма) и вторую строку(искомый мотив).

Используя цикл ищем все вхождения мотива в последовательность ДНК. Для каждого возможного положения в ДНК-последовательности выполняется выделение подстроки, длина которой соответствует длине мотива; поэлементное сравнение выделенного участка с искомым мотивом. При обнаружении полного совпадения программа регистрирует начальную позицию вхождения с учетом биологической нумерации (позиции нумеруются с 1). И данные обнаруженные позиции выводятся через пробел.

# Результат
Данная программа реализует алгоритм поиска точных совпадений короткой последовательности ДНК (мотива) в пределах более длинной последовательности. Метод основан на последовательном сравнении участков генетического кода стандартным методом скользящего окна.
Вот примеры того как все работает и рядом сравнение с данными нам OUT файлами.
![image](https://github.com/user-attachments/assets/d75df33f-e40f-4e66-9276-738d962e2159)

![image](https://github.com/user-attachments/assets/99f3535e-0f18-4058-a5c7-9d92e1f89655)



