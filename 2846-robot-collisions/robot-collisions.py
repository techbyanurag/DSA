class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        # indices
        idx = list(range(n))

        # sort by position
        idx.sort(key=lambda i: positions[i])

        stack = []

        for i in idx:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # L robot
                while stack and directions[stack[-1]] == 'R' and healths[i] > 0:
                    top = stack[-1]

                    if healths[top] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                    elif healths[top] > healths[i]:
                        healths[top] -= 1
                        healths[i] = 0
                    else:
                        stack.pop()
                        healths[i] = 0

                if healths[i] > 0:
                    stack.append(i)

        # collect survivors
        survivors = []
        while stack:
            i = stack.pop()
            survivors.append((i, healths[i]))

        # sort by original index
        survivors.sort()

        return [h for _, h in survivors]