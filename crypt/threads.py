from threading import Thread
import time

def car(velocidade, piloto):
    trajeto = 0
    
    while trajeto < 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f"Piloto: {piloto} Km: {trajeto} \n")



t1 = Thread(target=car, args=[1, 'Vitor'])
t2 = Thread(target=car, args=[2, 'Esteves'])

t1.start()
t2.start()



#if __name__ == "__main__":
  