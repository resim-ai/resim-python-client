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
  from ..models.experience import Experience





T = TypeVar("T", bound="ExperienceInput")


@_attrs_define
class ExperienceInput:
    """ 
        Attributes:
            update_mask (Union[Unset, List[str]]):
            experience (Union[Unset, Experience]):
     """

    update_mask: Union[Unset, List[str]] = UNSET
    experience: Union[Unset, 'Experience'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.experience import Experience
        update_mask: Union[Unset, List[str]] = UNSET
        if not isinstance(self.update_mask, Unset):
            update_mask = self.update_mask





        experience: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if update_mask is not UNSET:
            field_dict["updateMask"] = update_mask
        if experience is not UNSET:
            field_dict["experience"] = experience

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.experience import Experience
        d = src_dict.copy()
        update_mask = cast(List[str], d.pop("updateMask", UNSET))


        _experience = d.pop("experience", UNSET)
        experience: Union[Unset, Experience]
        if isinstance(_experience,  Unset):
            experience = UNSET
        else:
            experience = Experience.from_dict(_experience)




        experience_input = cls(
            update_mask=update_mask,
            experience=experience,
        )

        experience_input.additional_properties = d
        return experience_input

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
