"""Utilities and helpers for cryptographic operations."""

import hashlib
import hmac
import secrets
import string
import zlib


def _crc32_to_base62(number: int) -> str:
    """
    Convert a 32-bit integer to a base62 string.

    Args:
        number: The 32-bit integer to convert.

    Returns:
        The base62 encoded string.
    """
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base = len(characters)
    encoded = ""
    while number:
        number, remainder = divmod(number, base)
        encoded = characters[remainder] + encoded
    return encoded.zfill(6)  # Ensure the checksum is 6 characters long


def _generate_token(*, prefix: str = "") -> str:
    """
    Generate a random token with a CRC32 checksum.

    Args:
        prefix: An optional prefix to prepend to the token.

    Returns:
        The generated token with checksum.
    """
    # Generate a high entropy random token
    token = "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(37)
    )

    # Calculate a 32-bit CRC checksum
    checksum = zlib.crc32(token.encode("utf-8")) & 0xFFFFFFFF
    checksum_base62 = _crc32_to_base62(checksum)

    # Concatenate the prefix, token, and checksum
    return f"{prefix}{token}{checksum_base62}"


def get_token_hash(token: str, key: str) -> str:
    """
    Calculate the HMAC-SHA256 hash of a token.

    Args:
        token: The token to hash.
        key: The secret key used for HMAC.

    Returns:
        The hexadecimal representation of the HMAC-SHA256 hash.
    """
    hash = hmac.new(key.encode("ascii"), token.encode("ascii"), hashlib.sha256)
    return hash.hexdigest()


def generate_token_hash_pair(key: str, *, prefix: str = "") -> tuple[str, str]:
    """
    Generate a token and its corresponding HMAC-SHA256 hash. Only the latter
    should be stored in a database.

    The token includes a CRC32 checksum for integrity verification.

    It follows the GitHub recommendations for token generation:
        https://github.blog/engineering/platform-security/behind-githubs-new-authentication-token-formats/

    Args:
        key: The secret key used for HMAC.
        prefix: An optional prefix to prepend to the token.

    Returns:
        A tuple containing the generated token and its HMAC-SHA256 hash.
    """

    token = _generate_token(prefix=prefix)
    return token, get_token_hash(token, key=key)


__all__ = ["generate_token_hash_pair", "get_token_hash"]
