from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length=30)
    department: str = Field(..., regex="^(HR|Engineering|Marketing|Sales)$")
    age: Optional[int] = Field(None, ge=18, le=65)