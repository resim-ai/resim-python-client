from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..models.branch_type import BranchType


T = TypeVar("T", bound="BranchObjectDescription")


@_attrs_define
class BranchObjectDescription:
    """
    Attributes:
        name (Union[Unset, str]):
        project_name (Union[Unset, str]):
        type (Union[Unset, BranchType]):
    """

    name: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    type: Union[Unset, BranchType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        project_name = self.project_name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        project_name = d.pop("projectName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, BranchType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = BranchType(_type)

        branch_object_description = cls(
            name=name,
            project_name=project_name,
            type=type,
        )

        branch_object_description.additional_properties = d
        return branch_object_description

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
