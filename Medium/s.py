class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        change = 1
        while (change > 0):  # keep on repeating until no change is detected
            change = 0
            i = len(asteroids)-1
            skip = []  # index of asteriods that will be skipped
            # for i in range(len(asteroids)-1,-1,-1):
            while (i >= 1):
                ast_pos = i
                if asteroids[i] < 0:  # if negative asteriod comes up
                    j = i-1
                    # be in loop until previous element is positive and smaller than current negative asteriod
                    while ((abs(asteroids[j]) < abs(asteroids[i])) and j >= 0):
                        if asteroids[j] > 0:
                            skip.append(j)
                            j = j-1
                        else:
                            break
                    if j >= 0:
                        if asteroids[j] > 0:
                            # if +ve asteroid is heavy then -ve one will explode
                            if abs(asteroids[j]) > abs(asteroids[i]):
                                skip.append(i)
                                i = j-1
                                continue
                            # if both -ve and +ve asteoids are of same mass both should explode
                            elif abs(asteroids[j]) == abs(asteroids[i]):
                                skip.append(i)
                                skip.append(j)
                                i = j-1
                                continue
                        else:  # if -ve asteroids meets  -ve asteroid;
                            i = j
                            continue
                else:  # if pos asteroid comes
                    i = i-1
            change = len(skip)
            asteroids = [asteroids[i]
                         for i in range(len(asteroids)) if i not in skip]
        return asteroids


s2 = Solution()
arr = [1, -2, -2, -2]
print("answer", s2.asteroidCollision(arr))
