from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experience_filter_input import ExperienceFilterInput


T = TypeVar("T", bound="SelectExperiencesInput")


@_attrs_define
class SelectExperiencesInput:
    """
    Attributes:
        all_experiences (Union[Unset, bool]):
        experiences (Union[Unset, List[str]]):
        filters (Union[Unset, ExperienceFilterInput]):
    """

    all_experiences: Union[Unset, bool] = UNSET
    experiences: Union[Unset, List[str]] = UNSET
    filters: Union[Unset, "ExperienceFilterInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_experiences = self.all_experiences

        experiences: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experiences, Unset):
            experiences = self.experiences

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_experiences is not UNSET:
            field_dict["allExperiences"] = all_experiences
        if experiences is not UNSET:
            field_dict["experiences"] = experiences
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.experience_filter_input import ExperienceFilterInput

        d = src_dict.copy()
        all_experiences = d.pop("allExperiences", UNSET)

        experiences = cast(List[str], d.pop("experiences", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ExperienceFilterInput]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ExperienceFilterInput.from_dict(_filters)

        select_experiences_input = cls(
            all_experiences=all_experiences,
            experiences=experiences,
            filters=filters,
        )

        select_experiences_input.additional_properties = d
        return select_experiences_input

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
