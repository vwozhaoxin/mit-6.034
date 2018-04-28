from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    result2=[hypothesis]
#    while set[newh]!= set([hypothesis]):
    for condition in rules:
        resuls1=[]
        if isinstance(condition,IF):
            result=condition.antecedent()
            condition=condition.consequent()
            data = match(condition[0],hypothesis)
            if data is not None:
#                print(type(result))
                if not isinstance(result,list):
                    result = [result]
                for r in result:
                    if isinstance(r, OR):
                        for i in range(len(r)):
                            result3=[]
                            newh =populate(r[i],data)                            
#                            result3.append(newh)
                            result3.append(backchain_to_goal_tree(rules,newh))
                        resuls1.append(OR(result3))
                    elif isinstance(r, AND):
                        for i in range(len(r)):
                            result3=[]
                            newh =populate(r[i],data)
#                            result3.append(newh)
                            result3.append(backchain_to_goal_tree(rules,newh))
                        resuls1.append(AND(result3))
                    else:
                        newh=populate(r,data)
#                        resuls1.append(newh)
#                        print(newh)
                        newresult= backchain_to_goal_tree(rules,newh)
                        print(newresult)
                        resuls1.append(newresult)
                if isinstance(result,AND):
                    result2.append(AND(resuls1))
                else:
                    result2.append(OR(resuls1))
                    
    print(simplify(OR(result2)))
    return simplify(OR(result2))





# Here's an example of running the backward chainer - uncomment
# it to see it work:
print(backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')) 
