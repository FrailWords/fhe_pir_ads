from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IndexTreeResponse(_message.Message):
    __slots__ = ["idx_tree"]
    IDX_TREE_FIELD_NUMBER: _ClassVar[int]
    idx_tree: str
    def __init__(self, idx_tree: _Optional[str] = ...) -> None: ...

class PirRequest(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: bytes
    def __init__(self, request: _Optional[bytes] = ...) -> None: ...

class PirResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: bytes
    def __init__(self, response: _Optional[bytes] = ...) -> None: ...
