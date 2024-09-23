from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from typing import Union
from typing import cast
from ..models.batch_status import BatchStatus
from dateutil.parser import isoparse
from ..models.metric_status import MetricStatus

if TYPE_CHECKING:
    from ..models.batch_job_status_counts import BatchJobStatusCounts
    from ..models.batch_parameters import BatchParameters
    from ..models.batch_status_history_type import BatchStatusHistoryType
    from ..models.job_metrics_status_counts import JobMetricsStatusCounts


T = TypeVar("T", bound="Batch")


@_attrs_define
class Batch:
    """
    Attributes:
        associated_account (str):
        adhoc_test_suite (Union[Unset, bool]):
        batch_id (Union[Unset, str]):
        batch_metrics_status (Union[Unset, MetricStatus]):
        branch_id (Union[Unset, str]):
        build_id (Union[Unset, str]):
        creation_timestamp (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        friendly_name (Union[Unset, str]):
        job_metrics_status_counts (Union[Unset, JobMetricsStatusCounts]):
        job_status_counts (Union[Unset, BatchJobStatusCounts]):
        jobs_metrics_status (Union[Unset, MetricStatus]):
        last_updated_timestamp (Union[Unset, datetime.datetime]):
        metrics_build_id (Union[Unset, str]):
        org_id (Union[Unset, str]):
        overall_metrics_status (Union[Unset, MetricStatus]):
        parameters (Union[Unset, BatchParameters]):
        pool_labels (Union[Unset, List[str]]):
        project_id (Union[Unset, str]):
        status (Union[Unset, BatchStatus]):
        status_history (Union[Unset, List['BatchStatusHistoryType']]):
        system_id (Union[Unset, str]):
        test_suite_id (Union[Unset, str]):
        test_suite_revision (Union[Unset, int]):
        total_jobs (Union[Unset, int]):
        user_id (Union[Unset, str]):
    """

    associated_account: str
    adhoc_test_suite: Union[Unset, bool] = UNSET
    batch_id: Union[Unset, str] = UNSET
    batch_metrics_status: Union[Unset, MetricStatus] = UNSET
    branch_id: Union[Unset, str] = UNSET
    build_id: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    job_metrics_status_counts: Union[Unset, "JobMetricsStatusCounts"] = UNSET
    job_status_counts: Union[Unset, "BatchJobStatusCounts"] = UNSET
    jobs_metrics_status: Union[Unset, MetricStatus] = UNSET
    last_updated_timestamp: Union[Unset, datetime.datetime] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    overall_metrics_status: Union[Unset, MetricStatus] = UNSET
    parameters: Union[Unset, "BatchParameters"] = UNSET
    pool_labels: Union[Unset, List[str]] = UNSET
    project_id: Union[Unset, str] = UNSET
    status: Union[Unset, BatchStatus] = UNSET
    status_history: Union[Unset, List["BatchStatusHistoryType"]] = UNSET
    system_id: Union[Unset, str] = UNSET
    test_suite_id: Union[Unset, str] = UNSET
    test_suite_revision: Union[Unset, int] = UNSET
    total_jobs: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        associated_account = self.associated_account

        adhoc_test_suite = self.adhoc_test_suite

        batch_id = self.batch_id

        batch_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.batch_metrics_status, Unset):
            batch_metrics_status = self.batch_metrics_status.value

        branch_id = self.branch_id

        build_id = self.build_id

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        description = self.description

        friendly_name = self.friendly_name

        job_metrics_status_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_metrics_status_counts, Unset):
            job_metrics_status_counts = self.job_metrics_status_counts.to_dict()

        job_status_counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_status_counts, Unset):
            job_status_counts = self.job_status_counts.to_dict()

        jobs_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.jobs_metrics_status, Unset):
            jobs_metrics_status = self.jobs_metrics_status.value

        last_updated_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_timestamp, Unset):
            last_updated_timestamp = self.last_updated_timestamp.isoformat()

        metrics_build_id = self.metrics_build_id

        org_id = self.org_id

        overall_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.overall_metrics_status, Unset):
            overall_metrics_status = self.overall_metrics_status.value

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        pool_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pool_labels, Unset):
            pool_labels = self.pool_labels

        project_id = self.project_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status_history, Unset):
            status_history = []
            for componentsschemasbatch_status_history_item_data in self.status_history:
                componentsschemasbatch_status_history_item = (
                    componentsschemasbatch_status_history_item_data.to_dict()
                )
                status_history.append(componentsschemasbatch_status_history_item)

        system_id = self.system_id

        test_suite_id = self.test_suite_id

        test_suite_revision = self.test_suite_revision

        total_jobs = self.total_jobs

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "associatedAccount": associated_account,
            }
        )
        if adhoc_test_suite is not UNSET:
            field_dict["adhocTestSuite"] = adhoc_test_suite
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if batch_metrics_status is not UNSET:
            field_dict["batchMetricsStatus"] = batch_metrics_status
        if branch_id is not UNSET:
            field_dict["branchID"] = branch_id
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if description is not UNSET:
            field_dict["description"] = description
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if job_metrics_status_counts is not UNSET:
            field_dict["jobMetricsStatusCounts"] = job_metrics_status_counts
        if job_status_counts is not UNSET:
            field_dict["jobStatusCounts"] = job_status_counts
        if jobs_metrics_status is not UNSET:
            field_dict["jobsMetricsStatus"] = jobs_metrics_status
        if last_updated_timestamp is not UNSET:
            field_dict["lastUpdatedTimestamp"] = last_updated_timestamp
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id
        if overall_metrics_status is not UNSET:
            field_dict["overallMetricsStatus"] = overall_metrics_status
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if pool_labels is not UNSET:
            field_dict["poolLabels"] = pool_labels
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_history is not UNSET:
            field_dict["statusHistory"] = status_history
        if system_id is not UNSET:
            field_dict["systemID"] = system_id
        if test_suite_id is not UNSET:
            field_dict["testSuiteID"] = test_suite_id
        if test_suite_revision is not UNSET:
            field_dict["testSuiteRevision"] = test_suite_revision
        if total_jobs is not UNSET:
            field_dict["totalJobs"] = total_jobs
        if user_id is not UNSET:
            field_dict["userID"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_job_status_counts import BatchJobStatusCounts
        from ..models.batch_parameters import BatchParameters
        from ..models.batch_status_history_type import BatchStatusHistoryType
        from ..models.job_metrics_status_counts import JobMetricsStatusCounts

        d = src_dict.copy()
        associated_account = d.pop("associatedAccount")

        adhoc_test_suite = d.pop("adhocTestSuite", UNSET)

        batch_id = d.pop("batchID", UNSET)

        _batch_metrics_status = d.pop("batchMetricsStatus", UNSET)
        batch_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_batch_metrics_status, Unset):
            batch_metrics_status = UNSET
        else:
            batch_metrics_status = MetricStatus(_batch_metrics_status)

        branch_id = d.pop("branchID", UNSET)

        build_id = d.pop("buildID", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp, Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)

        description = d.pop("description", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        _job_metrics_status_counts = d.pop("jobMetricsStatusCounts", UNSET)
        job_metrics_status_counts: Union[Unset, JobMetricsStatusCounts]
        if isinstance(_job_metrics_status_counts, Unset):
            job_metrics_status_counts = UNSET
        else:
            job_metrics_status_counts = JobMetricsStatusCounts.from_dict(
                _job_metrics_status_counts
            )

        _job_status_counts = d.pop("jobStatusCounts", UNSET)
        job_status_counts: Union[Unset, BatchJobStatusCounts]
        if isinstance(_job_status_counts, Unset):
            job_status_counts = UNSET
        else:
            job_status_counts = BatchJobStatusCounts.from_dict(_job_status_counts)

        _jobs_metrics_status = d.pop("jobsMetricsStatus", UNSET)
        jobs_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_jobs_metrics_status, Unset):
            jobs_metrics_status = UNSET
        else:
            jobs_metrics_status = MetricStatus(_jobs_metrics_status)

        _last_updated_timestamp = d.pop("lastUpdatedTimestamp", UNSET)
        last_updated_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_timestamp, Unset):
            last_updated_timestamp = UNSET
        else:
            last_updated_timestamp = isoparse(_last_updated_timestamp)

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        org_id = d.pop("orgID", UNSET)

        _overall_metrics_status = d.pop("overallMetricsStatus", UNSET)
        overall_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_overall_metrics_status, Unset):
            overall_metrics_status = UNSET
        else:
            overall_metrics_status = MetricStatus(_overall_metrics_status)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, BatchParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = BatchParameters.from_dict(_parameters)

        pool_labels = cast(List[str], d.pop("poolLabels", UNSET))

        project_id = d.pop("projectID", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BatchStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BatchStatus(_status)

        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for componentsschemasbatch_status_history_item_data in _status_history or []:
            componentsschemasbatch_status_history_item = (
                BatchStatusHistoryType.from_dict(
                    componentsschemasbatch_status_history_item_data
                )
            )

            status_history.append(componentsschemasbatch_status_history_item)

        system_id = d.pop("systemID", UNSET)

        test_suite_id = d.pop("testSuiteID", UNSET)

        test_suite_revision = d.pop("testSuiteRevision", UNSET)

        total_jobs = d.pop("totalJobs", UNSET)

        user_id = d.pop("userID", UNSET)

        batch = cls(
            associated_account=associated_account,
            adhoc_test_suite=adhoc_test_suite,
            batch_id=batch_id,
            batch_metrics_status=batch_metrics_status,
            branch_id=branch_id,
            build_id=build_id,
            creation_timestamp=creation_timestamp,
            description=description,
            friendly_name=friendly_name,
            job_metrics_status_counts=job_metrics_status_counts,
            job_status_counts=job_status_counts,
            jobs_metrics_status=jobs_metrics_status,
            last_updated_timestamp=last_updated_timestamp,
            metrics_build_id=metrics_build_id,
            org_id=org_id,
            overall_metrics_status=overall_metrics_status,
            parameters=parameters,
            pool_labels=pool_labels,
            project_id=project_id,
            status=status,
            status_history=status_history,
            system_id=system_id,
            test_suite_id=test_suite_id,
            test_suite_revision=test_suite_revision,
            total_jobs=total_jobs,
            user_id=user_id,
        )

        batch.additional_properties = d
        return batch

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
