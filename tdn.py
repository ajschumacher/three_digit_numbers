"""Express a number with up to three symbols plus a symbol

Like this:
                   1.1 -> '  1 '
                  98.2 -> ' 98 '
                 111.7 -> '112 '
               9_876   -> '9.9K'
          12_345_678   -> ' 12M'
     123_456_789_012   -> '123B'
 999_123_456_789_012   -> '999T'

Negative numbers and anything that rounds to a quadrillion or higher
is rejected.

"""


def tdn(number):
    """Short (Three-Digit Number) string representation"""
    assert 0 <= number < 9.995e14, 'outside range of defined behavior'
    if number < 1000:
        return f'{round(number):3d} '
    number /= 1000
    for symbol in 'KMBT':
        if number >= 1000:
            number /= 1000
            continue
        if number >= 10:
            return f'{number:3.0f}{symbol}'
        return f'{number:1.1f}{symbol}'
    return result
