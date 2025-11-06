import zlib

from authmoderne.crypto import generate_token_hash_pair, get_token_hash


def _crc32_to_base62(number: int) -> str:
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base = len(characters)
    encoded = ""
    while number:
        number, remainder = divmod(number, base)
        encoded = characters[remainder] + encoded
    return encoded.zfill(6)


class TestGetTokenHash:
    def test_hash_format_and_determinism(self) -> None:
        token = "test_token_123"
        key = "secret_key"

        hash1 = get_token_hash(token, key)
        hash2 = get_token_hash(token, key)

        assert len(hash1) == 64
        assert all(c in "0123456789abcdef" for c in hash1)
        assert hash1 == hash2

    def test_different_inputs_produce_different_hashes(self) -> None:
        token1, token2 = "token_one", "token_two"
        key1, key2 = "key_one", "key_two"

        hash_diff_token = get_token_hash(token1, key1)
        hash_diff_token2 = get_token_hash(token2, key1)
        hash_diff_key = get_token_hash(token1, key2)

        assert hash_diff_token != hash_diff_token2
        assert hash_diff_token != hash_diff_key


class TestGenerateTokenHashPair:
    def test_token_structure_without_prefix(self) -> None:
        key = "test_key"
        token, hash_value = generate_token_hash_pair(key)

        assert isinstance(token, str)
        assert isinstance(hash_value, str)
        assert len(token) == 43
        assert len(hash_value) == 64

    def test_token_structure_with_prefix(self) -> None:
        key = "test_key"
        prefix = "auth_"
        token, _ = generate_token_hash_pair(key, prefix=prefix)

        assert token.startswith(prefix)
        assert len(token) == len(prefix) + 43

    def test_crc32_checksum_validity(self) -> None:
        key = "test_key"
        token, _ = generate_token_hash_pair(key)

        token_body = token[:37]
        checksum = token[-6:]

        expected_crc = zlib.crc32(token_body.encode("utf-8")) & 0xFFFFFFFF
        expected_checksum = _crc32_to_base62(expected_crc)

        assert len(checksum) == 6
        assert checksum == expected_checksum
        assert all(
            c in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            for c in checksum
        )
