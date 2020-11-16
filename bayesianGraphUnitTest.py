import unittest
from pomegranate import *
from bayesian_network_graph import Bayesian_graph, State_Data

def generate_test_network():
    guest_door = DiscreteDistribution({'A':1.0/3, 'B':1.0/3, 'C':1.0/3})
    prize_door = DiscreteDistribution({'A':1.0/3, 'B':1.0/3, 'C':1.0/3})

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
    
    state1 = State_Data(State( guest_door, name='guest'), ['A', 'B', 'C'])
    state2 = State_Data(State( prize_door, name='prize'), ['A', 'B', 'C'])
    state3 = State_Data(State( monty_door, name='monty'), ['A', 'B', 'C'])

    network = Bayesian_graph( "Monty Hall Problem" )
    network.add_states(state1, state2, state3)
    network.add_edge(state1, state3)
    network.add_edge(state2, state3)
    network.bake()
    return network

class TestGraphMethods(unittest.TestCase):
    
    ##check to see if new class is working
    def test_extended_bayesian_graph(self):
        network = generate_test_network()
        self.assertEqual(len(network.state_data),  3) 
    
    def test_get_data_length(self):
        network = generate_test_network()
        beliefs = network.predict_proba({'guest': 'A'})
        data = network.get_data(beliefs)
        self.assertEqual(len(data), 2)
    
    def test_get_data_length2(self):
        network = generate_test_network()
        beliefs = network.predict_proba({'guest': 'A'})
        data = network.get_data(beliefs)
        #print(data)
        self.assertEqual(data[0][0], 'prize')
        self.assertEqual(data[0][1], 'monty')
        
        
    def test_graph(self):
        network = generate_test_network()
        beliefs = network.predict_proba({'guest': 'A'})
        print(network.get_data(beliefs))
        network.show_data(beliefs)
        
    
if __name__== '__main__':
    unittest.main()
