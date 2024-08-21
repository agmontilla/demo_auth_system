from pydantic import AliasGenerator
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_pascal
from pydantic.alias_generators import to_snake


class PascalToSnakeSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_pascal,
            serialization_alias=to_snake,
        )
    )
