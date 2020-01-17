
def even(max):
    track=1
    while track<max:
        if track%2==0:
            yield track
        track+=1

o=even(10)
print(next(o))
print(next(o))
print(next(o))

print("sadas")
print(sum(even(10)))

