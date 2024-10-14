def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

# inner_function() # ошибка, т.к. невозможо доставать значения внутри функции (извне)

test_function()