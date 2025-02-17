class CommissionEmployee:

    def __init__(self, first_name: str, last_name: str, social_security_number: str, gross_sales: float, commission_rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.social_security_number = social_security_number
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    def earnings(self):
        return self.gross_sales * self.commission_rate

    def display_employee_details(self):
        space = " "
        print("Name: " + self.first_name + space + self.last_name)
        print("Last Name:" , self.last_name)
        print("Gross Sales" , self.gross_sales ,"\n Commission Rate:", self.commission_rate , "\nEarnings:" ,
              self.earnings() , "\n")


class BasePlusCommission(CommissionEmployee):

    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, social_security_number, gross_sales, commission_rate)
        self.base_salary = base_salary

    def earnings(self):
        return self.base_salary + (self.gross_sales * self.commission_rate)

    def set_base_salary(self, new_salary):
        if new_salary >= 0:
            self.base_salary = new_salary
        else:
            raise ValueError("The value should not be less than zero")


commission_employee1 = CommissionEmployee("Jermaine", "Lancaster", "035", 4500, 0.5)
base_plus_commission_employee = BasePlusCommission("Ulesses", "Parker", "9453", 3660, 0.4, 4500)
print("Salary for" , commission_employee1.first_name , ":" , commission_employee1.earnings())
print("Salary for" , base_plus_commission_employee.first_name , ":" , base_plus_commission_employee.earnings())
base_plus_commission_employee.set_base_salary(6000)
print("Salary for" , base_plus_commission_employee.first_name , ":" , base_plus_commission_employee.earnings())