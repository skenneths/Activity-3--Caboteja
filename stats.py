class userstat:
    def stat(thestat,base,IV,EV,lvl,natures):
        total = (((2*base+IV+(EV/4))*lvl)/100)+5
        if thestat == 1:
            total = (((2*base+IV+(EV/4))*lvl)/100)+lvl+10
        elif thestat == 2:
            if natures in {2,3,4,5}: total = total * 1.1
            if natures in {6,11,16,21}: total = total * 0.9
        elif thestat == 3:
            if natures in {6,8,9,10}: total = total * 1.1
            if natures in {2,12,17,22}: total = total * 0.9
        elif thestat == 4:
            if natures in {16,17,18,20}: total = total * 1.1
            if natures in {4,9,14,24}: total = total * 0.9
        elif thestat == 5:
            if natures in {21,22,23,24}: total = total * 1.1
            if natures in {5,10,15,20}: total = total * 0.9
        else:
            if natures in {11,12,14,15}: total = total * 1.1  
            if natures in {3,8,18,23}: total = total * 0.9 

        return total
