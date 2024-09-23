from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Union
from ..models.triggered_via import TriggeredVia

if TYPE_CHECKING:
    from ..models.batch_parameters import BatchParameters


T = TypeVar("T", bound="TestSuiteBatchInput")


@_attrs_define
class TestSuiteBatchInput:
    """
    Attributes:
        build_id (str):
        associated_account (Union[Unset, str]):
        parameters (Union[Unset, BatchParameters]):
        pool_labels (Union[Unset, List[str]]):
        triggered_via (Union[Unset, TriggeredVia]):
    """

    build_id: str
    associated_account: Union[Unset, str] = UNSET
    parameters: Union[Unset, "BatchParameters"] = UNSET
    pool_labels: Union[Unset, List[str]] = UNSET
    triggered_via: Union[Unset, TriggeredVia] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build_id = self.build_id

        associated_account = self.associated_account

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        pool_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pool_labels, Unset):
            pool_labels = self.pool_labels

        triggered_via: Union[Unset, str] = UNSET
        if not isinstance(self.triggered_via, Unset):
            triggered_via = self.triggered_via.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buildID": build_id,
            }
        )
        if associated_account is not UNSET:
            field_dict["associatedAccount"] = associated_account
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if pool_labels is not UNSET:
            field_dict["poolLabels"] = pool_labels
        if triggered_via is not UNSET:
            field_dict["triggeredVia"] = triggered_via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_parameters import BatchParameters

        d = src_dict.copy()
        build_id = d.pop("buildID")

        associated_account = d.pop("associatedAccount", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, BatchParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = BatchParameters.from_dict(_parameters)

        pool_labels = cast(List[str], d.pop("poolLabels", UNSET))

        _triggered_via = d.pop("triggeredVia", UNSET)
        triggered_via: Union[Unset, TriggeredVia]
        if isinstance(_triggered_via, Unset):
            triggered_via = UNSET
        else:
            triggered_via = TriggeredVia(_triggered_via)

        test_suite_batch_input = cls(
            build_id=build_id,
            associated_account=associated_account,
            parameters=parameters,
            pool_labels=pool_labels,
            triggered_via=triggered_via,
        )

        test_suite_batch_input.additional_properties = d
        return test_suite_batch_input

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
