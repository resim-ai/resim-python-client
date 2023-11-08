from enum import Enum


class JobStatus(str, Enum):
    CANCELLED = "CANCELLED"
    EXPERIENCE_RUNNING = "EXPERIENCE_RUNNING"
    FAILED = "FAILED"
    METRICS_QUEUED = "METRICS_QUEUED"
    METRICS_RUNNING = "METRICS_RUNNING"
    SUBMITTED = "SUBMITTED"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
