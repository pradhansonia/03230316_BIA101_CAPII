class PersonalIncomeTaxCalculator:
    def __init__(self, name, age, marital_status, has_children, children_school_going, gross_salary, bonus_rate, is_contract_employee=False, organization_type='Private'):
        self.name = name
        self.age = age
        self.marital_status = marital_status
        self.has_children = has_children
        self.children_school_going = children_school_going
        self.gross_salary = gross_salary
        self.bonus_rate = bonus_rate
        self.is_contract_employee = is_contract_employee
        self.organization_type = organization_type

    def calculate_tax(self):
        try:
            if self.age < 18:
                print("Employee is below 18 years old. No income tax payable.")
                return 0
            total_income = self.gross_salary * (1 + self.bonus_rate / 100)  # Calculate total income including bonus
            if total_income < self.get_taxable_income_threshold():
                return 0  # No tax if income is below threshold
            taxable_income = total_income - self.calculate_deductions()
            print("Taxable Income after deductions:", taxable_income)
            tax = self.calculate_tax_amount(taxable_income)
            return tax
        except Exception as e:
            print("Error in calculating tax:", str(e))

    def calculate_deductions(self):
        pf_gis_deduction = self.gross_salary * 0.05  # Assuming PF and GIS deductions are 5% of income
        general_deductions = min(self.gross_salary * 0.05, 350000)  # General deductions up to Nu. 350,000
        total_deductions = pf_gis_deduction + general_deductions
        if self.has_children:
            total_deductions += 350000  # Additional deduction for children
            if self.children_school_going:
                total_deductions += min(self.children_school_going * 350000, 350000)  # Education allowance for school-going children, max 350000
        print("Total deductions:", total_deductions)
        return total_deductions

    def calculate_tax_amount(self, taxable_income):
        # Tax slabs and rates
        tax_slabs = [(300000, 0.1), (600000, 0.15), (900000, 0.2), (1200000, 0.25)]
        tax_amount = 0
        for slab, rate in tax_slabs:
            if taxable_income > slab:
                tax_amount += slab * rate
                taxable_income -= slab
            else:
                tax_amount += taxable_income * rate
                break
        return tax_amount

    def get_taxable_income_threshold(self):
        if self.organization_type == 'Government' and not self.is_contract_employee:
            return 300000  # Minimum taxable income threshold for Government employees
        else:
            return 200000  # Minimum taxable income threshold for Private/Corporate employees

if __name__ == "__main__":
    name = input("Enter employee's name: ")
    age = int(input("Enter employee's age: "))
    if age < 18:
        print("Employee is below 18 years old. No need to pay tax.")
    else:
        marital_status = input("Enter employee's marital status (married/single): ").lower()
        if marital_status == 'single':
            has_children = False
            children_school_going = 0
        else:
            has_children = input("Does the employee have children? (yes/no): ").lower() == 'yes'
            children_school_going = 0
            if has_children:
                children_school_going = int(input("How many children go to school? (Enter 0 if none): "))
        
        gross_salary = float(input("Enter employee's gross salary: "))
        bonus_rate = float(input("Enter employee's bonus rate (% of gross salary): "))
        is_contract_employee = input("Is the employee a contract employee? (yes/no): ").lower() == 'yes'
        organization_type = input("Enter the employee's organization type (Government/Private/Corporate): ")
        
        tax_calculator = PersonalIncomeTaxCalculator(name, age, marital_status, has_children, children_school_going, gross_salary, bonus_rate, is_contract_employee, organization_type)
        tax = tax_calculator.calculate_tax()
        print("Total tax payable:", tax)#this is the fianal tax that an employee need to pay
