from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Union


T = TypeVar("T", bound="TestSuiteObjectDescription")


@_attrs_define
class TestSuiteObjectDescription:
    """
    Attributes:
        experience_names (Union[Unset, List[str]]):
        metrics_build_name (Union[Unset, str]):
        metrics_build_version (Union[Unset, str]):
        project_name (Union[Unset, str]):
        system_name (Union[Unset, str]):
        test_suite_description (Union[Unset, str]):
        test_suite_name (Union[Unset, str]):
    """

    experience_names: Union[Unset, List[str]] = UNSET
    metrics_build_name: Union[Unset, str] = UNSET
    metrics_build_version: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    system_name: Union[Unset, str] = UNSET
    test_suite_description: Union[Unset, str] = UNSET
    test_suite_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        experience_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experience_names, Unset):
            experience_names = self.experience_names

        metrics_build_name = self.metrics_build_name

        metrics_build_version = self.metrics_build_version

        project_name = self.project_name

        system_name = self.system_name

        test_suite_description = self.test_suite_description

        test_suite_name = self.test_suite_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if experience_names is not UNSET:
            field_dict["experienceNames"] = experience_names
        if metrics_build_name is not UNSET:
            field_dict["metricsBuildName"] = metrics_build_name
        if metrics_build_version is not UNSET:
            field_dict["metricsBuildVersion"] = metrics_build_version
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if test_suite_description is not UNSET:
            field_dict["testSuiteDescription"] = test_suite_description
        if test_suite_name is not UNSET:
            field_dict["testSuiteName"] = test_suite_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        experience_names = cast(List[str], d.pop("experienceNames", UNSET))

        metrics_build_name = d.pop("metricsBuildName", UNSET)

        metrics_build_version = d.pop("metricsBuildVersion", UNSET)

        project_name = d.pop("projectName", UNSET)

        system_name = d.pop("systemName", UNSET)

        test_suite_description = d.pop("testSuiteDescription", UNSET)

        test_suite_name = d.pop("testSuiteName", UNSET)

        test_suite_object_description = cls(
            experience_names=experience_names,
            metrics_build_name=metrics_build_name,
            metrics_build_version=metrics_build_version,
            project_name=project_name,
            system_name=system_name,
            test_suite_description=test_suite_description,
            test_suite_name=test_suite_name,
        )

        test_suite_object_description.additional_properties = d
        return test_suite_object_description

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
