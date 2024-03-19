from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

import datetime
from ..models.branch_type import BranchType
from dateutil.parser import isoparse
from typing import cast
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Branch")


@_attrs_define
class Branch:
    """ 
        Attributes:
            branch_id (Union[Unset, str]):
            name (Union[Unset, str]):
            project_id (Union[Unset, str]):
            branch_type (Union[Unset, BranchType]):
            creation_timestamp (Union[Unset, datetime.datetime]):
            user_id (Union[Unset, str]):
            org_id (Union[Unset, str]):
     """

    branch_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    branch_type: Union[Unset, BranchType] = UNSET
    creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        branch_id = self.branch_id

        name = self.name

        project_id = self.project_id

        branch_type: Union[Unset, str] = UNSET
        if not isinstance(self.branch_type, Unset):
            branch_type = self.branch_type.value


        creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.creation_timestamp, Unset):
            creation_timestamp = self.creation_timestamp.isoformat()

        user_id = self.user_id

        org_id = self.org_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branchID"] = branch_id
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if branch_type is not UNSET:
            field_dict["branchType"] = branch_type
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if org_id is not UNSET:
            field_dict["orgID"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch_id = d.pop("branchID", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("projectID", UNSET)

        _branch_type = d.pop("branchType", UNSET)
        branch_type: Union[Unset, BranchType]
        if isinstance(_branch_type,  Unset):
            branch_type = UNSET
        else:
            branch_type = BranchType(_branch_type)




        _creation_timestamp = d.pop("creationTimestamp", UNSET)
        creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_creation_timestamp,  Unset):
            creation_timestamp = UNSET
        else:
            creation_timestamp = isoparse(_creation_timestamp)




        user_id = d.pop("userID", UNSET)

        org_id = d.pop("orgID", UNSET)

        branch = cls(
            branch_id=branch_id,
            name=name,
            project_id=project_id,
            branch_type=branch_type,
            creation_timestamp=creation_timestamp,
            user_id=user_id,
            org_id=org_id,
        )

        branch.additional_properties = d
        return branch

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
