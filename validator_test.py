import unittest

import validator

class TestValidators(unittest.TestCase):
    def test_validate_has_amount(self):
        data = {}
        errors = validator.validate_has_amount(data)
        self.assertFalse(errors[0], 'Validator fails with missing currentAmount')
        
        data['currentAmount'] = 100
        errors = validator.validate_has_amount(data)
        self.assertTrue(errors[0], 'Validator passes')

    def test_validate_outlays_match_current_amount(self):
        data = {
          'currentAmount': 501,
          'initialAmount': 1000,
          'outlays': 500
        }
        errors = validator.validate_outlays_match_current_amount(data)
        self.assertFalse(errors[0],
            'Validator fails whe outlays and current added != initial')

        data['currentAmount'] = 500
        errors = validator.validate_outlays_match_current_amount(data)
        self.assertTrue(errors[0], 'Validator passes')


if __name__ == '__main__':
    unittest.main()
