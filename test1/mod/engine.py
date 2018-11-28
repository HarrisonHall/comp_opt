# engine.py by Harrison Hall

class engine:
    def __init__(self,n,vel_e,s_i,max_t):
        self.name = n
        self.exhaust_velocity = vel_e #km/s
        self.specific_impulse = s_i #sec 
        self.max_thrust = max_t #mN
