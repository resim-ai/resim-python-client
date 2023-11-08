import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricsBuild")


@_attrs_define
class MetricsBuild:
    """
    Attributes:
        creation_timestamp (Union[Unset, datetime.datetime]):
        image_uri (Union[Unset, str]):
        metrics_build_id (Union[Unset, str]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    image_uri: Union[Unset, str] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        image_uri = self.image_uri
        metrics_build_id = self.metrics_build_id
        name = self.name
        org_id = self.org_id
        user_id = self.user_id
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if image_uri is not UNSET:
            field_dict["imageUri"] = image_uri
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if version is not UNSET:
            field_dict["version"] = version

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

        image_uri = d.pop("imageUri", UNSET)

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("orgID", UNSET)

        user_id = d.pop("userID", UNSET)

        version = d.pop("version", UNSET)

        metrics_build = cls(
            creation_timestamp=creation_timestamp,
            image_uri=image_uri,
            metrics_build_id=metrics_build_id,
            name=name,
            org_id=org_id,
            user_id=user_id,
            version=version,
        )

        metrics_build.additional_properties = d
        return metrics_build

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
