from fastapi import HTTPException, status

IncorrectEntryException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Incorrect entry.",
)
