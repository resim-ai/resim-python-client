from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_view_sessions_response_200 import ListViewSessionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/view/sessions",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListViewSessionsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListViewSessionsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListViewSessionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[ListViewSessionsResponse200]:
    """Lists all View sessions.

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListViewSessionsResponse200]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[ListViewSessionsResponse200]:
    """Lists all View sessions.

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListViewSessionsResponse200
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[ListViewSessionsResponse200]:
    """Lists all View sessions.

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListViewSessionsResponse200]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[ListViewSessionsResponse200]:
    """Lists all View sessions.

    Args:
        page_size (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListViewSessionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
            order_by=order_by,
        )
    ).parsed
