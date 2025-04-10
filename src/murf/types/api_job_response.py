# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .api_job_response_dubbing_type import ApiJobResponseDubbingType
import pydantic
from .api_job_response_priority import ApiJobResponsePriority
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ApiJobResponse(UniversalBaseModel):
    file_url: typing.Optional[str] = None
    dubbing_type: ApiJobResponseDubbingType = pydantic.Field()
    """
    Dubbing Type
    """

    webhook_url: typing.Optional[str] = None
    file_name: str = pydantic.Field()
    """
    Your Uploaded File Name
    """

    priority: ApiJobResponsePriority = pydantic.Field()
    """
    Priority of the job. Allowed values: LOW, NORMAL, HIGH
    """

    source_locale: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source locale
    """

    job_id: str = pydantic.Field()
    """
    Your Job Id
    """

    target_locales: typing.List[str] = pydantic.Field()
    """
    List of target locales
    """

    warning: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
