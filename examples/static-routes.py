from frrpy.connection import FrrConnection
from frrpy.staticd import StaticRoute
import frrpy.staticd

connection = FrrConnection()

prefix_list = [
    '10.254.254.1/32',
    '10.254.254.2/32',
    '10.254.254.3/32',
    '10.254.254.4/32',
    '10.254.254.5/32',
    '10.254.254.6/32',
    '10.254.254.7/32',
    '10.254.254.8/32',
    '10.254.254.9/32',
    '10.254.254.10/32',
]

route_list = []
for prefix in prefix_list:
    route = StaticRoute(prefix)
    route.add_next_hop_interface('lo')
    route_list.append(route)

connection.commit(route_list)

# Find missing routes
routes = frrpy.staticd.load_routes(connection)
for route in routes:
    print(route)
