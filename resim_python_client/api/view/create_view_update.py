from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_view_update_response_201 import CreateViewUpdateResponse201
from ...types import Response


def _get_kwargs(
    view_session_id: str,
    view_update_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "post",
        "url": "/view/sessions/{viewSessionID}/updates/{viewUpdateID}".format(
            viewSessionID=view_session_id,
            viewUpdateID=view_update_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateViewUpdateResponse201]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateViewUpdateResponse201.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CreateViewUpdateResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    view_session_id: str,
    view_update_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateViewUpdateResponse201]]:
    """Adds an update to the View session.  Updates will be serialized sequentially by ID.

    Args:
        view_session_id (str):
        view_update_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateViewUpdateResponse201]]
    """

    kwargs = _get_kwargs(
        view_session_id=view_session_id,
        view_update_id=view_update_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    view_session_id: str,
    view_update_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateViewUpdateResponse201]]:
    """Adds an update to the View session.  Updates will be serialized sequentially by ID.

    Args:
        view_session_id (str):
        view_update_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateViewUpdateResponse201]
    """

    return sync_detailed(
        view_session_id=view_session_id,
        view_update_id=view_update_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    view_session_id: str,
    view_update_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, CreateViewUpdateResponse201]]:
    """Adds an update to the View session.  Updates will be serialized sequentially by ID.

    Args:
        view_session_id (str):
        view_update_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateViewUpdateResponse201]]
    """

    kwargs = _get_kwargs(
        view_session_id=view_session_id,
        view_update_id=view_update_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    view_session_id: str,
    view_update_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, CreateViewUpdateResponse201]]:
    """Adds an update to the View session.  Updates will be serialized sequentially by ID.

    Args:
        view_session_id (str):
        view_update_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateViewUpdateResponse201]
    """

    return (
        await asyncio_detailed(
            view_session_id=view_session_id,
            view_update_id=view_update_id,
            client=client,
        )
    ).parsed
