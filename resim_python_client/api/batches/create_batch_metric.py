from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_metric import BatchMetric
from ...types import Response


def _get_kwargs(
    batch_id: str,
    *,
    json_body: BatchMetric,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/batches/{batchID}/metrics".format(
            batchID=batch_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BatchMetric]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = BatchMetric.from_dict(response.json())

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
) -> Response[Union[Any, BatchMetric]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: BatchMetric,
) -> Response[Union[Any, BatchMetric]]:
    """Adds a batch metric. ID and location should be omitted and will be returned in the response.

    Args:
        batch_id (str):
        json_body (BatchMetric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BatchMetric]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: BatchMetric,
) -> Optional[Union[Any, BatchMetric]]:
    """Adds a batch metric. ID and location should be omitted and will be returned in the response.

    Args:
        batch_id (str):
        json_body (BatchMetric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BatchMetric]
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: BatchMetric,
) -> Response[Union[Any, BatchMetric]]:
    """Adds a batch metric. ID and location should be omitted and will be returned in the response.

    Args:
        batch_id (str):
        json_body (BatchMetric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BatchMetric]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: BatchMetric,
) -> Optional[Union[Any, BatchMetric]]:
    """Adds a batch metric. ID and location should be omitted and will be returned in the response.

    Args:
        batch_id (str):
        json_body (BatchMetric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BatchMetric]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
