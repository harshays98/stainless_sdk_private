# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inferencing import Inferencing, AsyncInferencing
from tests.utils import assert_matches_type
from inferencing.types.inference import CheckpointDelResponse, CheckpointListResponse, CheckpointRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Inferencing) -> None:
        checkpoint = client.inference.checkpoints.retrieve(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(CheckpointRetrieveResponse, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Inferencing) -> None:
        response = client.inference.checkpoints.with_raw_response.retrieve(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(CheckpointRetrieveResponse, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Inferencing) -> None:
        with client.inference.checkpoints.with_streaming_response.retrieve(
            filename="filename",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(CheckpointRetrieveResponse, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Inferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.inference.checkpoints.with_raw_response.retrieve(
                filename="",
                k_customer_id="K-Customer-ID",
            )

    @parametrize
    def test_method_list(self, client: Inferencing) -> None:
        checkpoint = client.inference.checkpoints.list(
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(CheckpointListResponse, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Inferencing) -> None:
        response = client.inference.checkpoints.with_raw_response.list(
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(CheckpointListResponse, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Inferencing) -> None:
        with client.inference.checkpoints.with_streaming_response.list(
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(CheckpointListResponse, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Inferencing) -> None:
        checkpoint = client.inference.checkpoints.delete(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(CheckpointDelResponse, checkpoint, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Inferencing) -> None:
        response = client.inference.checkpoints.with_raw_response.delete(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = response.parse()
        assert_matches_type(CheckpointDelResponse, checkpoint, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Inferencing) -> None:
        with client.inference.checkpoints.with_streaming_response.delete(
            filename="filename",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = response.parse()
            assert_matches_type(CheckpointDelResponse, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Inferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.inference.checkpoints.with_raw_response.delete(
                filename="",
                k_customer_id="K-Customer-ID",
            )


class TestAsyncCheckpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInferencing) -> None:
        checkpoint = await async_client.inference.checkpoints.retrieve(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(CheckpointRetrieveResponse, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.checkpoints.with_raw_response.retrieve(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(CheckpointRetrieveResponse, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.checkpoints.with_streaming_response.retrieve(
            filename="filename",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(CheckpointRetrieveResponse, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.inference.checkpoints.with_raw_response.retrieve(
                filename="",
                k_customer_id="K-Customer-ID",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncInferencing) -> None:
        checkpoint = await async_client.inference.checkpoints.list(
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(CheckpointListResponse, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.checkpoints.with_raw_response.list(
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(CheckpointListResponse, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.checkpoints.with_streaming_response.list(
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(CheckpointListResponse, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncInferencing) -> None:
        checkpoint = await async_client.inference.checkpoints.delete(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )
        assert_matches_type(CheckpointDelResponse, checkpoint, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInferencing) -> None:
        response = await async_client.inference.checkpoints.with_raw_response.delete(
            filename="filename",
            k_customer_id="K-Customer-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkpoint = await response.parse()
        assert_matches_type(CheckpointDelResponse, checkpoint, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInferencing) -> None:
        async with async_client.inference.checkpoints.with_streaming_response.delete(
            filename="filename",
            k_customer_id="K-Customer-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkpoint = await response.parse()
            assert_matches_type(CheckpointDelResponse, checkpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInferencing) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.inference.checkpoints.with_raw_response.delete(
                filename="",
                k_customer_id="K-Customer-ID",
            )
