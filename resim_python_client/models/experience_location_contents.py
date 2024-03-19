from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, List
from typing import Union






T = TypeVar("T", bound="ExperienceLocationContents")


@_attrs_define
class ExperienceLocationContents:
    """ 
        Attributes:
            objects (Union[Unset, List[str]]):
            object_count (Union[Unset, int]):
     """

    objects: Union[Unset, List[str]] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = self.objects





        object_count = self.object_count


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if objects is not UNSET:
            field_dict["objects"] = objects
        if object_count is not UNSET:
            field_dict["objectCount"] = object_count

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        objects = cast(List[str], d.pop("objects", UNSET))


        object_count = d.pop("objectCount", UNSET)

        experience_location_contents = cls(
            objects=objects,
            object_count=object_count,
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
