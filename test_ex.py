import allure
import pytest

@allure.feature("Пример теста")
class TestExample:
    @allure.story("Проверка сложения")
    def test_add(self):
        assert 1 + 1 == 2, "Ожидалось  что 1 + 1 = 2"

    @allure.story("Проверка вычитания")
    def test_sub(self):
        assert 2 - 1 == 1, "Ожидалось что 2 - 1 = 1"

    @allure.story("Падающий тест")
    def test_fail(self):
        assert 2 / 0 == 1, "Этот тест упадет из-за деления на ноль"
