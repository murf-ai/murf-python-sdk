# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...types.locale_response import LocaleResponse
from ...core.unchecked_base_model import construct_type
from ...errors.bad_request_error import BadRequestError
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.service_unavailable_error import ServiceUnavailableError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.source_locale_response import SourceLocaleResponse
from ...core.client_wrapper import AsyncClientWrapper


class LanguagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_destination_languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LocaleResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LocaleResponse]
            Ok

        Examples
        --------
        from murf import Murf

        client = Murf(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.languages.list_destination_languages()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/murfdub/list-destination-languages",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[LocaleResponse],
                    construct_type(
                        type_=typing.List[LocaleResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_source_languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SourceLocaleResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceLocaleResponse]
            Ok

        Examples
        --------
        from murf import Murf

        client = Murf(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.languages.list_source_languages()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/murfdub/list-source-languages",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[SourceLocaleResponse],
                    construct_type(
                        type_=typing.List[SourceLocaleResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLanguagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_destination_languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LocaleResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LocaleResponse]
            Ok

        Examples
        --------
        import asyncio

        from murf import AsyncMurf

        client = AsyncMurf(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dubbing.languages.list_destination_languages()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/murfdub/list-destination-languages",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[LocaleResponse],
                    construct_type(
                        type_=typing.List[LocaleResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_source_languages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SourceLocaleResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SourceLocaleResponse]
            Ok

        Examples
        --------
        import asyncio

        from murf import AsyncMurf

        client = AsyncMurf(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dubbing.languages.list_source_languages()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/murfdub/list-source-languages",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[SourceLocaleResponse],
                    construct_type(
                        type_=typing.List[SourceLocaleResponse],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
