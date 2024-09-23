from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Union

if TYPE_CHECKING:
    from ..models.experience_filter_input import ExperienceFilterInput


T = TypeVar("T", bound="CreateTestSuiteInput")


@_attrs_define
class CreateTestSuiteInput:
    """
    Attributes:
        description (str):
        experiences (List[str]):
        name (str):
        system_id (str):
        all_experiences (Union[Unset, bool]):
        excluded_experience_i_ds (Union[Unset, List[str]]):
        filters (Union[Unset, ExperienceFilterInput]):
        metrics_build_id (Union[Unset, str]):
    """

    description: str
    experiences: List[str]
    name: str
    system_id: str
    all_experiences: Union[Unset, bool] = UNSET
    excluded_experience_i_ds: Union[Unset, List[str]] = UNSET
    filters: Union[Unset, "ExperienceFilterInput"] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        experiences = self.experiences

        name = self.name

        system_id = self.system_id

        all_experiences = self.all_experiences

        excluded_experience_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_experience_i_ds, Unset):
            excluded_experience_i_ds = self.excluded_experience_i_ds

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        metrics_build_id = self.metrics_build_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "experiences": experiences,
                "name": name,
                "systemID": system_id,
            }
        )
        if all_experiences is not UNSET:
            field_dict["allExperiences"] = all_experiences
        if excluded_experience_i_ds is not UNSET:
            field_dict["excludedExperienceIDs"] = excluded_experience_i_ds
        if filters is not UNSET:
            field_dict["filters"] = filters
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.experience_filter_input import ExperienceFilterInput

        d = src_dict.copy()
        description = d.pop("description")

        experiences = cast(List[str], d.pop("experiences"))

        name = d.pop("name")

        system_id = d.pop("systemID")

        all_experiences = d.pop("allExperiences", UNSET)

        excluded_experience_i_ds = cast(
            List[str], d.pop("excludedExperienceIDs", UNSET)
        )

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ExperienceFilterInput]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ExperienceFilterInput.from_dict(_filters)

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        create_test_suite_input = cls(
            description=description,
            experiences=experiences,
            name=name,
            system_id=system_id,
            all_experiences=all_experiences,
            excluded_experience_i_ds=excluded_experience_i_ds,
            filters=filters,
            metrics_build_id=metrics_build_id,
        )

        create_test_suite_input.additional_properties = d
        return create_test_suite_input

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
