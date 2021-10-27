from dependency_injector.providers import Container
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from data.container import Container
from data.company_service import CompanyService
from data.employee_service import EmployeeService

router = APIRouter()


@router.get("/")
async def hello_world():
    return {"message": "Hello World"}


@router.get("/company/{company_id}")
@inject
async def get_company_info(
    company_id: str,
    company_service: CompanyService = Depends(Provide[Container.company_service]),
    employee_service: EmployeeService = Depends(Provide[Container.employee_service]),
):
    company_result = company_service.get_company_by_id(company_id)
    employee_result = employee_service.get_employees_by_company_id(company_id)
    return {"company_info": company_result, "employee_info": employee_result}
