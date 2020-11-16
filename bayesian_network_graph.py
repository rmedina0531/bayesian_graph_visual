import numpy as np

class State_Data:
    def __init__(state, choices):
        self.name = state.name
        self.choices = choices
        self.state = state
    def get_choices():
        return self.choices
    
    def get_state():
        return self.state
        
    def get_name():
        return self.name

class Bayesian_graph(BayesianNetwork):
    def __init__(title):
        self.state_data = []
        super().__init__(title)
        
    def add_states(*args):
        states = []
        for x in args:
            self.state_data.append(x)
            states.append(x.get_state())
        super().add_states(*states)
        
    def get_data(network, beliefs):
        labels = []
        data = []
        for state, belief in zip(network.states, beliefs):
            if type(belief) != type("srt"):
                labels.append(state.name)
                label_data = []
                for p in belief.parameters[0]:
                    label_data.append(belief.parameters[0][p])
                data.append(label_data)
        
        data = list(zip(*data))
        data2 = []
        for d in data:
            data2.append(list(d))
            
        return [labels, data2]
        
    def show_data
        
        bars = []
        ##first bar
        bars.append(np.arrange(len(labels))
        ##add the rest if they exists
        for i in range(1, len(data)):
            bars.append([j+w for j in bars[i-1])
        
        
        x = np.arange(len(labels))
        width = 0.25
        
        fig, ax = plt.subplots()
        rects = []
        for i in labels:
            ax.bar(x - width, data[0], width, label=temp[0])
        
        
    #def show_data(network, beliefs):
        #labels = []
        #data = []
        #for state, belief in zip(network.states, beliefs):
            #if type(belief) != type("srt"):
                #labels.append(state.name)
                #label_data = []
                #for p in belief.parameters[0]:
                    #label_data.append(belief.parameters[0][p])
                #data.append(label_data)
        
        #data = list(zip(*data))
        #data2 = []
        #for d in data:
            #data2.append(list(d))
        
        
        #x = np.arange(len(labels))
        #width = 0.25
        
        #fig, ax = plt.subplots()
        #rects = []
        #for i in labels:
            #ax.bar(x - width, data[0], width, label=temp[0])
        
        #rects1 = ax.bar(x - width, data[0], width, label=temp[0])
        #rects2 = ax.bar(x, data[1], width, label=temp[1])
        #rects3 = ax.bar(x + width, data[2], width, label=temp[2])
        
        #rects = []
        #for i in range(len(temp)):
            #rects.append(ax.bar(x - width/2, data[i], width, label=temp[i]))
            
        #ax.set_ylabel('Scores')
        #ax.set_title('Scores by Door Probabilities')
        #ax.set_xticks(x)
        #ax.set_xticklabels(labels)
        #ax.legend()
            
        #def autolabel(rects):
            #"""Attach a text label above each bar in *rects*, displaying its height."""
            #for rect in rects:
                #height = rect.get_height()
                #ax.annotate('{}'.format(height),
                            #xy=(rect.get_x() + rect.get_width() / 2, height),
                            #xytext=(0, 3),  # 3 points vertical offset
                            #textcoords="offset points",
                            #ha='center', va='bottom')
            
        #for rect in rects:
            #autolabel(rect)
            
        #fig.tight_layout()
        #plt.show()
    
