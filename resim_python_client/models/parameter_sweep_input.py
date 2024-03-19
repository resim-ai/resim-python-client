from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union
from typing import Dict
from typing import cast
from ..types import UNSET, Unset
from typing import cast, List
from typing import Union

if TYPE_CHECKING:
  from ..models.sweep_parameter import SweepParameter





T = TypeVar("T", bound="ParameterSweepInput")


@_attrs_define
class ParameterSweepInput:
    """ 
        Attributes:
            parameters (Union[Unset, List['SweepParameter']]):
            experience_i_ds (Union[List[str], None, Unset]):
            experience_tag_i_ds (Union[List[str], None, Unset]):
            experience_names (Union[List[str], None, Unset]):
            experience_tag_names (Union[List[str], None, Unset]):
            build_id (Union[Unset, str]):
            metrics_build_id (Union[Unset, str]):
     """

    parameters: Union[Unset, List['SweepParameter']] = UNSET
    experience_i_ds: Union[List[str], None, Unset] = UNSET
    experience_tag_i_ds: Union[List[str], None, Unset] = UNSET
    experience_names: Union[List[str], None, Unset] = UNSET
    experience_tag_names: Union[List[str], None, Unset] = UNSET
    build_id: Union[Unset, str] = UNSET
    metrics_build_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.sweep_parameter import SweepParameter
        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)





        experience_i_ds: Union[List[str], None, Unset]
        if isinstance(self.experience_i_ds, Unset):
            experience_i_ds = UNSET
        elif isinstance(self.experience_i_ds, list):
            experience_i_ds = self.experience_i_ds




        else:
            experience_i_ds = self.experience_i_ds

        experience_tag_i_ds: Union[List[str], None, Unset]
        if isinstance(self.experience_tag_i_ds, Unset):
            experience_tag_i_ds = UNSET
        elif isinstance(self.experience_tag_i_ds, list):
            experience_tag_i_ds = self.experience_tag_i_ds




        else:
            experience_tag_i_ds = self.experience_tag_i_ds

        experience_names: Union[List[str], None, Unset]
        if isinstance(self.experience_names, Unset):
            experience_names = UNSET
        elif isinstance(self.experience_names, list):
            experience_names = self.experience_names




        else:
            experience_names = self.experience_names

        experience_tag_names: Union[List[str], None, Unset]
        if isinstance(self.experience_tag_names, Unset):
            experience_tag_names = UNSET
        elif isinstance(self.experience_tag_names, list):
            experience_tag_names = self.experience_tag_names




        else:
            experience_tag_names = self.experience_tag_names

        build_id = self.build_id

        metrics_build_id = self.metrics_build_id


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if experience_i_ds is not UNSET:
            field_dict["experienceIDs"] = experience_i_ds
        if experience_tag_i_ds is not UNSET:
            field_dict["experienceTagIDs"] = experience_tag_i_ds
        if experience_names is not UNSET:
            field_dict["experienceNames"] = experience_names
        if experience_tag_names is not UNSET:
            field_dict["experienceTagNames"] = experience_tag_names
        if build_id is not UNSET:
            field_dict["buildID"] = build_id
        if metrics_build_id is not UNSET:
            field_dict["metricsBuildID"] = metrics_build_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sweep_parameter import SweepParameter
        d = src_dict.copy()
        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in (_parameters or []):
            parameters_item = SweepParameter.from_dict(parameters_item_data)



            parameters.append(parameters_item)


        def _parse_experience_i_ds(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experience_i_ds_type_0 = cast(List[str], data)

                return experience_i_ds_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        experience_i_ds = _parse_experience_i_ds(d.pop("experienceIDs", UNSET))


        def _parse_experience_tag_i_ds(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experience_tag_i_ds_type_0 = cast(List[str], data)

                return experience_tag_i_ds_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        experience_tag_i_ds = _parse_experience_tag_i_ds(d.pop("experienceTagIDs", UNSET))


        def _parse_experience_names(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experience_names_type_0 = cast(List[str], data)

                return experience_names_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        experience_names = _parse_experience_names(d.pop("experienceNames", UNSET))


        def _parse_experience_tag_names(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experience_tag_names_type_0 = cast(List[str], data)

                return experience_tag_names_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        experience_tag_names = _parse_experience_tag_names(d.pop("experienceTagNames", UNSET))


        build_id = d.pop("buildID", UNSET)

        metrics_build_id = d.pop("metricsBuildID", UNSET)

        parameter_sweep_input = cls(
            parameters=parameters,
            experience_i_ds=experience_i_ds,
            experience_tag_i_ds=experience_tag_i_ds,
            experience_names=experience_names,
            experience_tag_names=experience_tag_names,
            build_id=build_id,
            metrics_build_id=metrics_build_id,
        )

        parameter_sweep_input.additional_properties = d
        return parameter_sweep_input

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
