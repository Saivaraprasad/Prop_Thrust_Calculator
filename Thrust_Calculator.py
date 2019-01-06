import matplotlib

Constant1 = 4.392399 * pow(10,-8)
Constant2 = 4.2333 * pow(10,-4)

Motor_KV = 1000
Battery_Voltage = 11.5

#ropeller Parameters  in Inches
Diameter = 10
Pitch    = 4.5


Air_Stream_Velocity = 0  # For static Thrust


#Convert inches to SI unit
Diameter = Diameter * 0.0254
Pitch    = Pitch    * 0.0254

RPM = Motor_KV * Battery_Voltage
Thrust = ((Constant1 * RPM *pow(Diameter,3.5))/pow(Pitch,0.5)) * (Constant2 * RPM * Pitch - Air_Stream_Velocity)
