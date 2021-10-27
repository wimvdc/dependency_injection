class EmployeeService:
    def get_employees_by_company_id(self, company_id: str) -> dict:
        # this should contain the real logic
        # eg. a call to an other microservice
        raise NotImplementedError


class StubEmployeeService:
    def get_employees_by_company_id(self, company_id: str) -> dict:
        return {
            "employees": [
                {"id": 1, "name": "Jane Doe", "company_id": company_id},
                {"id": 2, "name": "John Doe", "company_id": company_id},
            ]
        }
