'''
You are going on a long trip. You start on the road at mile post 0. 
Along the way there are n hotels, at mile posts a1 < a2 < · · · < an, where each ai is measured from the starting point. 
The only places you are allowed to stop are at these hotels, but you can choose which of the hotels you stop at. 
You must stop at the final hotel (at distance an), which is your destination.
You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing of the hotels). 
If you travel x miles during a day, the penalty for that day is sqaure of (200 − x). 
You want to plan your trip so as to minimize the total penalty—that is, the sum, over all travel days, of the daily penalties.

Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.
'''


'''
Solution:
Let P(k) be the minimum penalty incurred by a sequence of stops that starts at mile post 0 and ends at mile post ak.
Set P(0) = 0 and a0 = 0. For 1 ≤ k ≤ n, we have P(k) = min{sqr(200−(ak −aj)) + P(j) : 0 ≤ j ≤ k −1}.
Indeed, consider an optimal sequence Sk of stops that starts at mile post 0 and ends at mile post
ak. Let aj be the second last stop in Sk, 0 ≤ j ≤ k −1. We claim that the subsequence Sj of Sk
that starts at mile post 0 and ends at mile post aj has to be optimal among sequences of stops
that start at mile post 0 and end at aj. Indeed, if Sj is not optimal, we have a better sequence S0j
that starts at 0 and ends at aj, after which we could drive from aj to ak with strictly less total
penalty than in Sk; this contradicts the optimality of Sk.
An O(n2) dynamic programming algorithm for computing P(n) is immediate from the recurrence for P(k). 
A corresponding sequence of hotels is obtained by keeping track for each k
of a value of j for which P(k) = (200 − (ak − aj))2 + P(j). Let p[k] be such a value. Then,
p[n], p[p[n]], p[p[p[n]]],...,0 is an optimal sequence of hotels.
'''

