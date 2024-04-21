from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="ExperienceLocationContents")


@_attrs_define
class ExperienceLocationContents:
    """
    Attributes:
        object_count (Union[Unset, int]):
        objects (Union[Unset, List[str]]):
    """

    object_count: Union[Unset, int] = UNSET
    objects: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_count = self.object_count

        objects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = self.objects

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_count is not UNSET:
            field_dict["objectCount"] = object_count
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_count = d.pop("objectCount", UNSET)

        objects = cast(List[str], d.pop("objects", UNSET))

        experience_location_contents = cls(
            object_count=object_count,
            objects=objects,
        )

        experience_location_contents.additional_properties = d
        return experience_location_contents

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
