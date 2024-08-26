from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metrics_data import MetricsData
from ...types import Response


def _get_kwargs(
    project_id: str,
    report_id: str,
    *,
    json_body: MetricsData,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectID}/reports/{reportID}/metricsData".format(
            projectID=project_id,
            reportID=report_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MetricsData]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = MetricsData.from_dict(response.json())

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
) -> Response[Union[Any, MetricsData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetricsData,
) -> Response[Union[Any, MetricsData]]:
    """Creates a new metrics data associated with a report. If this metrics data is an external file, then
    the filename field must be populated.

    Args:
        project_id (str):
        report_id (str):
        json_body (MetricsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetricsData]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        report_id=report_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetricsData,
) -> Optional[Union[Any, MetricsData]]:
    """Creates a new metrics data associated with a report. If this metrics data is an external file, then
    the filename field must be populated.

    Args:
        project_id (str):
        report_id (str):
        json_body (MetricsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MetricsData]
    """

    return sync_detailed(
        project_id=project_id,
        report_id=report_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetricsData,
) -> Response[Union[Any, MetricsData]]:
    """Creates a new metrics data associated with a report. If this metrics data is an external file, then
    the filename field must be populated.

    Args:
        project_id (str):
        report_id (str):
        json_body (MetricsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MetricsData]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        report_id=report_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    report_id: str,
    *,
    client: AuthenticatedClient,
    json_body: MetricsData,
) -> Optional[Union[Any, MetricsData]]:
    """Creates a new metrics data associated with a report. If this metrics data is an external file, then
    the filename field must be populated.

    Args:
        project_id (str):
        report_id (str):
        json_body (MetricsData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MetricsData]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            report_id=report_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
