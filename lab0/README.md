# ОТЧЕТ
## Задание
1.Создайте репозиторий для дисциплины на GitHub.

2.Склонируйте его себе на ПК.

3.Напишите свою первую программу.

4.Скомпилируйте и запустите её.

5.Получите по отдельности результаты каждого этапа компиляции.

## Консольные команды:
git clone https://github.com/llloo123

git init

Переинициализирован существующий репозиторий Git в /home/user/lab0/.git/

git add .

git commit -m "First commit"

git push

gcc -Wall 1.c -o 1

ls 

./1

git add .

git commit -m 

## Результаты вычислений

```c
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
} 
```

#1. Полная сборка программы и запуск использованного файла программы:
![pic 1](pics/1.png) 

#2. Получен вывод препроцессора файла log.txt.
![pic 2](pics/2.png)

Содержимое файла log.txt.
![pic 3](pics/3.png) 

Получен ассемблерный код в файле lab0.s.
![pic 4](pics/4.png) 

Содержимое файла lab0.s.
![pic 5](pics/5.png) 

Получен объектный файл lab0.o.
![pic 6](pics/6.png) 
