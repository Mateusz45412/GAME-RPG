
def energies(energia, start_energy, name):
    percent = int((energia * 100) / start_energy)
    see = [
        [f" {name}📗📗📗📗📗📗📗📗📗📗 {percent}%"],
        [f" {name}📗📗📗📗📗📗📗📗📗📕 {percent}%"],
        [f" {name}📗📗📗📗📗📗📗📗📕📕 {percent}%"],
        [f" {name}📗📗📗📗📗📗📗📕📕📕 {percent}%"],
        [f" {name}📗📗📗📗📗📗📕📕📕📕 {percent}%"],
        [f" {name}📗📗📗📗📗📕📕📕📕📕 {percent}%"],
        [f" {name}📗📗📗📗📕📕📕📕📕📕 {percent}%"],
        [f" {name}📗📗📗📕📕📕📕📕📕📕 {percent}%"],
        [f" {name}📗📗📕📕📕📕📕📕📕📕 {percent}%"],
        [f" {name}📗📕📕📕📕📕📕📕📕📕 {percent}%"],
        [f" {name}📕📕📕📕📕📕📕📕📕📕 0 %"],
    ]

    if energia == 100: print(*see[0])
    elif energia >= 90: print(*see[1])
    elif energia >= 80: print(*see[2])
    elif energia >= 70: print(*see[3])
    elif energia >= 60: print(*see[4])
    elif energia >= 50: print(*see[5])
    elif energia >= 40: print(*see[6])
    elif energia >= 30: print(*see[7])
    elif energia >= 20: print(*see[8])
    elif energia >= 10: print(*see[9])
    elif energia <= 0: print(*see[10])
    return percent
