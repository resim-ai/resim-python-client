from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union

if TYPE_CHECKING:
    from ..models.view_object import ViewObject
    from ..models.view_metadata import ViewMetadata


T = TypeVar("T", bound="ViewObjectAndMetadata")


@_attrs_define
class ViewObjectAndMetadata:
    """
    Attributes:
        view_metadata (Union[Unset, List['ViewMetadata']]):
        view_object (Union[Unset, ViewObject]):
    """

    view_metadata: Union[Unset, List["ViewMetadata"]] = UNSET
    view_object: Union[Unset, "ViewObject"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        view_metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.view_metadata, Unset):
            view_metadata = []
            for view_metadata_item_data in self.view_metadata:
                view_metadata_item = view_metadata_item_data.to_dict()
                view_metadata.append(view_metadata_item)

        view_object: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.view_object, Unset):
            view_object = self.view_object.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if view_metadata is not UNSET:
            field_dict["viewMetadata"] = view_metadata
        if view_object is not UNSET:
            field_dict["viewObject"] = view_object

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.view_object import ViewObject
        from ..models.view_metadata import ViewMetadata

        d = src_dict.copy()
        view_metadata = []
        _view_metadata = d.pop("viewMetadata", UNSET)
        for view_metadata_item_data in _view_metadata or []:
            view_metadata_item = ViewMetadata.from_dict(view_metadata_item_data)

            view_metadata.append(view_metadata_item)

        _view_object = d.pop("viewObject", UNSET)
        view_object: Union[Unset, ViewObject]
        if isinstance(_view_object, Unset):
            view_object = UNSET
        else:
            view_object = ViewObject.from_dict(_view_object)

        view_object_and_metadata = cls(
            view_metadata=view_metadata,
            view_object=view_object,
        )

        view_object_and_metadata.additional_properties = d
        return view_object_and_metadata

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
