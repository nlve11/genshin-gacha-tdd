import pytest
from business_logic import calculate_gacha_probability


class TestGachaProbability:

    def test_base_probability(self):
        """1-73抽：0.6%"""
        for pull in range(1, 74):
            prob = calculate_gacha_probability(pull)
            assert prob == pytest.approx(0.006, rel=1e-6)

    def test_soft_pity_start(self):
        """第74抽：6.6%"""
        prob = calculate_gacha_probability(74)
        assert prob == pytest.approx(0.066, rel=1e-6)

    def test_soft_pity_increase(self):
        """74-89抽递增"""
        expected_prob = 0.066
        for pull in range(74, 90):
            prob = calculate_gacha_probability(pull)
            assert prob == pytest.approx(expected_prob, rel=1e-6)
            expected_prob += 0.06

    def test_hard_pity_guarantee(self):
        """第90抽：100%"""
        prob = calculate_gacha_probability(90)
        assert prob == pytest.approx(1.0, rel=1e-6)

    def test_invalid_pull_number(self):
        """非法输入"""
        with pytest.raises(ValueError):
            calculate_gacha_probability(0)

        with pytest.raises(ValueError):
            calculate_gacha_probability(-1)

    def test_pull_over_90(self):
        """超过90抽：重置"""
        prob = calculate_gacha_probability(91)
        assert prob == pytest.approx(0.006, rel=1e-6)