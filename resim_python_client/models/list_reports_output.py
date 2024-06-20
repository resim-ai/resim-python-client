from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union

if TYPE_CHECKING:
    from ..models.report import Report


T = TypeVar("T", bound="ListReportsOutput")


@_attrs_define
class ListReportsOutput:
    """
    Attributes:
        next_page_token (Union[Unset, str]):
        reports (Union[Unset, List['Report']]):
        total (Union[Unset, int]):
    """

    next_page_token: Union[Unset, str] = UNSET
    reports: Union[Unset, List["Report"]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_page_token = self.next_page_token

        reports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reports, Unset):
            reports = []
            for reports_item_data in self.reports:
                reports_item = reports_item_data.to_dict()
                reports.append(reports_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if reports is not UNSET:
            field_dict["reports"] = reports
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report import Report

        d = src_dict.copy()
        next_page_token = d.pop("nextPageToken", UNSET)

        reports = []
        _reports = d.pop("reports", UNSET)
        for reports_item_data in _reports or []:
            reports_item = Report.from_dict(reports_item_data)

            reports.append(reports_item)

        total = d.pop("total", UNSET)

        list_reports_output = cls(
            next_page_token=next_page_token,
            reports=reports,
            total=total,
        )

        list_reports_output.additional_properties = d
        return list_reports_output

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
