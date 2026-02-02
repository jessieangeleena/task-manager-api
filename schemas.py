from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(TaskCreate):
    id: int
    completed: bool

    class Config:
        orm_mode = True
