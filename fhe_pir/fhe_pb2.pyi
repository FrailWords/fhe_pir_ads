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

class PirContext(_message.Message):
    __slots__ = ["ctx"]
    CTX_FIELD_NUMBER: _ClassVar[int]
    ctx: bytes
    def __init__(self, ctx: _Optional[bytes] = ...) -> None: ...

class PirRequest(_message.Message):
    __slots__ = ["col", "row"]
    COL_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    col: bytes
    row: bytes
    def __init__(self, row: _Optional[bytes] = ..., col: _Optional[bytes] = ...) -> None: ...

class PirResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: bytes
    def __init__(self, response: _Optional[bytes] = ...) -> None: ...
