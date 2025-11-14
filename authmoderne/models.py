def model_protocol[C](cls: type[C]) -> type[C]:
    """
    Stubbed version of typing.runtime_protocol so our models protocol
    can both:

    * Work with dishka's runtime type checking resolver.
    * Don't complain because of our property methods.

    Args:
        cls: The protocol class to mark as a runtime protocol.

    Returns:
        The same class marked as a runtime protocol.
    """
    setattr(cls, "_is_runtime_protocol", True)
    setattr(cls, "__non_callable_proto_members__", set())
    return cls


__all__ = ["model_protocol"]
