from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conflated_job_status import ConflatedJobStatus
from ...models.job_status import JobStatus
from ...models.list_jobs_output import ListJobsOutput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    batch_id: str,
    *,
    status: Union[Unset, None, JobStatus] = UNSET,
    conflated_status: Union[Unset, None, List[ConflatedJobStatus]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    json_conflated_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(conflated_status, Unset):
        if conflated_status is None:
            json_conflated_status = None
        else:
            json_conflated_status = []
            for conflated_status_item_data in conflated_status:
                conflated_status_item = conflated_status_item_data.value

                json_conflated_status.append(conflated_status_item)

    params["conflatedStatus"] = json_conflated_status

    params["name"] = name

    params["text"] = text

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/projects/{projectID}/batches/{batchID}/jobs".format(
            projectID=project_id,
            batchID=batch_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListJobsOutput]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListJobsOutput.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ListJobsOutput]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, JobStatus] = UNSET,
    conflated_status: Union[Unset, None, List[ConflatedJobStatus]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ListJobsOutput]]:
    """List the jobs in the given batch.

    Args:
        project_id (str):
        batch_id (str):
        status (Union[Unset, None, JobStatus]):
        conflated_status (Union[Unset, None, List[ConflatedJobStatus]]):
        name (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListJobsOutput]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        status=status,
        conflated_status=conflated_status,
        name=name,
        text=text,
        page_size=page_size,
        page_token=page_token,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, JobStatus] = UNSET,
    conflated_status: Union[Unset, None, List[ConflatedJobStatus]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ListJobsOutput]]:
    """List the jobs in the given batch.

    Args:
        project_id (str):
        batch_id (str):
        status (Union[Unset, None, JobStatus]):
        conflated_status (Union[Unset, None, List[ConflatedJobStatus]]):
        name (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListJobsOutput]
    """

    return sync_detailed(
        project_id=project_id,
        batch_id=batch_id,
        client=client,
        status=status,
        conflated_status=conflated_status,
        name=name,
        text=text,
        page_size=page_size,
        page_token=page_token,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, JobStatus] = UNSET,
    conflated_status: Union[Unset, None, List[ConflatedJobStatus]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ListJobsOutput]]:
    """List the jobs in the given batch.

    Args:
        project_id (str):
        batch_id (str):
        status (Union[Unset, None, JobStatus]):
        conflated_status (Union[Unset, None, List[ConflatedJobStatus]]):
        name (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListJobsOutput]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        status=status,
        conflated_status=conflated_status,
        name=name,
        text=text,
        page_size=page_size,
        page_token=page_token,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, JobStatus] = UNSET,
    conflated_status: Union[Unset, None, List[ConflatedJobStatus]] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    text: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ListJobsOutput]]:
    """List the jobs in the given batch.

    Args:
        project_id (str):
        batch_id (str):
        status (Union[Unset, None, JobStatus]):
        conflated_status (Union[Unset, None, List[ConflatedJobStatus]]):
        name (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListJobsOutput]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            batch_id=batch_id,
            client=client,
            status=status,
            conflated_status=conflated_status,
            name=name,
            text=text,
            page_size=page_size,
            page_token=page_token,
            order_by=order_by,
        )
    ).parsed
