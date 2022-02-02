from csp import CSP, Constraint


def test_csp_variables_domains():
    variables = ['Western Australia',
                'Northern Territory',
                'South Australia',
                'Queensland',
                'New South Wales',
                'Victoria',
                'Tasmania']
    domains = {}
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
    csp = CSP(variables, domains)
    assert csp.variables == variables
    assert csp.domains == {'Western Australia': ['red', 'green', 'blue'],
                        'Northern Territory': ['red', 'green', 'blue'],
                        'South Australia': ['red', 'green', 'blue'],
                        'Queensland': ['red', 'green', 'blue'],
                        'New South Wales': ['red', 'green', 'blue'],
                        'Victoria': ['red', 'green', 'blue'],
                        'Tasmania': ['red', 'green', 'blue']}

    
class NewConstraint(Constraint):
    def __init__(self, thing1, thing2):
        super().__init__([thing1, thing2])

def test_add_constraint():
    variables = ['One Thing', 'Another thing']
    domains = {}
    for variable in variables:
        domains[variable] = ["Domain1", "Domain2"]
    csp = CSP(variables, domains)

