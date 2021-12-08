
def simulate(fish, days):
    size = len(fish)
    d = dict()

    for i in range(len(fish)):
        d[i] = fish[i]



    #print("Inital state: " + "".join(str(fish)))
    for i in range(days):

        print(str(i) + "/"+ str(days))
    return len(fish)



if __name__ == "__main__":
    with open('./input.txt') as f:
        data = list(map(int,f.read().split(',')))
        print(simulate(data,256))
