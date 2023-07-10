

from challenges.challenge_encrypt_message import encrypt_message

import pytest # type: ignore

def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", key="5")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=5, key=6)

    assert encrypt_message("message", key=3) == "sem_egas"
    assert encrypt_message("test", key=4) == "tset"
