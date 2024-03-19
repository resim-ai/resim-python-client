from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from dateutil.parser import isoparse
from typing import cast
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="JobMetricsData")


@_attrs_define
class JobMetricsData:
    """ 
        Attributes:
            data_id (Union[Unset, str]):
            file_location (Union[Unset, str]):
            name (Union[Unset, str]):
            org_id (Union[Unset, str]):
            user_id (Union[Unset, str]):
            metrics_data_url (Union[Unset, str]):
            creation_timestamp (Union[Unset, datetime.datetime]):
            job_id (Union[Unset, str]):
     """

    data_id: Union[Unset, str] = UNSET
    file_location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    metrics_data_url: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    job_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        data_id = self.data_id

        file_location = self.file_location

        name = self.name

        org_id = self.org_id

        user_id = self.user_id

        metrics_data_url = self.metrics_data_url

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        job_id = self.job_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_id is not UNSET:
            field_dict["dataID"] = data_id
        if file_location is not UNSET:
            field_dict["fileLocation"] = file_location
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if metrics_data_url is not UNSET:
            field_dict["metricsDataURL"] = metrics_data_url
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if job_id is not UNSET:
            field_dict["jobID"] = job_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_id = d.pop("dataID", UNSET)

        file_location = d.pop("fileLocation", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("orgID", UNSET)

        user_id = d.pop("userID", UNSET)

        metrics_data_url = d.pop("metricsDataURL", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp,  Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)




        job_id = d.pop("jobID", UNSET)

        job_metrics_data = cls(
            data_id=data_id,
            file_location=file_location,
            name=name,
            org_id=org_id,
            user_id=user_id,
            metrics_data_url=metrics_data_url,
            creation_timestamp=creation_timestamp,
            job_id=job_id,
        )

        job_metrics_data.additional_properties = d
        return job_metrics_data

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
