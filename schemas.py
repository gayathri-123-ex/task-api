from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True