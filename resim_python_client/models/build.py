import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Build")


@_attrs_define
class Build:
    """
    Attributes:
        branch_id (Union[Unset, str]):
        build_id (Union[Unset, str]):
        creation_timestamp (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        image_uri (Union[Unset, str]):
        org_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    branch_id: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    image_uri: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch_id = self.branch_id
        build_id = self.build_id
        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        description = self.description
        image_uri = self.image_uri
        org_id = self.org_id
        project_id = self.project_id
        user_id = self.user_id
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_id is not UNSET:
            field_dict["branchID"] = branch_id
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if image_uri is not UNSET:
            field_dict["imageUri"] = image_uri
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch_id = d.pop("branchID", UNSET)

        build_id = d.pop("buildID", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp, Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)

        description = d.pop("description", UNSET)

        image_uri = d.pop("imageUri", UNSET)

        org_id = d.pop("orgID", UNSET)

        project_id = d.pop("projectID", UNSET)

        user_id = d.pop("userID", UNSET)

        version = d.pop("version", UNSET)

        build = cls(
            branch_id=branch_id,
            build_id=build_id,
            creation_timestamp=creation_timestamp,
            description=description,
            image_uri=image_uri,
            org_id=org_id,
            project_id=project_id,
            user_id=user_id,
            version=version,
        )

        build.additional_properties = d
        return build

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
