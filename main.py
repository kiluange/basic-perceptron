class Node(object):
    """ O tempo está bom?
    Seu namorado ou namorada quer acompanhá-lo(a)?
    O festival está perto de transporte público? (Você não possui um carro) """

    inputs = [0,0,1]
    weight = [0.4,-0.6,0.6]
    bias = 0.5
    threshold = 0
    step = 0.4
    expected = -1

    def __init__(self):
        self.learn()
        pass

    def activation(self,u):
        return -1 if u < self.threshold else 1

    def learn(self):
        u = 0

        print(self.weight)
        print(u)
        print(self.bias)
        print(self.activation(u))

        for i in range(len(self.inputs)):
            u += ((self.inputs[i] * self.weight[i]))
        u += self.bias

        if self.activation(u) != self.expected:
            for i in range(len(self.weight)):
                self.weight[i] = self.weight[i] + (self.step * self.inputs[i]) * (self.expected - self.activation(u))
            self.bias = self.bias + (self.step * (self.expected - self.activation(u)))
            self.learn()
        else:
            print('RESULT')
            print(self.weight)
            print(u)
            print(self.bias)
            print(self.activation(u))

Node()