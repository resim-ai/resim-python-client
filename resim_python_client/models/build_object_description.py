from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="BuildObjectDescription")


@_attrs_define
class BuildObjectDescription:
    """
    Attributes:
        branch_name (Union[Unset, str]):
        description (Union[Unset, str]):
        image (Union[Unset, str]):
        project_name (Union[Unset, str]):
        system_name (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    branch_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    system_name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch_name = self.branch_name

        description = self.description

        image = self.image

        project_name = self.project_name

        system_name = self.system_name

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_name is not UNSET:
            field_dict["branchName"] = branch_name
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch_name = d.pop("branchName", UNSET)

        description = d.pop("description", UNSET)

        image = d.pop("image", UNSET)

        project_name = d.pop("projectName", UNSET)

        system_name = d.pop("systemName", UNSET)

        version = d.pop("version", UNSET)

        build_object_description = cls(
            branch_name=branch_name,
            description=description,
            image=image,
            project_name=project_name,
            system_name=system_name,
            version=version,
        )

        build_object_description.additional_properties = d
        return build_object_description

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
