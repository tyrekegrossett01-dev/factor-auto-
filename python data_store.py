# data_store.py
# Shared data for the Factory Automation Management System.
 
# Valid machine statuses
MACHINE_STATUSES = (
    'AVAILABLE',
    'IN PRODUCTION',
    'MAINTENANCE',
    'OUT OF SERVICE'
)

# Valid employee roles from the official project brief
EMPLOYEE_ROLES = (
    'Machine Operator',
    'Maintenance Technician',
    'Electrical Technician',
    'Automation Technician',
    'Production Supervisor'
)

# Valid work shifts
SHIFTS = ('Morning', 'Evening', 'Night')

# Valid maintenance types
MAINTENANCE_TYPES = (
    'Preventitive',
    'Corrective',
    'ELectrical',
    'Mechanical',
    'Software/Control-System'
)

# Empty dictionaries to store factory records
machines = {}
employees = {}
orders = {}
maintenance = {}

# Four products supplied in thr official project brief
products = {
    'P001': {
        'name': 'aLED Lighting Unit',
        'category': 'Electrical',
        'time_per_unit': 4,
        'material_cost': 1500,
        'selling_price': 2800,
    },
    'P002': {
        'name': 'Smart Power Outlet',
        'category': 'Electrical',
        'time_per_unit': 6,
        'material_cost': 2200,
        'selling_price': 4000,
    },
    'P003': {
        'name': 'Electronic Control Module',
        'category': 'Electronics',
        'time_per_unit': 10,
        'material_cost': 3500,
        'selling_price': 6500
    },
    'P004': {
        'name': 'Sensor Module',
        'category': 'Electronics',
        'time_per_unit': 5,
        'material_cost': 1800,
        'selling_price': 3200
    }
}