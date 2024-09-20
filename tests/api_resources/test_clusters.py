# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inferencing import Inferencing, AsyncInferencing
from tests.utils import assert_matches_type
from inferencing.types import ClusterListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Inferencing) -> None:
        cluster = client.clusters.list()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Inferencing) -> None:
        response = client.clusters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Inferencing) -> None:
        with client.clusters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(ClusterListResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncInferencing) -> None:
        cluster = await async_client.clusters.list()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInferencing) -> None:
        response = await async_client.clusters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInferencing) -> None:
        async with async_client.clusters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(ClusterListResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True
