import numpy as np
import matplotlib.pyplot as plt
from pomegranate import *

##state cointainer used for storing the possible choices of the state
#Used for graphing purposes
#takes a state and a list of choices for the state
class State_Data:
    def __init__(self, state, choices):
        self.name = state.name
        self.choices = choices
        self.state = state
    def get_choices(self):
        return self.choices
    
    def get_state(self):
        return self.state
        
    def get_name(self):
        return self.name

#extends the BayesianNetwork class by adding a list of references to the new
#state data class, for use in graphing
class Bayesian_graph(BayesianNetwork):
    def __init__(self, title):
        self.state_data = {}
        super().__init__(title)
        
        
    #overrides the add_states method from the superclass
    #adds the state_Data objects to the dictionary in the class
    #while stripping the state object inside them to pass it to 
    #the super add_state method
    def add_states(self, *args):
        states = []
        for x in args:
            self.state_data[x.get_name()] = x
            states.append(x.get_state())
        super().add_states(*states)
        
    #strips the state from insied the state data class to pass
    #to the super add_edge method from the superclass
    def add_edge(self, *args):
        states = []
        for x in args:
            states.append(x.get_state())
        super().add_edge(*states)
        
    #returns the labels of the belief states as well as the percentages of each
    #possible choices
    def get_data(self, beliefs):
        labels = []
        data = []
        for state, belief in zip(self.states, beliefs):
            if type(belief) != type("srt"):
                labels.append(state.name)
                label_data = []
                for p in belief.parameters[0]:
                    label_data.append(belief.parameters[0][p])
                data.append(label_data)
        
        #data = list(zip(*data))
        #data2 = []
        #for d in data:
            #data2.append(list(d))
            
        return [labels, data]
        
        
    #uses the netowrk and the belifs calculated to project a pie chart
    #of all the states not being ovserved and the percentages of their
    # possibilities
    #Dynamically generated to function with any Bayesian network
    def show_data(self, beliefs):
        data = self.get_data(beliefs)
        labels = data[0]
        elements = data[1]
    
        fig, axs = plt.subplots(len(labels))
        
        if len(labels) > 1:
        
            for i in range(len(labels)):
                element_labels = self.state_data[labels[i]].get_choices()
                axs[i].pie(elements[i], labels=element_labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                axs[i].axis('equal')
                axs[i].set_title(labels[i])
        
        else:
            element_labels = self.state_data[labels[0]].get_choices()
            axs.pie(elements[0], labels=element_labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            axs.axis('equal')
            axs.set_title(labels[0])
        
        
        plt.show()
        
        
        

    
