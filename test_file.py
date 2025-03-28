import similarity_score_calculation
import data_loader

Exercise_list = data_loader.get_all_exercises()
small = Exercise_list[0:10]
lst = [x.properties for x in small]
name  = small[0].properties[0]
graph = data_loader.create_graph(small)
rec_list = graph.get_score_popular(name)
print(rec_list)




