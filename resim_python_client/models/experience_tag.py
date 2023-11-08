import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperienceTag")


@_attrs_define
class ExperienceTag:
    """
    Attributes:
        creation_timestamp (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        experience_tag_id (Union[Unset, str]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    experience_tag_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        description = self.description
        experience_tag_id = self.experience_tag_id
        name = self.name
        org_id = self.org_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if experience_tag_id is not UNSET:
            field_dict["experienceTagID"] = experience_tag_id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id

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

        description = d.pop("description", UNSET)

        experience_tag_id = d.pop("experienceTagID", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("orgID", UNSET)

        user_id = d.pop("userID", UNSET)

        experience_tag = cls(
            creation_timestamp=creation_timestamp,
            description=description,
            experience_tag_id=experience_tag_id,
            name=name,
            org_id=org_id,
            user_id=user_id,
        )

        experience_tag.additional_properties = d
        return experience_tag

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
