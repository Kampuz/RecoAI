import numpy as np
import graph as gp

def main():
    input_nodes = 2 # number of input nodes
    output_nodes = 2 # number of output nodes
    hidden_nodes = 3 # number of intermediate nodes

    batch_size = 8 # sample size
    
    input_data = np.random.randn(batch_size, input_nodes) # data inputed in the system
    output_data = np.random.randn(batch_size, output_nodes)
    
    weights_matrix = np.random.randn(input_nodes, hidden_nodes) # weights of the matrix
    weights_matrix_2 = np.random.randn(hidden_nodes, output_nodes) # weights of the matrix
    
    hidden_values = input_data.dot(weights_matrix) # take the dot product of the matrix input_data e weight_values
    
    # rectified linear unit: remove negatives values and replace with 0
    
    hidden_without_negatives = np.maximum(hidden_values, 0) # hidden node computation
    output_data_predictions = hidden_without_negatives.dot(weights_matrix_2) # 
    
    loss_matrix = np.square(output_data_predictions - output_data)
    loss_sum = loss_matrix.sum()

    output_prediction_gradient =
    
    print(input_data)
    print("\n\n")
    print(weights_matrix)
    print("\n\n")
    print(hidden_values)
    print("\n\n")
    print(hidden_without_negatives)
    print("\n\n")
    print(output_data_predictions)
    print("\n\n")
    print(loss_matrix)
    print("\n\n")
    print(loss_sum)

if __name__ == "__main__":
    main()
