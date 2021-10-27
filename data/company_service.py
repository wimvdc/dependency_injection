class CompanyService:
    def get_company_by_id(self, company_id: str) -> dict:
        # this should contain the real logic
        # eg. a call to an other microservice
        raise NotImplementedError


class StubCompanyService:
    def get_company_by_id(self, company_id: str) -> dict:
        return {"id": company_id, "name": "CraftCode"}
