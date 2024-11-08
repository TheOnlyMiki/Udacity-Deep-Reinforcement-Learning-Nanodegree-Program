import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        
        # Fully connected layers
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)
        
        # Pooling layer
        #self.avgpool = nn.AvgPool1d(kernel_size=2)
        #self.maxpool = nn.MaxPool1d(kernel_size=2)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        
        x = F.relu(self.fc1(state))
        #x = self.avgpool(x)
        x = F.relu(self.fc2(x))
        #x = self.maxpool(x)
        #x = F.softmax(self.fc3(x), dim=1)
        x = self.fc3(x)
        #print(x)
        
        return x

class Dueling_QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(Dueling_QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        
        # Fully connected layers
        self.fc1 = nn.Linear(state_size, 64)
        
        self.fc_value = nn.Linear(64, 256)
        self.fc_action = nn.Linear(64, 256)
        
        self.fc_value_output = nn.Linear(256, 1)
        self.fc_action_output = nn.Linear(256, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        
        x = F.relu(self.fc1(state))
        
        x_value = F.relu(self.fc_value(x))
        x_action = F.relu(self.fc_action(x))
        
        x_value = self.fc_value_output(x_value)
        x_action = self.fc_action_output(x_action)
        
        avg_x_action = torch.mean(x_action, dim=1, keepdim=True)
        q_value = x_value + x_action - avg_x_action
        
        return q_value