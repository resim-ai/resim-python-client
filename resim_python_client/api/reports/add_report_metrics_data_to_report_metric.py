from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.report_metrics_data_to_report_metric import ReportMetricsDataToReportMetric
from ...types import Response


def _get_kwargs(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    body: List[str],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/reports/{report_id}/metrics/{metric_id}/metricsData".format(
            project_id=project_id,
            report_id=report_id,
            metric_id=metric_id,
        ),
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ReportMetricsDataToReportMetric]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ReportMetricsDataToReportMetric.from_dict(response.json())

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
) -> Response[Union[Any, ReportMetricsDataToReportMetric]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Response[Union[Any, ReportMetricsDataToReportMetric]]:
    """Adds report metrics data (IDs) to a given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReportMetricsDataToReportMetric]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        report_id=report_id,
        metric_id=metric_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Optional[Union[Any, ReportMetricsDataToReportMetric]]:
    """Adds report metrics data (IDs) to a given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReportMetricsDataToReportMetric]
    """

    return sync_detailed(
        project_id=project_id,
        report_id=report_id,
        metric_id=metric_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Response[Union[Any, ReportMetricsDataToReportMetric]]:
    """Adds report metrics data (IDs) to a given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReportMetricsDataToReportMetric]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        report_id=report_id,
        metric_id=metric_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    body: List[str],
) -> Optional[Union[Any, ReportMetricsDataToReportMetric]]:
    """Adds report metrics data (IDs) to a given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReportMetricsDataToReportMetric]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            report_id=report_id,
            metric_id=metric_id,
            client=client,
            body=body,
        )
    ).parsed
