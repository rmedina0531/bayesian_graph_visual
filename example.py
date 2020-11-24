from bayesian_network_graph import Bayesian_graph
from pomegranate import *

def main():
    cloudy_table = DiscreteDistribution({'True':0.5, 'False':0.5})
    sprinkler_table = ConditionalProbabilityTable(
        [['False', 'False', 0.5],
         ['False', 'True', 0.5],
         ['True', 'False', 0.9],
         ['True', 'True', 0.1]], [cloudy_table])
    rain_table = ConditionalProbabilityTable(
        [['False', 'False', 0.8],
         ['False', 'True', 0.2],
         ['True', 'False', 0.2],
         ['True', 'True', 0.8]], [cloudy_table])
    wet_grass_table = ConditionalProbabilityTable(
        [['False', 'False', 'False', 1.0],
         ['False', 'False', 'True', 0],
         ['True', 'False', 'False', 0.1],
         ['True', 'False', 'True', 0.9],
         ['False', 'True', 'False', 0.1],
         ['False', 'True', 'True', 0.9],
         ['True', 'True', 'False', 0.01],
         ['True', 'True', 'True', 0.99]], [sprinkler_table, rain_table])
    
    state1 = State(cloudy_table, name='cloudy')
    state2 = State(sprinkler_table, name='sprinkler')
    state3 = State(rain_table, name='rain')
    state4 = State(wet_grass_table, name='wet grass')
    
    network = Bayesian_graph('Wet grass Example')
    network.add_states(state1, state2, state3, state4)
    network.add_edge(state1, state2)
    network.add_edge(state1, state3)
    network.add_edge(state2, state4)
    network.add_edge(state3, state4)
    network.bake()
    
    beliefs = network.predict_proba({'wet grass':'True'})
    print(beliefs)
    network.show_data(beliefs)


    beliefs = network.predict_proba({'wet grass':'True', 'rain':'True'})
    print(network.get_data(beliefs))
    network.show_data(beliefs)
     

if __name__ == '__main__':
    main()
