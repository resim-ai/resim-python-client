from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_metrics_data_and_metric_id_output import ListMetricsDataAndMetricIDOutput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    batch_id: str,
    job_id: str,
    metric_id: List[str],
    *,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/batches/{batch_id}/jobs/{job_id}/metrics/{metric_id}/metricsData".format(
            project_id=project_id,
            batch_id=batch_id,
            job_id=job_id,
            metric_id=metric_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListMetricsDataAndMetricIDOutput]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListMetricsDataAndMetricIDOutput.from_dict(response.json())

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
) -> Response[Union[Any, ListMetricsDataAndMetricIDOutput]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    batch_id: str,
    job_id: str,
    metric_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListMetricsDataAndMetricIDOutput]]:
    """Returns the metrics data associated with given metric ID(s)

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        metric_id (List[str]):
        page_size (Union[Unset, int]):
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListMetricsDataAndMetricIDOutput]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        job_id=job_id,
        metric_id=metric_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    batch_id: str,
    job_id: str,
    metric_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListMetricsDataAndMetricIDOutput]]:
    """Returns the metrics data associated with given metric ID(s)

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        metric_id (List[str]):
        page_size (Union[Unset, int]):
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListMetricsDataAndMetricIDOutput]
    """

    return sync_detailed(
        project_id=project_id,
        batch_id=batch_id,
        job_id=job_id,
        metric_id=metric_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    batch_id: str,
    job_id: str,
    metric_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListMetricsDataAndMetricIDOutput]]:
    """Returns the metrics data associated with given metric ID(s)

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        metric_id (List[str]):
        page_size (Union[Unset, int]):
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListMetricsDataAndMetricIDOutput]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        job_id=job_id,
        metric_id=metric_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    batch_id: str,
    job_id: str,
    metric_id: List[str],
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListMetricsDataAndMetricIDOutput]]:
    """Returns the metrics data associated with given metric ID(s)

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        metric_id (List[str]):
        page_size (Union[Unset, int]):
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListMetricsDataAndMetricIDOutput]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            batch_id=batch_id,
            job_id=job_id,
            metric_id=metric_id,
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
