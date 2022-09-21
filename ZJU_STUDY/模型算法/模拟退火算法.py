# def obj_func(p):
#     x1, x2, x3 = p
#     return x1 ** 2 + x2 ** 2 + x3 ** 2


# constraint_eq = [
#     lambda x: 1 - x[1] - x[2]
# ]

# constraint_ueq = [
#     lambda x: 1 - x[0] * x[1],
#     lambda x: x[0] * x[1] - 5
# ]

demo_func = lambda x: x[0] ** 2 + (x[1] - 0.05) ** 2 + x[2] ** 2
from sko.SA import SA

sa = SA(func=demo_func, x0=[1, 1, 1], T_max=1, T_min=1e-9, L=300, max_stay_counter=150)
best_x, best_y = sa.run()
print('best_x:', best_x, 'best_y', best_y)
from sko.SA import SA_TSP

sa_tsp = SA_TSP(func=cal_total_distance, x0=range(num_points), T_max=100, T_min=1, L=10 * num_points)

best_points, best_distance = sa_tsp.run()
print(best_points, best_distance, cal_total_distance(best_points))