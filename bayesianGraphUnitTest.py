import unittest
from pomegranate import *
from bayesian_network_graph import Bayesian_graph

def generate_test_network():
	#generate bayesian network to test
	#Test case is implementation of the monty hall problem
	#A, B, C are doors
	#guest_door is the door selected by the guest
	#prize_door is the door that contains the prize
	#monty_door is the door revealed based on the guest_door and monty_door

	#since the guest door and discrete door are independent, a discrete distrubution
	#table is set up for them with the probabilities of each option
    guest_door = DiscreteDistribution({'A':1.0/3, 'B':1.0/3, 'C':1.0/3})
    prize_door = DiscreteDistribution({'A':1.0/3, 'B':1.0/3, 'C':1.0/3})

	#monty door is based on the guest_door and prize_door so a
	#conditional probabilitie table is set up
	#the format is the following
	#[x,y,z,p] where [x,y] are based on the definitions at the end of the table
	#z is the choice possible of the current node
	#and p is the probability of that particular outcome
    monty_door = ConditionalProbabilityTable(
        [[ 'A', 'A', 'A', 0.0],
        [ 'A', 'A', 'B', 0.5],
        [ 'A', 'A', 'C', 0.5],
        [ 'A', 'B', 'A', 0.0],
        [ 'A', 'B', 'B', 0.0],
        [ 'A', 'B', 'C', 1.0],
        [ 'A', 'C', 'A', 0.0],
        [ 'A', 'C', 'B', 1.0],
        [ 'A', 'C', 'C', 0.0],
        [ 'B', 'A', 'A', 0.0],
        [ 'B', 'A', 'B', 0.0],
        [ 'B', 'A', 'C', 1.0],
        [ 'B', 'B', 'A', 0.5],
        [ 'B', 'B', 'B', 0.0],
        [ 'B', 'B', 'C', 0.5],
        [ 'B', 'C', 'A', 1.0],
        [ 'B', 'C', 'B', 0.0],
        [ 'B', 'C', 'C', 0.0],
        [ 'C', 'A', 'A', 0.0],
        [ 'C', 'A', 'B', 1.0],
        [ 'C', 'A', 'C', 0.0],
        [ 'C', 'B', 'A', 1.0],
        [ 'C', 'B', 'B', 0.0],
        [ 'C', 'B', 'C', 0.0],
        [ 'C', 'C', 'A', 0.5],
        [ 'C', 'C', 'B', 0.5],
        [ 'C', 'C', 'C', 0.0]], [guest_door, prize_door])
        
    #s1 = State( guest_door, name='guest')
    #s2 = State( prize_door, name='prize')
    #s3 = State( monty_door, name='monty')
    
	#definitions of states are using the new state_data, used for storing the
	#choices for use in future graphing

    state1 = State( guest_door, name='guest')
    state2 = State( prize_door, name='prize')
    state3 = State( monty_door, name='monty')
    network = Bayesian_graph( "Monty Hall Problem" )
    network.add_states(state1, state2, state3)
    network.add_edge(state1, state3)
    network.add_edge(state2, state3)
    network.bake()
    return network

def generate_test_network2():
	#similar to above, generates another test network
    exam_level = DiscreteDistribution({'Difficult':0.7, 'Easy':0.3})
    iq_level = DiscreteDistribution({'High':0.8, 'Low':0.2})

    marks = ConditionalProbabilityTable(
        [['High', 'Difficult', 'High', 0.6],
        ['High', 'Difficult', 'Low', 0.4],
        ['High', 'Easy', 'High', 0.9],
        ['High', 'Easy', 'Low', 0.1],
        ['Low', 'Difficult', 'High', 0.5],
        ['Low', 'Difficult', 'Low', 0.5],
        ['Low', 'Easy', 'High', 0.8],
        ['Low', 'Easy', 'Low', 0.2]], [iq_level, exam_level])

    apt_score = ConditionalProbabilityTable(
        [['High', 'High', 0.75],
        ['High', 'Low', 0.25],
        ['Low', 'High', 0.4],
        ['Low', 'Low', 0.6]], [iq_level])

    admission = ConditionalProbabilityTable(
        [['High', 'True', 0.6],
        ['High', 'False', 0.4],
        ['Low', 'True', 0.9],
        ['Low', 'False', 0.1]], [marks])
        
    exam_level_state = State( exam_level, name='exam_level')
    iq_level_state = State( iq_level, name='iq_level')
    marks_state = State( marks, name='marks')
    apt_score_state = State( apt_score, name='apt_score')
    admission_state = State( admission, name='admission')
    
    network = Bayesian_graph( "Admissions Chances" )
    network.add_states(exam_level_state, iq_level_state, 
                    marks_state, apt_score_state, admission_state)
    network.add_edge(exam_level_state, marks_state)
    network.add_edge(iq_level_state, marks_state)
    network.add_edge(iq_level_state, apt_score_state)
    network.add_edge(marks_state, admission_state)
    network.bake()
    
    return network

class TestGraphMethods(unittest.TestCase):
    
    
	##checks that the network_get_data() returns the appropriate data points
	##from the JSON jenerated buy the superclass
    def test_get_data_length(self):
        network = generate_test_network()
        beliefs = network.predict_proba({'guest': 'A'})
        data = network.get_data(beliefs)
        #print(data)
        self.assertEqual(len(data), len(network.states))
    
	#check that all the corrects states are being outputted in
	#the appropriate place in the list
    def test_get_data_length2(self):
        network = generate_test_network()
        beliefs = network.predict_proba({'guest': 'A'})
        data = network.get_data(beliefs)
        valid_states = ['prize', 'monty', 'guest']
        for element in data:
            self.assertIn(element[0], valid_states)
        
        
	#check that all beliefs are the correct data
    #def test_graph(self):
        #network = generate_test_network()
        #beliefs = network.predict_proba({'guest': 'A'})
        #data = network.get_data(beliefs)
        #correct_values = {'monty': 
                              #['monty', ['A', 0.0], ['B',0.49999999999999994], ['C', 0.49999999999999994]], 
                          #'guest':
                              #['guest', ['A', 1]],
                          #'prize':
                            #['prize', ['A', 0.3333333333333333], ['B', 0.3333333333333333], ['C', 0.3333333333333333]]}

        #for d in data:
            #for element in d:
                #self.assertIn(element, correct_values[d[0]])
        #network.show_data(beliefs)
        
	#runs code to display the graph to check functionality of
	#the visual representation
    def test_graph2(self):
        network = generate_test_network()
        beliefs = network.predict_proba({'guest': 'A'})
        network2 = generate_test_network2()
        beliefs2 = network2.predict_proba({'admission': 'True'})
        #print(network.get_data(beliefs))
        network.show_data(beliefs)
        network2.show_data(beliefs2)
        
    
if __name__== '__main__':
    unittest.main()
