import pytest

from tdn import tdn


def test_tdn():
    assert tdn(0) == '  0 '
    assert tdn(1) == '  1 '
    assert tdn(0.4) == '  0 '
    assert tdn(1.1) == '  1 '
    assert tdn(0.5) == '  0 '  # Bankers' rounding
    assert tdn(1.5) == '  2 '  # Bankers' rounding
    assert tdn(9.2) == '  9 '
    assert tdn(11.8) == ' 12 '
    assert tdn(923) == '923 '
    assert tdn(923.33) == '923 '
    assert tdn(1000) == '1.0K'
    assert tdn(1000.9) == '1.0K'
    assert tdn(1234) == '1.2K'
    assert tdn(12345) == ' 12K'
    assert tdn(12345.6) == ' 12K'
    assert tdn(12645.3) == ' 13K'
    assert tdn(123456) == '123K'
    assert tdn(123654) == '124K'
    assert tdn(1234567) == '1.2M'
    assert tdn(1284567) == '1.3M'
    assert tdn(12345678) == ' 12M'
    assert tdn(123456789) == '123M'
    assert tdn(1234567890) == '1.2B'
    assert tdn(12345678901) == ' 12B'
    assert tdn(123456789012) == '123B'
    assert tdn(1234567890123) == '1.2T'
    assert tdn(12345678901234) == ' 12T'
    assert tdn(123456789012345) == '123T'
    with pytest.raises(AssertionError):
        tdn(9.995e14)
    with pytest.raises(AssertionError):
        tdn(1000000000000000)
    with pytest.raises(AssertionError):
        tdn(9.3e17)
    with pytest.raises(AssertionError):
        tdn(-19.2)
    assert tdn(1.1) == '  1 '
    assert tdn(98.2) == ' 98 '
    assert tdn(111.7) == '112 '
    assert tdn(9_876) == '9.9K'
    assert tdn(12_345_678) == ' 12M'
    assert tdn(123_456_789_012) == '123B'
    assert tdn(999_123_456_789_012) == '999T'
    assert tdn(999_499_999_999_999) == '999T'
