from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaunchProfile")


@_attrs_define
class LaunchProfile:
    """
    Attributes:
        gpus (Union[Unset, int]):
        launch_profile_id (Union[Unset, str]):
        memory_mib (Union[Unset, int]):
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        vcpus (Union[Unset, int]):
    """

    gpus: Union[Unset, int] = UNSET
    launch_profile_id: Union[Unset, str] = UNSET
    memory_mib: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    vcpus: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gpus = self.gpus
        launch_profile_id = self.launch_profile_id
        memory_mib = self.memory_mib
        name = self.name
        org_id = self.org_id
        user_id = self.user_id
        vcpus = self.vcpus

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if launch_profile_id is not UNSET:
            field_dict["launchProfileID"] = launch_profile_id
        if memory_mib is not UNSET:
            field_dict["memory_mib"] = memory_mib
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if vcpus is not UNSET:
            field_dict["vcpus"] = vcpus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gpus = d.pop("gpus", UNSET)

        launch_profile_id = d.pop("launchProfileID", UNSET)

        memory_mib = d.pop("memory_mib", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("orgID", UNSET)

        user_id = d.pop("userID", UNSET)

        vcpus = d.pop("vcpus", UNSET)

        launch_profile = cls(
            gpus=gpus,
            launch_profile_id=launch_profile_id,
            memory_mib=memory_mib,
            name=name,
            org_id=org_id,
            user_id=user_id,
            vcpus=vcpus,
        )

        launch_profile.additional_properties = d
        return launch_profile

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
