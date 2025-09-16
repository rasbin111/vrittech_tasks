from fastapi import APIRouter, HTTPException
from .schemas import EmailRequest
from utils.email_check import check_mx_records, check_smtp, validate_email

router = APIRouter(
    prefix="/users",
    responses={
        404: {
            "description": "Not found"
        }
    }
)


@router.post("/verify-email")
async def verify_email(request: EmailRequest):
    """ verify single email """
    email = request.email.strip()
    domain = email.split("@")[1]
    is_syntatically_valid = validate_email(email)
    if is_syntatically_valid:
        pass
    else:
        raise HTTPException(status_code=400, detail="Invalid Email")
    mx_records = check_mx_records(domain)
    if not mx_records:
        raise HTTPException(status_code=400, detail="Domain has no MX records")
    is_valid = check_smtp(email, mx_records)
    
    return {"email": email, "valid": is_valid}