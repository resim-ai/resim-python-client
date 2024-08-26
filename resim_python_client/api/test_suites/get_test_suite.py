from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_suite import TestSuite
from ...types import Response


def _get_kwargs(
    project_id: str,
    test_suite_id: str,
) -> Dict[str, Any]:

    pass

    return {
        "method": "get",
        "url": "/projects/{projectID}/suites/{testSuiteID}".format(
            projectID=project_id,
            testSuiteID=test_suite_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TestSuite]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TestSuite.from_dict(response.json())

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
) -> Response[Union[Any, TestSuite]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    test_suite_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, TestSuite]]:
    """Returns a specific test suite's latest revision.

    Args:
        project_id (str):
        test_suite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TestSuite]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_suite_id=test_suite_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    test_suite_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, TestSuite]]:
    """Returns a specific test suite's latest revision.

    Args:
        project_id (str):
        test_suite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TestSuite]
    """

    return sync_detailed(
        project_id=project_id,
        test_suite_id=test_suite_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    test_suite_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, TestSuite]]:
    """Returns a specific test suite's latest revision.

    Args:
        project_id (str):
        test_suite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TestSuite]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_suite_id=test_suite_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    test_suite_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, TestSuite]]:
    """Returns a specific test suite's latest revision.

    Args:
        project_id (str):
        test_suite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TestSuite]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            test_suite_id=test_suite_id,
            client=client,
        )
    ).parsed
