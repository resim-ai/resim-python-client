from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from ..models.job_status import JobStatus
from typing import Union
from ..models.metric_status import MetricStatus
from dateutil.parser import isoparse
from typing import cast
from ..types import UNSET, Unset
from typing import cast, List
from typing import Dict

if TYPE_CHECKING:
  from ..models.job_status_history_type import JobStatusHistoryType
  from ..models.batch_parameters import BatchParameters





T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """ 
        Attributes:
            job_id (Union[Unset, str]):
            project_id (Union[Unset, str]):
            batch_id (Union[Unset, str]):
            job_status (Union[Unset, JobStatus]):
            job_metrics_status (Union[Unset, MetricStatus]):
            status_history (Union[Unset, List['JobStatusHistoryType']]):
            last_updated_timestamp (Union[Unset, datetime.datetime]):
            output_location (Union[Unset, str]):
            experience_id (Union[Unset, str]):
            experience_name (Union[Unset, str]):
            build_id (Union[Unset, str]):
            creation_timestamp (Union[Unset, datetime.datetime]):
            parameters (Union[Unset, BatchParameters]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
     """

    job_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    batch_id: Union[Unset, str] = UNSET
    job_status: Union[Unset, JobStatus] = UNSET
    job_metrics_status: Union[Unset, MetricStatus] = UNSET
    status_history: Union[Unset, List['JobStatusHistoryType']] = UNSET
    last_updated_timestamp: Union[Unset, datetime.datetime] = UNSET
    output_location: Union[Unset, str] = UNSET
    experience_id: Union[Unset, str] = UNSET
    experience_name: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    parameters: Union[Unset, 'BatchParameters'] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.job_status_history_type import JobStatusHistoryType
        from ..models.batch_parameters import BatchParameters
        job_id = self.job_id

        project_id = self.project_id

        batch_id = self.batch_id

        job_status: Union[Unset, str] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.value


        job_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.job_metrics_status, Unset):
            job_metrics_status = self.job_metrics_status.value


        status_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status_history, Unset):
            status_history = []
            for componentsschemasjob_status_history_item_data in self.status_history:
                componentsschemasjob_status_history_item = componentsschemasjob_status_history_item_data.to_dict()
                status_history.append(componentsschemasjob_status_history_item)





        last_updated_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_timestamp, Unset):
            last_updated_timestamp = self.last_updated_timestamp.isoformat()

        output_location = self.output_location

        experience_id = self.experience_id

        experience_name = self.experience_name

        build_id = self.build_id

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        user_id = self.user_id

        org_id = self.org_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if job_id is not UNSET:
            field_dict["jobID"] = job_id
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if job_metrics_status is not UNSET:
            field_dict["jobMetricsStatus"] = job_metrics_status
        if status_history is not UNSET:
            field_dict["statusHistory"] = status_history
        if last_updated_timestamp is not UNSET:
            field_dict["lastUpdatedTimestamp"] = last_updated_timestamp
        if output_location is not UNSET:
            field_dict["outputLocation"] = output_location
        if experience_id is not UNSET:
            field_dict["experienceID"] = experience_id
        if experience_name is not UNSET:
            field_dict["experienceName"] = experience_name
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_status_history_type import JobStatusHistoryType
        from ..models.batch_parameters import BatchParameters
        d = src_dict.copy()
        job_id = d.pop("jobID", UNSET)

        project_id = d.pop("projectID", UNSET)

        batch_id = d.pop("batchID", UNSET)

        _job_status = d.pop("jobStatus", UNSET)
        job_status: Union[Unset, JobStatus]
        if isinstance(_job_status,  Unset):
            job_status = UNSET
        else:
            job_status = JobStatus(_job_status)




        _job_metrics_status = d.pop("jobMetricsStatus", UNSET)
        job_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_job_metrics_status,  Unset):
            job_metrics_status = UNSET
        else:
            job_metrics_status = MetricStatus(_job_metrics_status)




        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for componentsschemasjob_status_history_item_data in (_status_history or []):
            componentsschemasjob_status_history_item = JobStatusHistoryType.from_dict(componentsschemasjob_status_history_item_data)



            status_history.append(componentsschemasjob_status_history_item)


        _last_updated_timestamp = d.pop("lastUpdatedTimestamp", UNSET)
        last_updated_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_timestamp,  Unset):
            last_updated_timestamp = UNSET
        else:
            last_updated_timestamp = isoparse(_last_updated_timestamp)




        output_location = d.pop("outputLocation", UNSET)

        experience_id = d.pop("experienceID", UNSET)

        experience_name = d.pop("experienceName", UNSET)

        build_id = d.pop("buildID", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp,  Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)




        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, BatchParameters]
        if isinstance(_parameters,  Unset):
            parameters = UNSET
        else:
            parameters = BatchParameters.from_dict(_parameters)




        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        job = cls(
            job_id=job_id,
            project_id=project_id,
            batch_id=batch_id,
            job_status=job_status,
            job_metrics_status=job_metrics_status,
            status_history=status_history,
            last_updated_timestamp=last_updated_timestamp,
            output_location=output_location,
            experience_id=experience_id,
            experience_name=experience_name,
            build_id=build_id,
            creation_timestamp=creation_timestamp,
            parameters=parameters,
            user_id=user_id,
            org_id=org_id,
        )

        job.additional_properties = d
        return job

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
