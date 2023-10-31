from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.launch_profile import LaunchProfile
from ...types import Response


def _get_kwargs(
    launch_profile_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/launchProfiles/{launchProfileID}".format(
            launchProfileID=launch_profile_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, LaunchProfile]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LaunchProfile.from_dict(response.json())

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
) -> Response[Union[Any, LaunchProfile]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    launch_profile_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, LaunchProfile]]:
    """Returns a specific launch profile.

    Args:
        launch_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LaunchProfile]]
    """

    kwargs = _get_kwargs(
        launch_profile_id=launch_profile_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    launch_profile_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, LaunchProfile]]:
    """Returns a specific launch profile.

    Args:
        launch_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LaunchProfile]
    """

    return sync_detailed(
        launch_profile_id=launch_profile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    launch_profile_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, LaunchProfile]]:
    """Returns a specific launch profile.

    Args:
        launch_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, LaunchProfile]]
    """

    kwargs = _get_kwargs(
        launch_profile_id=launch_profile_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    launch_profile_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, LaunchProfile]]:
    """Returns a specific launch profile.

    Args:
        launch_profile_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, LaunchProfile]
    """

    return (
        await asyncio_detailed(
            launch_profile_id=launch_profile_id,
            client=client,
        )
    ).parsed
