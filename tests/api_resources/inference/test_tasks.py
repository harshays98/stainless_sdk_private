# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inferencing import Inferencing, AsyncInferencing
from tests.utils import assert_matches_type
from inferencing.types.inference import (
    TaskListResponse,
    TaskCreateResponse,
    TaskRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Inferencing) -> None:
        task = client.inference.tasks.create(
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Inferencing) -> None:
        task = client.inference.tasks.create(
            k_customer_id="K-Customer-ID",
            argument="argument",
            checkpoint="checkpoint",
            environ="environ",
            max_batch_size=0,
            max_replicas=0,
            min_replicas=0,
            model="model",
            namespace="namespace",
            ngpu=0,
            path="path",
            priority=0,
            s3_access_key="s3_access_key",
            s3_endpoint="s3_endpoint",
            s3_region="s3_region",
            s3_secret="s3_secret",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Inferencing) -> None:
        response = client.inference.tasks.with_raw_response.create(
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Inferencing) -> None:
        with client.inference.tasks.with_streaming_response.create(
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Inferencing) -> None:
        task = client.inference.tasks.retrieve(
            id="id",
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Inferencing) -> None:
        response = client.inference.tasks.with_raw_response.retrieve(
            id="id",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Inferencing) -> None:
        with client.inference.tasks.with_streaming_response.retrieve(
            id="id",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Inferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inference.tasks.with_raw_response.retrieve(
                id="",
                k_customer_id="K-Customer-ID",
            )

    @parametrize
    def test_method_list(self, client: Inferencing) -> None:
        task = client.inference.tasks.list(
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Inferencing) -> None:
        task = client.inference.tasks.list(
            k_customer_id="K-Customer-ID",
            limit=0,
            offset=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Inferencing) -> None:
        response = client.inference.tasks.with_raw_response.list(
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Inferencing) -> None:
        with client.inference.tasks.with_streaming_response.list(
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Inferencing) -> None:
        task = client.inference.tasks.cancel(
            id="id",
            k_customer_id="K-Customer-ID",
        )
        assert task is None

    @parametrize
    def test_raw_response_cancel(self, client: Inferencing) -> None:
        response = client.inference.tasks.with_raw_response.cancel(
            id="id",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert task is None

    @parametrize
    def test_streaming_response_cancel(self, client: Inferencing) -> None:
        with client.inference.tasks.with_streaming_response.cancel(
            id="id",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Inferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.inference.tasks.with_raw_response.cancel(
                id="",
                k_customer_id="K-Customer-ID",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncInferencing) -> None:
        task = await async_client.inference.tasks.create(
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInferencing) -> None:
        task = await async_client.inference.tasks.create(
            k_customer_id="K-Customer-ID",
            argument="argument",
            checkpoint="checkpoint",
            environ="environ",
            max_batch_size=0,
            max_replicas=0,
            min_replicas=0,
            model="model",
            namespace="namespace",
            ngpu=0,
            path="path",
            priority=0,
            s3_access_key="s3_access_key",
            s3_endpoint="s3_endpoint",
            s3_region="s3_region",
            s3_secret="s3_secret",
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.tasks.with_raw_response.create(
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.tasks.with_streaming_response.create(
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInferencing) -> None:
        task = await async_client.inference.tasks.retrieve(
            id="id",
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.tasks.with_raw_response.retrieve(
            id="id",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.tasks.with_streaming_response.retrieve(
            id="id",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inference.tasks.with_raw_response.retrieve(
                id="",
                k_customer_id="K-Customer-ID",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncInferencing) -> None:
        task = await async_client.inference.tasks.list(
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInferencing) -> None:
        task = await async_client.inference.tasks.list(
            k_customer_id="K-Customer-ID",
            limit=0,
            offset=0,
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.tasks.with_raw_response.list(
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.tasks.with_streaming_response.list(
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncInferencing) -> None:
        task = await async_client.inference.tasks.cancel(
            id="id",
            k_customer_id="K-Customer-ID",
        )
        assert task is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.tasks.with_raw_response.cancel(
            id="id",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert task is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.tasks.with_streaming_response.cancel(
            id="id",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert task is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncInferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.inference.tasks.with_raw_response.cancel(
                id="",
                k_customer_id="K-Customer-ID",
            )
