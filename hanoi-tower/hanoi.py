def hanoi_solver(disks: int):
    first_road = list(range(1, disks+1))
    first_road = first_road[::-1]
    second_road = []
    third_road = []
    moves = []
    
    #core
    def hanoi(disks, source, destination, pivot):
        if disks == 1:
            destination.append(source.pop())
            moves.append(f"{first_road} {second_road} {third_road}")
            return

        hanoi(disks-1, source, pivot, destination)
        destination.append(source.pop())
        moves.append(f"{first_road} {second_road} {third_road}")
        hanoi(disks-1, pivot, destination, source)

    moves.append(f"{first_road} {second_road} {third_road}")
    hanoi(disks, first_road, third_road, second_road)
    return "\n".join(moves)

print(hanoi_solver(5))
