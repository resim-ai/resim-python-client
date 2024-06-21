from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from typing import cast

if TYPE_CHECKING:
    from ..models.sweep_parameter import SweepParameter


T = TypeVar("T", bound="SweepObjectDescription")


@_attrs_define
class SweepObjectDescription:
    """
    Attributes:
        associated_account (Union[Unset, str]):
        build_branch_name (Union[Unset, str]):
        build_version (Union[Unset, str]):
        experience_names (Union[Unset, List[str]]):
        experience_tag_names (Union[Unset, List[str]]):
        metrics_build_name (Union[Unset, str]):
        metrics_build_version (Union[Unset, str]):
        parameters (Union[Unset, List['SweepParameter']]):
        project_name (Union[Unset, str]):
    """

    associated_account: Union[Unset, str] = UNSET
    build_branch_name: Union[Unset, str] = UNSET
    build_version: Union[Unset, str] = UNSET
    experience_names: Union[Unset, List[str]] = UNSET
    experience_tag_names: Union[Unset, List[str]] = UNSET
    metrics_build_name: Union[Unset, str] = UNSET
    metrics_build_version: Union[Unset, str] = UNSET
    parameters: Union[Unset, List["SweepParameter"]] = UNSET
    project_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        associated_account = self.associated_account

        build_branch_name = self.build_branch_name

        build_version = self.build_version

        experience_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experience_names, Unset):
            experience_names = self.experience_names

        experience_tag_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.experience_tag_names, Unset):
            experience_tag_names = self.experience_tag_names

        metrics_build_name = self.metrics_build_name

        metrics_build_version = self.metrics_build_version

        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        project_name = self.project_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_account is not UNSET:
            field_dict["associatedAccount"] = associated_account
        if build_branch_name is not UNSET:
            field_dict["buildBranchName"] = build_branch_name
        if build_version is not UNSET:
            field_dict["buildVersion"] = build_version
        if experience_names is not UNSET:
            field_dict["experienceNames"] = experience_names
        if experience_tag_names is not UNSET:
            field_dict["experienceTagNames"] = experience_tag_names
        if metrics_build_name is not UNSET:
            field_dict["metricsBuildName"] = metrics_build_name
        if metrics_build_version is not UNSET:
            field_dict["metricsBuildVersion"] = metrics_build_version
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if project_name is not UNSET:
            field_dict["projectName"] = project_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sweep_parameter import SweepParameter

        d = src_dict.copy()
        associated_account = d.pop("associatedAccount", UNSET)

        build_branch_name = d.pop("buildBranchName", UNSET)

        build_version = d.pop("buildVersion", UNSET)

        experience_names = cast(List[str], d.pop("experienceNames", UNSET))

        experience_tag_names = cast(List[str], d.pop("experienceTagNames", UNSET))

        metrics_build_name = d.pop("metricsBuildName", UNSET)

        metrics_build_version = d.pop("metricsBuildVersion", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = SweepParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        project_name = d.pop("projectName", UNSET)

        sweep_object_description = cls(
            associated_account=associated_account,
            build_branch_name=build_branch_name,
            build_version=build_version,
            experience_names=experience_names,
            experience_tag_names=experience_tag_names,
            metrics_build_name=metrics_build_name,
            metrics_build_version=metrics_build_version,
            parameters=parameters,
            project_name=project_name,
        )

        sweep_object_description.additional_properties = d
        return sweep_object_description

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
