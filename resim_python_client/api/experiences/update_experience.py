from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.experience import Experience
from ...models.update_experience_json_body import UpdateExperienceJsonBody
from ...types import Response


def _get_kwargs(
    experience_id: str,
    *,
    json_body: UpdateExperienceJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/experiences/{experienceID}".format(
            experienceID=experience_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Experience]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Experience.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, Experience]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    experience_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceJsonBody,
) -> Response[Union[Any, Experience]]:
    """Updates the experience.

    Args:
        experience_id (str):
        json_body (UpdateExperienceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Experience]]
    """

    kwargs = _get_kwargs(
        experience_id=experience_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experience_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceJsonBody,
) -> Optional[Union[Any, Experience]]:
    """Updates the experience.

    Args:
        experience_id (str):
        json_body (UpdateExperienceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Experience]
    """

    return sync_detailed(
        experience_id=experience_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    experience_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceJsonBody,
) -> Response[Union[Any, Experience]]:
    """Updates the experience.

    Args:
        experience_id (str):
        json_body (UpdateExperienceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Experience]]
    """

    kwargs = _get_kwargs(
        experience_id=experience_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experience_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceJsonBody,
) -> Optional[Union[Any, Experience]]:
    """Updates the experience.

    Args:
        experience_id (str):
        json_body (UpdateExperienceJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Experience]
    """

    return (
        await asyncio_detailed(
            experience_id=experience_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
