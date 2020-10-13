import configparser
import os
import sys
import shutil

def get_config():
    config = configparser.ConfigParser()
    config.read('iselenium.ini')
    config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
    # config.read(os.path.join('iselenium.ini'))
    # return config
get_config()


from behave_webdriver import before_all_factory, use_fixture_tag
from behave_webdriver.driver import Chrome, ChromeOptions
from functools import partial
from behave_webdriver.fixtures import transformation_fixture, fixture_browser
from behave_webdriver.transformers import FormatTransformer
from behave.fixture import use_fixture
import behave_webdriver
from helpers.log import Log
log = Log()
print('*---------------ENVIRON-------------------*')
print(os.environ)
print('*----------------HOME------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*--------------PATH--------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')


def get_driver(**kwargs):
    args = []
    kwargs.setdefault('default_wait', 5)
    Driver = behave_webdriver.utils._from_env(default_driver='Chrome')
    if Driver == behave_webdriver.Chrome:
        opts = ChromeOptions()
        opts.add_argument('--no-sandbox')  # for travis build
        kwargs['chrome_options'] = opts

    pwd_driver_path = os.path.abspath(os.path.join(os.getcwd(), Driver._driver_name))
    if sys.version_info[0] < 3:
        ex_path = pwd_driver_path
    else:
        ex_path = shutil.which(Driver._driver_name) or pwd_driver_path
    kwargs['executable_path'] = ex_path
    if os.environ.get('BEHAVE_WEBDRIVER_HEADLESS', None) and hasattr(Driver, 'headless'):
        Driver = Driver.headless
    return Driver, kwargs

    #context.behave_driver = context.BehaveDriver()


def before_all(context):

    log.info("---------------------测试开始---------------------------")
    # get_config()


    userdata = context.config.userdata
    context.api_url = userdata.get("api_url")

    driver, kwargs = get_driver()
    context.BehaveDriver = partial(driver, **kwargs)
    use_fixture(fixture_browser, context, webdriver=driver, **kwargs)
    use_fixture(transformation_fixture, context, FormatTransformer, BASE_URL='http://192.168.2.87:30080')


def before_tag(context, tag):
    use_fixture_tag(context, tag)


def before_feature(context, feature):
    pass
    # if "after_login" in feature.tags:
    #     try:
    #         context.execute_steps(u'''
    # Then I expect that element "xpath=>/html/body/div[1]/div/div/div[1]/div[1]/a/span" is visible
    #     ''')
    #     except Exception:
    #         context.execute_steps(u'''
    #         Given I open the site "{BASE_URL}"
    #         And I maximize the window
    #         When I set "{username}" to the inputfield "{username_location}"
    #     And I set "{password}" to the inputfield "{password_location}"
    #     And I set "{verification_code}" to the inputfield "{verification_code_location}"
    #     When I click on the button "{login_location}"
    #         '''.format(BASE_URL="http://192.168.2.87:30080",
    #                    username="nice001",
    #                    username_location="xpath=>/html/body/div/div/div/form/div[2]/div/div[2]/input",
    #                    password="a123456",
    #                    password_location="xpath=>/html/body/div/div/div/form/div[3]/div/div[2]/input",
    #                    verification_code="ewp5",
    #                    verification_code_location="xpath=>/html/body/div/div/div/form/div[4]/div/div/input",
    #                    login_location='xpath=>/html/body/div/div/div/form/div[5]/div/button/span'))
    # if "fresh_driver" in feature.tags:
    #     print("---------------->fresh")
    #     before_all(context)
    #     # context.behave_driver.default_wait = 5


def before_scenario(context, scenario):
    print("\n\nBefore Scenario: {} | {}".format(scenario.feature, scenario.name))
    if "skip_firefox" in scenario.effective_tags and os.environ.get("BEHAVE_WEBDRIVER", '').lower() == 'firefox':
        scenario.skip("Skipping because @skip_firefox tag (usually this is because of a known-issue with firefox)")
        return


def after_scenario(context, scenario):
    print("\nAfter Scenario: {} | {} | Status: {}".format(scenario.feature, scenario.name, scenario.status))


def after_feature(context, feature):
    pass
    # 当所有场景连起来的时候，下面注释部分可以放开
    # if "close_all_options" in feature.tags:
    #     context.execute_steps(u'''
    #         When  I click on the element "{close_operation}"
    #         When  I click on the element "{close_all_location}"
    #         '''.format(close_operation="xpath=>/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div/span",
    #                    close_all_location="xpath=>/html/body/ul/li[1]"))


def after_all(context):
    log.info("---------------------测试结束---------------------------")
    # sys.setrecursionlimit(100000000)
    # context.behave_driver.quit()
