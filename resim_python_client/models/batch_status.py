from enum import Enum


class BatchStatus(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    SUBMITTED = "SUBMITTED"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
