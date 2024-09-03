class CRC:
    @classmethod
    def xor(self, a, b):
        x = ""
        for i in range(1, len(b)):
            if a[i] == b[i]:
                x += "0"
            else:
                x += "1"
        return x

    @classmethod
    def binaryDivision(self, divident, divisor):
        m = len(divisor)
        n = len(divident)
        temp = divident[0: m]

        while m < n:
            if temp[0] == '1':
                temp = self.xor(divisor, temp) + divident[m]
            else:
                temp = self.xor("0"*len(divisor), temp) + divident[m]
            m += 1
        if temp[0] == '1':
            temp = self.xor(divisor, temp)
        else:
            temp = self.xor("0"*len(divisor), temp)
        return temp

    @classmethod
    def generateCRC(self, data, poly):
        k = len(poly)
        ndata = data + "0"*(k - 1)
        rem = self.binaryDivision(ndata, poly)
        crc = data + rem
        return crc

    @classmethod
    def checkCRC(self, data, poly):
        rem = self.binaryDivision(data, poly)
        if rem == "0"*len(rem):
            return False
        return True
