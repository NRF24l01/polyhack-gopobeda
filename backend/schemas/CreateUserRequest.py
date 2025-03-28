from pydantic import BaseModel, Field, field_validator, EmailStr


class CreateUserRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(..., min_length=8, max_length=120)
    password: str = Field(..., min_length=8, max_length=60)


    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not (8 <= len(value) <= 60 and any(c.isupper() for c in value) and any(c.islower() for c in value) and any(
                c.isdigit() for c in value)):
            raise ValueError('Password incorrect')

        return value
