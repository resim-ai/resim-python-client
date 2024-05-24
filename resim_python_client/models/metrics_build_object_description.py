from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricsBuildObjectDescription")


@_attrs_define
class MetricsBuildObjectDescription:
    """
    Attributes:
        image (Union[Unset, str]):
        name (Union[Unset, str]):
        project_name (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    image: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image = self.image
        name = self.name
        project_name = self.project_name
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        project_name = d.pop("projectName", UNSET)

        version = d.pop("version", UNSET)

        metrics_build_object_description = cls(
            image=image,
            name=name,
            project_name=project_name,
            version=version,
        )

        metrics_build_object_description.additional_properties = d
        return metrics_build_object_description

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
