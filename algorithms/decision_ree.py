#-*- coding:utf-8 -*-
#author:tinnarey@qq.com

from math import  log

class DecsionTree:
    trainData = []
    trainLable = []
    featureValues = {}
    def __init__(self,trainData, trainLable, threshold):
        self.loadData(trainData, trainLable)
        self.threshold = threshold
        self.tree = self.createTree(range(0,len(trainLable)),range(0,len(trainData[0])))

    def loadData(self,trainData,trainLable):
        if len(trainData) != len(trainLable):
            raise ValueError('input error')
        self.trainData = trainData
        self.trainLable = trainLable

        for data in trainData:
            for index,value in enumerate(data):
                if not index in self.featureValues.keys():
                    self.featureValues[index] = [value]
                if not value in self.featureValues[index]:
                    self.featureValues[index].append(value)
        # print(self.featureValues) featurevalues 指的是每种特征包含的特征指标

    #信息熵
    def caculateEntropy(self,dataset):
        labelCount = self.labelCount(dataset)
        size = len(dataset)
        result = 0
        for i in labelCount.values():
            pi = i / float(size) #第i类样本所占比例
            result -= pi*(log(pi)/log(2))
        return result

    #信息增益
    def caculateGain(self,dataset, feature):
        values = self.featureValues[feature]
        result = 0
        for value in values:
            subDataset = self.splitDataset(dataset=dataset,feature=feature,value = value) #
            result += len(subDataset) /float(len(dataset))*self.caculateEntropy(subDataset)
        return self.caculateEntropy(dataset=dataset) - result

    def labelCount(self,dataset):
        lableCount = {}
        for i in dataset:
            if self.trainLable[i] in lableCount.keys():
                lableCount[self.trainLable[i]] +=1
            else:
                lableCount[self.trainLable[i]] = 1

        return lableCount

    def splitDataset(self,dataset, feature, value):
        result = []
        for index in dataset:
            if self.trainData[index][feature] == value:
                result.append(index)
        return result

    def createTree(self,dataset, features):
        labelCount = self.labelCount(dataset)

        #若特征集为空，则该树为单节点数
        #计算数据集中出现次数最多的标签

        if not features:
            return max(list(labelCount.items()),key= lambda x:x[1])[0]

        #如果数据集中只包含同一标签，则该树为单节点树
        if len(labelCount) == 1:
            return list(labelCount.keys())[0]

        #计算特征集中每个特征的信息增益
        l = map(lambda x : [x,self.caculateGain(dataset=dataset,feature=x)], features)

        #选取信息增益最大的特征
        feature ,gain = max(l, key=lambda x:x[1])

        #如果最大信息增益小于阈值，则该树为单节点树
        if self.threshold >gain:
            return max(list(labelCount.items()),key=lambda x:x[1])[0]

        tree = {}
        #选取特征子集
        subFeatures = filter(lambda x:x!=feature,features)
        tree['feature'] = feature

        #构建子树
        for value in self.featureValues[feature]:
            subDataset = self.splitDataset(dataset,feature,value)
            #保证子数据集非空
            if not subDataset:
                continue
            tree[value] = self.createTree(dataset= subDataset,features=subFeatures)

        return tree

    def classify(self,data):
        def f(tree,data):
            if type(tree) != dict:
                return tree
            else:
                return f(tree[data[tree['feature']]], data)
        return f(self.tree, data)

if __name__ == '__main__':
    trainData = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 2],
        [1, 0, 1, 2],
        [2, 0, 1, 2],
        [2, 0, 1, 1],
        [2, 1, 0, 1],
        [2, 1, 0, 2],
        [2, 0, 0, 0],]

    trainLabel = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
    tree = DecsionTree(trainData, trainLabel, threshold=0.1)
    assert len(trainLabel) >= 0
    print(tree.tree)

