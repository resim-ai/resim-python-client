from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch import Batch
from ...models.test_suite_batch_input import TestSuiteBatchInput
from ...types import Response


def _get_kwargs(
    project_id: str,
    test_suite_id: str,
    *,
    json_body: TestSuiteBatchInput,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/projects/{projectID}/suites/{testSuiteID}/batches".format(
            projectID=project_id,
            testSuiteID=test_suite_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Batch]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Batch.from_dict(response.json())

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
) -> Response[Union[Any, Batch]]:
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
    json_body: TestSuiteBatchInput,
) -> Response[Union[Any, Batch]]:
    """Creates a batch for that test suite

    Args:
        project_id (str):
        test_suite_id (str):
        json_body (TestSuiteBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Batch]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_suite_id=test_suite_id,
        json_body=json_body,
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
    json_body: TestSuiteBatchInput,
) -> Optional[Union[Any, Batch]]:
    """Creates a batch for that test suite

    Args:
        project_id (str):
        test_suite_id (str):
        json_body (TestSuiteBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Batch]
    """

    return sync_detailed(
        project_id=project_id,
        test_suite_id=test_suite_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    test_suite_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TestSuiteBatchInput,
) -> Response[Union[Any, Batch]]:
    """Creates a batch for that test suite

    Args:
        project_id (str):
        test_suite_id (str):
        json_body (TestSuiteBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Batch]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_suite_id=test_suite_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    test_suite_id: str,
    *,
    client: AuthenticatedClient,
    json_body: TestSuiteBatchInput,
) -> Optional[Union[Any, Batch]]:
    """Creates a batch for that test suite

    Args:
        project_id (str):
        test_suite_id (str):
        json_body (TestSuiteBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Batch]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            test_suite_id=test_suite_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
