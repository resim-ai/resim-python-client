from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddMetricsDataToMetricResponse201")


@_attrs_define
class AddMetricsDataToMetricResponse201:
    """
    Attributes:
        metric_id (Union[Unset, str]):
        metrics_data_i_ds (Union[Unset, List[str]]):
    """

    metric_id: Union[Unset, str] = UNSET
    metrics_data_i_ds: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metric_id = self.metric_id
        metrics_data_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.metrics_data_i_ds, Unset):
            metrics_data_i_ds = self.metrics_data_i_ds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric_id is not UNSET:
            field_dict["metricID"] = metric_id
        if metrics_data_i_ds is not UNSET:
            field_dict["metricsDataIDs"] = metrics_data_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metric_id = d.pop("metricID", UNSET)

        metrics_data_i_ds = cast(List[str], d.pop("metricsDataIDs", UNSET))

        add_metrics_data_to_metric_response_201 = cls(
            metric_id=metric_id,
            metrics_data_i_ds=metrics_data_i_ds,
        )

        add_metrics_data_to_metric_response_201.additional_properties = d
        return add_metrics_data_to_metric_response_201

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
