from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal

class Course(BaseModel):
    name: Annotated[str, Field(...,description="The name of the course", example="Introduction to Python")]
    teacher: Annotated[str, Field(...,description="The teacher of the course", example="Jane Smith")]
    duration: Annotated[int, Field(...,gt=0,description="The duration of the course in weeks", example=12)]  # duration in weeks