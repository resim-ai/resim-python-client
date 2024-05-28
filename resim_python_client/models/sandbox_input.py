from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_specification import SandboxSpecification


T = TypeVar("T", bound="SandboxInput")


@_attrs_define
class SandboxInput:
    """
    Attributes:
        org_id (Union[Unset, str]):
        sandbox_specification (Union[Unset, SandboxSpecification]):
        user_id (Union[Unset, str]):
    """

    org_id: Union[Unset, str] = UNSET
    sandbox_specification: Union[Unset, "SandboxSpecification"] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        org_id = self.org_id
        sandbox_specification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_specification, Unset):
            sandbox_specification = self.sandbox_specification.to_dict()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if sandbox_specification is not UNSET:
            field_dict["sandboxSpecification"] = sandbox_specification
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sandbox_specification import SandboxSpecification

        d = src_dict.copy()
        org_id = d.pop("orgID", UNSET)

        _sandbox_specification = d.pop("sandboxSpecification", UNSET)
        sandbox_specification: Union[Unset, SandboxSpecification]
        if isinstance(_sandbox_specification, Unset):
            sandbox_specification = UNSET
        else:
            sandbox_specification = SandboxSpecification.from_dict(_sandbox_specification)

        user_id = d.pop("userID", UNSET)

        sandbox_input = cls(
            org_id=org_id,
            sandbox_specification=sandbox_specification,
            user_id=user_id,
        )

        sandbox_input.additional_properties = d
        return sandbox_input

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
