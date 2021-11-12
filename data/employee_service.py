class EmployeeService:
    def get_employees_by_company_id(self, company_id: str) -> dict:
        # this should contain the real logic
        # eg. a call to an other microservice
        return {
            "employees": [
                {"id": 1, "name": "Mock Doe 1", "company_id": company_id},
                {"id": 2, "name": "Mock Doe 2", "company_id": company_id},
            ]
        }
