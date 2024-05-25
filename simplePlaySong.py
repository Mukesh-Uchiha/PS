import multiprocessing
from playsound import playsound 

if __name__ == "__main__":
        
    p = multiprocessing.Process(target=playsound, args=("Song/Song.mp3",))
    p.start()
    enter=input("press enter")
    if enter =="":
        print("Pressed Enter")
        p.terminate()

    p.join()

    
