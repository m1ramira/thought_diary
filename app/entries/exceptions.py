from fastapi import HTTPException, status

IncorrectEntryException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Incorrect entry.",
)

EntryIsNotExistException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Entry is not exist.",
)

UpdatingEntryErrorException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="An error occurs when updating entry.",
)
