from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast


T = TypeVar("T", bound="CreateTestSuiteInput")


@_attrs_define
class CreateTestSuiteInput:
    """
    Attributes:
        description (str):
        experiences (List[str]):
        name (str):
        system_id (str):
        metrics_build_id (Union[Unset, str]):
    """

    description: str
    experiences: List[str]
    name: str
    system_id: str
    metrics_build_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        experiences = self.experiences

        name = self.name

        system_id = self.system_id

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
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        experiences = cast(List[str], d.pop("experiences"))

        name = d.pop("name")

        system_id = d.pop("systemID")

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        create_test_suite_input = cls(
            description=description,
            experiences=experiences,
            name=name,
            system_id=system_id,
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
