from collections import deque




class Node:
    # constructor
    def _init_(self, state, action=-1, cost=0, parent=None):
        self.State = state
        self.Action = action
        self.Cost = cost
        self.Parent = parent

    def _repr_(self):
        return f"<Node {self.State}>"
# End of Node class


def goal_test(node, goal, states):
    for index in range(len(states)):
        # checking that weather the initial state is in the states's list or not
        if goal == states[index]:
            if node.State == index:
                return True
            else:
                return False


MNT = str(input("enter header"))
MNT = MNT.split()
M = int(MNT[0])
N = int(MNT[1])
T = int(MNT[2])


states = []
Actions = []
# transition model matrix
transition_model = []
print("Enter States")
for i in range(M):
    states.append(input())
print("Actions")
for i in range(N):
    Actions.append(input())
# take input in graph
print("Transition table")
for i in range(M):
    row = []
    row = input().split()
    row = [int(z) for z in row]
    transition_model.append(row)
def search_problem(problem):

    for index in range(len(states)):
        # checking that weather the initial state is in the states's list or not
        if problem[0] == states[index]:
            # initializing the Node with initial state's index
            FirstNode = Node(index)
            # Creating Frontier using Queue DataStructure
            frontier = deque([FirstNode])
            # Creating explored set
            explored = set()
            exploredNode = set()
    sol = []
    while True:
        if frontier is not None:
            # poping the parent
            node = frontier.popleft()
            explored.add(node.State)

            # check weather the node is goal or not
            if goal_test(node, problem[1], states):
                # return solution
                print("ahtesham")
                return sol
            else:
                # expand the chosen node
                state_of_current_node = node.State
                children = transition_model[state_of_current_node]
                # adding the resulting nodes to the frontier
                for child in range(len(children)):
                    # creating node from the state no
                    new_child_node = Node(int(children[child]), child, node.Cost + 1, node)
                    # only if not in the frontier or explored set
                    if new_child_node.State not in explored and new_child_node not in frontier:
                        sol.append(Actions[child])
                        if goal_test(new_child_node, problem[1], states):
                            return sol
                            # return new_child_node
                        # adding into the frontier
                        frontier.append(new_child_node)
                        break

        else:
            return None


def main():
    print("Enter Test case")
    for x in range(T):
        start_goal = input().split("\t")
        solution = search_problem(start_goal)
        for i in range(len(solution)):
            print(solution[i], end="")
            if i is not len(solution) - 1:
                print("->", end="")
        print("")
main(