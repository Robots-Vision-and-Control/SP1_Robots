class PID_Controller:

    def __init__(self, kp, ki, kd, T, tau, limitMax, limitMin, limit_max_int, limit_min_int):
        self.integral_error = None
        self.derivative_error = None

        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integrator = None
        self.T = T  # TODO figure this out
        self.prevError = None
        self.limitMax = limitMax
        self.limitMin = limitMin
        self.differentiator = None
        self.prevMeasurement = None
        self.tau = tau  # TODO figure this out
        self.output = None
        self.limit_max_int = limit_max_int
        self.limit_min_int = limit_min_int

    def controller_init(self):  # TODO All Good
        self.integrator = 0
        self.prevError = 0
        self.differentiator = 0
        self.prevMeasurement = 0
        self.output = 0
        # New junk
        self.integral_error = 0
        self.derivative_error = 0

    def controller_Update(self, set_point, measurement):  # setpoint is
        # Error
        error = set_point - measurement

        # Proportional
        proportional = self.kp * error

        # Integral
        self.integrator = self.integrator + 0.5 * self.ki * self.T * (error + self.prevError)

        # anti-windup for the integrator clamping
        if self.integrator > self.limit_max_int:
            self.integrator = self.limit_max_int
        elif self.integrator < self.limit_min_int:
            self.integrator = self.limit_min_int

        # Derivative (Band_limited)
        self.differentiator = -(2 + self.kd * (measurement - self.prevMeasurement) + (2 * self.tau - self.T) * self.differentiator) / (2 * self.tau + self.T)

        # Calc output
        self.output = proportional + self.integrator + self.differentiator

        # limit controller output
        if self.output > self.limitMax:
            self.output = self.limitMax
        elif self.output < self.limitMin:
            self.output = self.limitMin

        # Store error and measurements for the next loop
        self.prevError = error
        self.prevMeasurement = measurement

        return self.output

    def compute(self, set_point, measurement):
        error = set_point - measurement
        self.integral_error += error * self.T
        self.derivative_error = (error - self.prevError) / self.T
        self.prevError = error
        self.output = self.kp * error + self.ki * self.integral_error + self.kd * self.derivative_error
        return self.output
