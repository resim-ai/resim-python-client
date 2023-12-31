from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.build import Build
from ...types import Response


def _get_kwargs(
    project_id: str,
    branch_id: str,
    *,
    json_body: Build,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectID}/branches/{branchID}/builds".format(
            projectID=project_id,
            branchID=branch_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Build]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Build.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Build]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    branch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Build,
) -> Response[Union[Any, Build]]:
    """Adds a build.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        branch_id (str):
        json_body (Build):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Build]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        branch_id=branch_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    branch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Build,
) -> Optional[Union[Any, Build]]:
    """Adds a build.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        branch_id (str):
        json_body (Build):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Build]
    """

    return sync_detailed(
        project_id=project_id,
        branch_id=branch_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    branch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Build,
) -> Response[Union[Any, Build]]:
    """Adds a build.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        branch_id (str):
        json_body (Build):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Build]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        branch_id=branch_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    branch_id: str,
    *,
    client: AuthenticatedClient,
    json_body: Build,
) -> Optional[Union[Any, Build]]:
    """Adds a build.  ID should be omitted and will be returned in the response.

    Args:
        project_id (str):
        branch_id (str):
        json_body (Build):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Build]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            branch_id=branch_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
