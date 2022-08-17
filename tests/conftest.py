import allure
import pytest
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = True

@pytest.fixture(scope='function', autouse=True)
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@allure.step('open git main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('search repository {repo}')
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step('go to repository {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('open tab Issues')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('check visibility Issue with num {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()