from itertools import combinations

def encontrarDupla(A,N):
    for c in A:
        for x in A:
            if c + x == N:
                return print('La dupla es {} - {} para obtener {}'.format(x,c,N))
    
def encontrarDuplaV2(list_numbers,number):
    number_pairs = combinations(list_numbers, 2)
    for firts,second in number_pairs:
        if firts + second == number:
            return print('La dupla es {} - {} para obtener {}'.format(firts,second,number))
    
def main():
    list_numbers = [2,5,8,11]
    number = 10
    # encontrarDuplaV2(list_numbers, number)
    # encontrarDupla(list_numbers, number)
    
    list_projects = [1,0,1,1,0,2,0,2,]
    list_costs = [23,45,2,6,7,3,4,1]
    #result = project_Cost(list_projects, list_costs)
    result = project_Cost(list_projects, list_costs)
    print(result, sum(result[1]))
    
def project_Cost(list_projects, list_costs):
    id_projects = []
    cost_projects = []
    flag = -1
    count = 0
    for id in list_projects:
        try:
            flag = id_projects.index(id)
            if cost_projects[flag] > list_costs[count]:
                cost_projects[flag] = list_costs[count]
        except:
            id_projects.append(id)
            cost_projects.append(list_costs[count])
        count += 1
    
    return id_projects, cost_projects    
            
            
if __name__ == '__main__':
    main()