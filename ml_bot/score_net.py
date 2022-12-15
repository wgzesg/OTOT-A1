import torch
import torch.nn as nn
import torch.nn.functional as F

class ScoreNet(nn.Module):
    """
    input: state and action
    output: opponent type vector
    """
    def __init__(self):
        super(ScoreNet, self).__init__()

        # self.fc1 = nn.Linear(20, 20)
        self.fc2 = nn.Linear(20, 10)
        self.fc3 = nn.Linear(10, 10) 

    def forward(self, s):
        # s: state   a: action  o: opponent
        s = s.view(-1,20)                # batch_size x 1 x  x 
        # s= self.fc1(s)
        s = torch.sign(self.fc2(s))
        s = F.relu(s)
        o = self.fc3(s)
        return o


# make dataset
import csv

def calcScore(a, b):
    score = []
    for i in range(len(a)):
        if a[i] > b[i]:
            score.append(i+1)
        elif a[i] == b[i]:
            score.append(0.5*(i+1))
        else:
            score.append(0)
    return score

def makeDataset():
    # read data
    with open('data/riddler-castles/castle-solutions.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        header = data[0]
        data = data[1:]

    for i in range(len(data)):
        data[i] = data[i][:10]
        data[i] = [int(x) for x in data[i]]

    # make dataset
    dataset = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            score = calcScore(data[i], data[j])
            full_values = data[i] + data[j] + score
            dataset.append(full_values)

    # save to csv
    with open('data/battles.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'score1', 'score2', 'score3', 'score4', 'score5', 'score6', 'score7', 'score8', 'score9', 'score10'])
        writer.writerows(dataset)

# makeDataset()

# train
inputs = csv.reader(open('data/battles.csv', 'r'))
header = next(inputs)
inputs = [[float(i) for i in x] for x in inputs]

x = torch.tensor([i[:20] for i in inputs], dtype=torch.float)
print(x.shape)
y = torch.tensor([i[20:] for i in inputs], dtype=torch.float)
y = y.view(-1,10)
print(y.shape)
print(y[0])

model = ScoreNet()

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, gamma=0.9, step_size=100)

for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(x/100)
    print(outputs[0])
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    scheduler.step()
    if epoch % 10 == 0:
        print(epoch, loss.item())

