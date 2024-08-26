from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metric_tag import MetricTag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    json_body: List["MetricTag"],
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:

    pass

    params: Dict[str, Any] = {}
    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": "/projects/{projectID}/reports/{reportID}/metrics/{metricID}/tags".format(
            projectID=project_id,
            reportID=report_id,
            metricID=metric_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["MetricTag"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MetricTag.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["MetricTag"]]]:
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
    json_body: List["MetricTag"],
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["MetricTag"]]]:
    """Adds tags to the given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        json_body (List['MetricTag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['MetricTag']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        report_id=report_id,
        metric_id=metric_id,
        json_body=json_body,
        page_size=page_size,
        page_token=page_token,
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
    json_body: List["MetricTag"],
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["MetricTag"]]]:
    """Adds tags to the given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        json_body (List['MetricTag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['MetricTag']]
    """

    return sync_detailed(
        project_id=project_id,
        report_id=report_id,
        metric_id=metric_id,
        client=client,
        json_body=json_body,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List["MetricTag"],
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["MetricTag"]]]:
    """Adds tags to the given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        json_body (List['MetricTag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['MetricTag']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        report_id=report_id,
        metric_id=metric_id,
        json_body=json_body,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    report_id: str,
    metric_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List["MetricTag"],
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["MetricTag"]]]:
    """Adds tags to the given report metric

    Args:
        project_id (str):
        report_id (str):
        metric_id (str):
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        json_body (List['MetricTag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['MetricTag']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            report_id=report_id,
            metric_id=metric_id,
            client=client,
            json_body=json_body,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
