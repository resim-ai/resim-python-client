from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import cast
import datetime
from dateutil.parser import isoparse
from ..models.event_timestamp_type import EventTimestampType
from ..models.metric_status import MetricStatus


T = TypeVar("T", bound="EventInput")


@_attrs_define
class EventInput:
    """
    Attributes:
        description (str):
        metrics_i_ds (List[str]):
        name (str):
        status (MetricStatus):
        tags (List[str]):
        timestamp (datetime.datetime):
        timestamp_type (EventTimestampType):
    """

    description: str
    metrics_i_ds: List[str]
    name: str
    status: MetricStatus
    tags: List[str]
    timestamp: datetime.datetime
    timestamp_type: EventTimestampType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        metrics_i_ds = self.metrics_i_ds

        name = self.name

        status = self.status.value

        tags = self.tags

        timestamp = self.timestamp.isoformat()

        timestamp_type = self.timestamp_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "metricsIDs": metrics_i_ds,
                "name": name,
                "status": status,
                "tags": tags,
                "timestamp": timestamp,
                "timestampType": timestamp_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        metrics_i_ds = cast(List[str], d.pop("metricsIDs"))

        name = d.pop("name")

        status = MetricStatus(d.pop("status"))

        tags = cast(List[str], d.pop("tags"))

        timestamp = isoparse(d.pop("timestamp"))

        timestamp_type = EventTimestampType(d.pop("timestampType"))

        event_input = cls(
            description=description,
            metrics_i_ds=metrics_i_ds,
            name=name,
            status=status,
            tags=tags,
            timestamp=timestamp,
            timestamp_type=timestamp_type,
        )

        event_input.additional_properties = d
        return event_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
