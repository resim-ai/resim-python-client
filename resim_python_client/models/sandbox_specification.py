from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union

if TYPE_CHECKING:
    from ..models.batch_object_description import BatchObjectDescription
    from ..models.build_object_description import BuildObjectDescription
    from ..models.sweep_object_description import SweepObjectDescription
    from ..models.system_object_description import SystemObjectDescription
    from ..models.branch_object_description import BranchObjectDescription
    from ..models.test_suite_run_object_description import TestSuiteRunObjectDescription
    from ..models.test_suite_object_description import TestSuiteObjectDescription
    from ..models.experience_tag_object_description import (
        ExperienceTagObjectDescription,
    )
    from ..models.experience_object_description import ExperienceObjectDescription
    from ..models.metrics_build_object_description import MetricsBuildObjectDescription
    from ..models.project_object_description import ProjectObjectDescription


T = TypeVar("T", bound="SandboxSpecification")


@_attrs_define
class SandboxSpecification:
    """
    Attributes:
        batches (Union[Unset, List['BatchObjectDescription']]):
        branches (Union[Unset, List['BranchObjectDescription']]):
        builds (Union[Unset, List['BuildObjectDescription']]):
        experience_tags (Union[Unset, List['ExperienceTagObjectDescription']]):
        experiences (Union[Unset, List['ExperienceObjectDescription']]):
        metrics_builds (Union[Unset, List['MetricsBuildObjectDescription']]):
        projects (Union[Unset, List['ProjectObjectDescription']]):
        sweeps (Union[Unset, List['SweepObjectDescription']]):
        systems (Union[Unset, List['SystemObjectDescription']]):
        test_suite_runs (Union[Unset, List['TestSuiteRunObjectDescription']]):
        test_suites (Union[Unset, List['TestSuiteObjectDescription']]):
    """

    batches: Union[Unset, List["BatchObjectDescription"]] = UNSET
    branches: Union[Unset, List["BranchObjectDescription"]] = UNSET
    builds: Union[Unset, List["BuildObjectDescription"]] = UNSET
    experience_tags: Union[Unset, List["ExperienceTagObjectDescription"]] = UNSET
    experiences: Union[Unset, List["ExperienceObjectDescription"]] = UNSET
    metrics_builds: Union[Unset, List["MetricsBuildObjectDescription"]] = UNSET
    projects: Union[Unset, List["ProjectObjectDescription"]] = UNSET
    sweeps: Union[Unset, List["SweepObjectDescription"]] = UNSET
    systems: Union[Unset, List["SystemObjectDescription"]] = UNSET
    test_suite_runs: Union[Unset, List["TestSuiteRunObjectDescription"]] = UNSET
    test_suites: Union[Unset, List["TestSuiteObjectDescription"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.batches, Unset):
            batches = []
            for batches_item_data in self.batches:
                batches_item = batches_item_data.to_dict()
                batches.append(batches_item)

        branches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        builds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.builds, Unset):
            builds = []
            for builds_item_data in self.builds:
                builds_item = builds_item_data.to_dict()
                builds.append(builds_item)

        experience_tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.experience_tags, Unset):
            experience_tags = []
            for experience_tags_item_data in self.experience_tags:
                experience_tags_item = experience_tags_item_data.to_dict()
                experience_tags.append(experience_tags_item)

        experiences: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.experiences, Unset):
            experiences = []
            for experiences_item_data in self.experiences:
                experiences_item = experiences_item_data.to_dict()
                experiences.append(experiences_item)

        metrics_builds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics_builds, Unset):
            metrics_builds = []
            for metrics_builds_item_data in self.metrics_builds:
                metrics_builds_item = metrics_builds_item_data.to_dict()
                metrics_builds.append(metrics_builds_item)

        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        sweeps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sweeps, Unset):
            sweeps = []
            for sweeps_item_data in self.sweeps:
                sweeps_item = sweeps_item_data.to_dict()
                sweeps.append(sweeps_item)

        systems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = []
            for systems_item_data in self.systems:
                systems_item = systems_item_data.to_dict()
                systems.append(systems_item)

        test_suite_runs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_suite_runs, Unset):
            test_suite_runs = []
            for test_suite_runs_item_data in self.test_suite_runs:
                test_suite_runs_item = test_suite_runs_item_data.to_dict()
                test_suite_runs.append(test_suite_runs_item)

        test_suites: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.test_suites, Unset):
            test_suites = []
            for test_suites_item_data in self.test_suites:
                test_suites_item = test_suites_item_data.to_dict()
                test_suites.append(test_suites_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batches is not UNSET:
            field_dict["batches"] = batches
        if branches is not UNSET:
            field_dict["branches"] = branches
        if builds is not UNSET:
            field_dict["builds"] = builds
        if experience_tags is not UNSET:
            field_dict["experienceTags"] = experience_tags
        if experiences is not UNSET:
            field_dict["experiences"] = experiences
        if metrics_builds is not UNSET:
            field_dict["metricsBuilds"] = metrics_builds
        if projects is not UNSET:
            field_dict["projects"] = projects
        if sweeps is not UNSET:
            field_dict["sweeps"] = sweeps
        if systems is not UNSET:
            field_dict["systems"] = systems
        if test_suite_runs is not UNSET:
            field_dict["testSuiteRuns"] = test_suite_runs
        if test_suites is not UNSET:
            field_dict["testSuites"] = test_suites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.batch_object_description import BatchObjectDescription
        from ..models.build_object_description import BuildObjectDescription
        from ..models.sweep_object_description import SweepObjectDescription
        from ..models.system_object_description import SystemObjectDescription
        from ..models.branch_object_description import BranchObjectDescription
        from ..models.test_suite_run_object_description import (
            TestSuiteRunObjectDescription,
        )
        from ..models.test_suite_object_description import TestSuiteObjectDescription
        from ..models.experience_tag_object_description import (
            ExperienceTagObjectDescription,
        )
        from ..models.experience_object_description import ExperienceObjectDescription
        from ..models.metrics_build_object_description import (
            MetricsBuildObjectDescription,
        )
        from ..models.project_object_description import ProjectObjectDescription

        d = src_dict.copy()
        batches = []
        _batches = d.pop("batches", UNSET)
        for batches_item_data in _batches or []:
            batches_item = BatchObjectDescription.from_dict(batches_item_data)

            batches.append(batches_item)

        branches = []
        _branches = d.pop("branches", UNSET)
        for branches_item_data in _branches or []:
            branches_item = BranchObjectDescription.from_dict(branches_item_data)

            branches.append(branches_item)

        builds = []
        _builds = d.pop("builds", UNSET)
        for builds_item_data in _builds or []:
            builds_item = BuildObjectDescription.from_dict(builds_item_data)

            builds.append(builds_item)

        experience_tags = []
        _experience_tags = d.pop("experienceTags", UNSET)
        for experience_tags_item_data in _experience_tags or []:
            experience_tags_item = ExperienceTagObjectDescription.from_dict(
                experience_tags_item_data
            )

            experience_tags.append(experience_tags_item)

        experiences = []
        _experiences = d.pop("experiences", UNSET)
        for experiences_item_data in _experiences or []:
            experiences_item = ExperienceObjectDescription.from_dict(
                experiences_item_data
            )

            experiences.append(experiences_item)

        metrics_builds = []
        _metrics_builds = d.pop("metricsBuilds", UNSET)
        for metrics_builds_item_data in _metrics_builds or []:
            metrics_builds_item = MetricsBuildObjectDescription.from_dict(
                metrics_builds_item_data
            )

            metrics_builds.append(metrics_builds_item)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = ProjectObjectDescription.from_dict(projects_item_data)

            projects.append(projects_item)

        sweeps = []
        _sweeps = d.pop("sweeps", UNSET)
        for sweeps_item_data in _sweeps or []:
            sweeps_item = SweepObjectDescription.from_dict(sweeps_item_data)

            sweeps.append(sweeps_item)

        systems = []
        _systems = d.pop("systems", UNSET)
        for systems_item_data in _systems or []:
            systems_item = SystemObjectDescription.from_dict(systems_item_data)

            systems.append(systems_item)

        test_suite_runs = []
        _test_suite_runs = d.pop("testSuiteRuns", UNSET)
        for test_suite_runs_item_data in _test_suite_runs or []:
            test_suite_runs_item = TestSuiteRunObjectDescription.from_dict(
                test_suite_runs_item_data
            )

            test_suite_runs.append(test_suite_runs_item)

        test_suites = []
        _test_suites = d.pop("testSuites", UNSET)
        for test_suites_item_data in _test_suites or []:
            test_suites_item = TestSuiteObjectDescription.from_dict(
                test_suites_item_data
            )

            test_suites.append(test_suites_item)

        sandbox_specification = cls(
            batches=batches,
            branches=branches,
            builds=builds,
            experience_tags=experience_tags,
            experiences=experiences,
            metrics_builds=metrics_builds,
            projects=projects,
            sweeps=sweeps,
            systems=systems,
            test_suite_runs=test_suite_runs,
            test_suites=test_suites,
        )

        sandbox_specification.additional_properties = d
        return sandbox_specification

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
