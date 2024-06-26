from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.update_system_fields import UpdateSystemFields


T = TypeVar("T", bound="UpdateSystemInput")


@_attrs_define
class UpdateSystemInput:
    """
    Attributes:
        system (Union[Unset, UpdateSystemFields]):
        update_mask (Union[Unset, List[str]]):
    """

    system: Union[Unset, "UpdateSystemFields"] = UNSET
    update_mask: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        system: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        update_mask: Union[Unset, List[str]] = UNSET
        if not isinstance(self.update_mask, Unset):
            update_mask = self.update_mask

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system is not UNSET:
            field_dict["system"] = system
        if update_mask is not UNSET:
            field_dict["updateMask"] = update_mask

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_system_fields import UpdateSystemFields

        d = src_dict.copy()
        _system = d.pop("system", UNSET)
        system: Union[Unset, UpdateSystemFields]
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = UpdateSystemFields.from_dict(_system)

        update_mask = cast(List[str], d.pop("updateMask", UNSET))

        update_system_input = cls(
            system=system,
            update_mask=update_mask,
        )

        update_system_input.additional_properties = d
        return update_system_input

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
