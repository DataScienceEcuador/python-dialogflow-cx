# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple

from google.cloud.dialogflowcx_v3.types import security_settings


class ListSecuritySettingsPager:
    """A pager for iterating through ``list_security_settings`` requests.

    This class thinly wraps an initial
    :class:`~.security_settings.ListSecuritySettingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``security_settings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSecuritySettings`` requests and continue to iterate
    through the ``security_settings`` field on the
    corresponding responses.

    All the usual :class:`~.security_settings.ListSecuritySettingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., security_settings.ListSecuritySettingsResponse],
        request: security_settings.ListSecuritySettingsRequest,
        response: security_settings.ListSecuritySettingsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.security_settings.ListSecuritySettingsRequest`):
                The initial request object.
            response (:class:`~.security_settings.ListSecuritySettingsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = security_settings.ListSecuritySettingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[security_settings.ListSecuritySettingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[security_settings.SecuritySettings]:
        for page in self.pages:
            yield from page.security_settings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSecuritySettingsAsyncPager:
    """A pager for iterating through ``list_security_settings`` requests.

    This class thinly wraps an initial
    :class:`~.security_settings.ListSecuritySettingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``security_settings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSecuritySettings`` requests and continue to iterate
    through the ``security_settings`` field on the
    corresponding responses.

    All the usual :class:`~.security_settings.ListSecuritySettingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[security_settings.ListSecuritySettingsResponse]
        ],
        request: security_settings.ListSecuritySettingsRequest,
        response: security_settings.ListSecuritySettingsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.security_settings.ListSecuritySettingsRequest`):
                The initial request object.
            response (:class:`~.security_settings.ListSecuritySettingsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = security_settings.ListSecuritySettingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterable[security_settings.ListSecuritySettingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[security_settings.SecuritySettings]:
        async def async_generator():
            async for page in self.pages:
                for response in page.security_settings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
