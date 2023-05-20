from mrjob.job import MRJob
from mrjob.step import MRStep

class AverageSalary(MRJob):
    def mapper(self,_,line):
        company, price, date = line.split(',')
        yield (f"(Min-max)-day-({company}): "), (float(price), date)
        yield (f"Upward-stocks({company}): "), float(price)
        yield (f"Blackday: " ),

    def reducer(self, key, values):
        


    def steps(self):
        return[
            MRStep(mapper=self.mapper, reducer=self.reducer),
        ]
    
if __name__ == "__main__":
    AverageSalary.run()
