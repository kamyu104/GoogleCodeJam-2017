# [GoogleCodeJam 2017](https://codingcompetitions.withgoogle.com/codejam/archive/2017) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![Progress](https://img.shields.io/badge/progress-26%20%2F%2027-ff69b4.svg)

Python solutions of Google Code Jam 2017. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A `4-minute` timer is set for the small dataset and a `8-minute` timer is set for the large dataset this year.

* [Code Jam 2016](https://github.com/kamyu104/GoogleCodeJam-2016)
* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2017#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2017#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2017#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2017#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2017#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2017#round-3)
* [World Finals](https://github.com/kamyu104/GoogleCodeJam-2017#world-finals)
* [Code Jam 2018](https://github.com/kamyu104/GoogleCodeJam-2018)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Oversized Pancake Flipper](https://code.google.com/codejam/contest/3264486/dashboard#s=p0)| [Python](./Qualification%20Round/pancake-flipper.py)| _O(K * S)_ | _O(S)_ | Easy | | Greedy |
|B| [Tidy Numbers](https://code.google.com/codejam/contest/3264486/dashboard#s=p1)| [Python](./Qualification%20Round/tidy-numbers.py)| _O((logN)^2)_ | _O(logN)_ | Easy | | Math Analysis |
|C| [Bathroom Stalls](https://code.google.com/codejam/contest/3264486/dashboard#s=p2)| [Python](./Qualification%20Round/bathroom-stalls.py)| _O(logK)_ | _O(1)_ | Easy | | BST |
|D| [Fashion Show](https://code.google.com/codejam/contest/3264486/dashboard#s=p3)| [Python](./Qualification%20Round/fashion-show.py)| _O(N^2)_ | _O(N)_ | Hard | | Greedy |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Alphabet Cake](https://code.google.com/codejam/contest/5304486/dashboard#s=p0)| [Python](./Round%201A/alphabet-cake.py)| _O(R * C)_ | _O(1)_ | Easy | | Greedy |
|B| [Ratatouille](https://code.google.com/codejam/contest/5304486/dashboard#s=p1)| [Python](./Round%201A/ratatouille.py)| _O(N^2 * P^2)_ | _O(N * P)_ | Medium | | Greedy |
|C| [Play The Dragon](https://code.google.com/codejam/contest/5304486/dashboard#s=p2)| [Python](./Round%201A/play-the-dragon.py)| _O(sqrt(N))_ | _O(1)_ | Hard | | Math Analysis |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Steed 2: Cruise Control](https://code.google.com/codejam/contest/8294486/dashboard#s=p0)| [Python](./Round%201B/cruise-control.py)| _O(N)_ | _O(1)_ | Easy | | Math Analysis |
|B| [Stable Neigh-bors](https://code.google.com/codejam/contest/8294486/dashboard#s=p1)| [Python](./Round%201B/stable-neighbors.py)| _O(N)_ | _O(1)_ | Hard | | Math Analysis |
|C| [Pony Express](https://code.google.com/codejam/contest/8294486/dashboard#s=p2)| [Python](./Round%201B/pony-express.py)| _O(N^3)_ | _O(1)_ | Medium | | Floyd-Warshall |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Ample Syrup](https://code.google.com/codejam/contest/3274486/dashboard#s=p0)| [Python](./Round%201C/ample-syrup.py)| _O(NlogK)_ | _O(K)_ | Easy | | Sort, Heap |
|B| [Parenting Partnering](https://code.google.com/codejam/contest/3274486/dashboard#s=p1)| [Python](./Round%201C/parenting-partnering.py)| _O(NlogN)_ | _O(N)_ | Medium | | Sort, Greedy |
|C| [Core Training](https://code.google.com/codejam/contest/3274486/dashboard#s=p2)| [Python](./Round%201C/core-training.py)| _O(N^2 * K)_ | _O(N)_ | Hard | | DP, Probability|

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Fresh Chocolate](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/00000000002017f4)| [Python](./Round%202/fresh_chocolate.py) | _O(1)_ | _O(1)_ | Easy | | Math, Greedy |
|B| [Roller Coaster Scheduling](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201845)| [Python](./Round%202/roller_coaster_scheduling.py) | _O(M + N)_ | _O(M)_ | Easy | | Math, Greedy |
|C| [Beaming With Joy](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201876)| [Python](./Round%202/beaming_with_joy.py) | _O(R * C)_ | _O(R * C)_ | Medium | | CNF, 2-SAT, SCC, Tarjan's Algorithm |
|D| [Shoot the Turrets](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201900/0000000000201901)| [Python](./Round%202/shoot_the_turrets.py) | _O(S * R * C + S * T^2 + T * S * (R + C))_ | _O(S * R * C)_ | Hard | | BFS, Bipartite Matching |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Googlements](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/00000000002017f6)| [Python](./Round%203/googlements.py) | _O(L * (H(L + 1, L) - 1))_ | _O(L)_  | Easy | | Math, Backtracking, Pruning |
|B| [Good News and Bad News](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201846)|[Python](./Round%203/good_news_and_bad_news.py) | _O(P^2)_ | _O(P)_ | Medium | | Graph, DFS, Spanning Tree |
|C| [Mountain Tour](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201877)| [Python](./Round%203/mountain_tour.py) | _O(C * log*(C))_ | _O(C)_ | Medium | | Union Find, Greedy |
|D| [Slate Modern](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201902/0000000000201903)| [Python](./Round%203/slate_modern.py) | _O(N^2)_ | _O(N^2)_ | Hard | | Manhattan Distance, Coordinate Compression, DP, Arithmetic Progression |

## World Finals
You can relive the magic of the 2017 Code Jam World Finals by watching the [Live Stream Recording](https://www.youtube.com/watch?v=Pq-wdw9TRoI) of the competition, problem explanations, interviews with Google and Code Jam engineers, and announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Dice Straight](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/00000000002017fc)| [PyPy](./World%20Finals/dice_straight.py) [PyPy](./World%20Finals/dice_straight2.py) | _O(N^2)_ | _O(N)_ | Medium | | Sliding Window, Bipartite Matching, Ford-Fulkerson Algorithm |
|B| [Operation](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020184a)| [Python](./World%20Finals/operation.py) | _O(11*2^11 * (N * D^2))_ | _O(2^11 * (N * D))_ | Medium | | Grouping, Greedy, DP |
|C| [Spanning Planning](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020187a)| [PyPy](./World%20Finals/spanning_planning.py) | _O(R * N^3)_ | _O(N^2)_ | Hard | | Cycle, Spanning Tree, Kirchhoff Matrix Tree Theorem, Determinant, Gaussian Elimination |
|D| [Omnicircumnavigation](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/000000000020190a)| [PyPy](./World%20Finals/omnicircumnavigation.py) | _O(N^2)_ | _O(N)_ | Easy | | Geometry, Plane, Vector, Inner Product, Outer Product |
|E| [Stack Management](https://codingcompetitions.withgoogle.com/codejam/round/0000000000201909/00000000002017fd)| [Python](./World%20Finals/stack_management.py) | _O((N * C) * logN)_ | _O(N * C)_ | Very Hard | | Preprocess, Stack, DFS |
|F| [Teleporters](https://code.google.com/codejam/contest/6314486/dashboard#s=p5)|||| Very Hard | | |
