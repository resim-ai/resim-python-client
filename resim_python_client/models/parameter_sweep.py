from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Dict
from ..models.parameter_sweep_status import ParameterSweepStatus
import datetime
from dateutil.parser import isoparse
from typing import cast
from ..types import UNSET, Unset
from typing import cast, List
from typing import Union

if TYPE_CHECKING:
  from ..models.sweep_parameter import SweepParameter
  from ..models.parameter_sweep_status_history_type import ParameterSweepStatusHistoryType





T = TypeVar("T", bound="ParameterSweep")


@_attrs_define
class ParameterSweep:
    """ 
        Attributes:
            parameter_sweep_id (Union[Unset, str]):
            project_id (Union[Unset, str]):
            name (Union[Unset, str]):
            status (Union[Unset, ParameterSweepStatus]):
            status_history (Union[Unset, List['ParameterSweepStatusHistoryType']]):
            last_updated_timestamp (Union[Unset, datetime.datetime]):
            creation_timestamp (Union[Unset, datetime.datetime]):
            parameters (Union[Unset, List['SweepParameter']]):
            batches (Union[Unset, List[str]]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
     """

    parameter_sweep_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ParameterSweepStatus] = UNSET
    status_history: Union[Unset, List['ParameterSweepStatusHistoryType']] = UNSET
    last_updated_timestamp: Union[Unset, datetime.datetime] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    parameters: Union[Unset, List['SweepParameter']] = UNSET
    batches: Union[Unset, List[str]] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.sweep_parameter import SweepParameter
        from ..models.parameter_sweep_status_history_type import ParameterSweepStatusHistoryType
        parameter_sweep_id = self.parameter_sweep_id

        project_id = self.project_id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        status_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status_history, Unset):
            status_history = []
            for componentsschemasparameter_sweep_status_history_item_data in self.status_history:
                componentsschemasparameter_sweep_status_history_item = componentsschemasparameter_sweep_status_history_item_data.to_dict()
                status_history.append(componentsschemasparameter_sweep_status_history_item)





        last_updated_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_timestamp, Unset):
            last_updated_timestamp = self.last_updated_timestamp.isoformat()

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)





        batches: Union[Unset, List[str]] = UNSET
        if not isinstance(self.batches, Unset):
            batches = self.batches





        user_id = self.user_id

        org_id = self.org_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if parameter_sweep_id is not UNSET:
            field_dict["parameterSweepID"] = parameter_sweep_id
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_history is not UNSET:
            field_dict["statusHistory"] = status_history
        if last_updated_timestamp is not UNSET:
            field_dict["lastUpdatedTimestamp"] = last_updated_timestamp
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if batches is not UNSET:
            field_dict["batches"] = batches
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sweep_parameter import SweepParameter
        from ..models.parameter_sweep_status_history_type import ParameterSweepStatusHistoryType
        d = src_dict.copy()
        parameter_sweep_id = d.pop("parameterSweepID", UNSET)

        project_id = d.pop("projectID", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ParameterSweepStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ParameterSweepStatus(_status)




        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for componentsschemasparameter_sweep_status_history_item_data in (_status_history or []):
            componentsschemasparameter_sweep_status_history_item = ParameterSweepStatusHistoryType.from_dict(componentsschemasparameter_sweep_status_history_item_data)



            status_history.append(componentsschemasparameter_sweep_status_history_item)


        _last_updated_timestamp = d.pop("lastUpdatedTimestamp", UNSET)
        last_updated_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_timestamp,  Unset):
            last_updated_timestamp = UNSET
        else:
            last_updated_timestamp = isoparse(_last_updated_timestamp)




        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp,  Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)




        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in (_parameters or []):
            parameters_item = SweepParameter.from_dict(parameters_item_data)



            parameters.append(parameters_item)


        batches = cast(List[str], d.pop("batches", UNSET))


        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        parameter_sweep = cls(
            parameter_sweep_id=parameter_sweep_id,
            project_id=project_id,
            name=name,
            status=status,
            status_history=status_history,
            last_updated_timestamp=last_updated_timestamp,
            creation_timestamp=creation_timestamp,
            parameters=parameters,
            batches=batches,
            user_id=user_id,
            org_id=org_id,
        )

        parameter_sweep.additional_properties = d
        return parameter_sweep

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
