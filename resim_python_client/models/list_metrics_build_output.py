from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_build import MetricsBuild


T = TypeVar("T", bound="ListMetricsBuildOutput")


@_attrs_define
class ListMetricsBuildOutput:
    """
    Attributes:
        metrics_builds (Union[Unset, List['MetricsBuild']]):
        next_page_token (Union[Unset, str]):
    """

    metrics_builds: Union[Unset, List["MetricsBuild"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics_builds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics_builds, Unset):
            metrics_builds = []
            for metrics_builds_item_data in self.metrics_builds:
                metrics_builds_item = metrics_builds_item_data.to_dict()

                metrics_builds.append(metrics_builds_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics_builds is not UNSET:
            field_dict["metricsBuilds"] = metrics_builds
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.metrics_build import MetricsBuild

        d = src_dict.copy()
        metrics_builds = []
        _metrics_builds = d.pop("metricsBuilds", UNSET)
        for metrics_builds_item_data in _metrics_builds or []:
            metrics_builds_item = MetricsBuild.from_dict(metrics_builds_item_data)

            metrics_builds.append(metrics_builds_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_metrics_build_output = cls(
            metrics_builds=metrics_builds,
            next_page_token=next_page_token,
        )

        list_metrics_build_output.additional_properties = d
        return list_metrics_build_output

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
