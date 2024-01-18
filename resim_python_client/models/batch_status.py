from enum import Enum


class BatchStatus(str, Enum):
    BATCH_METRICS_QUEUED = "BATCH_METRICS_QUEUED"
    BATCH_METRICS_RUNNING = "BATCH_METRICS_RUNNING"
    CANCELLED = "CANCELLED"
    EXPERIENCES_RUNNING = "EXPERIENCES_RUNNING"
    FAILED = "FAILED"
    SUBMITTED = "SUBMITTED"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
