from mrjob.job import MRJob
from mrjob.step import MRStep

class AverageSalary(MRJob):
    def mapper(self,_,line):
        idemp, sececon, salary, year = line.split(',')
        yield (f"avg-salary-per-idemp({idemp}): "), float(salary)
        yield (f"avg-salary-per-sececon({sececon}): "), float(salary)
        yield (f"idemp-per-sececon(id:{idemp}): "), sececon

    def reducer(self, key, values):
        if key.startswith("avg"):
            total = 0
            count = 0
            for value in values:
                total += value
                count += 1
            yield key, total/count
        else:
            pastsec = set()
            count = 0
            for value in values:
                if value not in pastsec:
                    pastsec.add(value)
                    count += 1
            yield key, count


    def steps(self):
        return[
            MRStep(mapper=self.mapper, reducer=self.reducer),
        ]
    
if __name__ == "__main__":
    AverageSalary.run()