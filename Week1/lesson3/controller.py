import model

# Getters
def get_salary():
    return model.salary

def get_name():
    return model.name

def get_skills():
    return model.skills

#sumar boonos#calcular y 2 restar impuestos
def sum_bonos():
    bonos = model.get_bonos()
    return sum([bonos.b1, bonos.b2])

def compute_taxes():
    salary = get_salary()
    taxes = model.get_taxes()
    all_taxes = [taxes.tax1, taxes.tax2, taxes.tax3]
    single_taxes = [salary*x for x in all_taxes]
    return sum(single_taxes)


# Setters
def set_skills(new_skill):
    model.skills+=new_skill