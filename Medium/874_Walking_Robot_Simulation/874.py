#URL : https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
#[Medium] [874] 
#Title: [Walking Robot Simulation]
#Author: Kartik Bhatnagar
#Date : 2024-09-04 (YYYY-MM-DD)
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        cur_dir = "N" #given the robot is facing the North at the start
        dirs1=['N','E','S','W']#if -1 is the command the sequence of nect direction
        dirs2=['N','W','S','E'] # If -2 is the command the sequence of next direction
        c_pos=(0,0)
        y_obs =  list(set([o[1] for o in obstacles]))
        x_obs =  list(set([o[0] for o in obstacles]))
        max_ecu_dis =0
        
        def ecu_dis(pos):
            return (abs(pos[0])**2) +(abs(pos[1]**2))

        def check_obstacle(pos,d,u):
            if d =="N":
                if pos[0] in x_obs:
                    for i in range(1,u+1):
                        if [pos[0],pos[1]+i] in obstacles:
                            print("obstacle found",[pos[0],pos[1]+i] ,d,u)
                            return True,(pos[0],pos[1]+i-1)
                            break
                return False,(0,0)
            if d =="E":
                if pos[1] in y_obs:                    
                    for i in range(1,u+1):
                        if [pos[0]+i,pos[1]] in obstacles:
                            print("obstacle found",[pos[0]+i,pos[1]],d,u)
                            return True,(pos[0]+i-1,pos[1])
                            break
                return False,(0,0)
            if d =="W":
                if pos[1] in y_obs:
                    for i in range(1,u+1):
                        if [pos[0]-i,pos[1]] in obstacles:
                            print("obstacle found",[pos[0]-i,pos[1]],d,u)
                            return True,(pos[0]-i+1,pos[1])
                            break
                return False,(0,0)
            if d =="S":
                if pos[0] in x_obs:
                    for i in range(1,u+1):
                        if [pos[0],pos[1]-i] in obstacles:
                            print("obstacle found",[pos[0],pos[1]-i],d,u)
                            return True,(pos[0],pos[1]-i+1)
                            break
                return False,(0,0)

        def move(pos,d,u):
            #returns the new postion of the robot after moving 'u' units in the given 'd' direction
            if d =="N":
                pos = (pos[0],pos[1]+u) #increment u units in y-axis
            elif d=="S":
                pos = (pos[0],pos[1]-u) #decrement u units in y-axis
            elif d =="W":
                pos = (pos[0]-u,pos[1]) #decrement u units in x-axis
            elif d=="E":
                pos = (pos[0]+u,pos[1]) #increment u units in x-axis
            else:
                pass
            return pos

        for c in commands:
            if c  == -1:
                cur_dir = dirs1[(dirs1.index(cur_dir)+1)%4]
                print(cur_dir)
                continue
            if c == -2:
                cur_dir = dirs2[(dirs2.index(cur_dir)+1)%4]
                print(cur_dir)
                continue
            if c>0:
                obs,obs_pos=check_obstacle(c_pos,cur_dir,c)
                if(not obs):
                    c_pos = move(c_pos,cur_dir,c)
                else:
                    c_pos = obs_pos
                max_ecu_dis = max(ecu_dis(c_pos) ,max_ecu_dis)
                if ecu_dis(c_pos) == 5140:
                    print(pos,"sameee")
                
                print(c_pos)
        return max_ecu_dis

                
                
        
if __name__ == "__main__":
    s=Solution()
