import json
from dependency_injector import containers, providers

from data.company_service import (
    CompanyService,
    StubCompanyService,
)  # keep all Stub imports as well!
from data.employee_service import (
    EmployeeService,
    StubEmployeeService,
)  # keep all Stub imports as well!


class Container(containers.DeclarativeContainer):

    company_service = providers.Singleton(CompanyService)
    employee_service = providers.Singleton(EmployeeService)


@containers.override(Container)
class OverridingContainer(containers.DeclarativeContainer):
    try:
        f = open("./config/injection.json")
        injections = json.load(f)

        if injections.get("company-service", None) is not None:
            company_service = providers.Singleton(
                globals().get(injections["company-service"])
            )
        if injections.get("employee-service", None) is not None:
            employee_service = providers.Singleton(
                globals().get(injections["employee-service"])
            )

        print("Dependency injection has been overriden!")
    except FileNotFoundError:
        print("No dependency injection override")
