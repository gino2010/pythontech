# Toilet

一个搞笑的算法面试题，搞笑两个原因：
1. 场景假设有很多牵强之处（即不准确，不完整），这样不准确的需求推出的"解决方案"有点让人莫名其妙
2. 是出题者设计这么一个贴近生活（工作）细节的场景，有点给人一种小题大做的搞笑

A funny interview question for algorithm, two reasons for funny:
1. The scenario assumes a lot of far-fetched (inaccurate, incomplete), so the "solution" of the inaccurate demand is a bit confusing.
2. It is the scene of the design of such a close to the details of life(work), a little bit funny of making a fuss over a trifle

### Question

Many potential conflicts lurk in the workplace and one of the most sensitive issues involves toilet seats. Should you leave the seat “up” or “down”? This also affects productivity, particularly at large companies. Hours each week are lost when employees need to adjust toilet seats. Your task is to analyze the impact different bathroom policies will have on the number of seat adjustments required.

The classical assumption is that a male usually uses a toilet with the seat “up” whereas a female usually uses it with the seat “down”. However, we will divide the population into those who prefer the seat up and those who prefer it down, regardless of gender.

Now, there are several possible policies that one could use, here are a few:

1. When you leave, always leave the seat up
2. When you leave, always leave the seat down
3. When you leave, always leave the seat as you would like to find it

So, a person may have to adjust the seat prior to using the toilet and, depending on policy, may need to adjust it before leaving.

#### Task
Your task is to evaluate these different policies. For a given sequence of people’s preferences, you are supposed to calculate how many seat adjustments are made for each policy.

#### Input
The first and only line of input contains a string of characters ’U’ and ’D’, indicating that a person in the sequence wants the seat up or down. The string has length at least 2 and at most 1000.
The first character indicates the initial position of the toilet seat, and the following n - 1 characters indicate how a sequence of n - 1 people prefer the seat. You should compute the total number of seat adjustments needed for each of the three policies described above.

#### Output
Output three numbers, each on a separate line, the total number of seat adjustments for each policy.

UUUDDUDU : 6, 7, 4
