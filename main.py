from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr

app = FastAPI(
    title="Patient Records API",
    description="A beginner-friendly REST API for managing fictional patient records.",
    version="1.0.0",
)

# In-memory sample data. Records reset whenever the application restarts.
patients = [
    {"id": 1, "name": "Ali", "age": 25},
    {"id": 2, "name": "Sara", "age": 30},
]


class PatientCreate(BaseModel):
    """Validate data received when creating a patient."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: StrictStr = Field(min_length=1, max_length=100)
    age: StrictInt = Field(gt=0, le=120)


class PatientResponse(BaseModel):
    """Shape of a patient record returned by the API."""
    id: int
    name: str
    age: int


@app.get("/", tags=["General"])
def home():
    """Return a welcome message."""
    return {"message": "My First FastAPI Application"}


@app.get("/patients", response_model=list[PatientResponse], tags=["Patients"])
def get_patients():
    """Return all patient records."""
    return patients


@app.post(
    "/patients",
    response_model=PatientResponse,
    status_code=201,
    tags=["Patients"],
)
def add_patient(patient: PatientCreate):
    """Validate and add a new fictional patient record."""
    next_id = max((record["id"] for record in patients), default=0) + 1

    new_patient = {
        "id": next_id,
        "name": patient.name,
        "age": patient.age,
    }
    patients.append(new_patient)
    return new_patient
