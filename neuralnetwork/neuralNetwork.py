import numpy 
from scipy.special import expit
import pandas as pd

class neuralNetwork:

    #신경망 초기화하기
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate, path = None):
        #입력, 은닉, 출력 계층의 노드 개수 설정
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        #학습률
        self.lr = learningrate

        #가중치 행렬 
        if(path != None) :
            self.load_weight(path)
        else:
            self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
            self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        #활성화 함수로 시그모이드 함수 설정
        self.activation_function = lambda x: expit(x)

        pass

    def load_weight(self, path):
        self.wih = pd.read_csv(path + "_wih.csv", header=None)
        self.who = pd.read_csv(path + "_who.csv", header=None)
    
    def save_weight(self, path):
        pd.DataFrame(self.wih).to_csv(path+ "_wih.csv", index = False, header= None)
        pd.DataFrame(self.who).to_csv(path+ "_who.csv", index = False, header= None)

    #신경망 학습시키기
    def train(self, inputs_list, targets_list):
        #입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T 

        #은닉계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        #은닉계층에서 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        #최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        #최종 출력 계층으로 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        #2단계 가중치 업데이트
        #출력계층의 오차(실제값 - 계산값)
        output_errors = targets - final_outputs
        #은닉계층의 오차는 가중치 값의 비례로 재조정
        hidden_errors = numpy.dot(self.who.T, output_errors)

        #은닉계층과 출력계층간의 가중치 업데이트 
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))

        
        
    #신경망에 질의하기
    def query(self, inputs_list):
        #입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T
        
        #은닉계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        #은닉계층에서 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        #최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)

        #최종 출력 계층으로 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        return final_outputs
        
if __name__ == "__main__":
    #입력, 은닉, 출력 노드의 수
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3

    #학습률은 0.3으로 정의
    learning_rate = 0.3
    #신경망의 인스턴스를 생성
    n = neuralNetwork(input_nodes, hidden_nodes,output_nodes, learning_rate)

    print("n.query = ", n.query([1.0, 0.5, -1.5]))
