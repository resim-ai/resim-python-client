from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="ViewSessionUpdate")


@_attrs_define
class ViewSessionUpdate:
    """
    Attributes:
        id (Union[Unset, str]):
        mcap (Union[Unset, str]):
        view (Union[Unset, str]): A link to view the session.
    """

    id: Union[Unset, str] = UNSET
    mcap: Union[Unset, str] = UNSET
    view: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        mcap = self.mcap

        view = self.view

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mcap is not UNSET:
            field_dict["mcap"] = mcap
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mcap = d.pop("mcap", UNSET)

        view = d.pop("view", UNSET)

        view_session_update = cls(
            id=id,
            mcap=mcap,
            view=view,
        )

        view_session_update.additional_properties = d
        return view_session_update

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
