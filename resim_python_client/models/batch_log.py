from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from ..models.log_type import LogType
from typing import cast
from ..types import UNSET, Unset
from ..models.execution_step import ExecutionStep
from typing import Union






T = TypeVar("T", bound="BatchLog")


@_attrs_define
class BatchLog:
    """ 
        Attributes:
            log_id (Union[Unset, str]):
            file_name (Union[Unset, str]):
            file_size (Union[Unset, int]):
            checksum (Union[Unset, str]):
            creation_timestamp (Union[Unset, datetime.datetime]):
            location (Union[Unset, str]):
            log_output_location (Union[Unset, str]):
            execution_step (Union[Unset, ExecutionStep]):
            log_type (Union[Unset, LogType]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
            batch_id (Union[Unset, str]):
     """

    log_id: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    file_size: Union[Unset, int] = UNSET
    checksum: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    log_output_location: Union[Unset, str] = UNSET
    execution_step: Union[Unset, ExecutionStep] = UNSET
    log_type: Union[Unset, LogType] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    batch_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        log_id = self.log_id

        file_name = self.file_name

        file_size = self.file_size

        checksum = self.checksum

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        location = self.location

        log_output_location = self.log_output_location

        execution_step: Union[Unset, str] = UNSET
        if not isinstance(self.execution_step, Unset):
            execution_step = self.execution_step.value


        log_type: Union[Unset, str] = UNSET
        if not isinstance(self.log_type, Unset):
            log_type = self.log_type.value


        user_id = self.user_id

        org_id = self.org_id

        batch_id = self.batch_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if log_id is not UNSET:
            field_dict["logID"] = log_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if location is not UNSET:
            field_dict["location"] = location
        if log_output_location is not UNSET:
            field_dict["logOutputLocation"] = log_output_location
        if execution_step is not UNSET:
            field_dict["executionStep"] = execution_step
        if log_type is not UNSET:
            field_dict["logType"] = log_type
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log_id = d.pop("logID", UNSET)

        file_name = d.pop("fileName", UNSET)

        file_size = d.pop("fileSize", UNSET)

        checksum = d.pop("checksum", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp,  Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)




        location = d.pop("location", UNSET)

        log_output_location = d.pop("logOutputLocation", UNSET)

        _execution_step = d.pop("executionStep", UNSET)
        execution_step: Union[Unset, ExecutionStep]
        if isinstance(_execution_step,  Unset):
            execution_step = UNSET
        else:
            execution_step = ExecutionStep(_execution_step)




        _log_type = d.pop("logType", UNSET)
        log_type: Union[Unset, LogType]
        if isinstance(_log_type,  Unset):
            log_type = UNSET
        else:
            log_type = LogType(_log_type)




        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        batch_id = d.pop("batchID", UNSET)

        batch_log = cls(
            log_id=log_id,
            file_name=file_name,
            file_size=file_size,
            checksum=checksum,
            creation_timestamp=creation_timestamp,
            location=location,
            log_output_location=log_output_location,
            execution_step=execution_step,
            log_type=log_type,
            user_id=user_id,
            org_id=org_id,
            batch_id=batch_id,
        )

        batch_log.additional_properties = d
        return batch_log

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
