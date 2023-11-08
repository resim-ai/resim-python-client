import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Log")


@_attrs_define
class Log:
    """
    Attributes:
        checksum (Union[Unset, str]):
        creation_timestamp (Union[Unset, datetime.datetime]):
        file_name (Union[Unset, str]):
        file_size (Union[Unset, int]):
        job_id (Union[Unset, str]):
        location (Union[Unset, str]):
        log_id (Union[Unset, str]):
        log_output_location (Union[Unset, str]):
        org_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    checksum: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    file_name: Union[Unset, str] = UNSET
    file_size: Union[Unset, int] = UNSET
    job_id: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    log_id: Union[Unset, str] = UNSET
    log_output_location: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checksum = self.checksum
        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        file_name = self.file_name
        file_size = self.file_size
        job_id = self.job_id
        location = self.location
        log_id = self.log_id
        log_output_location = self.log_output_location
        org_id = self.org_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if job_id is not UNSET:
            field_dict["jobID"] = job_id
        if location is not UNSET:
            field_dict["location"] = location
        if log_id is not UNSET:
            field_dict["logID"] = log_id
        if log_output_location is not UNSET:
            field_dict["logOutputLocation"] = log_output_location
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        checksum = d.pop("checksum", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp, Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)

        file_name = d.pop("fileName", UNSET)

        file_size = d.pop("fileSize", UNSET)

        job_id = d.pop("jobID", UNSET)

        location = d.pop("location", UNSET)

        log_id = d.pop("logID", UNSET)

        log_output_location = d.pop("logOutputLocation", UNSET)

        org_id = d.pop("orgID", UNSET)

        user_id = d.pop("userID", UNSET)

        log = cls(
            checksum=checksum,
            creation_timestamp=creation_timestamp,
            file_name=file_name,
            file_size=file_size,
            job_id=job_id,
            location=location,
            log_id=log_id,
            log_output_location=log_output_location,
            org_id=org_id,
            user_id=user_id,
        )

        log.additional_properties = d
        return log

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
