class object:
    def __init__(self,weight,profit,i) -> None:
        self.profit=profit
        self.name=f'O{i+1}'
        self.weight=weight
    def get_profit_by_weight(self):
        return self.profit/self.weight
    def __str__(self):
        return f'weight {weight}, profit {profit}'
n=int(input('Enter no. of objects: '))
weight=[int(i) for i in input(f'Enter weight for {n} objects separated by \',\': ').split(',')]
profit=[int(i) for i in input(f'Enter profit for {n} objects separated by \',\': ').split(',')]
objects=[object(weight=weight[i],profit=profit[i],i=i) for i in range(len(weight))]
objects.sort(key=lambda x:x.get_profit_by_weight())
m=int(input('Enter capacity'))
current_weight=0
sack=[]
profit=0
for i in objects:
    if current_weight<m:
        if current_weight+i.weight<=m:
            current_weight+=i.weight
            sack.append(f'{i.name} * 1')
            profit+=i.profit
        else:
            weight_left=m-current_weight
            frac=weight_left/i.weight
            current_weight+=(i.weight*frac)
            profit+=(i.profit*frac)
            sack.append(f'{i.name} * {frac}')


print(sack)
print(profit)

