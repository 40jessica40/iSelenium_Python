
#该功能给开发使用，不开放，无需测试

@close_all_options
@after_login
Feature:  系统管理-菜单管理
	As a tester
	I want to test menu management

    Scenario Outline: click menu management
		When I move to element "<drop_down_arrows>"
		When I click on the link element "<menu_location>"
		Then I expect that element "<menu_title_location>" is visible
        Then I want to refresh the window
        Examples:
              | drop_down_arrows | menu_location | menu_title_location |
              |xpath=>/html/body/div[1]/div/div/div[1]/div[1]/div[2]/ul/div[7]/li/div/i|#/systeManage/menu|xpath=>/html/body/div[1]/div/div/section/div/div/div[1]|


  Scenario Outline: click add for dashboard
      When I click on the element "<add_location>"
      When I pause for 1000ms
      When I click on the element "<father_location>"
      #需要点两次，已提bug
      When I click on the element "<father_location>"
      When I select the 8th option of elements "<dashboard_location>" and click

#      And I click on the element "<dashboard_location>"

      Then I select the 2st option of elements "<elements>" and set value "<text_name>"
      When I pause for 1000ms

      Then I select the 3st option of elements "<elements>" and set value "<name>"
      When I pause for 1000ms

      Then I select the 4st option of elements "<elements>" and set value "<page_path>"
      When I pause for 1000ms

      Then I select the 5st option of elements "<elements>" and set value "<path>"
      When I pause for 1000ms

      Then I select the 6st option of elements "<elements>" and set value " "
      When I pause for 1000ms

      When I click on the element "<add1_location>"
      When I pause for 5000ms
      Then I wait on element "<alert_location>" for 2000ms to be visible

      Then I want to refresh the window
      Examples:
        | add_location | father_location | dashboard_location | elements | text_name | name | page_path | path | icon | add1_location | alert_location|
        |xpath=>/html/body/div[1]/div/div/section/div/div/div[2]/div/div/div[1]/div/div[1]/div/button/span|xpath=>/html/body/div[1]/div/div/section/div/div/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/div/div/span/span/i|classes=>el-tree-node__content|classes=>el-input__inner|自动化测试仪表盘|自动化测试仪表盘|views/home/homepage|/homepage||xpath=>/html/body/div[1]/div/div/section/div/div/div[2]/div/div/div[2]/div/div/div/form/div[10]/div/button[1]|class=>el-notification|

  Scenario Outline: click added dashboard and modify and delete
      When I click on the element "<added_dashboard_location>"
      When I pause for 1000ms

      Then I select the 2st option of elements "<elements>" and set value "<text_name>"
      When I pause for 1000ms
      When I click on the element "<modify>"
      Then I wait on element "<alert_location>" for 2000ms to be visible
      When I pause for 2000ms
  #    Then I see that element "text_name_location>" contains the text "<text_name>"
      When I click on the element "<delete_location>"
      Then I wait on element "<alert_location>" for 2000ms to be visible
      Examples:
        | added_dashboard_location | elements | text_name | modify | delete_location | alert_location |
        |xpath=>/html/body/div/div/div/section/div/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/span[2]/span/span|classes=>el-input__inner|修改自动化测试仪表盘|xpath=>/html/body/div[1]/div/div/section/div/div/div[2]/div/div/div[2]/div/div/div/form/div[10]/div/button[1]|xpath=>/html/body/div[1]/div/div/section/div/div/div[2]/div/div/div[2]/div/div/div/form/div[10]/div/button[2]/span|class=>el-notification|