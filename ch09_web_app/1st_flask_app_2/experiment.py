def my_shiny_new_decorator(function_to_decorate):
     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
     # получая возможность исполнять произвольный код до и после неё.
     def the_wrapper_around_the_original_function():
         print("Я - код, который отработает до вызова функции")
         print("Сама функция")
         function_to_decorate() # Сама функция
         print("Да еще раз")
         function_to_decorate() # Сама функция еще раз
         print("Да еще много-много раз")
         function_to_decorate() # Сама функция и еще много-много раз
         print("А я - код, срабатывающий после")
     # Вернём эту функцию
     return the_wrapper_around_the_original_function

"""
def stand_alone_function():
     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

print("stand_alone_function() = ", stand_alone_function())
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
myFunc = stand_alone_function_decorated()
print("all inside the print")
print("stand_alone_function_decorated() = ", stand_alone_function_decorated())
stand_alone_function_decorated()
"""

@my_shiny_new_decorator
def stand_alone_function():
    print("With at @ symbol: Я не простая одинокая функция")

stand_alone_function()

