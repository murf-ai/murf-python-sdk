from .base_client import BaseClient, AsyncBaseClient
from .environment import MurfEnvironment
import typing
import os
import httpx
from .version import __version__

class Murf(BaseClient):
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------

    environment : MurfEnvironment
        The environment to use for requests from the client. from .environment import MurfEnvironment



        Defaults to MurfEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from murf import Murf

    client = Murf(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        environment: MurfEnvironment = MurfEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("MURF_API_KEY"),
        timeout: typing.Optional[float] = 60,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        default_params = {'origin': f'python_sdk_{__version__}'}
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        httpx_client=httpx_client if httpx_client is not None else httpx.Client(params=default_params, timeout=_defaulted_timeout, follow_redirects=follow_redirects) if follow_redirects is not None else httpx.Client(params=default_params, timeout=_defaulted_timeout)

        super().__init__(
            environment=environment,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client
        )
        self.dubbing = None # type: ignore


class AsyncMurf(AsyncBaseClient):
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------

    environment : MurfEnvironment
        The environment to use for requests from the client. from .environment import MurfEnvironment



        Defaults to MurfEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from murf import AsyncMurf

    client = AsyncMurf(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        environment: MurfEnvironment = MurfEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("MURF_API_KEY"),
        timeout: typing.Optional[float] = 60,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        default_params = {'origin': f'python_sdk_{__version__}'}
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        httpx_client=httpx_client if httpx_client is not None else httpx.AsyncClient(params=default_params, timeout=_defaulted_timeout, follow_redirects=follow_redirects) if follow_redirects is not None else httpx.AsyncClient(params=default_params, timeout=_defaulted_timeout)
        
        super().__init__(
            environment=environment,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client
        )
        self.dubbing = None # type: ignore