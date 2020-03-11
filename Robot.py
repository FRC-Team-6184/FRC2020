import wpilib

class MyRobot(wpilib.timedRobot,self):
    def robotInit(self):
        
        #drive define
        self.fL = wpilib.PWMTalonFX(0)
        self.fR = wpilib.PWMTalonFX(1)
        self.bL = wpilib.PWMTalonFX(2)
        self.bR = wpilib.PWMTalonFX(3)
        
        #shooter define
        self.wheelL = wpilib.PWMVictorSPX(4)
        self.wheelR = wpilib.PWMVictorSPX(5)
        self.conveyor = wpilib.PWMVictorSPX(6)
        
        #lift
        self.liftUp = wpilib.PWMVictorSPX(7)
        self.liftDown = wpilib.PWMVictorSPX(8)
        
                self.driverXbox = wpilib.XboxController(0)
        
        self.dXL = 1
        self.dYL = 2
        self.dXR = 4
        self.dYR = 5
        self.dTrig = 3
        
        self.operatorXbox = wpilib.XboxController(1)
        
        self.oXL = 1
        self.oYL = 2
        self.oXR = 4
        self.oYR = 5
        self.oTrig = 3
        
    def autounomousInit(self):
        
        pass
        
        
    def teleopPeriodic(self):
        
        #shoot
        self.wheelL.set(self.operatorXbox.getRawAxis(3)+self.operatorXbox.getRawAxis(1))
        self.wheelR.set(self.operatorXbox.getRawAxis(3)-self.operatorXbox.getRawAxis(1))
        
        self.conveyor.set(self.operatorXbox.getRawAxis(6))
        

    
#lift
    if self.operatorXbox.getRawButton(5)== True :
        self.liftUp.set(self.operatorXbox.getRawAxis(5))
    
    if self.operatorXbox.getRawButton(6) ==  True : 
        self.liftDown.set(self.operatorXbox.getRawAxis(5))
    
    self.fL.set( (self.driverXbox.getRawAxis(2) ) + (2* ( self.driverXbox.getRawAxis(1)) ))
    self.fR.set( (self.driverXbox.getRawAxis(2) ) - ( 2* (self.driverXbox.getRawAxis(1) )))
    
    self.bL.set( (self.driverXbox.getRawAxis(2)) + ( 2* (self.driverXbox.getRawAxis(1))) +   ( 2* (self.driverXbox.getRawAxis(4))))
    
    self.bR.set( (self.driverXbox.getRawAxis(2) ) - (2* (self.driverXbox.getRawAxis(1))) -(2* (self.driverXbox.getRawAxis(4))))
    


if __name__ == "__main__":
    wpilib.run(MyRobot)
    
