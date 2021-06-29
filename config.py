import math

# Describe the scenarios that will be simulated
# scenarios should be described in the following format:
# scenario_name = (routing_topology, sleep_scheduling, aggregation_model)
# where routing_topology may be:
#   'DC'   : Direct Communication
#   'MTE'  : Minimum Transmission Energy
#   'LEACH': LEACH
#   'FCM  ': Fuzzy C-Means
# and sleep_scheduling may be:
#   None                 : No sleep scheduling (mind that None is not a string)
#   'Pso'                : Particle Swarm Optimization
#   'ModifiedPso'        : Modified PSO
#   'GeneticAlgorithm'   : Genetic Algorithm
# and aggregation_model may be:
#   'zero'  : Zero cost
#   'total' : 100% cost
#   'linear': TODO spec
#   'log'   : log cost
# 4th arg is a ud name for the plot

scenario0 = ('DC', None, 'zero', None)
scenario1 = ('LEACH', None, 'zero', None)
scenario2 = ('MTE', None, 'total', None)
scenario3 = ('FCM', None, 'zero', None)
scenario4 = ('FCM', 'ModifiedPso', 'zero', 'FCMMPSO')
scenario5 = ('FCM', 'Pso', 'zero', None)
scenario6 = ('FCM', 'Ecca', 'zero', 'ECCA')
scenario7 = ('FCM', 'GeneticAlgorithm', 'zero', None)
scenario8 = ('AP', None, 'zero', None)
scenario31 = ('FCM', None, 'zero', 'BS at (125,125)')
scenario32 = ('FCM', None, 'zero', 'BS at (65,65)')
scenario33 = ('FCM', None, 'zero', 'BS at (0,0)')
scenario34 = ('FCM', None, 'zero', 'BS at (-65,-65)')

scenarios = [
    scenario0,  # dc
    "plot_nodes(network)",
    "plot_time_of_death(network)",
    scenario2,  # mte
    "plot_nodes(network)",
    "plot_time_of_death(network)",
    scenario3,  # fcm
    "plot_clusters(network)",
    "plot_time_of_death(network)",

    "plot_traces(traces)",
    "save2csv(traces)",
]

# tracer options
TRACE_ENERGY = 1
TRACE_ALIVE_NODES = 1
TRACE_COVERAGE = 1
TRACE_LEARNING_CURVE = 0

# Runtime configuration
MAX_ROUNDS = 15000

# number of transmissions of sensed information to cluster heads or to
# base station (per round)
MAX_TX_PER_ROUND = 1

NOTIFY_POSITION = 0

# network config
# number of nodes
NB_NODES = 200

# node sensor range
COVERAGE_RADIUS = 15  # all dist in m

# node transmission range
TX_RANGE = 30
BSID = -1  # bs identifier

# area definition
AREA_WIDTH = 100.0
AREA_LENGTH = 100.0

# base station position
BS_POS_X = 50.0
BS_POS_Y = 50.0

# packet config
MSG_LENGTH = 4000  # bits
HEADER_LENGTH = 150  # bits

# initial node energy
INITIAL_ENERGY = 0.325  # all energy in joules

# energy config
# energy dissipated at the transceiver electronic (/bit)
E_ELEC = 50e-9  # Joules
# energy dissipated at the data aggregation (/bit)
E_DA = 5e-9  # Joules
# energy dissipated at the power amplifier (supposing a multi-path
# fading channel) (/bit/m^4)
E_MP = 0.0013e-12
# energy dissipated at the power amplifier (supposing a line-of-sight
# free-space channel (/bit/m^2)
E_FS = 10e-12
THRESHOLD_DIST = math.sqrt(E_FS / E_MP)

# routing config
NB_CLUSTERS = 6

# FCM fuzzy coefficient
FUZZY_M = 1.5

# sleep scheduling configurations:
NB_INDIVIDUALS = 10
MAX_ITERATIONS = 50
# ALPHA and BETA are the fitness function' weights
# where ALPHA optimizes energy lifetime, BETA the coverage
FITNESS_ALPHA = 0.34
FITNESS_BETA = 0.33
FITNESS_GAMMA = 0.33
WMAX = 0.6
WMIN = 0.1

# other:
# grid precision (the bigger the faster the simulation)
GRID_PRECISION = 1  # in meters
# useful constants (for readability)
INFINITY = float('inf')
MINUS_INFINITY = float('-inf')

RESULTS_PATH = './results_test/'
