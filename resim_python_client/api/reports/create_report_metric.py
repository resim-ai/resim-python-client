from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metric import Metric
from ...types import Response


def _get_kwargs(
    project_id: str,
    report_id: str,
    *,
    json_body: Metric,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectID}/reports/{reportID}/metrics".format(
            projectID=project_id,
            reportID=report_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Metric]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Metric.from_dict(response.json())

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
) -> Response[Union[Any, Metric]]:
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
    json_body: Metric,
) -> Response[Union[Any, Metric]]:
    """Adds a report metric. ID and location should be omitted and will be returned in the response.

    Args:
        project_id (str):
        report_id (str):
        json_body (Metric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Metric]]
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
    json_body: Metric,
) -> Optional[Union[Any, Metric]]:
    """Adds a report metric. ID and location should be omitted and will be returned in the response.

    Args:
        project_id (str):
        report_id (str):
        json_body (Metric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Metric]
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
    json_body: Metric,
) -> Response[Union[Any, Metric]]:
    """Adds a report metric. ID and location should be omitted and will be returned in the response.

    Args:
        project_id (str):
        report_id (str):
        json_body (Metric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Metric]]
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
    json_body: Metric,
) -> Optional[Union[Any, Metric]]:
    """Adds a report metric. ID and location should be omitted and will be returned in the response.

    Args:
        project_id (str):
        report_id (str):
        json_body (Metric):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Metric]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            report_id=report_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
