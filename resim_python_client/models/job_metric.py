import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.metric_status import MetricStatus
from ..models.metric_type import MetricType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobMetric")


@_attrs_define
class JobMetric:
    """
    Attributes:
        creation_timestamp (Union[Unset, datetime.datetime]):
        data_i_ds (Union[Unset, List[str]]):
        event_metric (Union[Unset, bool]): true if this metric is for an event
        file_location (Union[Unset, str]):
        metric_id (Union[Unset, str]):
        metric_url (Union[Unset, str]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        status (Union[Unset, MetricStatus]):
        type (Union[Unset, MetricType]):
        user_id (Union[Unset, str]):
        value (Union[Unset, None, float]):
        batch_id (Union[Unset, str]):
        job_id (Union[Unset, str]):
    """

    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    data_i_ds: Union[Unset, List[str]] = UNSET
    event_metric: Union[Unset, bool] = UNSET
    file_location: Union[Unset, str] = UNSET
    metric_id: Union[Unset, str] = UNSET
    metric_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    status: Union[Unset, MetricStatus] = UNSET
    type: Union[Unset, MetricType] = UNSET
    user_id: Union[Unset, str] = UNSET
    value: Union[Unset, None, float] = UNSET
    batch_id: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        data_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data_i_ds, Unset):
            data_i_ds = self.data_i_ds

        event_metric = self.event_metric
        file_location = self.file_location
        metric_id = self.metric_id
        metric_url = self.metric_url
        name = self.name
        org_id = self.org_id
        project_id = self.project_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        user_id = self.user_id
        value = self.value
        batch_id = self.batch_id
        job_id = self.job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if data_i_ds is not UNSET:
            field_dict["dataIDs"] = data_i_ds
        if event_metric is not UNSET:
            field_dict["eventMetric"] = event_metric
        if file_location is not UNSET:
            field_dict["fileLocation"] = file_location
        if metric_id is not UNSET:
            field_dict["metricID"] = metric_id
        if metric_url is not UNSET:
            field_dict["metricURL"] = metric_url
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if value is not UNSET:
            field_dict["value"] = value
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if job_id is not UNSET:
            field_dict["jobID"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp, Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)

        data_i_ds = cast(List[str], d.pop("dataIDs", UNSET))

        event_metric = d.pop("eventMetric", UNSET)

        file_location = d.pop("fileLocation", UNSET)

        metric_id = d.pop("metricID", UNSET)

        metric_url = d.pop("metricURL", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("orgID", UNSET)

        project_id = d.pop("projectID", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MetricStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MetricStatus(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, MetricType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = MetricType(_type)

        user_id = d.pop("userID", UNSET)

        value = d.pop("value", UNSET)

        batch_id = d.pop("batchID", UNSET)

        job_id = d.pop("jobID", UNSET)

        job_metric = cls(
            creation_timestamp=creation_timestamp,
            data_i_ds=data_i_ds,
            event_metric=event_metric,
            file_location=file_location,
            metric_id=metric_id,
            metric_url=metric_url,
            name=name,
            org_id=org_id,
            project_id=project_id,
            status=status,
            type=type,
            user_id=user_id,
            value=value,
            batch_id=batch_id,
            job_id=job_id,
        )

        job_metric.additional_properties = d
        return job_metric

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
