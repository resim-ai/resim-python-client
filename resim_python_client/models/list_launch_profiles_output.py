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





T = TypeVar("T", bound="ListLaunchProfilesOutput")


@_attrs_define
class ListLaunchProfilesOutput:
    """ 
        Attributes:
            launch_profiles (Union[Unset, List['LaunchProfile']]):
            next_page_token (Union[Unset, str]):
     """

    launch_profiles: Union[Unset, List['LaunchProfile']] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.launch_profile import LaunchProfile
        launch_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.launch_profiles, Unset):
            launch_profiles = []
            for launch_profiles_item_data in self.launch_profiles:
                launch_profiles_item = launch_profiles_item_data.to_dict()
                launch_profiles.append(launch_profiles_item)





        next_page_token = self.next_page_token


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if launch_profiles is not UNSET:
            field_dict["launchProfiles"] = launch_profiles
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.launch_profile import LaunchProfile
        d = src_dict.copy()
        launch_profiles = []
        _launch_profiles = d.pop("launchProfiles", UNSET)
        for launch_profiles_item_data in (_launch_profiles or []):
            launch_profiles_item = LaunchProfile.from_dict(launch_profiles_item_data)



            launch_profiles.append(launch_profiles_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        list_launch_profiles_output = cls(
            launch_profiles=launch_profiles,
            next_page_token=next_page_token,
        )

        list_launch_profiles_output.additional_properties = d
        return list_launch_profiles_output

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
