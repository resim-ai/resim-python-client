import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.batch_status import BatchStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Batch")


@_attrs_define
class Batch:
    """
    Attributes:
        batch_id (Union[Unset, str]):
        build_id (Union[Unset, str]):
        creation_timestamp (Union[Unset, datetime.datetime]):
        friendly_name (Union[Unset, str]):
        instantiated_experience_i_ds (Union[Unset, List[str]]):
        instantiated_experience_tag_i_ds (Union[Unset, List[str]]):
        metrics_build_id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        status (Union[Unset, BatchStatus]):
        user_id (Union[Unset, str]):
    """

    batch_id: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    instantiated_experience_i_ds: Union[Unset, List[str]] = UNSET
    instantiated_experience_tag_i_ds: Union[Unset, List[str]] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    status: Union[Unset, BatchStatus] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_id = self.batch_id
        build_id = self.build_id
        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        friendly_name = self.friendly_name
        instantiated_experience_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instantiated_experience_i_ds, Unset):
            instantiated_experience_i_ds = self.instantiated_experience_i_ds

        instantiated_experience_tag_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instantiated_experience_tag_i_ds, Unset):
            instantiated_experience_tag_i_ds = self.instantiated_experience_tag_i_ds

        metrics_build_id = self.metrics_build_id
        org_id = self.org_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if instantiated_experience_i_ds is not UNSET:
            field_dict["instantiatedExperienceIDs"] = instantiated_experience_i_ds
        if instantiated_experience_tag_i_ds is not UNSET:
            field_dict["instantiatedExperienceTagIDs"] = instantiated_experience_tag_i_ds
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if status is not UNSET:
            field_dict["status"] = status
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        batch_id = d.pop("batchID", UNSET)

        build_id = d.pop("buildID", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp, Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)

        friendly_name = d.pop("friendlyName", UNSET)

        instantiated_experience_i_ds = cast(List[str], d.pop("instantiatedExperienceIDs", UNSET))

        instantiated_experience_tag_i_ds = cast(List[str], d.pop("instantiatedExperienceTagIDs", UNSET))

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        org_id = d.pop("orgID", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BatchStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BatchStatus(_status)

        user_id = d.pop("userID", UNSET)

        batch = cls(
            batch_id=batch_id,
            build_id=build_id,
            creation_timestamp=creation_timestamp,
            friendly_name=friendly_name,
            instantiated_experience_i_ds=instantiated_experience_i_ds,
            instantiated_experience_tag_i_ds=instantiated_experience_tag_i_ds,
            metrics_build_id=metrics_build_id,
            org_id=org_id,
            status=status,
            user_id=user_id,
        )

        batch.additional_properties = d
        return batch

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
