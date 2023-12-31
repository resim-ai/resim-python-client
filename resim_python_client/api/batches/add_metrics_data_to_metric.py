from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_metrics_data_to_metric_response_201 import AddMetricsDataToMetricResponse201
from ...types import Response


def _get_kwargs(
    batch_id: str,
    job_id: str,
    metric_id: str,
    *,
    json_body: List[str],
) -> Dict[str, Any]:
    pass

    json_json_body = json_body

    return {
        "method": "post",
        "url": "/batches/{batchID}/jobs/{jobID}/metrics/{metricID}/metricsData".format(
            batchID=batch_id,
            jobID=job_id,
            metricID=metric_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddMetricsDataToMetricResponse201, Any]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AddMetricsDataToMetricResponse201.from_dict(response.json())

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
) -> Response[Union[AddMetricsDataToMetricResponse201, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    job_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
) -> Response[Union[AddMetricsDataToMetricResponse201, Any]]:
    """Adds metrics data (IDs) to a given metric

    Args:
        batch_id (str):
        job_id (str):
        metric_id (str):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddMetricsDataToMetricResponse201, Any]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        job_id=job_id,
        metric_id=metric_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    job_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
) -> Optional[Union[AddMetricsDataToMetricResponse201, Any]]:
    """Adds metrics data (IDs) to a given metric

    Args:
        batch_id (str):
        job_id (str):
        metric_id (str):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddMetricsDataToMetricResponse201, Any]
    """

    return sync_detailed(
        batch_id=batch_id,
        job_id=job_id,
        metric_id=metric_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    job_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
) -> Response[Union[AddMetricsDataToMetricResponse201, Any]]:
    """Adds metrics data (IDs) to a given metric

    Args:
        batch_id (str):
        job_id (str):
        metric_id (str):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddMetricsDataToMetricResponse201, Any]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        job_id=job_id,
        metric_id=metric_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    job_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
) -> Optional[Union[AddMetricsDataToMetricResponse201, Any]]:
    """Adds metrics data (IDs) to a given metric

    Args:
        batch_id (str):
        job_id (str):
        metric_id (str):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddMetricsDataToMetricResponse201, Any]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            job_id=job_id,
            metric_id=metric_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
