gravity = -9.81
bounciness = 0.8
timestep=1e-3
end_time=1e1

def energy(height,velocity_1,velocity_2):
    gravitational=-1*gravity*height
    kinetic=0.5*(velocity_1*velocity_1+velocity_2*velocity_2)
    return gravitational+kinetic

#rather crude bouncing model...
def bounce(velocity):
    if velocity<0:velocity*=-1
    return velocity*bounciness

print("Enter height")
x=0
y=float(input())
print("Enter horizontal velocity")
vel_x=float(input())
vel_y=0
starting_energy=energy(y,vel_x,vel_y)
time=0

print("time,x,y,vel_x,vel_y,energy")
while True:
    #output current parameters
    output_line=str(time)+","+str(x)+","+str(y)+","+str(vel_x)+","+str(vel_y)+","+str(energy(y,vel_x,vel_y))
    print(output_line)
    
    #handle bouncing
    if y<-1*timestep*vel_y:
        this_timestep=y/vel_y
        vel_x=bounce(vel_x)
        vel_y=bounce(vel_y)
    else:
        this_timestep=timestep

    #increment parameters
    time+=this_timestep
    x+=this_timestep*vel_x
    y+=this_timestep*vel_y
    vel_y+=this_timestep*gravity

    #stop if energy mostly gone
    if energy(y,vel_x,vel_y) < starting_energy / 1e3 : break

    #stop if we reach end_time
    if time >= end_time : break
