class CompanyService:
    def get_company_by_id(self, company_id: str) -> dict:
        # this should contain the real logic
        # eg. a call to an other microservice
        return {"id": company_id, "name": "MockCompany"}
