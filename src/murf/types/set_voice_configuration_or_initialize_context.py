# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .set_voice_configuration_or_initialize_context_voice_config import (
    SetVoiceConfigurationOrInitializeContextVoiceConfig,
)
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SetVoiceConfigurationOrInitializeContext(UncheckedBaseModel):
    voice_config: SetVoiceConfigurationOrInitializeContextVoiceConfig
    context_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional context identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
