from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_batch_metrics_data_for_batch_metrics_data_i_ds_response_200 import (
    ListBatchMetricsDataForBatchMetricsDataIDsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    batch_id: str,
    metrics_data_id: List[str],
    *,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/batches/{batchID}/metricsData/{metricsDataID}".format(
            batchID=batch_id,
            metricsDataID=metrics_data_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListBatchMetricsDataForBatchMetricsDataIDsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    metrics_data_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]:
    """Lists the batch metrics data associated with given batch metrics data IDs

    Args:
        batch_id (str):
        metrics_data_id (List[str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        metrics_data_id=metrics_data_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    metrics_data_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]:
    """Lists the batch metrics data associated with given batch metrics data IDs

    Args:
        batch_id (str):
        metrics_data_id (List[str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]
    """

    return sync_detailed(
        batch_id=batch_id,
        metrics_data_id=metrics_data_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    metrics_data_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]:
    """Lists the batch metrics data associated with given batch metrics data IDs

    Args:
        batch_id (str):
        metrics_data_id (List[str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        metrics_data_id=metrics_data_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    metrics_data_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]]:
    """Lists the batch metrics data associated with given batch metrics data IDs

    Args:
        batch_id (str):
        metrics_data_id (List[str]):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListBatchMetricsDataForBatchMetricsDataIDsResponse200]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            metrics_data_id=metrics_data_id,
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
