from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_status import JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        build_id (Union[Unset, str]):
        experience_id (Union[Unset, str]):
        job_id (Union[Unset, str]):
        job_status (Union[Unset, JobStatus]):
        org_id (Union[Unset, str]):
        output_location (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    build_id: Union[Unset, str] = UNSET
    experience_id: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    job_status: Union[Unset, JobStatus] = UNSET
    org_id: Union[Unset, str] = UNSET
    output_location: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build_id = self.build_id
        experience_id = self.experience_id
        job_id = self.job_id
        job_status: Union[Unset, str] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.value

        org_id = self.org_id
        output_location = self.output_location
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if experience_id is not UNSET:
            field_dict["experienceID"] = experience_id
        if job_id is not UNSET:
            field_dict["jobID"] = job_id
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if output_location is not UNSET:
            field_dict["outputLocation"] = output_location
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        build_id = d.pop("buildID", UNSET)

        experience_id = d.pop("experienceID", UNSET)

        job_id = d.pop("jobID", UNSET)

        _job_status = d.pop("jobStatus", UNSET)
        job_status: Union[Unset, JobStatus]
        if isinstance(_job_status, Unset):
            job_status = UNSET
        else:
            job_status = JobStatus(_job_status)

        org_id = d.pop("orgID", UNSET)

        output_location = d.pop("outputLocation", UNSET)

        user_id = d.pop("userID", UNSET)

        job = cls(
            build_id=build_id,
            experience_id=experience_id,
            job_id=job_id,
            job_status=job_status,
            org_id=org_id,
            output_location=output_location,
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
