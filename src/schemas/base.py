from typing import Annotated

from annotated_types import MinLen
from pydantic import AliasGenerator
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import SecretStr
from pydantic.alias_generators import to_pascal
from pydantic.alias_generators import to_snake

PasswordStr = Annotated[SecretStr, MinLen(8)]
PhoneNumberStr = Annotated[str, MinLen(10)]


class PascalToSnakeSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_pascal,
            serialization_alias=to_snake,
        )
    )
