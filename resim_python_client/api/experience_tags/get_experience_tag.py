from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.experience_tag import ExperienceTag
from ...types import Response


def _get_kwargs(
    experience_tag_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/experienceTags/{experienceTagID}".format(
            experienceTagID=experience_tag_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ExperienceTag]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExperienceTag.from_dict(response.json())

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
) -> Response[Union[Any, ExperienceTag]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExperienceTag]]:
    """Returns a specific experience tag.

    Args:
        experience_tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExperienceTag]]
    """

    kwargs = _get_kwargs(
        experience_tag_id=experience_tag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExperienceTag]]:
    """Returns a specific experience tag.

    Args:
        experience_tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExperienceTag]
    """

    return sync_detailed(
        experience_tag_id=experience_tag_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ExperienceTag]]:
    """Returns a specific experience tag.

    Args:
        experience_tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExperienceTag]]
    """

    kwargs = _get_kwargs(
        experience_tag_id=experience_tag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ExperienceTag]]:
    """Returns a specific experience tag.

    Args:
        experience_tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExperienceTag]
    """

    return (
        await asyncio_detailed(
            experience_tag_id=experience_tag_id,
            client=client,
        )
    ).parsed
