# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.inference import task_list_params, task_create_params
from ...types.inference.task_list_response import TaskListResponse
from ...types.inference.task_create_response import TaskCreateResponse
from ...types.inference.task_retrieve_response import TaskRetrieveResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        k_customer_id: str,
        argument: str | NotGiven = NOT_GIVEN,
        checkpoint: str | NotGiven = NOT_GIVEN,
        environ: str | NotGiven = NOT_GIVEN,
        max_batch_size: int | NotGiven = NOT_GIVEN,
        max_replicas: int | NotGiven = NOT_GIVEN,
        min_replicas: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        namespace: str | NotGiven = NOT_GIVEN,
        ngpu: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        s3_access_key: str | NotGiven = NOT_GIVEN,
        s3_endpoint: str | NotGiven = NOT_GIVEN,
        s3_region: str | NotGiven = NOT_GIVEN,
        s3_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create inference task

        Args:
          argument: additional argument to parse to inference engine

          checkpoint: Checkpoint name.

          environ: environment variable to parse to inference engine

          max_batch_size: max batch size

          max_replicas: Max number of replicas

          min_replicas: Min number of replicas

          model: Model name.

          namespace: Task Name.

          ngpu: Number of GPU to be used by the inference task.

          path: Checkpoint path.

          priority: Task priority.

          s3_access_key: S3 access key

          s3_endpoint: S3 endpoint

          s3_region: S3 region

          s3_secret: S3 secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return self._post(
            "/api/v1/inference/tasks",
            body=maybe_transform(
                {
                    "argument": argument,
                    "checkpoint": checkpoint,
                    "environ": environ,
                    "max_batch_size": max_batch_size,
                    "max_replicas": max_replicas,
                    "min_replicas": min_replicas,
                    "model": model,
                    "namespace": namespace,
                    "ngpu": ngpu,
                    "path": path,
                    "priority": priority,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        k_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Get inference task information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return self._get(
            f"/api/v1/inference/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    def list(
        self,
        *,
        k_customer_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        List inference tasks

        Args:
          limit: Limit the max number of item to be return.

          offset: Offset index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return self._get(
            "/api/v1/inference/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        k_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancel inference task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"K-Customer-ID": k_customer_id})
        return self._get(
            f"/api/v1/inference/tasks/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        k_customer_id: str,
        argument: str | NotGiven = NOT_GIVEN,
        checkpoint: str | NotGiven = NOT_GIVEN,
        environ: str | NotGiven = NOT_GIVEN,
        max_batch_size: int | NotGiven = NOT_GIVEN,
        max_replicas: int | NotGiven = NOT_GIVEN,
        min_replicas: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        namespace: str | NotGiven = NOT_GIVEN,
        ngpu: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        s3_access_key: str | NotGiven = NOT_GIVEN,
        s3_endpoint: str | NotGiven = NOT_GIVEN,
        s3_region: str | NotGiven = NOT_GIVEN,
        s3_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create inference task

        Args:
          argument: additional argument to parse to inference engine

          checkpoint: Checkpoint name.

          environ: environment variable to parse to inference engine

          max_batch_size: max batch size

          max_replicas: Max number of replicas

          min_replicas: Min number of replicas

          model: Model name.

          namespace: Task Name.

          ngpu: Number of GPU to be used by the inference task.

          path: Checkpoint path.

          priority: Task priority.

          s3_access_key: S3 access key

          s3_endpoint: S3 endpoint

          s3_region: S3 region

          s3_secret: S3 secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return await self._post(
            "/api/v1/inference/tasks",
            body=await async_maybe_transform(
                {
                    "argument": argument,
                    "checkpoint": checkpoint,
                    "environ": environ,
                    "max_batch_size": max_batch_size,
                    "max_replicas": max_replicas,
                    "min_replicas": min_replicas,
                    "model": model,
                    "namespace": namespace,
                    "ngpu": ngpu,
                    "path": path,
                    "priority": priority,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        k_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Get inference task information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return await self._get(
            f"/api/v1/inference/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    async def list(
        self,
        *,
        k_customer_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        List inference tasks

        Args:
          limit: Limit the max number of item to be return.

          offset: Offset index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return await self._get(
            "/api/v1/inference/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        k_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancel inference task.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"K-Customer-ID": k_customer_id})
        return await self._get(
            f"/api/v1/inference/tasks/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.cancel = to_raw_response_wrapper(
            tasks.cancel,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            tasks.cancel,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.cancel = to_streamed_response_wrapper(
            tasks.cancel,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            tasks.cancel,
        )
