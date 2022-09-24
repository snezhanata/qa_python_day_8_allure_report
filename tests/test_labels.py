# Task 4: Разметка тестов всеми аннотациями

import allure
from allure_commons.types import Severity



def test_dynamic_labels():
    allure.dynamic.tag('normal')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature('List of tasks in the repository')
    allure.dynamic.story('Unauthorized user shouldn\'t create a task')
    allure.dynamic.link('https://github.com/snezhanata/qa_python_day_8_allure_report', name='Repository')
    pass


@allure.tag('trivial')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Snezhana')
@allure.feature('List of tasks in the repository')
@allure.story('User creates a task')
@allure.link('https://github.com', name='Repository')
def test_decorator_labels():
    pass
