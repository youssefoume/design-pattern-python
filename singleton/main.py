from singleton import Singleton
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)
s = Singleton.getInstance()

print(s)