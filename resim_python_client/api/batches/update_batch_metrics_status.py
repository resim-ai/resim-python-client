from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch import Batch
from ...models.metric_status import MetricStatus
from ...types import Response


def _get_kwargs(
    project_id: str,
    batch_id: str,
    *,
    body: MetricStatus,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/batches/{batch_id}/metricsStatus".format(
            project_id=project_id,
            batch_id=batch_id,
        ),
    }

    _body = body.value

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Batch]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Batch.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, Batch]]:
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
    body: MetricStatus,
) -> Response[Union[Any, Batch]]:
    """Updates a batch's metrics status.

    Args:
        project_id (str):
        batch_id (str):
        body (MetricStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Batch]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        body=body,
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
    body: MetricStatus,
) -> Optional[Union[Any, Batch]]:
    """Updates a batch's metrics status.

    Args:
        project_id (str):
        batch_id (str):
        body (MetricStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Batch]
    """

    return sync_detailed(
        project_id=project_id,
        batch_id=batch_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: MetricStatus,
) -> Response[Union[Any, Batch]]:
    """Updates a batch's metrics status.

    Args:
        project_id (str):
        batch_id (str):
        body (MetricStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Batch]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: MetricStatus,
) -> Optional[Union[Any, Batch]]:
    """Updates a batch's metrics status.

    Args:
        project_id (str):
        batch_id (str):
        body (MetricStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Batch]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            batch_id=batch_id,
            client=client,
            body=body,
        )
    ).parsed
