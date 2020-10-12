from behave_webdriver.steps import *
# use_step_matcher('re')
from nose.tools import assert_equal, assert_not_equal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@step('I maximize the window')
def step_impl(context):
    context.behave_driver.max_window()


@step("I want to refresh the window")
def step_impl(context):
    context.behave_driver.F5()


@step("I want to close the window")
def step_impl(context):
    context.behave_driver.close()


@then('I expect that executing the step "{step_text}" raises an exception')
def test_step_raises_exception(context, step_text):
    try:
        context.execute_steps(step_text)
        time.sleep(4)
    except Exception as e:
        print(e)
    else:
        raise AssertionError('Step did not raise exception')


@step('I select the {nth} option of dropdown_item')
def step_impl(context, nth):
    # ul = context.behave_driver.get_elements(element)[int(index)]
    index = int(''.join(char for char in nth if char in string.digits))
    li = context.ul.find_elements_by_tag_name('li')
    print("index---------------------------->", index)
    print("li[index].text------------------->", li[index].text)
    time.sleep(2)
    li[index].click()


@step('I select the {nth} option of elements "{elements}" and set value "{value}"')
def step_impl(context, nth, elements, value):
    index = int(''.join(char for char in nth if char in string.digits))
    elem = context.behave_driver.get_elements(elements)[index]
    elem.clear()
    elem.send_keys(value)


@step('I select the {nth} option of elements "{elements}" and click')
def step_impl(context, nth, elements):
    index = int(''.join(char for char in nth if char in string.digits))
    elem = context.behave_driver.get_elements(elements)[index]
    print("elem .text-------------->", elem .text)
    time.sleep(1)
    # elem.click()
    try:
        context.behave_driver.element_left_click(elem)
    except:
        elem.click()


@step('I scroll to the bottom')
def step_impl(context):
    # todo：将滚动条移动到页面的底部，该方法无效
    js = "var q=document.documentElement.scrollTop=100000"
    context.behave_driver.execute_script(js)
    time.sleep(3)


@step('I scroll to the top')
def step_impl(context):
    # todo：将滚动条移动到页面的顶部，该方法无效
    js = "var q=document.documentElement.scrollTop=0"
    context.behave_driver.execute_script(js)
    time.sleep(3)


@step('I click on the link element "{link_target}"')
def step_impl(context, link_target):
    length = len(context.behave_driver.find_elements_by_tag_name("a"))
    print("link_target_length------------->", length)
    for i in range(0, length):
        links = context.behave_driver.find_elements_by_tag_name("a")
        link = links[i]
        if link_target in link.get_attribute("href"):
            print("href------------->", link.get_attribute("href"))
            time.sleep(3)
            link.click()
            time.sleep(3)
            break


@step('I click the {nth} option of elements "{checkbox_location}" and the "{attribute}" will be changed')
def step_impl(context, nth, checkbox_location, attribute):
    index = int(''.join(char for char in nth if char in string.digits))
    value1 = context.behave_driver.get_elements(checkbox_location)[index].get_attribute(attribute)
    context.behave_driver.get_elements(checkbox_location)[index].click()
    time.sleep(1)
    value2 = context.behave_driver.get_elements(checkbox_location)[index].get_attribute(attribute)
    print("v1------------>", value1)
    print("v2------------>", value2)
    assert_not_equal(value2, value1)


@step('I click on the element "{switch_location}" and click the {nth} option of sure button "{sure_button_location}" and the "{attribute}" will be changed')
def step_impl(context, switch_location, nth, sure_button_location, attribute):
    value1 = context.behave_driver.get_element(switch_location).get_attribute(attribute)
    time.sleep(2)
    context.behave_driver.get_element(switch_location).click()
    time.sleep(2)
    index = int(''.join(char for char in nth if char in string.digits))

    #不是alert弹窗，不用以下步骤
    # context.behave_driver.switch_to.default_content()
    # alert = context.behave_driver.alert()
    # alert.get_element(sure_button_location).click()
    context.behave_driver.get_elements(sure_button_location)[index].click()

    #以下注释了，skin_management与后面用例冲突（todo：已经放开下面的内容，skin_management相关需要重新写）
    time.sleep(2)
    value2 = context.behave_driver.get_element(switch_location).get_attribute(attribute)
    print("v1------------>", value1)
    print("v2------------>", value2)
    assert_not_equal(value2, value1)


@step('I except that the element "{ele}" will be seen just for a while')
def step_impl(context, ele):
    # 方法一：
    WebDriverWait(context.behave_driver, 2000, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, ele)))

    # 方法二
    # count = 0
    # while count < 20000:
    #     if context.behave_driver.get_element(ele).is_displayed():
    #         break
    #     else:
    #         count += count


@step('I see that element "{element}" contains the text "{value}"')
def step_impl(context, element, value):
    text = context.behave_driver.get_element(element).text
    return text in value


# @step('I set varied "{value}" to the inputfield "{element}"')
# def step_impl(context, value, element):
#     if value == "__ID":
#         value = generate_random_string_with_lower_case_letters_and_digits()
#     elem = context.behave_driver.get_element(element)
#     elem.clear()
#     time.sleep(2)
#     elem.send_keys(value)
#
#
# # 以下是api的behave测试复制过来的
#
#
# @step('I get system infomation')
# def step_impl(context):
#     context.status_code, context.response = Getsysinfo(context.api_url).post_getsysinfo()
#     try:
#         if 200 == context.status_code and 1 == context.response["code"]:
#             context.token = context.response["data"]["token"]
#             context.key = context.response["data"]["Key"]
#     except Exception as e:
#         print(e)
#
#
# @step('I login with clientType "{clientType}", os_type "{os_type}", username "{username}", '
#       'userpass "{userpass}", time "{time}"')
# def step_impl(context, clientType, os_type, username, userpass, time):
#     clientType = judge_whether_a_digit(clientType)
#     os_type = judge_whether_a_digit(os_type)
#     if username == "__XIDADA":
#         username = context.username
#     if "__TIME" == time:
#         time = get_time_stamp10()
#     else:
#         time = judge_whether_a_digit(time)
#     payload = set_payload(clientType=clientType, os_type=os_type, username=username, userpass=userpass, time=time)
#     url = "/home/login"
#     get_context_result_before_login(context, url, context.token, payload)
#     try:
#         if 200 == context.status_code and 1 == context.response["code"]:
#             context.session_key = context.response["data"]["session_key"]
#             context.userkey = context.response["data"]["userkey"]
#             context.username = context.response["data"]["username"]
#     except Exception as e:
#         print(e)
#
#
# @step('I save Gold into yuebao with access_gold "{access_gold}"')
# def step_impl(context, access_gold):
#     if access_gold.isdigit():
#         access_gold = int(access_gold)
#     payload = Payload(access_gold)
#     headers = Headers(context.session_key, context.userkey)
#     context.status_code, context.response = YuebaosaveGold(context.api_url, payload, headers).post_yuebaosaveGold(
#         context.session_key, str(context.username))
#
#
# @step('I take out Gold from yuebao with access_gold "{access_gold}", passwd "{passwd}"')
# def step_impl(context, access_gold, passwd):
#     if access_gold.isdigit():
#         access_gold = int(access_gold)
#     payload = Payload1(access_gold, passwd)
#     headers = Headers(context.session_key, context.userkey)
#     context.status_code, context.response = YuebaotakeoutGold(context.api_url, payload, headers).post_yuebaotakeoutGold(context.session_key, str(context.username))
#
#
