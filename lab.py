import scipy
import matplotlib.pyplot as plt
import math


G = 0.000_000_000_066743
M = 5_972_000_000_000_000_000_000_000
Mm = 73_480_000_000_000_000_000_000
GM = G*M
r = 7_000_000
Rm = 384_400_000
h = 10

def f1(t, x, y, vx, vy):
    return vx

def f2(t, x, y, vx, vy):
    return vy

def f3(t, x, y, vx, vy):
    return (-1*GM*x)/(pow((x**2 + y**2), 3/2))

def f4(t, x, y, vx, vy):
    return (-1*GM*y)/(pow((x**2 + y**2), 3/2))


def f3m(t, x, y, vx, vy):
    return (-1*GM*x)/(pow((x**2 + y**2), 3/2)) - (G*Mm*(x))/(abs(pow((x**2 + (y-Rm)**2), 1/2))**3)

def f4m(t, x, y, vx, vy):
    return (-1*GM*y)/(pow((x**2 + y**2), 3/2)) - (G*Mm*(y-Rm))/(abs(pow((x**2 + (y-Rm)**2), 1/2))**3)


MyInput = '0'
while MyInput != 'q':
    MyInput = input("a, b, c, or q to quit: ")
    print("choice is: ", MyInput)
    if MyInput == 'a':
        print("You have chosen part a: simulation of an orbit")

        xode = []
        yode = []

        kenergy = []
        penergy = []
        energy = []

        t = 0

        x0 = float(input("Enter a value for x (floating point position in metres): "))
        y0 = math.sqrt(r**2 - x0**2)
        vx = -1 * float(input("Enter a value for vx (floating point component of velocity in m/s): "))
        vy = -vx

        xode.append(x0)
        yode.append(y0)

        for i in range(5000):
            x = xode[i]
            y = yode[i]

            pe = -1*(GM/math.sqrt(x**2 + y**2))
            penergy.append(pe)
            ke = 0.5*(vx**2 + vy**2)
            kenergy.append(ke)
            e = ke + pe
            energy.append(e)

            kx = []
            ky = [] 
            kvx = []
            kvy = []

            kx.append(f1(0, x, y, vx, vy))
            ky.append(f2(0, x, y, vx, vy))
            kvx.append(f3(0, x, y, vx, vy))
            kvy.append(f4(0, x, y, vx, vy))

            kx.append(f1(0, x, y, vx + (h*kvx[0])/2, vy))
            ky.append(f2(0, x, y, vx, vy + (h*kvy[0])/2))
            kvx.append(f3(0, x  + (h*kx[0])/2, y + (h*ky[0])/2, vx, vy))
            kvy.append(f4(0, x  + (h*kx[0])/2, y + (h*ky[0])/2, vx, vy))

            kx.append(f1(0, x, y, vx + (h*kvx[1])/2, vy))
            ky.append(f2(0, x, y, vx, vy + (h*kvy[1])/2))
            kvx.append(f3(0, x  + (h*kx[1])/2, y + (h*ky[1])/2, vx, vy))
            kvy.append(f4(0, x  + (h*kx[1])/2, y + (h*ky[1])/2, vx, vy))

            kx.append(f1(0, x, y, vx + h*kvx[2], vy))
            ky.append(f2(0, x, y, vx, vy + h*kvy[2]))
            kvx.append(f3(0, x + h*kx[2], y + h*ky[2], vx, vy))
            kvy.append(f4(0, x + h*kx[2], y + h*ky[2], vx, vy))
            
            x += (h/6) * (kx[0] + 2*kx[1] + 2*kx[2] + kx[3])
            y += (h/6) * (ky[0] + 2*ky[1] + 2*ky[2] + ky[3])
            vx += (h/6) * (kvx[0] + 2*kvx[1] + 2*kvx[2] + kvx[3])
            vy += (h/6) * (kvy[0] + 2*kvy[1] + 2*kvy[2] + kvy[3])

            xode.append(x)
            yode.append(y)
            t += h

        plt.plot(xode, yode)
        plt.plot([0], [0], marker='o')
        plt.title("4th order Runge-Kutta elliptical orbit")
        plt.show()

        plt.plot(kenergy, color ='r')
        plt.plot(penergy, color = 'b')
        plt.plot(energy, color = 'hotpink')
        plt.title("energy of elliptical orbit")
        plt.legend(["kinetic", "potential", "total"])
        plt.show()

    elif MyInput == 'b':
        print("You have chosen part b: shooting the moon")

        xode = []
        yode = []

        kenergy = []
        penergy = []
        energy = []

        x0 = -460257.297336
        y0 = -7312314.927224
        vx = float(input("Enter a value for vx (floating point component of velocity in m/s): "))
        vy = float(input("Enter a value for vy (floating point component of velocity in m/s): "))

        x= x0
        y= y0

        t = 0
        for i in range(78_000):

            pe = -1*(GM/math.sqrt(x**2 + y**2))
            penergy.append(pe)
            ke = 0.5*(vx**2 + vy**2)
            kenergy.append(ke)
            e = ke + pe
            energy.append(e)

            kx = []
            ky = [] 
            kvx = []
            kvy = []

            kx.append(f1(0, x, y, vx, vy))
            ky.append(f2(0, x, y, vx, vy))
            kvx.append(f3m(0, x, y, vx, vy))
            kvy.append(f4m(0, x, y, vx, vy))

            kx.append(f1(0, x, y, vx + (h*kvx[0])/2, vy))
            ky.append(f2(0, x, y, vx, vy + (h*kvy[0])/2))
            kvx.append(f3m(0, x  + (h*kx[0])/2, y + (h*ky[0])/2, vx, vy))
            kvy.append(f4m(0, x  + (h*kx[0])/2, y + (h*ky[0])/2, vx, vy))

            kx.append(f1(0, x, y, vx + (h*kvx[1])/2, vy))
            ky.append(f2(0, x, y, vx, vy + (h*kvy[1])/2))
            kvx.append(f3m(0, x  + (h*kx[1])/2, y + (h*ky[1])/2, vx, vy))
            kvy.append(f4m(0, x  + (h*kx[1])/2, y + (h*ky[1])/2, vx, vy))

            kx.append(f1(0, x, y, vx + h*kvx[2], vy))
            ky.append(f2(0, x, y, vx, vy + h*kvy[2]))
            kvx.append(f3m(0, x + h*kx[2], y + h*ky[2], vx, vy))
            kvy.append(f4m(0, x + h*kx[2], y + h*ky[2], vx, vy))
            
            x += (h/6) * (kx[0] + 2*kx[1] + 2*kx[2] + kx[3])
            y += (h/6) * (ky[0] + 2*ky[1] + 2*ky[2] + ky[3])
            vx += (h/6) * (kvx[0] + 2*kvx[1] + 2*kvx[2] + kvx[3])
            vy += (h/6) * (kvy[0] + 2*kvy[1] + 2*kvy[2] + kvy[3])

            # make sure rocket doesn't hit moons surface
            if (pow((x**2 + y**2), 1/2) < 1_750_000):
                break
            
            xode.append(x)
            yode.append(y)
            t += h
        
        print("time taken: ", t)
        plt.plot(xode, yode)
        plt.plot([0], [0], marker='o')
        plt.plot([0], [Rm], marker='o')
        plt.xlim(-100_000_000, 100_000_000)
        plt.ylim(-50_000_000, 500_000_000)
        ax = plt.gca()
        ax.set_aspect('equal', adjustable='box')
        plt.draw()
        plt.title("earth and moon orbit")
        plt.show()

        #plt.plot(kenergy, color ='r')
        # plt.plot(penergy, color = 'b')
        # plt.plot(energy, color = 'hotpink')
        # plt.title("energy of elliptical orbit")
        # plt.legend(["kinetic", "potential", "total"])
        # plt.show()
    
    elif MyInput != 'q':
        print("This is not a valid choice")

print("You have chosen to finish - goodbye")









