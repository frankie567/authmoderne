import typing


class Subject[SubjectID](typing.Protocol):
    id: SubjectID


__all__ = ["Subject"]
