
def validate_has_amount(data):
    if data.get('currentAmount'):
        return (True, {})
    else:
        return (False, {
            'error': 'Missing current amount',
            'location': 'row 1'})

def validate_outlays_match_current_amount(data):
    if data.get('currentAmount') + data.get('outlays') \
            != data.get('initialAmount'):
        return (False, {
            'error': 'Current amount does not match outlays',
            'location': 'row 1'
        })
    else:
        return (True, {})

validators = [
  validate_has_amount
]

def validate(data):
    total_errors = []
    for validator in validators:
        valid = validator(data)
        if not valid[0]:
            total_errors.append(valid[1])

    return total_errors
