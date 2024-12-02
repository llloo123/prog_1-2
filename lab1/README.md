## Отчет 
##Лабораторная №1
## (Вариант 1)
*Вывести сумму цифр числа a если она больше b, если равна b - сообщение Сумма цифр = b, и значение суммы, увеличенное на b, если сумма меньше b.*
## Ход работы
1. Разобрать код из примера и изучить палгоритм работы с `if`
2. Составить блок-схему для совего варианта
3. С помощью блок-схемы и программы преподавателя написать программу по совему варианту
4. Переместить в свой репозиторий на `Github`
## Код
```c
#include <stdio.h>

int calc_sum_digits(int num)
{
    int sum_digits = 0;
    while(num != 0) {
        sum_digits += num % 10;
        num = num / 10;
    }   
    return sum_digits;
}

int main()
{
    int a, b;
    printf("Enter a -> ");
    scanf("%d", &a);
    printf("Enter b -> ");
    scanf("%d", &b);

    int sum_digits_a, sum_digits_b;
    sum_digits_a = calc_sum_digits(a);
    sum_digits_b = calc_sum_digits(b);

    if (sum_digits_a > b)
        printf("sum_digits_a = %d\n", sum_digits_a);
    if (sum_digits_a == b)
        printf("sum_digits_b = %d\n", sum_digits_b);
    if (sum_digits_a < b)
       printf("sum_digits_a + b = %d\n", sum_digits_a + b);
    return 0;
}
```

## Скриншоты результата работы
<image src = <...>.png alt="блок-схема">
<image src = <...>.png alt="результат кода">

## Источники 
(https://programforyou.ru/block-diagram-redactor)
(https://evil-teacher.on.fleek.co/prog_pm/term1/lab01/)
(https://doka.guide/tools/markdown/)
