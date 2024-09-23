from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Union


T = TypeVar("T", bound="BatchMetricsDataToBatchMetric")


@_attrs_define
class BatchMetricsDataToBatchMetric:
    """
    Attributes:
        batch_metric_id (Union[Unset, str]):
        batch_metrics_data_i_ds (Union[Unset, List[str]]):
    """

    batch_metric_id: Union[Unset, str] = UNSET
    batch_metrics_data_i_ds: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_metric_id = self.batch_metric_id

        batch_metrics_data_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.batch_metrics_data_i_ds, Unset):
            batch_metrics_data_i_ds = self.batch_metrics_data_i_ds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_metric_id is not UNSET:
            field_dict["batchMetricID"] = batch_metric_id
        if batch_metrics_data_i_ds is not UNSET:
            field_dict["batchMetricsDataIDs"] = batch_metrics_data_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        batch_metric_id = d.pop("batchMetricID", UNSET)

        batch_metrics_data_i_ds = cast(List[str], d.pop("batchMetricsDataIDs", UNSET))

        batch_metrics_data_to_batch_metric = cls(
            batch_metric_id=batch_metric_id,
            batch_metrics_data_i_ds=batch_metrics_data_i_ds,
        )

        batch_metrics_data_to_batch_metric.additional_properties = d
        return batch_metrics_data_to_batch_metric

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
