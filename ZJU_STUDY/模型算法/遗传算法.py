from cmath import pi
import math
import random
import operator

from numpy import piecewise

class GA():
    max_min_index = False
    def __init__(self, length, count):
        self.length = length #染色体长度
        self.count = count #种群中染色体数量
        self.population = self.gen_population(length, count) #随机生成初始种群

    def evolve(self,retain_rate = 0.2, random_select_rate = 0.5, mutation_rate = 0.01):
        """
        进化，对当前一代种群一次进行选择，交叉并产生新一代种群，然后对新一代种群进行变异
        """
        parents = self.selection(retain_rate, random_select_rate)
        self.crossover(parents)
        self.mutation(mutation_rate)

    def gen_chromosome(self, length):
        """
        随机生成长度为length的染色体，每个基因的取值是0或1
        用一个bit表示一个基因
        """
        chromosome = 0
        # c = 0
        # The above code will generate a random chromosome.
        for i in range(length):
            
            chromosome |= (1 << i) * random.randint(0,1) #random.randint(0,1)会随机产生0/1
            # a = random.randint(0,1)
            # b = (1 << i)
            # c |=b*a
            # print(i,c,a,b,a*b)
        # print(chromosome)
        return chromosome

    def gen_population(self,length,count):
        """
        获取初始种群（一个含有count个长度为length的染色体列表）
        """
        # print(len([self.gen_chromosome(length) for i in range(count)]))
        return [self.gen_chromosome(length) for i in range(count)]

    def fitness(self, chromosome):
        """
    计算适应度，将染色体解码在0-9之间的数字，带入函数计算
    因为是求最大值，所以数值越大，适应度越高
        """
        x = self.decode(chromosome)
        print(x)
        # return x + 10*math.sin(5*x) + 7*math.cos(4*x)
        return -(x-5)**2+3

    def decode(self,chromosome):
        """
        解码染色体，将二进制转或成属于【2，8】的实数
        """
        return 2+chromosome * 6 / (2**self.length-1)

    def selection(self, retain_rate, random_select_rate):
        """
        选择
        先对适应度从大到小排序，选出存活的染色体
        在进行随机选择，选出适应度虽然小，但是幸存下来的个体
        """
        #对适应度从大到小排序
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        # print(graded)
        graded = [x[1] for x in sorted(graded, reverse = True)] # reverse = ？根据求最大T还是最小值F
        # print(graded)
        #选出适应性强的染色体 
        retain_length = int(len(graded) * retain_rate)
        parents = graded[:retain_length]
        #选出是是影响不强，但是幸存的染色体
        for chromosome in graded[retain_length:]:
            if random.random() < random_select_rate:
                parents.append(chromosome)
        # print(parents)
        return  parents

    def crossover(self,parents):
        """
        染色体的交叉，反之，生成新一代的种群
        """
        #新出生的孩子，最终会被加入存活下来的父母之中，形成新一代的种群
        children = []
        #需要繁殖的孩子的量
        target_count = len(self.population) - len(parents)
        #开始根据需要的量进行繁殖
        while len(children) < target_count:
            male = random.randint(0, len(parents)-1)
            female = random.randint(0, len(parents)-1)
            if male != female:
                #随机选取交叉点
                cross_pos = random.randint(0, self.length)
                #生成掩码，方便位操作
                mask = 0
                for i in range(cross_pos):
                    mask |= (1 << i)
                male = parents[male]
                female = parents[female]
                #孩子将获得父亲在交叉点前的基因和母亲在交叉点后（包括交差点）的基因
                child = ((male & mask) | (female & ~mask)) & ((1<<self.length) - 1)
                children.append(child)
                #经过繁殖后，孩子和父母的数量与原始种群数量相等，可以更新种群
        self.population = parents + children

    def mutation(self, rate):
        """
        变异，对种群的所有个体，随机改变某个个体中的某个基因
        """
        for i in range(len(self.population)):
            if random.random() < rate:
                j = random.randint(0, self.length-1)
                self.population[i] ^= 1 << j

    

    def result(self):
        """
         获得当前代的最优值，这里取的是函数取最大值时候的x的值
        """
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        # print(graded)
        graded = [x[1] for x in sorted(graded, reverse = True)]
        return ga.decode(graded[0])

if __name__ == '__main__':
        #染色体长度为17，种群数量为300
    ga = GA(7,300)
    print(ga)
        #200次迭代
    for x in range(100):
        ga.evolve()
    print (ga.result())
