from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from typing import Union
from ..models.conflated_job_status import ConflatedJobStatus
from ..models.job_status import JobStatus
from dateutil.parser import isoparse
from ..models.metric_status import MetricStatus

if TYPE_CHECKING:
    from ..models.batch_parameters import BatchParameters
    from ..models.job_status_history_type import JobStatusHistoryType


T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        batch_id (Union[Unset, str]):
        branch_id (Union[Unset, str]):
        build_id (Union[Unset, str]):
        conflated_status (Union[Unset, ConflatedJobStatus]):
        creation_timestamp (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        experience_id (Union[Unset, str]):
        experience_name (Union[Unset, str]):
        job_id (Union[Unset, str]):
        job_metrics_status (Union[Unset, MetricStatus]):
        job_status (Union[Unset, JobStatus]):
        last_updated_timestamp (Union[Unset, datetime.datetime]):
        org_id (Union[Unset, str]):
        output_location (Union[Unset, str]):
        parameters (Union[Unset, BatchParameters]):
        project_id (Union[Unset, str]):
        status_history (Union[Unset, List['JobStatusHistoryType']]):
        system_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    batch_id: Union[Unset, str] = UNSET
    branch_id: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    conflated_status: Union[Unset, ConflatedJobStatus] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    experience_id: Union[Unset, str] = UNSET
    experience_name: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    job_metrics_status: Union[Unset, MetricStatus] = UNSET
    job_status: Union[Unset, JobStatus] = UNSET
    last_updated_timestamp: Union[Unset, datetime.datetime] = UNSET
    org_id: Union[Unset, str] = UNSET
    output_location: Union[Unset, str] = UNSET
    parameters: Union[Unset, "BatchParameters"] = UNSET
    project_id: Union[Unset, str] = UNSET
    status_history: Union[Unset, List["JobStatusHistoryType"]] = UNSET
    system_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_id = self.batch_id

        branch_id = self.branch_id

        build_id = self.build_id

        conflated_status: Union[Unset, str] = UNSET
        if not isinstance(self.conflated_status, Unset):
            conflated_status = self.conflated_status.value

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        description = self.description

        experience_id = self.experience_id

        experience_name = self.experience_name

        job_id = self.job_id

        job_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.job_metrics_status, Unset):
            job_metrics_status = self.job_metrics_status.value

        job_status: Union[Unset, str] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.value

        last_updated_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_timestamp, Unset):
            last_updated_timestamp = self.last_updated_timestamp.isoformat()

        org_id = self.org_id

        output_location = self.output_location

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        project_id = self.project_id

        status_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status_history, Unset):
            status_history = []
            for componentsschemasjob_status_history_item_data in self.status_history:
                componentsschemasjob_status_history_item = (
                    componentsschemasjob_status_history_item_data.to_dict()
                )
                status_history.append(componentsschemasjob_status_history_item)

        system_id = self.system_id

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if branch_id is not UNSET:
            field_dict["branchID"] = branch_id
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if conflated_status is not UNSET:
            field_dict["conflatedStatus"] = conflated_status
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if experience_id is not UNSET:
            field_dict["experienceID"] = experience_id
        if experience_name is not UNSET:
            field_dict["experienceName"] = experience_name
        if job_id is not UNSET:
            field_dict["jobID"] = job_id
        if job_metrics_status is not UNSET:
            field_dict["jobMetricsStatus"] = job_metrics_status
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if last_updated_timestamp is not UNSET:
            field_dict["lastUpdatedTimestamp"] = last_updated_timestamp
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if output_location is not UNSET:
            field_dict["outputLocation"] = output_location
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if status_history is not UNSET:
            field_dict["statusHistory"] = status_history
        if system_id is not UNSET:
            field_dict["systemID"] = system_id
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_parameters import BatchParameters
        from ..models.job_status_history_type import JobStatusHistoryType

        d = src_dict.copy()
        batch_id = d.pop("batchID", UNSET)

        branch_id = d.pop("branchID", UNSET)

        build_id = d.pop("buildID", UNSET)

        _conflated_status = d.pop("conflatedStatus", UNSET)
        conflated_status: Union[Unset, ConflatedJobStatus]
        if isinstance(_conflated_status, Unset):
            conflated_status = UNSET
        else:
            conflated_status = ConflatedJobStatus(_conflated_status)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp, Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)

        description = d.pop("description", UNSET)

        experience_id = d.pop("experienceID", UNSET)

        experience_name = d.pop("experienceName", UNSET)

        job_id = d.pop("jobID", UNSET)

        _job_metrics_status = d.pop("jobMetricsStatus", UNSET)
        job_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_job_metrics_status, Unset):
            job_metrics_status = UNSET
        else:
            job_metrics_status = MetricStatus(_job_metrics_status)

        _job_status = d.pop("jobStatus", UNSET)
        job_status: Union[Unset, JobStatus]
        if isinstance(_job_status, Unset):
            job_status = UNSET
        else:
            job_status = JobStatus(_job_status)

        _last_updated_timestamp = d.pop("lastUpdatedTimestamp", UNSET)
        last_updated_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_timestamp, Unset):
            last_updated_timestamp = UNSET
        else:
            last_updated_timestamp = isoparse(_last_updated_timestamp)

        org_id = d.pop("orgID", UNSET)

        output_location = d.pop("outputLocation", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, BatchParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = BatchParameters.from_dict(_parameters)

        project_id = d.pop("projectID", UNSET)

        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for componentsschemasjob_status_history_item_data in _status_history or []:
            componentsschemasjob_status_history_item = JobStatusHistoryType.from_dict(
                componentsschemasjob_status_history_item_data
            )

            status_history.append(componentsschemasjob_status_history_item)

        system_id = d.pop("systemID", UNSET)

        user_id = d.pop("userID", UNSET)

        job = cls(
            batch_id=batch_id,
            branch_id=branch_id,
            build_id=build_id,
            conflated_status=conflated_status,
            creation_timestamp=creation_timestamp,
            description=description,
            experience_id=experience_id,
            experience_name=experience_name,
            job_id=job_id,
            job_metrics_status=job_metrics_status,
            job_status=job_status,
            last_updated_timestamp=last_updated_timestamp,
            org_id=org_id,
            output_location=output_location,
            parameters=parameters,
            project_id=project_id,
            status_history=status_history,
            system_id=system_id,
            user_id=user_id,
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
