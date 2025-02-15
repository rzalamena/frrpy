import re
import frrpy.frr_northbound_pb2

STATICD_ROOT_XPATH = \
    '/frr-routing:routing' + \
    '/control-plane-protocols' + \
    '/control-plane-protocol' + \
    '[type=\'frr-staticd:staticd\'][name=\'staticd\'][vrf=\'{}\']'


class StaticRouteNextHop:
    "Represents a next hop in a static route."
    TYPE_IFINDEX = 'ifindex'
    TYPE_IPV4 = 'ip4'
    TYPE_IPV4_IFINDEX = 'ip4-ifindex'
    TYPE_IPV6 = 'ip6'
    TYPE_IPV6_IFINDEX = 'ip6-ifindex'
    TYPE_BLACKHOLE = 'blackhole'

    def __init__(self, type, vrf, gateway='', interface='', table=0, metric=1, distance=1):
        self.type = type
        self.vrf = vrf
        self.gateway = gateway
        self.interface = interface
        self.table = table
        self.metric = metric
        self.distance = distance

    def __repr__(self):
        return f"|{self.type},{self.gateway},{self.interface}|"


class StaticRoute:
    "Represents a static route in FRR."
    AFI_SAFI_IPV4_UNICAST = 'frr-routing:ipv4-unicast'
    AFI_SAFI_IPV6_UNICAST = 'frr-routing:ipv6-unicast'

    def __init__(self, prefix, vrf='default'):
        self.vrf = vrf
        self.prefix = prefix
        if re.search(r':', self.prefix):
            self.afi_safi = self.AFI_SAFI_IPV6_UNICAST
        else:
            self.afi_safi = self.AFI_SAFI_IPV4_UNICAST

        self.next_hops = []

    def __repr__(self):
        return f"StaticRoute[{self.prefix}, vrf={self.vrf}] next hops: {self.next_hops}"

    def add_next_hop_interface(self, interface):
        self.next_hops.append(
            StaticRouteNextHop(
                StaticRouteNextHop.TYPE_IFINDEX,
                self.vrf,
                interface=interface))

    def add_next_hop_ip(self, gateway):
        if self.afi_safi == AFI_SAFI_IPV4_UNICAST:
            self.next_hops.append(
                StaticRouteNextHop(
                    StaticRouteNextHop.TYPE_IPV4,
                    self.vrf,
                    gateway=gateway))
        else:
            self.next_hops.append(
                StaticRouteNextHop(
                    StaticRouteNextHop.TYPE_IPV6,
                    self.vrf,
                    gateway=gateway))

    def add_next_hop_ip_interface(self, gateway, interface):
        if self.afi_safi == AFI_SAFI_IPV4_UNICAST:
            self.next_hops.append(
                StaticRouteNextHop(
                    StaticRouteNextHop.TYPE_IPV4,
                    self.vrf,
                    gateway=gateway,
                    interface=interface))
        else:
            self.next_hops.append(
                StaticRouteNextHop(
                    StaticRouteNextHop.TYPE_IPV6,
                    self.vrf,
                    gateway=gateway,
                    interface=interface))

    def _next_hop_to_xpath(self, next_hop):
        "Function used exclusively by StaticRoute to generate XPath."
        return f"/path-list[table-id='{next_hop.table}'][metric='{next_hop.metric}'][distance='{next_hop.distance}']" + \
            f"/frr-nexthops/nexthop[nh-type='{next_hop.type}'][vrf='{next_hop.vrf}'][gateway='{next_hop.gateway}'][interface='{next_hop.interface}']"

    def to_xpath(self, delete=False):
        xpath_base = STATICD_ROOT_XPATH.format(self.vrf) + \
            f"/frr-staticd:staticd/route-list[prefix='{self.prefix}'][afi-safi='{self.afi_safi}']"

        xpaths = []
        if delete:
            path = frrpy.frr_northbound_pb2.PathValue()
            path.path = xpath_base
            xpaths.append(path)
        else:
            for next_hop in self.next_hops:
                path = frrpy.frr_northbound_pb2.PathValue()
                path.path = (xpath_base + self._next_hop_to_xpath(next_hop))
                xpaths.append(path)

        return xpaths


def load_routes(connection, vrf='default'):
    routes = connection.configuration(STATICD_ROOT_XPATH.format(vrf))
    try:
        routes = routes['frr-routing:control-plane-protocol'][0]['frr-staticd:staticd']['route-list']
    except KeyError:
        return []

    route_list = []
    for entry in routes:
        route = StaticRoute(entry['prefix'], vrf=vrf)
        route_list.append(route)

        path = entry['path-list'][0]
        for next_hop in path['frr-nexthops']['nexthop']:
            if next_hop['nh-type'] == StaticRouteNextHop.TYPE_IFINDEX:
                route.add_next_hop_interface(next_hop['interface'])
            elif next_hop['nh-type'] == StaticRouteNextHop.TYPE_IPV4 or next_hop['nh-type'] == StaticRouteNextHop.TYPE_IPV6:
                route.add_next_hop_ip(next_hop['gateway'])
            else:
                route.add_next_hop_ip_interface(nexthop['gateway'], next_hop['interface'])

    return route_list
