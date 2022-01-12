N = int(input())
horas = (N // 3600)
minutos = int(((N % 3600)/3600) * 60)
segundos = (N % 3600) %60

print(horas, minutos, segundos, sep = ":")