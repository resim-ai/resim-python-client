from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Union


T = TypeVar("T", bound="ExperienceObjectDescription")


@_attrs_define
class ExperienceObjectDescription:
    """
    Attributes:
        description (Union[Unset, str]):
        location (Union[Unset, str]):
        name (Union[Unset, str]):
        project_name (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
    """

    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        location = self.location

        name = self.name

        project_name = self.project_name

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        project_name = d.pop("projectName", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        experience_object_description = cls(
            description=description,
            location=location,
            name=name,
            project_name=project_name,
            tags=tags,
        )

        experience_object_description.additional_properties = d
        return experience_object_description

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
