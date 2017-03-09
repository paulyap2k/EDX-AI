import Queue,time, sys, resource,copy


def setup_initial_state(input):
    modified=[]
    startstate=[]
    for i in range(0,18,2):
        startstate.insert(i/2,int(input[i]))
    modified.insert(0,("Start",startstate))
    print modified
    return modified

def check_goal_state(inputstate):
    return inputstate[1]==goal_state[1]
         
def visited_state(chkexploredstate):
    if len(chkexploredstate)>0:
    #    print ('is state visited ?'),chkexploredstate[0][1]
    #    print ('list of explored state:'), exploredstatenp
    #    print ("state in list, True or False ?"), chkexploredstate[0][1] in exploredstatenp
        return chkexploredstate[0][1] in exploredstatenp
   
        
def Move_up(state):
    newstate=[]
    teststate=list(state[1])
    i=teststate.index(0)
    teststate[i],teststate[i-3] = teststate[i-3],teststate[i]
    newstate.insert(0,('Up',teststate))
    return newstate

def Move_down(state):
    newstate=[]
    teststate=list(state[1])
    i=teststate.index(0)
    teststate[i],teststate[i+3] = teststate[i+3],teststate[i]
   
    newstate.insert(0,('Down',teststate))
    return newstate

def Move_left(state):
    newstate=[]
    teststate=list(state[1])
    i=teststate.index(0)
    teststate[i],teststate[i-1] = teststate[i-1],teststate[i]

    newstate.insert(0,('Left',teststate))
    return newstate

def Move_right(state):
    newstate=[]
    teststate=list(state[1])
    i=teststate.index(0)
    teststate[i],teststate[i+1] = teststate[i+1],teststate[i]

    newstate.insert(0,('Right',teststate))
    return newstate


####------------------MAIN PROGRAM--------------------
def BFS():
    print ('start of BFS, start state is:')
    print exploredstate
    
    # Running BFS----------------
    expanded_node=0
    
    for num in range(20):
        print 'number:',num
        upstate=[]
        downstate=[]
        leftstate=[]
        rightstate=[]


        popstate=frontier_states.get()
        
        print ('popstate: '), popstate

        if check_goal_state(popstate)==True: # (Found Solution)
            print 'Path Found, will need reverse path !'
            break

        if  check_goal_state(popstate)==True: # (Found Solution)
            print 'Path Found, will need reverse path !'
            #exploredstate.insert(0,popstate)
            break
            
        else:
            i=popstate[1].index(0)
            if not (i==0 or i==1 or i==2):
                upstate=Move_up(popstate)
         #       print 'no constraint to move up'
                if not visited_state(upstate):
          #          print 'ensode state', upstate[0][:]
                    frontier_states.put(upstate[0][:])
                    exploredstate.insert(0,upstate[0][:])
                    exploredstatenp.insert(0,upstate[0][:][1])
           #         print ('popstate'),popstate
           #         print ('updatet'),upstate
                  #  if  check_goal_state(upstate[0][:])==True: # (Found Solution)
                  #      print 'Path Found, will need reverse path !'
                  #      break

          
            if not (i==6 or i==7 or i==8):
                downstate=Move_down(popstate)
            #    print 'no constraint to move down'
                if not visited_state(downstate):
             #       print 'ensode state', downstate[0][:]
                    frontier_states.put(downstate[0][:])
                    exploredstate.insert(0,downstate[0][:])
                    exploredstatenp.insert(0,downstate[0][:][1])
                    #if  check_goal_state(downstate[0][:])==True: # (Found Solution)
                    #    print 'Path Found, will need reverse path !'
                    #    break
                    

            if not (i==0 or i==3 or i==6):
                leftstate=Move_left(popstate)
              #  print 'no constraint to move left'
                if not visited_state(leftstate):
               #     print 'ensode state', leftstate[0][:]
                    frontier_states.put(leftstate[0][:])
                    exploredstate.insert(0,leftstate[0][:])
                    exploredstatenp.insert(0,leftstate[0][:][1])
                    #if  check_goal_state(leftstate[0][:])==True: # (Found Solution)
                    #    print 'Path Found, will need reverse path !'
                    #    break

            if not (i==2 or i==5 or i==8): 
                rightstate=Move_right(popstate)
                #print 'no constraint to move right'
                if not visited_state(rightstate):
                 #   print 'ensode state', rightstate[0][:]
                    frontier_states.put(rightstate[0][:])
                    exploredstate.insert(0,rightstate[0][:])
                    exploredstatenp.insert(0,rightstate[0][:][1])
                   # if  check_goal_state(rightstate[0][:])==True: # (Found Solution)
                   #     print 'Path Found, will need reverse path !'
                   #     break
    
                  
            expanded_node+=1
            print 'expanded node+++++++++++++++++++', expanded_node 
        
        
    

##---Variable------------------
start_time = time.time()
goal_state=('End',[0,1,2,3,4,5,6,7,8])
exploredstate=[] #exploredstate=[('direction',[state]),(),...]
exploredstatenp=[]
nodes_expanded=0
level=0
fringe=0
path=[]

#-------initialize & Run BFS--------
try:
    firststate=setup_initial_state(sys.argv[1])
except IndexError:
    firststate = ('Start',[1,2,5,3,4,0,6,7,8])
    #firststate = ('Start',[5,3,6,1,2,7,4,0,8])
    print ("use default start state since none given")

frontier_states=Queue.Queue()
frontier_states.put(firststate)

exploredstate=[firststate]
exploredstatenp=[[5,3,6,1,2,7,4,0,8]]


BFS()
print 'explored state',exploredstate
print len(exploredstate)

running_time=(time.time() - start_time) 
max_ram_usage=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
print("  Max Ram Used (MB): %s " %  max_ram_usage)
print("  Runtime: %s secs " % running_time)




""" # write to file
with open('output.txt', 'w') as f:
    f.write(('Coordinate: %s \n')%test)
    f.write(('path_to_go: %s \n')%path)
    f.write('Runtime: ')
    f.write('\nThis is a test')
    
f.closed
                
# Parameter requires in the reporting

for i in range(len(q)):
    q.put(sys.argv[1]
q=Queue.Queue()


start_time = time.time()
path_to_goal=0
cost_of_path=0
nodes_expanded=0
fringe_size=0
search_depth=0
max_search_depth=0
running_time=(time.time() - start_time) 
max_ram_usage=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000
print("  Max Ram Used (MB): %s " %  max_ram_usage)
print("  Runtime: %s secs " % running_time)
"""
