import pytest
from card_draw import draw_card
from user_profile import get_user_profile

def test_draw_card_structure():
    user_id = "test_user"
    card = draw_card(user_id)
    assert "id" in card
    assert "name" in card
    assert "rarity" in card