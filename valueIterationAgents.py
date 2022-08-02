# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        
        states = mdp.getStates()
        for i in range(0, iterations):
            i_val = util.Counter() # Fixed Counter vk-1 (has to be Batch, not online)

            for state in states:
                if not mdp.isTerminal(state):
                    actions = mdp.getPossibleActions(state) # s' belongs S
                    max = float('-inf')
                    
                    for action in actions: # a belongs to A(s)
                        qVal = self.computeQValueFromValues(state, action) # Q(a,s)
                        if qVal > max:
                            max = qVal
                
                    i_val[state] = max  # We update the actual iteration, not self.values         
            
            self.values = i_val    # We update self.values with the new calculated vector.

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        nextStatesProb = self.mdp.getTransitionStatesAndProbs(state, action)
        sumatori = 0

        for nextState, prob in nextStatesProb:
            reward = self.mdp.getReward(state, action, nextState) # r(s,a)
            sumatori += prob * self.getValue(nextState) # P(s'|s)*V(s')
        
        return reward + self.discount * sumatori # r(s,a) + summation P(s'|s)*V(s')

        # util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # If terminal state or no legal actions return None
        bestAction = None
        if self.mdp.isTerminal(state):
            return bestAction

        max = float('-inf')
        actions = self.mdp.getPossibleActions(state)
        for action in actions:
            qVal = self.computeQValueFromValues(state, action) # Q(s,a)
            if qVal > max: # best action will have the highest Q(s,a)
                max = qVal
                bestAction = action

        return bestAction

        # util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
