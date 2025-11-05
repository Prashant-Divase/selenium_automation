import logging
import os.path

import pytest
from pygments.lexer import default
from selenium import webdriver
import yaml,datetime


def pytest_addoption(parser):
    parser.addoption("--env",action='store',default='qa',help='Environment to run tests: dev/qa/prod')
    parser.addoption("--browser",action="store",default='chrome',help="Environment to run tests: dev/qa/prod")

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    config_path = f"config/{env}.yaml"

    with open(config_path) as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture(scope="session")
def browser(request,config):
    return request.config.getoption('--browser')


@pytest.fixture(scope='function')
def driver(browser,config):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("unsupported browser")

    driver.maximize_window()
    # driver.get(config['browser'])
    yield driver
    driver.quit()

def pytest_configure(config):
    # Create reports folder
    os.makedirs("reports", exist_ok=True)

    # Dynamic filename: class + test + timestamp
    test_name = os.environ.get("PYTEST_CURRENT_TEST", "test").split(":")[-1].split(" ")[0]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"report_{test_name}_{timestamp}.html"
    report_path = os.path.join("reports", report_name)

    # ✅ This auto-generates HTML without CLI args
    config.option.htmlpath = report_path
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Automation Test Execution Report"


# ✅ Updated: Use plain HTML instead of py.xml
def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Class Name</th>")
    cells.insert(2, "<th>Test Name</th>")


def pytest_html_results_table_row(report, cells):
    class_name = getattr(report, "class_name", "N/A")
    test_name = getattr(report, "test_name", "N/A")
    cells.insert(1, f"<td>{class_name}</td>")
    cells.insert(2, f"<td>{test_name}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.class_name = item.cls.__name__ if item.cls else "NoClass"
    report.test_name = item.name

@pytest.fixture(scope='session', autouse=True)
def setup_logger():
    os.makedirs('logs',exist_ok=True)
    log_file = os.path.join("logs", f"test_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        handlers=[
        logging.FileHandler(log_file,'a', encoding='utf-8'),
        logging.StreamHandler()]
    )
    logger = logging.getLogger('pytest-automation')
    logger.info("========== Test Execution Started ==========")
    yield logger
    logger.info("========== Test Execution Started ==========")
