from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal

class Teacher(BaseModel):
    name: Annotated[str, Field(...,description="The name of the teacher", example="Jane Smith")]
    age: Annotated[int, Field(...,gt = 0,lt = 120,description="The age of the teacher", example=35)]
    subject: Annotated[str, Field(...,description="The subject the teacher teaches", example="Mathematics")]
    experience: Annotated[int, Field(...,ge=0,description="The years of experience the teacher has", example=10)]  # years of experience