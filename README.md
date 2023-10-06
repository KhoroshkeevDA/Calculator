# API Калькулятор с запуском Docker.

## Установка и запуск через CMD.

1. cd <Путь к папке>
2. docker build -t calculator-app .
3. docker run -it -p 4000:4000 calculator-app

## Описание

Calc.py работает на 4000 порту.
Запросы осуществляются в виде: http://127.0.0.1:4000/{OPERANDUM}?a={NUMBER}&b={NUMBER}

Где: 
OPERANDUM - операнд.
> Суммирование: sum

> Вычитание: sum

> Деление: div

> Умножение: mult
                    
NUMBER - число.

## Пример работы:

>![image](https://github.com/KhoroshkeevDA/Calculator/assets/147157811/df4e3fc6-6207-4d42-a748-e4eaee7f37be)
>![image](https://github.com/KhoroshkeevDA/Calculator/assets/147157811/d14b05e3-e318-409c-aa5d-8c50413ea8ad)
>![image](https://github.com/KhoroshkeevDA/Calculator/assets/147157811/caff91c2-b75a-496c-ba12-c6bdd0104073)

