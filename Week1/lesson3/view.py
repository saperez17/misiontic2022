import controller as  con

def run():
    print(con.get_salary())
    print(con.get_skills())
    con.set_skills(' Python')
    print(con.get_skills())
    
    salary = con.get_salary()
    bonous = con.sum_bonos()
    taxes = con.compute_taxes()
    # view bonus
    print(bonous)
    #view taxes
    print(taxes)
    #salary + bonous - taxes 
    print('comptued salary:', salary+bonous-taxes)

if __name__ == '__main__':
    run()