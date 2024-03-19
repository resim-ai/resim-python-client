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
  from ..models.build import Build





T = TypeVar("T", bound="ListBuildsOutput")


@_attrs_define
class ListBuildsOutput:
    """ 
        Attributes:
            builds (Union[Unset, List['Build']]):
            next_page_token (Union[Unset, str]):
     """

    builds: Union[Unset, List['Build']] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.build import Build
        builds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.builds, Unset):
            builds = []
            for builds_item_data in self.builds:
                builds_item = builds_item_data.to_dict()
                builds.append(builds_item)





        next_page_token = self.next_page_token


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if builds is not UNSET:
            field_dict["builds"] = builds
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.build import Build
        d = src_dict.copy()
        builds = []
        _builds = d.pop("builds", UNSET)
        for builds_item_data in (_builds or []):
            builds_item = Build.from_dict(builds_item_data)



            builds.append(builds_item)


        next_page_token = d.pop("nextPageToken", UNSET)

        list_builds_output = cls(
            builds=builds,
            next_page_token=next_page_token,
        )

        list_builds_output.additional_properties = d
        return list_builds_output

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
