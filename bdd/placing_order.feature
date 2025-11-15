Feature: Placing an Order

  Scenario Outline: Place an order and verify the success message
    Given Go to greenkart page
    And Verify the home page
    When All products visible
    Then Search one item <item_name>
    And Add <item_name> to cart
    Then Go to cart page
    And Apply the <promo_code>
    And Verify promo code message
    And Place order
    And Select the <country_name>
    And Complete the purchase
    Then Verify the message

    Examples:
      | item_name   | country_name | promo_code         |
      | Cauliflower | India        | rahulshettyacademy |

