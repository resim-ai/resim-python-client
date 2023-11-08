from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job import Job
from ...types import Response


def _get_kwargs(
    batch_id: str,
    job_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/batches/{batchID}/jobs/{jobID}".format(
            batchID=batch_id,
            jobID=job_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Job]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Job.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, Job]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Job]]:
    """Retrieve the given job.

    Args:
        batch_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Job]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Job]]:
    """Retrieve the given job.

    Args:
        batch_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Job]
    """

    return sync_detailed(
        batch_id=batch_id,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Job]]:
    """Retrieve the given job.

    Args:
        batch_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Job]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Job]]:
    """Retrieve the given job.

    Args:
        batch_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Job]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            job_id=job_id,
            client=client,
        )
    ).parsed
