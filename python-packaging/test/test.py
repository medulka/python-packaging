#!/user/bin/env python3

# ../test/

import pytest
import numpy as np
from calculate_hanka import calculate_hanka

def test_flip_coin():
    coin = calculate_hanka.flip_coin()
    assert coin in ["heads", "tails"]

@pytest.mark.parametrize("n_dice", [1, 2, 3, 4, 5, 6])
@pytest.mark.parametrize("n_sides", [2,3,6,8])
def test_roll_dice(n_dice, n_sides):
    dice = calculate_hanka.roll_dice(n_dice, n_sides)
    assert len(dice) == n_dice
    assert np.all(dice >= 1)
    assert np.all(dice <= n_sides)




