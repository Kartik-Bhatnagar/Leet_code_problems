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
                print("i:", i)
                if asteroids[i] < 0:  # if negative asteriod comes up
                    j = i-1
                    # be in loop until previous element is positive and smaller than current negative asteriod
                    while ((abs(asteroids[j]) < abs(asteroids[i])) and j >= 0):
                        if asteroids[j] > 0:
                            skip.append(j)
                            print("skipped j:", j)
                            j = j-1
                        else:
                            break
                    if j >= 0:
                        if asteroids[j] > 0:
                            # if +ve asteroid is heavy then -ve one will explode
                            if abs(asteroids[j]) > abs(asteroids[i]):
                                skip.append(i)
                                i = j-1
                                print("j greater than i i: ", i)
                                continue
                            # if both -ve and +ve asteoids are of same mass both should explode
                            elif abs(asteroids[j]) == abs(asteroids[i]):
                                skip.append(i)
                                skip.append(j)
                                i = j-1
                                print("j equal  i i: ", i)
                                continue
                        else:  # if -ve asteroids meets  -ve asteroid;
                            i = j
                            continue
                i = i-1
            change = len(skip)
            asteroids = [asteroids[i]
                         for i in range(len(asteroids)) if i not in skip]
            print("change /;", change, asteroids)
        return asteroids


s1 = Solution()
arr = [1, -2, -2, -2]
print(s1.asteroidCollision(arr))
