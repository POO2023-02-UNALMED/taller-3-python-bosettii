from televisores.tv import TV
from televisores.marca import Marca
from televisores.control import Control

if __name__ == "__main__":
#    marca1 = Marca("Semsung")
 #   marca2 = Marca("Lj")
#
 #   tv1 = TV(marca1, True)
  #  tv2 = TV(marca2, False)
#
 #   tv1.setPrecio(2000)
#    tv2.setCanal(90)
 #   tv1.setCanal(121)
  #  tv2.setVolumen(7)
#
 #   control1 = Control()
  #  control1.enlazar(tv1)
   # control1.turnOff()
    #control1.setCanal(50)
    #control1.turnOn()
#    control1.canalUp()
 #   control1.volumenUp()
#
 #   print(tv2.getCanal())
  #  print(tv1.getPrecio())
   # print(tv1.getMarca().getNombre())
    #print(tv1.getCanal())

    marca = Marca("Ipple")

    tv1 = TV(marca, True)
    tv1.setCanal(80)
    tv1.canalDown()
    tv1.canalUp()
    tv1.canalDown()
    tv1.canalDown()
    tv1.turnOff()
    tv1.canalUp()

    tv2 = TV(marca, False)
    tv2.setCanal(70)
    tv2.canalUp()
    tv2.canalDown()
    tv2.turnOn()
    tv2.canalUp()
    tv2.canalUp()
    tv2.canalDown()
    tv2.canalUp()

    tv3 = TV(marca, True)
    tv3.setCanal(121)
    tv3.canalUp()

    tv4 = TV(marca, True)
    tv4.setCanal(0)
    tv4.canalUp()

    tv5 = TV(marca, True)
    tv5.canalDown()

    tv6 = TV(marca, True)
    tv6.setCanal(120)
    tv6.canalUp()

    tv7 = TV(marca, True)
    tv7.setCanal(35)
    tv7.canalDown()
    tv7.setCanal(200)

    print(tv1.getCanal())
    print(tv2.getCanal())
    print(tv3.getCanal())
    print(tv4.getCanal())
    print(tv5.getCanal())
    print(tv6.getCanal())
    print(tv7.getCanal())
