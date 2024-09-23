from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union

if TYPE_CHECKING:
    from ..models.job_metrics_data import JobMetricsData


T = TypeVar("T", bound="ListJobMetricsDataOutput")


@_attrs_define
class ListJobMetricsDataOutput:
    """
    Attributes:
        metrics_data (Union[Unset, List['JobMetricsData']]):
        next_page_token (Union[Unset, str]):
    """

    metrics_data: Union[Unset, List["JobMetricsData"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics_data, Unset):
            metrics_data = []
            for metrics_data_item_data in self.metrics_data:
                metrics_data_item = metrics_data_item_data.to_dict()
                metrics_data.append(metrics_data_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics_data is not UNSET:
            field_dict["metricsData"] = metrics_data
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_metrics_data import JobMetricsData

        d = src_dict.copy()
        metrics_data = []
        _metrics_data = d.pop("metricsData", UNSET)
        for metrics_data_item_data in _metrics_data or []:
            metrics_data_item = JobMetricsData.from_dict(metrics_data_item_data)

            metrics_data.append(metrics_data_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_job_metrics_data_output = cls(
            metrics_data=metrics_data,
            next_page_token=next_page_token,
        )

        list_job_metrics_data_output.additional_properties = d
        return list_job_metrics_data_output

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
