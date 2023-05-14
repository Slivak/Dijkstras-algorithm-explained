#Таблица узлов

graph = {}

#Это стартовый узел
graph["start"] = {}
#А это его соседи (см. graph.png)
graph["start"]["a"] = 6
graph["start"]["b"] = 2
#Узел А и Его соседи
graph["a"] = {}
graph["a"]["fin"] = 1
#Узел В и его соседи
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
#Финальный узел(у него нет соседей для перехода)
graph["fin"] = {}

#Таблица весов(цен)

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#Таблица родителей(родительских узлов)

parents = {}
parents["a"] = "start"
parents["b"] = "start"
#Мы пока не знаем из какого объекта туда попадём
parents["fin"] = None


#Массив уже обработанных узлов
processed = []


#Функция нахождения узла с наименьшим весом

def find_lowest_node(costs):
    #По умолчанию минимальная цена = бесконечность, а узел с мин.ценой = None
    lowest_cost = float("inf")
    lowest_cost_node = None
    #Для каждого узла
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#Находим узел с минимальной ценой
node = find_lowest_node(costs)
while node is not None:
    #Цена мимнимального узла
    cost = costs[node]
    #Соседи минимального узла
    neighbors = graph[node]
    #Для каждого соседа
    for n in neighbors.keys():
        #Новая цена(цена родителького узла + цена соседа)
        new_cost = cost + neighbors[n]
        #Если к соседу можно быстрее добраться через текущий узел
        if costs[n] > new_cost:
            #Обновить его стоимость на новую
            costs[n] = new_cost
            #А родителем поставить прошлый узел
            parents[n] = node
    #Добавляем узел в обработанный
    processed.append(node)
    #Ищем новый узел с мин.ценой
    node = find_lowest_node(costs)

#А вот и минимальная стоимость
print(costs["fin"])


"""
Вообще в директории description скрины из книги, пошагово разбирающие работу алгоритма
(ОООООООООООООчень полезные скрины)
"""
