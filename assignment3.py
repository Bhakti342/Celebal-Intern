import matplotlib.pyplot as plt
y_views = [600, 242, 546, 464, 465, 577, 725]
f_views = [123, 456, 567, 345, 668, 786, 234]
t_views = [234, 207, 678, 456, 872, 456, 81]
days= range(1, 8)

plt.plot(days, y_views, label = 'Youtube Views', color = 'g', marker = 'o', markerfacecolor = 'g', linestyle = '-.')
plt.plot(days, f_views, label = 'Facebook Views', color = 'r', marker = 'o')
plt.plot(days, t_views, label = 'Twitter Views', color = 'b', marker = 'o')
plt.xlabel('Day no.')
plt.ylabel('Views')
plt.legend(loc = 'upper right')
plt.title('Daily views for marketing channel')
plt.show()
