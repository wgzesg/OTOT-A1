import torch
import torch.nn as nn
import torch.nn.functional as F

class AINet(nn.Module):
    """
    input: state and action
    output: opponent type vector
    """
    def __init__(self, scores, soldiers, max_step=-1):
        # game params
        self.max_step = max_step if max_step > 0 else 100
        self.num_of_castles = len(scores)
        self.state_height = self.max_step * self.num_of_castles
        self.state_width = self.game.max_step

        super(AINet, self).__init__()

        self.conv1_1 = nn.Conv2d(1, 4, kernel_size = (self.state_height, int(self.state_width/5))) #4*int(self.state_width/5)+1  # kernel size = (4, 2)
        self.conv2_1 = nn.Conv2d(1, 8, kernel_size = (self.state_height, 2*int(self.state_width/5))) #3*int(self.state_width/5)+1 # kernel size = (4, 4)
        self.conv3_1 = nn.Conv2d(1, 12, kernel_size = (self.state_height, 3*int(self.state_width/5))) #2*int(self.state_width/5)+1 # kernel size = (4, 6)
        self.conv4_1 = nn.Conv2d(1, 16, kernel_size = (self.state_height, 4*int(self.state_width/5))) #int(self.state_width/5)+1
        self.conv5_1 = nn.Conv2d(1, 20, kernel_size = (self.state_height, 5*int(self.state_width/5))) #1


       
        self.conv1_2 = nn.Conv2d(4, 1, kernel_size = (1, 1)) 
        self.conv2_2 = nn.Conv2d(8, 1, kernel_size = (1, 1)) 
        self.conv3_2 = nn.Conv2d(12, 1, kernel_size = (1, 1)) 
        self.conv4_2 = nn.Conv2d(16, 1, kernel_size = (1, 1)) 
        self.conv5_2 = nn.Conv2d(20, 1, kernel_size = (1, 1)) 
  

        self.fc1 = nn.Linear(10*int(self.state_width/5)+5+self.n_actions, 10*int(self.state_width/5)+5)
        self.fc2 = nn.Linear(10*int(self.state_width/5)+5, 10*int(self.state_width/5)+5)
        self.fc3 = nn.Linear(10*int(self.state_width/5)+5, numNurtureOppo) #numNurtureOppo is the number of rules to nurture the player
 

    def forward(self, s, a):
        # s: state   a: action  o: opponent
        s = s.view(-1, 1, self.state_height, self.state_width)                # batch_size x 1 x  x 
        s1 = F.relu(self.conv1_1(s))                          # batch_size x num_channels x  x 
        s1 = F.relu(self.conv1_2(s1))
        s1 = s1.view(-1, 4*int(self.state_width/5)+1)
        
        s2 = F.relu(self.conv2_1(s))                          # batch_size x num_channels x  x 
        s2 = F.relu(self.conv2_2(s2))
        s2 = s2.view(-1, 3*int(self.state_width/5)+1)
        
        s3 = F.relu(self.conv3_1(s))                         # batch_size x num_channels x  x 
        s3 = F.relu(self.conv3_2(s3))
        s3 = s3.view(-1, 2*int(self.state_width/5)+1)
        
        s4 = F.relu(self.conv4_1(s))                          # batch_size x num_channels x  x 
        s4 = F.relu(self.conv4_2(s4))
        s4 = s4.view(-1, int(self.state_width/5)+1)
        
        s5 = F.relu(self.conv5_1(s))                          # batch_size x  x  x 
        s5 = F.relu(self.conv5_2(s5))
        s5 = s5.view(-1, 1)
  

        a = a.view(-1, self.n_actions) 
        s = torch.cat((s1,s2,s3,s4,s5,a),1)        

        s = F.dropout(F.relu(self.fc1(s)), p=self.args_nn.dropout, training=self.training)  
        s = F.dropout(F.relu(self.fc2(s)), p=self.args_nn.dropout, training=self.training)  

        o = self.fc3(s) 
                                                                     # batch_size x action_size

        return F.log_softmax(o, dim=1)
