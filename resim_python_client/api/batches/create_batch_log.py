from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_log import BatchLog
from ...types import Response


def _get_kwargs(
    project_id: str,
    batch_id: str,
    *,
    body: BatchLog,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/batches/{batch_id}/logs".format(
            project_id=project_id,
            batch_id=batch_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BatchLog]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = BatchLog.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BatchLog]]:
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
    body: BatchLog,
) -> Response[Union[Any, BatchLog]]:
    """Adds a log.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        batch_id (str):
        body (BatchLog):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BatchLog]]
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
    body: BatchLog,
) -> Optional[Union[Any, BatchLog]]:
    """Adds a log.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        batch_id (str):
        body (BatchLog):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BatchLog]
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
    body: BatchLog,
) -> Response[Union[Any, BatchLog]]:
    """Adds a log.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        batch_id (str):
        body (BatchLog):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BatchLog]]
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
    body: BatchLog,
) -> Optional[Union[Any, BatchLog]]:
    """Adds a log.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        batch_id (str):
        body (BatchLog):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BatchLog]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            batch_id=batch_id,
            client=client,
            body=body,
        )
    ).parsed
