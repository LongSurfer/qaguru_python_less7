import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from tests.conftest import should_see_issue_with_number, open_main_page, search_for_repository, go_to_repository, \
    open_issue_tab


def test_dynamic_steps():
    with allure.step('open git main page'):
        browser.open("https://github.com")

    with allure.step('search repository'):
        s(".header-search-input").click()
        s(".header-search-input").type("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step('go to repository'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('open tab Issues'):
        s("#issues-tab").click()

    with allure.step('check visibility Issue with num 76'):
        s(by.partial_text("#76")).should(be.visible)



def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


