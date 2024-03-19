from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="LaunchProfile")


@_attrs_define
class LaunchProfile:
    """ 
        Attributes:
            launch_profile_id (Union[Unset, str]):
            project_id (Union[Unset, str]):
            name (Union[Unset, str]):
            vcpus (Union[Unset, int]):
            memory_mib (Union[Unset, int]):
            gpus (Union[Unset, int]):
            shared_memory_mb (Union[Unset, int]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
     """

    launch_profile_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    vcpus: Union[Unset, int] = UNSET
    memory_mib: Union[Unset, int] = UNSET
    gpus: Union[Unset, int] = UNSET
    shared_memory_mb: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        launch_profile_id = self.launch_profile_id

        project_id = self.project_id

        name = self.name

        vcpus = self.vcpus

        memory_mib = self.memory_mib

        gpus = self.gpus

        shared_memory_mb = self.shared_memory_mb

        user_id = self.user_id

        org_id = self.org_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if launch_profile_id is not UNSET:
            field_dict["launchProfileID"] = launch_profile_id
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if vcpus is not UNSET:
            field_dict["vcpus"] = vcpus
        if memory_mib is not UNSET:
            field_dict["memory_mib"] = memory_mib
        if gpus is not UNSET:
            field_dict["gpus"] = gpus
        if shared_memory_mb is not UNSET:
            field_dict["shared_memory_mb"] = shared_memory_mb
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        launch_profile_id = d.pop("launchProfileID", UNSET)

        project_id = d.pop("projectID", UNSET)

        name = d.pop("name", UNSET)

        vcpus = d.pop("vcpus", UNSET)

        memory_mib = d.pop("memory_mib", UNSET)

        gpus = d.pop("gpus", UNSET)

        shared_memory_mb = d.pop("shared_memory_mb", UNSET)

        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        launch_profile = cls(
            launch_profile_id=launch_profile_id,
            project_id=project_id,
            name=name,
            vcpus=vcpus,
            memory_mib=memory_mib,
            gpus=gpus,
            shared_memory_mb=shared_memory_mb,
            user_id=user_id,
            org_id=org_id,
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
