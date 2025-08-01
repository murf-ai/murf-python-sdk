# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.murf_api_translation_response import MurfApiTranslationResponse
from ..core.unchecked_base_model import construct_type
from ..errors.bad_request_error import BadRequestError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.service_unavailable_error import ServiceUnavailableError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def translate(
        self,
        *,
        target_language: str,
        texts: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MurfApiTranslationResponse:
        """
        Parameters
        ----------
        target_language : str
            The language code for the target translation

        texts : typing.Sequence[str]
            List of texts to translate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MurfApiTranslationResponse
            Ok

        Examples
        --------
        from murf import Murf

        client = Murf(
            api_key="YOUR_API_KEY",
        )
        client.text.translate(
            target_language="es-ES",
            texts=["Hello, world.", "How are you?"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/text/translate",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "targetLanguage": target_language,
                "texts": texts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MurfApiTranslationResponse,
                    construct_type(
                        type_=MurfApiTranslationResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
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


class AsyncTextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def translate(
        self,
        *,
        target_language: str,
        texts: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MurfApiTranslationResponse:
        """
        Parameters
        ----------
        target_language : str
            The language code for the target translation

        texts : typing.Sequence[str]
            List of texts to translate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MurfApiTranslationResponse
            Ok

        Examples
        --------
        import asyncio

        from murf import AsyncMurf

        client = AsyncMurf(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.text.translate(
                target_language="es-ES",
                texts=["Hello, world.", "How are you?"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/text/translate",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "targetLanguage": target_language,
                "texts": texts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MurfApiTranslationResponse,
                    construct_type(
                        type_=MurfApiTranslationResponse,  # type: ignore
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
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
