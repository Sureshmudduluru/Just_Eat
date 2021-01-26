Feature: JustEat search page
  Scenario: Logo presence on Just-Eat home page
    Given Launch chrome browser
    When Open Just-Eat homepage
    Then Verify Just-Eat logo present on page
    And Close browser

 Scenario Outline: Outline: Search for restaurants in an area with in-valid area code
    Given Launch chrome browser
    When Open Just-Eat homepage
    Then Verify search results with invalid area code "<Area-Code>"
    And Close browser

    Examples:
      | Area-Code |
      | XYZWERTYG |


  Scenario Outline: Search for restaurants in an area with valid area code
    Given Launch chrome browser
    When Open Just-Eat homepage
    Then Verify search results with an area code "<Area-Code>"
    And Close browser

    Examples:
      | Area-Code |
      | AR51 1AA  |

