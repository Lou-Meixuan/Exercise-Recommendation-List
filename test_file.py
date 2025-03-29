import weight_calculation
import data_loader

Exercise_list = data_loader.get_all_exercises()
small = Exercise_list[0:10]
lst = [x.properties for x in small]
name = small[0].properties[0]
na = [x.properties[0] for x in small]
graph = data_loader.create_graph(small)
se = graph.get_name_vertices()
prc = graph.popular_recommendation(name)
print(prc)
nprc = graph.not_popular_recommendation(name)
print(nprc)
cl = ['force', 'level', 'mechanic']
cc = graph.custom_recommendation(name, cl)
print(cc)




