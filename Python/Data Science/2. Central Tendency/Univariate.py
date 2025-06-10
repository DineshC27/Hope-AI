class Univariate():
    
    def quanQual(dataset):
        Quan=[]
        Qual=[]
        for row in dataset.columns:
            if(dataset[row].dtype=='O'):
                Qual.append(row)
            else:
                Quan.append(row)
        return Quan,Qual