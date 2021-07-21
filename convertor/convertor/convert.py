class convert:

    def __init__(self):
        pass

    def bytes(self,values):
        values = values.split(' ')
        print('-------------------------')
        print(values)
        print('-------------------------')
        if 'B' == values[1]:
            return values[0]
        elif 'GB' == values[1]:
            values = int(values[0])*(2**30)
            return values
        elif 'MB' == values[1]:
            values = int(values[0])*(2**20)
            return values
        elif 'KB' == values[1]:
            values = int(values[0])*(2**10)
            return values
        else:
            return "Invalid values..."


    def gigabytes(self,byte_value):
        gb = byte_value/(2**30)
        return gb
    
    def megabytes(self,byte_value):
        mb = byte_value/(2**20)
        return mb

    def kilobytes(self,byte_value):
        kb = byte_value/(2**10)
        return kb

#convert = convert()
#byte_value = convert.bytes("1024 B")
#G = convert.gigabytes(byte_value)
#M = convert.megabytes(byte_value)
#K = convert.kilobytes(byte_value)
#print(str(G) + " GB")
#print(str(M) +" MB")
#print(str(K) +" KB")
#print(str(byte_value) + " B")

