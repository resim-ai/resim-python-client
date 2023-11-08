from enum import Enum


class MetricStatus(str, Enum):
    FAILED = "FAILED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    PASSED = "PASSED"
    RAW = "RAW"

    def __str__(self) -> str:
        return str(self.value)
