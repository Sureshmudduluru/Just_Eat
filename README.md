# Just_Eat
Just Eat BDD project documentation

JUST EAT Documentation To build JustEat automation suite I used BDD framework with following configurations like Python, Selenium WebDriver, Behave, Allure reports. 

Before test execution, install below dependencies:

--Install Python
-- Configure python path in system environment variables
-- Install PyCharm IDE 
-- Install Selenium 
-- Install Behave 
-- Install allure-behave 
-- copy Chrome driver from selenium portal and set path in environment variables.


Create BDD project "JustEat_Project" and copy 'Featured' and 'Drivers' folder under created project. 
In Featured folder we have a 'JustEat_Search.feature' it has all the Scenario or Scenario Outline. 
In Featured folder we have steps folder, its consists ‘searchpage_steps.py’ it has all step definitions. 

To execute features, in pycharm IDE open terminal and run following command: Behave Featured\JustEat_Search.feature
