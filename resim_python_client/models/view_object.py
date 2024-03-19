from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from typing import cast
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ViewObject")


@_attrs_define
class ViewObject:
    """ 
        Attributes:
            view_session_id (Union[Unset, str]):
            friendly_name (Union[Unset, str]):
            view_timestamp (Union[Unset, datetime.datetime]):
            object_count (Union[Unset, int]):
            mcap_url (Union[Unset, str]):
            view_url (Union[Unset, str]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
     """

    view_session_id: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    view_timestamp: Union[Unset, datetime.datetime] = UNSET
    object_count: Union[Unset, int] = UNSET
    mcap_url: Union[Unset, str] = UNSET
    view_url: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        view_session_id = self.view_session_id

        friendly_name = self.friendly_name

        view_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.view_timestamp, Unset):
            view_timestamp = self.view_timestamp.isoformat()

        object_count = self.object_count

        mcap_url = self.mcap_url

        view_url = self.view_url

        user_id = self.user_id

        org_id = self.org_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if view_session_id is not UNSET:
            field_dict["viewSessionID"] = view_session_id
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if view_timestamp is not UNSET:
            field_dict["viewTimestamp"] = view_timestamp
        if object_count is not UNSET:
            field_dict["objectCount"] = object_count
        if mcap_url is not UNSET:
            field_dict["mcapURL"] = mcap_url
        if view_url is not UNSET:
            field_dict["viewURL"] = view_url
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        view_session_id = d.pop("viewSessionID", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        _view_timestamp = d.pop("viewTimestamp", UNSET)
        view_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_view_timestamp,  Unset):
            view_timestamp = UNSET
        else:
            view_timestamp = isoparse(_view_timestamp)




        object_count = d.pop("objectCount", UNSET)

        mcap_url = d.pop("mcapURL", UNSET)

        view_url = d.pop("viewURL", UNSET)

        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        view_object = cls(
            view_session_id=view_session_id,
            friendly_name=friendly_name,
            view_timestamp=view_timestamp,
            object_count=object_count,
            mcap_url=mcap_url,
            view_url=view_url,
            user_id=user_id,
            org_id=org_id,
        )

        view_object.additional_properties = d
        return view_object

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
