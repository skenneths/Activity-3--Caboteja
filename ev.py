class userev:
    def single(thestat,base,IV,EV,lvl,natures,stat):
        d = (2*base+IV+(EV/4))*(lvl/100)
        
        if thestat == 1:
            if natures in {2,3,4,5}: natures = 1.1
            elif natures in {6,11,16,21}: natures = 0.9
            else: natures = 1
        elif thestat == 2:
            if natures in {6,8,9,10}: natures = 1.1
            elif natures in {2,12,17,22}: natures = 0.9
            else: natures = 1
        elif thestat == 3:
            if natures in {16,17,18,20}: natures = 1.1
            elif natures in {4,9,14,24}: natures = 0.9
            else: natures = 1
        elif thestat == 4:
            if natures in {21,22,23,24}: natures = 1.1
            elif natures in {5,10,15,20}: natures = 0.9
            else: natures = 1
        else:
            if natures in {11,12,14,15}: natures = 1.1  
            elif natures in {3,8,18,23}: natures = 0.9 
            else: natures = 1

        evmo = (((((stat/natures)-d)*400)/lvl)/4)*4
        return evmo
    
    def all(x,naku,desire,IV,EV,lvl,natures,stat):
        for a in range (len(x)):
            d = (2*naku+IV+(EV/4))*(lvl/100)

            if a == 0:
                if natures in {2,3,4,5}: natures = 1.1
                elif natures in {6,11,16,21}: natures = 0.9
                else: natures = 1
            elif a == 1:
                if natures in {6,8,9,10}: natures = 1.1
                elif natures in {2,12,17,22}: natures = 0.9
                else: natures = 1
            elif a == 2:
                if natures in {16,17,18,20}: natures = 1.1
                elif natures in {4,9,14,24}: natures = 0.9
                else: natures = 1
            elif a == 5:
                if natures in {21,22,23,24}: natures = 1.1
                elif natures in {5,10,15,20}: natures = 0.9
                else: natures = 1
            else:
                if natures in {11,12,14,15}: natures = 1.1  
                elif natures in {3,8,18,23}: natures = 0.9 
                else: natures = 1

        for b in range (len(x)):    
            total = (((((desire/natures)-d)*400)/lvl)/4)*4
            return total