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
  from ..models.launch_profile import LaunchProfile





T = TypeVar("T", bound="LaunchProfileInput")


@_attrs_define
class LaunchProfileInput:
    """ 
        Attributes:
            update_mask (Union[Unset, List[str]]):
            launch_profile (Union[Unset, LaunchProfile]):
     """

    update_mask: Union[Unset, List[str]] = UNSET
    launch_profile: Union[Unset, 'LaunchProfile'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.launch_profile import LaunchProfile
        update_mask: Union[Unset, List[str]] = UNSET
        if not isinstance(self.update_mask, Unset):
            update_mask = self.update_mask





        launch_profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch_profile, Unset):
            launch_profile = self.launch_profile.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if update_mask is not UNSET:
            field_dict["updateMask"] = update_mask
        if launch_profile is not UNSET:
            field_dict["launchProfile"] = launch_profile

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.launch_profile import LaunchProfile
        d = src_dict.copy()
        update_mask = cast(List[str], d.pop("updateMask", UNSET))


        _launch_profile = d.pop("launchProfile", UNSET)
        launch_profile: Union[Unset, LaunchProfile]
        if isinstance(_launch_profile,  Unset):
            launch_profile = UNSET
        else:
            launch_profile = LaunchProfile.from_dict(_launch_profile)




        launch_profile_input = cls(
            update_mask=update_mask,
            launch_profile=launch_profile,
        )

        launch_profile_input.additional_properties = d
        return launch_profile_input

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
