class Univariate():
    
    def quanQual(self,dataset):
        Quan=[]
        Qual=[]
        for row in dataset.columns:
            if(dataset[row].dtype=='O'):
                Quan.append(row)
            else:
                Qual.append(row)
        return Quan,Qual