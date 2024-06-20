from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union


T = TypeVar("T", bound="TestSuiteRunObjectDescription")


@_attrs_define
class TestSuiteRunObjectDescription:
    """
    Attributes:
        associated_account (Union[Unset, str]):
        build_branch_name (Union[Unset, str]):
        build_version (Union[Unset, str]):
        project_name (Union[Unset, str]):
        test_suite_name (Union[Unset, str]):
    """

    associated_account: Union[Unset, str] = UNSET
    build_branch_name: Union[Unset, str] = UNSET
    build_version: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    test_suite_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        associated_account = self.associated_account

        build_branch_name = self.build_branch_name

        build_version = self.build_version

        project_name = self.project_name

        test_suite_name = self.test_suite_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_account is not UNSET:
            field_dict["associatedAccount"] = associated_account
        if build_branch_name is not UNSET:
            field_dict["buildBranchName"] = build_branch_name
        if build_version is not UNSET:
            field_dict["buildVersion"] = build_version
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if test_suite_name is not UNSET:
            field_dict["testSuiteName"] = test_suite_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        associated_account = d.pop("associatedAccount", UNSET)

        build_branch_name = d.pop("buildBranchName", UNSET)

        build_version = d.pop("buildVersion", UNSET)

        project_name = d.pop("projectName", UNSET)

        test_suite_name = d.pop("testSuiteName", UNSET)

        test_suite_run_object_description = cls(
            associated_account=associated_account,
            build_branch_name=build_branch_name,
            build_version=build_version,
            project_name=project_name,
            test_suite_name=test_suite_name,
        )

        test_suite_run_object_description.additional_properties = d
        return test_suite_run_object_description

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
