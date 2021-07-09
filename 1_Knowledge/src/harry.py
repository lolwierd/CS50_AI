from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited hagrid
dumbledore = Symbol("dumbledore") # Harry visited dumbledore


knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

# If it is not raining -> Harry visites hagrid
# Harry vists hagrid or dumbledore
# Harry does not visit hagrid and dumbledore
# Harry vists dumbledore

print(model_check(knowledge, rain))
