# Class to provide functionality of the methods for the view/edit rules page

class RuleBackend():

    def __init__(self, ruleNum, ruleEdits):

        for i in range(1,ruleNum):
            self.ruleNewValue[i] = ruleEdits[i]

    # Update rules database with new rule values
    def updateRules(self, tupleRuleNumEdit):
        # tupleRuleEdits = (ruleNum, ruleEdit)
        # Update specific rule using rule edit value
        return 0
