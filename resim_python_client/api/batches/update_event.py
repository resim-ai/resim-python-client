from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event import Event
from ...models.update_event_input import UpdateEventInput
from ...types import Response


def _get_kwargs(
    project_id: str,
    batch_id: str,
    job_id: str,
    event_id: str,
    *,
    json_body: UpdateEventInput,
) -> Dict[str, Any]:

    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/projects/{projectID}/batches/{batchID}/jobs/{jobID}/events/{eventID}".format(
            projectID=project_id,
            batchID=batch_id,
            jobID=job_id,
            eventID=event_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Event]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Event.from_dict(response.json())

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
) -> Response[Union[Any, Event]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    batch_id: str,
    job_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateEventInput,
) -> Response[Union[Any, Event]]:
    """Updates the event.

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        event_id (str):
        json_body (UpdateEventInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Event]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        job_id=job_id,
        event_id=event_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    batch_id: str,
    job_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateEventInput,
) -> Optional[Union[Any, Event]]:
    """Updates the event.

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        event_id (str):
        json_body (UpdateEventInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Event]
    """

    return sync_detailed(
        project_id=project_id,
        batch_id=batch_id,
        job_id=job_id,
        event_id=event_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    batch_id: str,
    job_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateEventInput,
) -> Response[Union[Any, Event]]:
    """Updates the event.

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        event_id (str):
        json_body (UpdateEventInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Event]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        batch_id=batch_id,
        job_id=job_id,
        event_id=event_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    batch_id: str,
    job_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateEventInput,
) -> Optional[Union[Any, Event]]:
    """Updates the event.

    Args:
        project_id (str):
        batch_id (str):
        job_id (str):
        event_id (str):
        json_body (UpdateEventInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Event]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            batch_id=batch_id,
            job_id=job_id,
            event_id=event_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
