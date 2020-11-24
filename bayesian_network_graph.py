#dependencies
#cython 0.29.21
#pomegranate 0.13.2

import numpy as np
import matplotlib.pyplot as plt
from pomegranate import *

#extends the BayesianNetwork class by adding a list of references to the new
#state data class, for use in graphing
class Bayesian_graph(BayesianNetwork):

    #returns the labels of the belief states as well as the percentages of each
    #possible choices
    def get_data(self, beliefs):
        data = []
        #print(len(self.states))
        #print(len(beliefs))
        for state, belief in zip(self.states, beliefs):
            try:
            #if type(belief) != type("srt"):
                data_element = []
                data_element.append(state.name)
                for p in belief.parameters[0]:
                    data_point = [p,belief.parameters[0][p]]
                    data_element.append(data_point)
                data.append(data_element)
            except:
                data_element = []
                data_element.append(state.name)
                data_element.append([belief, 1])
                data.append(data_element)
        
        #data = list(zip(*data))
        #data2 = []
        #for d in data:
            #data2.append(list(d))
            
        return data
        
        
    #uses the netowrk and the belifs calculated to project a pie chart
    #of all the states not being ovserved and the percentages of their
    # possibilities
    #Dynamically generated to function with any Bayesian network
    def show_data(self, beliefs):
        data = self.get_data(beliefs)
    	
		#the following is set up for displaying the graphs
        fig, axs = plt.subplots(len(data))
        fig.tight_layout(pad=1.5)
        
		#pulls label names for the graphs
        if len(data) > 1:
        	
			#adds the data to the appropriate graph per element in the data array
            for i in range(len(data)):
                graph_name = data[i][0]
                element_labels = [x[0] for x in data[i][1:]]
                graph_data = [x[1] for x in data[i][1:]]
                
                axs[i].pie(graph_data, labels=element_labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                axs[i].axis('equal')
                axs[i].set_title(graph_name)
        
        else:
			#run only when there is one graph to display
            graph_name = data[0]
            element_labels = [x[0] for x in data[1:]]
            graph_data = [x[1] for x in data[1:]]
            
            axs.pie(graph_data, labels=element_labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            axs.axis('equal')
            axs.set_title(graph_name)
			
			
            #element_labels = self.state_data[labels[0]].get_choices()
            #axs.pie(elements[0], labels=element_labels, autopct='%1.1f%%',
                    #shadow=True, startangle=90)
            #axs.axis('equal')
            #axs.set_title(labels[0])
        
        
        plt.show()
        
        
        

    
