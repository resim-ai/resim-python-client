from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.experience_tag import ExperienceTag
from ...models.update_experience_tag_json_body import UpdateExperienceTagJsonBody
from ...types import Response


def _get_kwargs(
    experience_tag_id: str,
    *,
    json_body: UpdateExperienceTagJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/experienceTags/{experienceTagID}".format(
            experienceTagID=experience_tag_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ExperienceTag]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExperienceTag.from_dict(response.json())

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
    json_body: UpdateExperienceTagJsonBody,
) -> Response[Union[Any, ExperienceTag]]:
    """Updates the experience tag.  Experience membership cannot be changed with this method.

    Args:
        experience_tag_id (str):
        json_body (UpdateExperienceTagJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExperienceTag]]
    """

    kwargs = _get_kwargs(
        experience_tag_id=experience_tag_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceTagJsonBody,
) -> Optional[Union[Any, ExperienceTag]]:
    """Updates the experience tag.  Experience membership cannot be changed with this method.

    Args:
        experience_tag_id (str):
        json_body (UpdateExperienceTagJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ExperienceTag]
    """

    return sync_detailed(
        experience_tag_id=experience_tag_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceTagJsonBody,
) -> Response[Union[Any, ExperienceTag]]:
    """Updates the experience tag.  Experience membership cannot be changed with this method.

    Args:
        experience_tag_id (str):
        json_body (UpdateExperienceTagJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ExperienceTag]]
    """

    kwargs = _get_kwargs(
        experience_tag_id=experience_tag_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experience_tag_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateExperienceTagJsonBody,
) -> Optional[Union[Any, ExperienceTag]]:
    """Updates the experience tag.  Experience membership cannot be changed with this method.

    Args:
        experience_tag_id (str):
        json_body (UpdateExperienceTagJsonBody):

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
            json_body=json_body,
        )
    ).parsed
