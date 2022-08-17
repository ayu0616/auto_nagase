from typing import TypedDict


class TaskItem(TypedDict):
    as_id: str
    code: str
    count: int
    deadline: str
    defective: bool
    file_name: str
    previous: bool
    school_name: str
    score: str
    status: str
    student_code: int
    student_name: str
    type: str
    outline: str
    uploaded: bool
