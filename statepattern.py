import random

class GumballMachine:
    def __init__(self, soldOutState, noQuarterState, hasQuarterState, soldState, winnerState, numberOfGumballs: int):
        self.soldOutState = soldOutState(self)
        self.noQuarterState = noQuarterState(self)
        self.hasQuarterState = hasQuarterState(self)
        self.soldState = soldState(self)
        self.count = numberOfGumballs
        self.state = self.soldOutState
        self.winnerState = winnerState(self)
        if self.count > 0:
            self.state = self.noQuarterState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def releaseBall(self):
        print("A gumball comes rolling out the slot...")  
        if self.count != 0:
            self.count -= 1

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getSoldOutState(self):
        return self.soldOutState

    def getCount(self):
        return self.count


class State:
    def __init__(self, gumballMachine: GumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        pass

    def ejectQuarter(self):
        pass

    def turnCrank(self):
        pass
    
    def dispense(self):
        pass


class SoldState(State):
    def __init__(self, gumballMachine: GumballMachine):
        super().__init__(gumballMachine)

    def insertQuarter(self):
        print("Please wait, we're already giving you a gumball.")

    def ejectQuarter(self):
        print("Sorry, you already turned the crank")

    def turnCrank(self):
        print("Turning twice doesn't get you another gummball")

    def dispense(self):
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("Oops, out of gumballs!")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())



class NoQuarterState(State):
    def __init__(self, gumballMachine: GumballMachine):
        super().__init__(gumballMachine)

    def insertQuarter(self):
        print("You inserted a quarter")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")


class HasQuarterState(State):
    def __init__(self, gumballMachine: GumballMachine):
        super().__init__(gumballMachine)

    def insertQuarter(self):
        print("You can't insert another quarter")

    def ejectQuarter(self):
        print("Quarter returned")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("You turned...")
        winner = random.randint(0, 10)
        self.gumballMachine.releaseBall()
        if winner == 5 and self.gumballMachine.getCount() > 1:
            self.gumballMachine.setState(self.gumballMachine.getwinnerState())
        else:
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("No gumball dispensed")


class SoldOutState(State):
    def __init__(self, gumballMachine: GumballMachine):
        super().__init__(gumballMachine)

    def insertQuarter(self):
        print("Please wait, we're currently out of gumballs.")

    def ejectQuarter(self):
        print("No quarter available")

    def turnCrank(self):
        print("Please wait, we're currently out of gumballs.")

    def dispense(self):
        print("Please wait, we're currently out of gumballs.")


class WinnerState(State):
    def __init__(self, gumballMachine: GumballMachine):
        super().__init__(gumballMachine)

    def insertQuarter(self):
        print("Error inserting quarter")

    def ejectQuarter(self):
        print("Error ejecting quarter")

    def turnCrank(self):
        print("Error turning crank")

    def dispense(self):
        print("You're a winner, you get 2 gumballs for your current quarter")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())


gumballMachine = GumballMachine(SoldOutState, NoQuarterState, HasQuarterState, SoldState, WinnerState, 5)

gumballMachine.insertQuarter()
gumballMachine.turnCrank()
gumballMachine.turnCrank()

print(gumballMachine.getCount())
print(gumballMachine.getState())
