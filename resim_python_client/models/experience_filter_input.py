from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="ExperienceFilterInput")


@_attrs_define
class ExperienceFilterInput:
    """
    Attributes:
        name (Union[Unset, str]): Filter experiences by name
        search (Union[Unset, str]): A search query. Supports searching by tag_id Example: tag_id IN
            ("71b96a67-9990-426b-993e-0f3d9c6bbe48").
        text (Union[Unset, str]): Filter experiences by a text string on name and description
    """

    name: Union[Unset, str] = UNSET
    search: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        search = self.search

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if search is not UNSET:
            field_dict["search"] = search
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        search = d.pop("search", UNSET)

        text = d.pop("text", UNSET)

        experience_filter_input = cls(
            name=name,
            search=search,
            text=text,
        )

        experience_filter_input.additional_properties = d
        return experience_filter_input

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
