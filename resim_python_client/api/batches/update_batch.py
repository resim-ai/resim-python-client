from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch import Batch
from ...models.update_batch_input import UpdateBatchInput
from ...types import Response


def _get_kwargs(
    project_id: str,
    batch_id: str,
    *,
    json_body: UpdateBatchInput,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/projects/{projectID}/batches/{batchID}".format(
            projectID=project_id,
            batchID=batch_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Batch]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Batch.from_dict(response.json())

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
    json_body: UpdateBatchInput,
) -> Response[Union[Any, Batch]]:
    """Updates the batch.

    Args:
        project_id (str):
        batch_id (str):
        json_body (UpdateBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Batch]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        json_body=json_body,
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
    json_body: UpdateBatchInput,
) -> Optional[Union[Any, Batch]]:
    """Updates the batch.

    Args:
        project_id (str):
        batch_id (str):
        json_body (UpdateBatchInput):

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
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateBatchInput,
) -> Response[Union[Any, Batch]]:
    """Updates the batch.

    Args:
        project_id (str):
        batch_id (str):
        json_body (UpdateBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Batch]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateBatchInput,
) -> Optional[Union[Any, Batch]]:
    """Updates the batch.

    Args:
        project_id (str):
        batch_id (str):
        json_body (UpdateBatchInput):

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
            json_body=json_body,
        )
    ).parsed
