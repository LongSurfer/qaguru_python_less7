import allure
from allure_commons.types import Severity

'''
def test_no_labels():
    pass


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass
'''

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'eroshenkoam')
@allure.feature('Useless test')
@allure.story('Find issue number #76')
@allure.link('https://github.com/evgenyshandrik', name='Labels testing')
def test_decorator_labels():
    pass
