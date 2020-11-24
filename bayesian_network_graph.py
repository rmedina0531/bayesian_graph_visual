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
        
    def make_plot_grid(self, num_of_plots):
        possible_grid_sizes = [2,3,4,6,9]
        grids = {2:[1,2], 3:[1,3], 4:[2,2], 6:[2,3], 9:[3,3]}
        grids[5] = grids[6]
        for i in range(7,10):
            grids[i] = grids[9]
            
        return grids[num_of_plots]

    
    
    #uses the netowrk and the belifs calculated to project a pie chart
    #of all the states not being ovserved and the percentages of their
    # possibilities
    #Dynamically generated to function with any Bayesian network
    def show_data(self, beliefs):
        data = self.get_data(beliefs)
    	
		#the following is set up for displaying the graphs
        
		#pulls label names for the graphs
        if len(data) > 1:
            grid = self.make_plot_grid(len(data))
            fig, axs = plt.subplots(grid[0], grid[1])
            fig.canvas.set_window_title('Probabilities')
            #print(axs)
            #print(type(fig))
            #print(type(axs))
            #fig.tight_layout(pad=1.5)
			#adds the data to the appropriate graph per element in the data array
            row = 0
            col = 0
            for i in range((grid[0]*grid[1])):
                #make blank
                if i >= len(data):
                    print('turned off')
                    axs[row,col].axis('off')
                    col += 1
                    if col % grid[1] == 0:
                        col = 0
                        row += 1
                else:
                    graph_name = data[i][0]
                    element_labels = [x[0] for x in data[i][1:]]
                    graph_data = [x[1] for x in data[i][1:]]
                    
                    if grid[0] > 1:
                        axs[row,col].pie(graph_data, labels=element_labels, autopct='%1.1f%%',
                                shadow=True, startangle=90)
                        axs[row,col].axis('equal')
                        axs[row,col].set_title(graph_name)
                        
                        col += 1
                        if col % grid[1] == 0:
                            col = 0
                            row += 1
                    else:
                        axs[col].pie(graph_data, labels=element_labels, autopct='%1.1f%%',
                                shadow=True, startangle=90)
                        axs[col].axis('equal')
                        axs[col].set_title(graph_name)
                        col += 1
        
        else:
			#run only when there is one graph to display
            fig, axs = plt.subplots()
            fig.canvas.set_window_title('Probabilities')
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
        
        
        

    
