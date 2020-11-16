import numpy as np
import matplotlib.pyplot as plt
from pomegranate import *
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

class Bayesian_graph(BayesianNetwork):
    def __init__(self, title):
        self.state_data = {}
        super().__init__(title)
        
    def add_states(self, *args):
        states = []
        for x in args:
            self.state_data[x.get_name()] = x
            states.append(x.get_state())
        super().add_states(*states)
        
    def add_edge(self, *args):
        states = []
        for x in args:
            states.append(x.get_state())
        super().add_edge(*states)
        
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
        
        
        

    
