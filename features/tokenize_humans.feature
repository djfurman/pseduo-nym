Feature: It tokenizes human data

   As a service provider, I must identify my customers and their interactions with my system, however it is not germain to any domain to have this infomration available in one place. Instead, a harmless (and meaningless) token can be passed where only the appropriate privilaged services can reverse the data.

   Scenario: It tokenizes individual data
    Given a fake person
    And a fake address
    And a fake tax ID
    When the value is tokenized
    Then a token should be returned
    And the information should be stored in the persistance layer

  # Scenario: It detokenizes individual data
  #   Given a token
  #   When the value is detokenized
  #   Then it should return the person
  #   And the address
  #   And the tax ID
