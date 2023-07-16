from abc import ABC, abstractmethod

class InvalidOperationErro(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise InvalidOperationErro("Data stream is already opened")
        self.opened=True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationErro("Data stream is already closed")
        
        self.opened=False
           
    @abstractmethod           
    def read():
        pass 
            
# class NetworkStream(Stream):
#     def read():
#         print("network data")        

      
# class FieStream(Stream):
#     def read():
#         print("file data")        


st = Stream.read()