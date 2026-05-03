import pytest
from business_logic import calculate_gacha_probability

class TestGachaProbability:

    def test_base(self):
        for i in range(1, 74):
            assert calculate_gacha_probability(i) == 0.006

    def test_soft(self):
        assert calculate_gacha_probability(74) == 0.066

    def test_hard(self):
        assert calculate_gacha_probability(90) == 1.0

    def test_invalid(self):
        with pytest.raises(ValueError):
            calculate_gacha_probability(0)