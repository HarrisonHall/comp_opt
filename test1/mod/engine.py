# engine.py by Harrison Hall

class engine:
    name = ""
    specific_impulse = 0 #sec
    max_thrust = 0 #mN
    exhaust_velocity = 0 #km/s
    def __init__(self,n,vel_e,s_i,max_t):
        self.name = n
        self.exhaust_velocity = vel_e
        self.specific_impulse = s_i        
        self.max_thrust = max_t
