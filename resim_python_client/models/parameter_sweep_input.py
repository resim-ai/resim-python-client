from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.triggered_via import TriggeredVia
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sweep_parameter import SweepParameter


T = TypeVar("T", bound="ParameterSweepInput")


@_attrs_define
class ParameterSweepInput:
    """
    Attributes:
        associated_account (Union[Unset, str]):
        build_id (Union[Unset, str]):
        experience_i_ds (Union[Unset, None, List[str]]):
        experience_names (Union[Unset, None, List[str]]):
        experience_tag_i_ds (Union[Unset, None, List[str]]):
        experience_tag_names (Union[Unset, None, List[str]]):
        metrics_build_id (Union[Unset, str]):
        parameters (Union[Unset, List['SweepParameter']]):
        pool_labels (Union[Unset, List[str]]):
        triggered_via (Union[Unset, TriggeredVia]):
    """

    associated_account: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    experience_i_ds: Union[Unset, None, List[str]] = UNSET
    experience_names: Union[Unset, None, List[str]] = UNSET
    experience_tag_i_ds: Union[Unset, None, List[str]] = UNSET
    experience_tag_names: Union[Unset, None, List[str]] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    parameters: Union[Unset, List["SweepParameter"]] = UNSET
    pool_labels: Union[Unset, List[str]] = UNSET
    triggered_via: Union[Unset, TriggeredVia] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        associated_account = self.associated_account
        build_id = self.build_id
        experience_i_ds: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.experience_i_ds, Unset):
            if self.experience_i_ds is None:
                experience_i_ds = None
            else:
                experience_i_ds = self.experience_i_ds

        experience_names: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.experience_names, Unset):
            if self.experience_names is None:
                experience_names = None
            else:
                experience_names = self.experience_names

        experience_tag_i_ds: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.experience_tag_i_ds, Unset):
            if self.experience_tag_i_ds is None:
                experience_tag_i_ds = None
            else:
                experience_tag_i_ds = self.experience_tag_i_ds

        experience_tag_names: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.experience_tag_names, Unset):
            if self.experience_tag_names is None:
                experience_tag_names = None
            else:
                experience_tag_names = self.experience_tag_names

        metrics_build_id = self.metrics_build_id
        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()

                parameters.append(parameters_item)

        pool_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pool_labels, Unset):
            pool_labels = self.pool_labels

        triggered_via: Union[Unset, str] = UNSET
        if not isinstance(self.triggered_via, Unset):
            triggered_via = self.triggered_via.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_account is not UNSET:
            field_dict["associatedAccount"] = associated_account
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if experience_i_ds is not UNSET:
            field_dict["experienceIDs"] = experience_i_ds
        if experience_names is not UNSET:
            field_dict["experienceNames"] = experience_names
        if experience_tag_i_ds is not UNSET:
            field_dict["experienceTagIDs"] = experience_tag_i_ds
        if experience_tag_names is not UNSET:
            field_dict["experienceTagNames"] = experience_tag_names
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if pool_labels is not UNSET:
            field_dict["poolLabels"] = pool_labels
        if triggered_via is not UNSET:
            field_dict["triggeredVia"] = triggered_via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sweep_parameter import SweepParameter

        d = src_dict.copy()
        associated_account = d.pop("associatedAccount", UNSET)

        build_id = d.pop("buildID", UNSET)

        experience_i_ds = cast(List[str], d.pop("experienceIDs", UNSET))

        experience_names = cast(List[str], d.pop("experienceNames", UNSET))

        experience_tag_i_ds = cast(List[str], d.pop("experienceTagIDs", UNSET))

        experience_tag_names = cast(List[str], d.pop("experienceTagNames", UNSET))

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = SweepParameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        pool_labels = cast(List[str], d.pop("poolLabels", UNSET))

        _triggered_via = d.pop("triggeredVia", UNSET)
        triggered_via: Union[Unset, TriggeredVia]
        if isinstance(_triggered_via, Unset):
            triggered_via = UNSET
        else:
            triggered_via = TriggeredVia(_triggered_via)

        parameter_sweep_input = cls(
            associated_account=associated_account,
            build_id=build_id,
            experience_i_ds=experience_i_ds,
            experience_names=experience_names,
            experience_tag_i_ds=experience_tag_i_ds,
            experience_tag_names=experience_tag_names,
            metrics_build_id=metrics_build_id,
            parameters=parameters,
            pool_labels=pool_labels,
            triggered_via=triggered_via,
        )

        parameter_sweep_input.additional_properties = d
        return parameter_sweep_input

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
