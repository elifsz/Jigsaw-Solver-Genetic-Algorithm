# Jigsaw Solver Genetic Algorithm
 
![image](https://user-images.githubusercontent.com/46938621/148816085-7e59eb84-ed3a-47fc-bb60-a3a311e0a09f.png)

**Introduction Genetic Algorithm**

The selected photo is turned into a 9-piece puzzle using the skimage
view_as_blocks function. The dictionary is assigned 9 sections as the target
[0,1,2,3,4,5,6,7,8]. The puzzle pieces are then mixed with the shuffle and this is
done for the initial population number. In this case, the initial population is
created.

**Selection Function**

Among the created populations, the most suitable one is selected and the next
generation is created. In order to create the next generation, those with the most
unsuccessful fitness values from the previous generation are removed and
children formed from the best parents are added.

**Fitness function**

The Member travels the Population and increases its fitness value by one when
the Member's Chromosome equals the Target Chromosome. This process takes
place as long as the target's length. Those with great fitness value are closest to
the target. When the Member's Fitness value is equal to the Target's length, the
target is found.

**Crossover Function**

The individual (chromosome) in the received population is ranked according to
the fitness value. Using selection, the two best individuals (parents) from the
population are selected. If the probability value we calculated is less than 0.4, if
it is between 0.4 and 0.8 from the first parent, the gene is selected for the image
sequence from the second parent and the child is created.

**Mutation Function**

If the probability is not between these values, the mutation is applied. A picture
block is added to the child randomly from the image orders.
Here, duplicate values are removed in order not to add parts that already exist in
the photo, and the process is added again until there are no identical orders.


![image](https://user-images.githubusercontent.com/46938621/148816238-7198ec56-e680-4bd0-911f-80336eded6e1.png)


