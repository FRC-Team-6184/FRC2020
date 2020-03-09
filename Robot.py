import wpilib

class MyRobot(wpilib.timedRobot,self):
    def robotInit(self):
        
        #drive define
        self.fL = wpilib.PWMTalonFX(0)
        self.fR = wpilib.PWMTalonFX(1)
        self.bL = wpilib.PWMTalonFX(2)
        self.bR = wpilib.PWMTalonFX(3)
        self.fLE = wpilib.analogEncoder(0)
        #shooter define
        self.wheelL = wpilib.PWMVictorSPX(4)
        self.wheelR = wpilib.PWMVictorSPX(5)
        self.conveyor = wpilib.PWMVictorSPX(6)
        
        #lift
        self.liftUp = wpilib.PWMVictorSPX(7)
        self.liftDown = wpilib.PWMVictorSPX(8)
        
                self.driverXbox = wpilib.XboxControler(0)
        
        self.dXL = 1
        self.dYL = 2
        self.dXR = 4
        self.dYR = 5
        self.dTrig = 3
        
        self.operatorXbox = wpilib.XboxControler(1)
        
        self.oXL = 1
        self.oYL = 2
        self.oXR = 4
        self.oYR = 5
        self.oTrig = 3
        
    def autounomousInit(self):
        
        for self.fLE.get()< 5:
            self.fL.
        
        
    def teleopPeriodic(self):
        
        #shoot
        self.wheelL.set(self.operatorXbox.getRawAxis(self.oTrig)+self.operatorXbox.getRawAxis(self.oXR))
        self.wheelR.set(self.operatorXbox.getRawAxis(self.oTrig)-self.operatorXbox.getRawAxis(self.oXR))
        
        self.conveyor.set(self.operatorXbox.getRawAxis(self.oYL))
        
        #lift
    if self.operatorXbox.bumper(left) = true :
        self.liftUp.set(self.operatorXbox.getRawAxis(self.oYR))
    
    if self.operatorXbox.bumper(right) = true : 
        self.liftDown.set(self.operatorXbox.getRawAxis(self.oYR))
    
    self.fL.set((self.driverXbox.getRawAxis(dYL))+(2*(self.driverXbox.getRawAxis(self.dXL)))
    self.fR.set((self.driverXbox.getRawAxis(dYL))-(2*(self.driverXbox.getRawAxis(self.dXL)))
    
    self.bL.set((self.driverXbox.getRawAxis(dYL))+(2*(self.driverXbox.getRawAxis(self.dXL))+(2*(self.driverXbox.getRawAxis(self.dXR)))
    
    self.bR.set((self.driverXbox.getRawAxis(dYL))-(2*(self.driverXbox.getRawAxis(self.dXL))-(2*(self.driverXbox.getRawAxis(self.dXR)))
    


if __name__ == "__main__":
    wpilib.run(MyRobot)
    
