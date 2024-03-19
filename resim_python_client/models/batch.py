from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from ..types import UNSET, Unset
from typing import Union
from ..models.batch_status import BatchStatus
from dateutil.parser import isoparse
from typing import cast
from ..models.metric_status import MetricStatus
from typing import cast, List
from typing import Dict

if TYPE_CHECKING:
  from ..models.batch_status_history_type import BatchStatusHistoryType
  from ..models.batch_parameters import BatchParameters





T = TypeVar("T", bound="Batch")


@_attrs_define
class Batch:
    """ 
        Attributes:
            batch_id (Union[Unset, str]):
            project_id (Union[Unset, str]):
            status (Union[Unset, BatchStatus]):
            batch_metrics_status (Union[Unset, MetricStatus]):
            jobs_metrics_status (Union[Unset, MetricStatus]):
            overall_metrics_status (Union[Unset, MetricStatus]):
            status_history (Union[Unset, List['BatchStatusHistoryType']]):
            last_updated_timestamp (Union[Unset, datetime.datetime]):
            friendly_name (Union[Unset, str]):
            creation_timestamp (Union[Unset, datetime.datetime]):
            build_id (Union[Unset, str]):
            metrics_build_id (Union[Unset, str]):
            instantiated_experience_i_ds (Union[Unset, List[str]]):
            instantiated_experience_tag_i_ds (Union[Unset, List[str]]):
            parameters (Union[Unset, BatchParameters]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
     """

    batch_id: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    status: Union[Unset, BatchStatus] = UNSET
    batch_metrics_status: Union[Unset, MetricStatus] = UNSET
    jobs_metrics_status: Union[Unset, MetricStatus] = UNSET
    overall_metrics_status: Union[Unset, MetricStatus] = UNSET
    status_history: Union[Unset, List['BatchStatusHistoryType']] = UNSET
    last_updated_timestamp: Union[Unset, datetime.datetime] = UNSET
    friendly_name: Union[Unset, str] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    build_id: Union[Unset, str] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    instantiated_experience_i_ds: Union[Unset, List[str]] = UNSET
    instantiated_experience_tag_i_ds: Union[Unset, List[str]] = UNSET
    parameters: Union[Unset, 'BatchParameters'] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.batch_status_history_type import BatchStatusHistoryType
        from ..models.batch_parameters import BatchParameters
        batch_id = self.batch_id

        project_id = self.project_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        batch_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.batch_metrics_status, Unset):
            batch_metrics_status = self.batch_metrics_status.value


        jobs_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.jobs_metrics_status, Unset):
            jobs_metrics_status = self.jobs_metrics_status.value


        overall_metrics_status: Union[Unset, str] = UNSET
        if not isinstance(self.overall_metrics_status, Unset):
            overall_metrics_status = self.overall_metrics_status.value


        status_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.status_history, Unset):
            status_history = []
            for componentsschemasbatch_status_history_item_data in self.status_history:
                componentsschemasbatch_status_history_item = componentsschemasbatch_status_history_item_data.to_dict()
                status_history.append(componentsschemasbatch_status_history_item)





        last_updated_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_timestamp, Unset):
            last_updated_timestamp = self.last_updated_timestamp.isoformat()

        friendly_name = self.friendly_name

        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        build_id = self.build_id

        metrics_build_id = self.metrics_build_id

        instantiated_experience_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instantiated_experience_i_ds, Unset):
            instantiated_experience_i_ds = self.instantiated_experience_i_ds





        instantiated_experience_tag_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instantiated_experience_tag_i_ds, Unset):
            instantiated_experience_tag_i_ds = self.instantiated_experience_tag_i_ds





        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        user_id = self.user_id

        org_id = self.org_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if batch_metrics_status is not UNSET:
            field_dict["batchMetricsStatus"] = batch_metrics_status
        if jobs_metrics_status is not UNSET:
            field_dict["jobsMetricsStatus"] = jobs_metrics_status
        if overall_metrics_status is not UNSET:
            field_dict["overallMetricsStatus"] = overall_metrics_status
        if status_history is not UNSET:
            field_dict["statusHistory"] = status_history
        if last_updated_timestamp is not UNSET:
            field_dict["lastUpdatedTimestamp"] = last_updated_timestamp
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id
        if instantiated_experience_i_ds is not UNSET:
            field_dict["instantiatedExperienceIDs"] = instantiated_experience_i_ds
        if instantiated_experience_tag_i_ds is not UNSET:
            field_dict["instantiatedExperienceTagIDs"] = instantiated_experience_tag_i_ds
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_status_history_type import BatchStatusHistoryType
        from ..models.batch_parameters import BatchParameters
        d = src_dict.copy()
        batch_id = d.pop("batchID", UNSET)

        project_id = d.pop("projectID", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BatchStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = BatchStatus(_status)




        _batch_metrics_status = d.pop("batchMetricsStatus", UNSET)
        batch_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_batch_metrics_status,  Unset):
            batch_metrics_status = UNSET
        else:
            batch_metrics_status = MetricStatus(_batch_metrics_status)




        _jobs_metrics_status = d.pop("jobsMetricsStatus", UNSET)
        jobs_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_jobs_metrics_status,  Unset):
            jobs_metrics_status = UNSET
        else:
            jobs_metrics_status = MetricStatus(_jobs_metrics_status)




        _overall_metrics_status = d.pop("overallMetricsStatus", UNSET)
        overall_metrics_status: Union[Unset, MetricStatus]
        if isinstance(_overall_metrics_status,  Unset):
            overall_metrics_status = UNSET
        else:
            overall_metrics_status = MetricStatus(_overall_metrics_status)




        status_history = []
        _status_history = d.pop("statusHistory", UNSET)
        for componentsschemasbatch_status_history_item_data in (_status_history or []):
            componentsschemasbatch_status_history_item = BatchStatusHistoryType.from_dict(componentsschemasbatch_status_history_item_data)



            status_history.append(componentsschemasbatch_status_history_item)


        _last_updated_timestamp = d.pop("lastUpdatedTimestamp", UNSET)
        last_updated_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_timestamp,  Unset):
            last_updated_timestamp = UNSET
        else:
            last_updated_timestamp = isoparse(_last_updated_timestamp)




        friendly_name = d.pop("friendlyName", UNSET)

        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp,  Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)




        build_id = d.pop("buildID", UNSET)

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        instantiated_experience_i_ds = cast(List[str], d.pop("instantiatedExperienceIDs", UNSET))


        instantiated_experience_tag_i_ds = cast(List[str], d.pop("instantiatedExperienceTagIDs", UNSET))


        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, BatchParameters]
        if isinstance(_parameters,  Unset):
            parameters = UNSET
        else:
            parameters = BatchParameters.from_dict(_parameters)




        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        batch = cls(
            batch_id=batch_id,
            project_id=project_id,
            status=status,
            batch_metrics_status=batch_metrics_status,
            jobs_metrics_status=jobs_metrics_status,
            overall_metrics_status=overall_metrics_status,
            status_history=status_history,
            last_updated_timestamp=last_updated_timestamp,
            friendly_name=friendly_name,
            creation_timestamp=creation_timestamp,
            build_id=build_id,
            metrics_build_id=metrics_build_id,
            instantiated_experience_i_ds=instantiated_experience_i_ds,
            instantiated_experience_tag_i_ds=instantiated_experience_tag_i_ds,
            parameters=parameters,
            user_id=user_id,
            org_id=org_id,
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
