
def validate_has_amount(data):
    if data.get('currentAmount'):
        return (True, {})
    else:
        return (False, {
            'error': 'Missing current amount'})

def validate_outlays_match_current_amount(data):
    if data.get('currentAmount', 0) + data.get('outlays', 0) \
            != data.get('initialAmount', 0):
        return (False, {
            'error': 'Current amount does not match outlays'
        })
    else:
        return (True, {})

validators = [
  validate_has_amount,
  validate_outlays_match_current_amount
]

def validate(data):
    total_errors = []
    for idx, data_row in enumerate(data):
        for validator in validators:
            valid = validator(data_row)
            if not valid[0]:
                valid[1]['location'] = 'row ' + str(idx + 1)
                total_errors.append(valid[1])

    return total_errors
