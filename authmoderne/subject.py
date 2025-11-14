import typing

from authmoderne.models import model_protocol


@model_protocol
class Subject(typing.Protocol):
    id: typing.Any


__all__ = ["Subject"]
