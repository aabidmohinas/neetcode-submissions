class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def Sieve(L, R):
            ## Sieve of Erantosthenes
            n = R 
            IsPrime = [True] * (n + 1)
            
            IsPrime[0] = False
            IsPrime[1] = False
            
            for i in range(2, int(n ** 0.5) + 1):
                if IsPrime[i]:
                    for j in range(i * i, n + 1, i):
                        IsPrime[j] = False
            
            Primes = [
                k for k in range(max(2, L), n + 1) if IsPrime[k]
            ]
            return Primes

        Primes = Sieve(left, right)
        if len(Primes) < 2: return [-1, -1]

        MinPairs = [-float('inf'), float('inf')]
        
        Difference = lambda x: x[1] - x[0]

        for i in range(len(Primes) - 1):
            Diff = Difference(Primes[i: i + 2])
            CurrentDifference = Difference(MinPairs)

            if Diff < CurrentDifference:
                MinPairs[0] = Primes[i]
                MinPairs[1] = Primes[i + 1]

        return MinPairs


            
