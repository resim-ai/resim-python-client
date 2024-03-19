from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from ..types import UNSET, Unset
from typing import cast, List
from typing import Union

if TYPE_CHECKING:
  from ..models.experience_tag import ExperienceTag





T = TypeVar("T", bound="ExperienceTagInput")


@_attrs_define
class ExperienceTagInput:
    """ 
        Attributes:
            update_mask (Union[Unset, List[str]]):
            experience_tag (Union[Unset, ExperienceTag]):
     """

    update_mask: Union[Unset, List[str]] = UNSET
    experience_tag: Union[Unset, 'ExperienceTag'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.experience_tag import ExperienceTag
        update_mask: Union[Unset, List[str]] = UNSET
        if not isinstance(self.update_mask, Unset):
            update_mask = self.update_mask





        experience_tag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experience_tag, Unset):
            experience_tag = self.experience_tag.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if update_mask is not UNSET:
            field_dict["updateMask"] = update_mask
        if experience_tag is not UNSET:
            field_dict["experienceTag"] = experience_tag

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.experience_tag import ExperienceTag
        d = src_dict.copy()
        update_mask = cast(List[str], d.pop("updateMask", UNSET))


        _experience_tag = d.pop("experienceTag", UNSET)
        experience_tag: Union[Unset, ExperienceTag]
        if isinstance(_experience_tag,  Unset):
            experience_tag = UNSET
        else:
            experience_tag = ExperienceTag.from_dict(_experience_tag)




        experience_tag_input = cls(
            update_mask=update_mask,
            experience_tag=experience_tag,
        )

        experience_tag_input.additional_properties = d
        return experience_tag_input

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
