from trains.models import Train


def dfs_paths(graph, start, goal):
    """The searching all roads from city to city.
     Visiting the same city more than once is not considered"""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form):

    context = {'form': form}
    qs = Train.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities_through']
    travelling_time = data['travelling_time']
    all_routs = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_routs):
        raise ValueError('The route does not exist.')
    if cities:
        _cities = [city.id for city in cities ]
        right_routes = []
        for route in all_routs:
            if all(city in route for city in _cities):
                right_routes.append(route)
        if not right_routes:
            raise ValueError('The route does not exist through the city.')
    else:
        right_ways = all_routs
        routes = []
        all_trains = {}
        for q in qs:
            all_trains.setdefault((q.from_city_id, q.to_city_id), [])
            all_trains[(q.from_city_id, q.to_city_id)].append(q)
        for route in right_ways:
            tmp = {}
            tmp['trains'] = []
            total_time = 0
            for i in range(len(route) - 1):
                qs = all_trains[(route[i], route[i + 1])]
                q = qs[0]
                total_time += q.travel_time
                tmp['trains'].append(q)
            tmp['travel_time'] = total_time
            if total_time <= travelling_time:
                routes.append(tmp)
        if not routes:
            raise ValueError('Travel time more than specified.')

        sorted_routes = []
        if len(routes) == 1:
            sorted_routes = routes
        else:
            times = list(set(r['total_time'] for r in routes))
            times = sorted(times)
            for time in times:
                for route in routes:
                    if time == route['total_time']:
                        sorted_routes.append(route)

        context['routes'] = sorted_routes
        context['cities'] = {'from_city': from_city.name, 'to_city': to_city.name}
        return context

