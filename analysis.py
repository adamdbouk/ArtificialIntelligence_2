# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    # We want the agent to not end in an unintended state so the noise should be 0.
    answerDiscount = 0.9 
    answerNoise = 0 
    return answerDiscount, answerNoise

"""(0<disc<1): GREATER -> FUTURE REWARD MORE IMPORTANT, LOWER -> MORE IMPORTANT IMMEDIATE REWARD.
   (0<=noise<=1): GREATER -> MORE UNCERTAINTY IN NEXT STATE
   (real number): POSITIVE: EACH STEP HAS A REWARD (LONG PATH), NEGATIVE: TAKE THE SHORTEST PATH."""

def question3a():
    # closest exit(negative living reward, low discount), risky path (no noise)
    answerDiscount = 0.1 
    answerNoise = 0 
    answerLivingReward = -1 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    # Close exit (low discount, negative living reward), avoid clifs (some noise)
    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    # distant exit (high discount, positive living reward), risky path (no noise)
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    # distant exit (high discount, positive living reward), avoid clifs (some noise)
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    # avoid exits (living reward higher than the reward of terminal nodes >1 and >10)
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 11
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    # 50 iterations are not enough with any epsilon and learning rate.
    answerEpsilon = None
    answerLearningRate = None
    return "NOT POSSIBLE"
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
