class CommissionEmployee:
    def __init__(self, first_name:str , last_name:str , social_security_number:str , gross_sales: float, commission_rate: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__social_security_number = social_security_number
        self.__gross_sales = gross_sales
        self.__commission_rate = commission_rate

    def get_first_name(self) -> str :
        return self.__first_name

    def set_first_name(self, first_name):
        if not isinstance(first_name, str):
            raise ValueError("Must be a string value")
        self.__first_name = first_name

    def get_last_name(self)-> str:
        return self.__last_name


    def set_last_name(self, last_name):
        if not isinstance(last_name, str):
            raise ValueError("Must be a string value")
        self.__last_name = last_name

    @property
    def get_social_security_number(self) -> str:
        return self.__social_security_number


    def set_social_security_number(self, social_security_number):
        if isinstance(social_security_number, str):
            raise ValueError("Must be a string value")
        self.__social_security_number = social_security_number

    def get_gross_sales(self) -> float:
        return self.__gross_sales
    def set_gross_sales(self, gross_sales) :
        if isinstance(gross_sales, float) or gross_sales < 0:
            raise ValueError("Value must be numeric (Preferably a float)")
        self.__gross_sales = gross_sales

    def get_commission_rate(self) -> float:
        return self.__commission_rate

    def set_commission_rate(self, commission_rate):
        if isinstance(commission_rate, float) or (commission_rate < 1 | commission_rate > 0):
            self.__commission_rate = commission_rate
        else:
            raise ValueError("Value must be numeric (Preferably a float between 0 and 1)")

    def earnings(self) -> float:
        grossSales = self.get_gross_sales()
        commissionRate = self.get_commission_rate()
        return grossSales*commissionRate


employee1 = CommissionEmployee("John", "MacCarthy", "0011" ,4000, 0.3 )
employee1.set_gross_sales(4500)
employee1.set_commission_rate(0.4)
space = " "
print(f"{employee1.get_first_name()+ space + employee1.get_last_name()} earns: {employee1.earnings()}")
