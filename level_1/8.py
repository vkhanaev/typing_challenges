import decimal
import uuid
from typing import Callable

from constants import ___


def get_user_balance(user_id: uuid.UUID) -> decimal.Decimal:
    #reveal_type(user_id)
    pass


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
